from django.http import HttpResponse,Http404
from .models import Question  
from django.shortcuts import render 
import random 
import numpy as np
from django.core.files.storage import FileSystemStorage
import math
from skimage.measure import compare_ssim
import imutils
import cv2

import base64

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context= {"latest_question_list":latest_question_list}
    return render(request,"polls/index.html",context)

def test(request):
    return HttpResponse(random.randint(0,10) * random.randint(0,10))



def detail(request, question_id):
    try:
        q = Question.objects.get(pk=question_id)
    except Question.DoesNotExsist:
        raise Http404("Question does not exsist")
    return render(request,"polls/detail.html",{"question":q})

def results(request, question_id):
    response = "Youre looking at question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Youre voting on question %s." % question_id)

def simple_upload(request):
    original = request.FILES.get("original")
    myfile = request.FILES.get("myfile")
   

    if request.method == 'POST' and original and myfile :
        print("------------------------------------------------------------------------")
        print(request.FILES.get("original"))
        print("------------------------------------------------------------------------")
        print(request.FILES)
        data1 = original.read()
        data2 = myfile.read()
        f = open("./media/1.jpg","wb")
        f.write(data1)
        f2 = open("./media/2.jpg","wb")
        f2.write(data2)
        f.close()
        f2.close()
        (score,diff) = calculate_ssim("./media/1.jpg","./media/2.jpg")
        mseScore = mse("./media/1.jpg","./media/2.jpg")
        print(PSNR("./media/1.jpg","./media/2.jpg"))
        calcScore = int(round((score)*100)) + int(round((50000-mseScore)/1000))
        context = {
            'uploaded_file_url':"./media/",
            'mseScore': mseScore,
            'calcScore': calcScore,
            'score': score,

        }
        f.close()
        f2.close()
        return render(request, 'polls/simple_upload.html',context)
        
    return render(request, 'polls/simple_upload.html')

 
# the methods to determine
def calculate_ssim(file1,file2):
    img1 = cv2.imread(file1,cv2.IMREAD_UNCHANGED)
    img2 = cv2.imread(file2,cv2.IMREAD_UNCHANGED)

    #width = int(img1.shape[1])
    #height = int(img1.shape[0])
    #dim = (width, height)
    # resize image
    #resized = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)*/

    gray1 = cv2.cvtColor(img1,cv2.COLOR_BGR2Luv)
    gray2 = cv2.cvtColor(img2,cv2.COLOR_BGR2Luv)
    (score,diff)= compare_ssim(gray1,gray2,full=True,multichannel=True)
    diff= (diff * 255).astype("uint8")
    print(score)
    return (score,diff)

def mse(file1, file2):
    imageA = cv2.imread(file1)
    imageB = cv2.imread(file2)
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])
    return err

def PSNR(original, compressed): 

    mseScore =mse(original,compressed)
    if(mseScore == 0):  # MSE is zero means no noise is present in the signal . 
                  # Therefore PSNR have no importance. 
        return 100
    max_pixel = 255.0
    psnr = 20 * math.log10(max_pixel / math.sqrt(mseScore)) 
    return psnr 
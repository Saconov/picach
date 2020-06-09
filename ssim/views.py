from django.http import HttpResponse,Http404,JsonResponse
from django.shortcuts import render 
import random 
import numpy as np
from django.core.files.storage import FileSystemStorage
import math
from skimage.measure import compare_ssim
import imutils
import cv2
import os
from django.contrib.auth import authenticate, login
import base64
from django.views.decorators.csrf import csrf_exempt
from  .models import Challenge,Image
from django.core import serializers
from django.utils.crypto import get_random_string



@csrf_exempt
def loginUser(request):
    
    print(request.POST.dict())
    #user = authenticate(request, username=username, password=password)
    #if user is not None:
        #login(request, user)
        # Redirect to a success page.
    if(request.POST.dict()== {}):
        	return render(request,"ssim/Login.html",{})
    req_dict = request.POST.dict()
    user = authenticate(request, username=req_dict.get("username"), password=req_dict.get("password"))
    if(user == None):
        return HttpResponse("invalid user",status= 403)
    return HttpResponse(user)
    

def vote(request, question_id):
    return HttpResponse("Youre voting on question %s." % question_id)

@csrf_exempt
def simple_upload(request):
    print(request.POST.dict())
    i = Image.objects.get(pk = int(request.POST.dict().get("challenge_picture")))
    original = i.location + i.name
    myfile = (request.FILES.get("picture")).read()
    mypath= "./data/temp/"+get_random_string(length=15)+".png"
    f = open(mypath,"wb")
    f.write(myfile)
    result = None
    if request.method == 'POST' and original and myfile :
        (score,diff) = calculate_ssim(original,mypath)
        mseScore = mse(original,mypath)
        print(PSNR(original,mypath))
        calcScore = int(round((score)*100)) + int(round((50000-mseScore)/1000))
        result = (score,calcScore)
        
    f.close()
    os.remove(mypath)   
    return HttpResponse(result)

@csrf_exempt
def create_challenge(request):
    dictionary = request.POST.dict()
    print(dictionary)
    title = dictionary.get("title")
    descr = dictionary.get("description")
    image = Image.objects.get(pk = int(dictionary.get("picture_id")))
    challenge = Challenge.create(image,None,descr,title,"0,0",0)
    challenge.save()
    return HttpResponse("ok")

@csrf_exempt
def upload_image(request):
    name = get_random_string(length=15) +'.png'
    location= "./data/"
    f = open(location+name, 'w+b')
    byte_arr = request.body
    binary_format = bytearray(byte_arr)
    f.write(binary_format)
    f.close()
    image = Image.create(name,"0,0",location)
    image.save()
    return HttpResponse(image.pk)

def get_challenges(request):
    return JsonResponse(serializers.serialize("json",Challenge.objects.all()),safe=False)


def get_image(request,image_id):
    print(image_id)
    i = Image.objects.get(pk = int(image_id))
    f = open(i.location + i.name,"rb");
    return HttpResponse(f.read(), content_type='image/png')
   
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
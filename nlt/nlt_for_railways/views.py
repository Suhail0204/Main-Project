from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import users_collection
from django.views.decorators.csrf import csrf_exempt
from transformerAPI import *
from gettraininfo import *
from googletrans import Translator
from google_trans_new import google_translator

# Create your views here.
@csrf_exempt
def index(request):
    if request.method == "POST":
        form_type = request.POST.get('form_type')
        if form_type == 'signup':
            email = request.POST['email']
            lang = request.POST['lang']
            password = request.POST['password']
            record = {"email" : email ,"language" : lang,"password" : password}
            users_collection.insert_one(record)
        elif form_type == 'signin':
            username = request.POST['username']
            password = request.POST['password']
            record = {"email":username,"password":password}
            logincheck = users_collection.find_one(record)
            if logincheck != None:
                return HttpResponseRedirect('servicesbt')
            else :
                return HttpResponse("Invalid credential")
    return render(request,'index.html')


@csrf_exempt
def home1(request):
    global output
    output ={}
    if request.method == "POST":
        txtmsg = request.POST['txtmsg']
        output = query({"inputs": txtmsg, "parameters" : { "src_lang":"en_XX","tgt_lang":"ta_IN"}})
    return render(request,'homepage.html',{"translatedtxt" : output})



def API(request):
    translator = google_translator()  
    translate_text = translator.translate('สวัสดีจีน',lang_tgt='en')  
    print(translate_text)
    return HttpResponse(translate_text)
#     translator = Translator(service_urls=['translate.googleapis.com'])
#     translation = translator.translate("Der Himmel ist blau und ich mag Bananen", dest='en')
#     print(translation.text) 
#     return HttpResponse(translation.text) 
def home(request):
    #from todayinternationalnews import todayinternationalnews
    output = query({"inputs": "todayinternationalnews","parameters" : {"src_lang" : "en_XX","tgt_lang":"ta_IN"}})
    return render(request,"Navigate.html",{"translatedtxt_tin" : output[0].values()})

@csrf_exempt
def service_sbt(request):
    global tno_trans
    tno_trans=""
    if request.method == "POST":
        tno = request.POST['tno']
        tno_output = query1(tno)
        data = tno_output.get('data')
        t_name = data.get('train_name')
        t_type = data.get('type')
        t_from_stn_name = data.get('from_stn_name')
        t_from_time = data.get('from_time')
        t_to_stn_name = data.get('to_stn_name')
        t_to_time = data.get('to_time')
        t_running_days = data.get('running_days')
        t_travel_time = data.get('travel_time')
        # t1 = tno
        # t2 = t_name
        # t3 = t_type
        # t4 = t_from_stn_name
        # t5 = t_from_time
        # t6 = t_to_stn_name
        # t7 = t_to_time
        # t8 = t_running_days
        # t9 = t_travel_time
        t_anno = "You searched for Train Number {t1}. The train, {t2}, a {t3}, departs from {t4} at {t5} and arriving at {t6} at {t7}. This train operates on {t8} and covers the journey in approximately {t9}.".format(t1 = tno,
        t2 = t_name,
        t3 = t_type,
        t4 = t_from_stn_name,
        t5 = t_from_time,
        t6 = t_to_stn_name,
        t7 = t_to_time,
        t8 = t_running_days,
        t9 = t_travel_time)
        temp = query({"inputs": t_anno, "parameters" : { "src_lang":"en_XX","tgt_lang":"ta_IN"}})
        tno_trans =  temp[0].get('translation_text')
        print(tno_trans)
        
    return render(request,"sbt.html",{"translatedtxt_tno" : tno_trans})

def service_sbs(request):
    return render(request,"sbs.html")

def service_sbp(request):
    return render(request,"sbp.html")

def contact(request):
    return render(request,"contact.html")

def about(request):
    return render(request,"about.html")

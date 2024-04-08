from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import users_collection
from .models import *
from django.views.decorators.csrf import csrf_exempt
from transformerAPI import *
from gettraininfo import *
from eleventts import *
from getroute import *

# Create your views here.
@csrf_exempt
def index(request):
    global user_language
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
                user_language = logincheck.get('language', 'english')
                return HttpResponseRedirect('home')
                #return HttpResponse(user_language)
            else :
                return HttpResponse("Invalid credential")
    return render(request,'index.html')


def home(request):
    return render(request,'home.html')

def booking(request):
    return render(request,'booking.html')

def feedback(request):
    return render(request,'feedback.html')

def arvrmodel(request):
    return render(request,'3Dmodels.html')

def model1(request):
    return render(request,'model1.html')

def railtalk(request):
    return render(request,'railtalk.html')

@csrf_exempt
def announcement1(request):
    global tno_trans,t_anno
    tno_trans=""
    t_anno=""
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
     #   t_anno = "Kind Attention Please - Train number  {t1} - {t2} - which is to be arrive on arriving_timing - the train is now on train_status - the next station of the train is Train_route - Thank You"
        t_anno = "You searched for Train Number {t1}. The train, {t2}, a {t3}, departs from {t4} at {t5} and arriving at {t6} at {t7}. This train operates on {t8} and covers the journey in approximately {t9}.".format(t1 = tno,
        t2 = t_name,
        t3 = t_type,
        t4 = t_from_stn_name,
        t5 = t_from_time,
        t6 = t_to_stn_name,
        t7 = t_to_time,
        t8 = t_running_days,
        t9 = t_travel_time)
        # language_name = 'French'
        language_code = get_language_code(user_language)
        # print(f"The language code for {language_name} is {language_code}")
        temp = query({"inputs": t_anno, "parameters" : { "src_lang":"en_XX","tgt_lang":language_code}})
        tno_trans =  temp[0].get('translation_text')
        # tts(tno_trans)
        # print(tno_trans)
    return render(request,'announcement1.html',{"translatedtxt_tno" : tno_trans , "src_anno" : t_anno})


def announcement2(request):
    global  output_string1
    global trans_text
    output_string = ""
    trans_text=""
    output_string1=""
    if request.method == "POST":
        tno = request.POST['tno']
        json_output = get_train_route(train_no)
        # print(json_output)
       

        # Iterate over each station data
        for station_data in json_output["data"]:
            station_name = station_data["source_stn_name"]
            station_code = station_data["source_stn_code"]
            arrive_time = station_data["arrive"]
    
            # Construct the string for each station
            # station_string = f"The train departing from {station_name} ({station_code}) and stopping at {station_name} ({station_code}) at {arrive_time},\n"
            station_string = f"Station: {station_name}, {station_code}, {arrive_time}\n"
            output_string1 += station_string
            

        print(output_string)
        output_string =  output_string1[:399]
        language_code = get_language_code(user_language)
        temp = query({"inputs": output_string, "parameters" : { "src_lang":"en_XX","tgt_lang":language_code}})
        print(temp)
        trans_text =  temp[0].get('translation_text')

    return render(request,'announcement2.html',{ "translatedtxt_tno" : trans_text , "src_anno" : output_string1})


def contact(request):
    return render(request,"contact.html")



import json
import re
#import db
from fetchpage import fetchpage


classname={'CC':'AC CHAIR CAR',
           '1A':'FIRST AC',
           '2A':'SECOND AC',
           '3A':'THIRD AC',
           'SL':'SLEEPER CLASS',
           'FC':'FIRST CLASS',
           '3E':'3rd AC ECONOMY',
           '2S':'SECOND SEATING'}

quotaname={'GN':'GENERAL QUOTA',
           'LD':'Ladies Quota',
           'HO':'Headquarters/Official quota',
           'DF':'Defence Quota',
           'PH':'Parliament House Quota',
           'FT':'Foreign Tourist Quota',
           'DP':'Duty Pass Quota',
           'CK':'Tatkal Quota',
           'SS':'Women Above 45 years/Senior Citizens',
           'HP':'Physically Handicapped Quota',
           'RE':'Railway Employee Staff on Duty for Train',
           'GNRS':'General Quota Road Side',
           'OS':'Out Station',
           'PQ':'Pooled Qouta',
           'RC':'Reservation Against Cancellation',
           'RS':'Road Side',
           'YU':'Yuva',
           'LB':'Lower Berth',
           'PT':'Premium Tatkal Quota'}

def get_fare(k):
    url="http://www.indianrail.gov.in/cgi_bin/inet_frenq_cgi.cgi"
    doj=k['doj'].split('-')
    if len(doj)<=1:
        doj=['31','12','2015'] #Default Date
    k['quota']=k['quota'].upper()
    values={"lccp_trnno":k['train'],
            "lccp_day":doj[0],
            "lccp_month":doj[1],
            "lccp_srccode":k['source'],
            "lccp_dstncode":k['dest'],
            #"lccp_classopt":k['pref'],
            "lccp_classopt":"ZZ",
            "lccp_age":k['age'],
            "lccp_frclass1":k['quota'],
            "lccp_conc":"ZZZZZZ",
            "lccp_enrtcode":None,
            "lccp_viacode":None,
            "lccp_frclass2":"ZZ",
            "lccp_frclass3":"ZZ",
            "lccp_frclass4":"ZZ",
            "lccp_frclass5":"ZZ",
            "lccp_frclass6":"ZZ",
            "lccp_frclass7":"ZZ",
            "lccp_disp_avl_flg":"1",
            "getIt":"Please Wait...",
    }

    header={"Origin":"http://www.indianrail.gov.in",
            "Host":"www.indianrail.gov.in",
            "User-Agent":"Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)",
            "Referer":"http://www.indianrail.gov.in/fare_Enq.html"
            }
    
    html=fetchpage(url,values,header)
    cls=re.findall("(?<=Class -- )[0-9A-Za-z]+",html)
    fares=re.findall("(?<=both\">)[0-9]+",html)
    f=[]
    l=len(cls)
    for i in range(l):
        t={}
        t['class']=cls[i]
        t['fare']=fares[-l+i]
        f.append(t)
    return f

def format_result_json(r,k):
    d={}
    d['response_code']=200
    d['from']={}
   # sd=db.station_metadata(k['source'])
    d['from']['name']=sd['fullname']
    d['from']['code']=sd['code']
    d['to']={}
   #sd=db.station_metadata(k['dest'])
    d['to']['name']=sd['fullname']
    d['to']['code']=sd['code']
    d['fare']=[]
    for i in r:
        t={}
        t['code']=i['class']
        t['name']=classname.get(i['class'])
        t['fare']=i['fare']
        d['fare'].append(t)
    d['quota']={}
    d['quota']['code']=k['quota']
    d['quota']['name']=quotaname.get(k['quota'])
    #td=db.train_metadata(k['train'])
    d['train']={}
    d['train']['name']=td['name']
    d['train']['number']=k['train'] #ensures result in case if DB has no record of such a train
    d=json.dumps(d,indent=4)
    return d

def fare(**k):
    r=get_fare(k)
    r=format_result_json(r,k)
    return r


def getStatus(self,TN,DD,MMM,YYYY,STN):
    D = '-'.join([str(DD), MMM, str(YYYY)])
    URL_Live = "https://data.erail.in/getIR.aspx?&jsonp=true&Data=RUNSTATUS~0_"+str(TN)+"_"+D+"_"+STN
    return loads(get(URL_Live).text.strip('()'))

print(getStatus(22666,22,"mar",2024,"ERODE JN"))
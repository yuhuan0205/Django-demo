import json
from django.shortcuts import render,redirect
from django.http import HttpResponse,request,JsonResponse,HttpResponseRedirect
from .models import ClientProduct,ClientInfo,data_view,cros_view,to_excel,top3,get_info_cros,fb_view,line_view
import os
from django.core.cache import cache,caches
from django.contrib import auth


# Create your views here.


def data(request):
    x = data_view()

    # ensure_ascii=False 處理編碼問題
    return HttpResponse(json.dumps(x,ensure_ascii=False), content_type='application/json')

def top3_view(request):
    x = cache.get("top3_cache")
    if not x:
        print("have no cache!")
        top3_list = top3(3)
        x = cros_view(date1 = [""] , date2 = [""] ,cli = top3_list,pro =[""],cam = [""],g1 = [""],g2 = [""], g3 = [""],med = [""],lin =[""],pay=[""],reg = [""],ord = [""] )
        cache.set("top3_cache",x,3600)
    #return HttpResponse(json.dumps(x[:5],ensure_ascii=False), content_type='application/json')
    return HttpResponse(json.dumps(x,ensure_ascii=False), content_type='application/json')

#需再精簡
def download(request):

    date_1 = request.GET.getlist("date1","")
    date_2 = request.GET.getlist("date2","")
    cli1 = request.GET.getlist("clientname","")
    pro1 = request.GET.getlist("productname","")
    cam1 = request.GET.getlist("campaign","")
    ga1 = request.GET.getlist("ga1","")
    ga2 = request.GET.getlist("ga2","")
    ga3 = request.GET.getlist("ga3","")
    med1 = request.GET.getlist("media","")
    lin1 = request.GET.getlist("link_type","")
    payMeth = request.GET.getlist("paymethod","")
    regu = request.GET.getlist("regular","")
    orderT = request.GET.getlist("ordertype","")
    mod = request.GET.getlist("mode","")
    splitList = [date_1,date_2,cli1,pro1,cam1,ga1,ga2,ga3,med1,lin1,payMeth,regu,orderT]
    
    for i in range(13):
        try:
            splitList[i] = splitList[i][0].split(",")
        except IndexError:
            continue
    for i in range(len(splitList[11])):
        if splitList[11][i] == "定期":
            splitList[11][i] = "1"
        elif splitList[11][i] == "都度":
            splitList[11][i] = "0"

    if splitList[2][0] == "top1":
        if mod[0] == "cros":
            x = cache.get("top1_cache_cros")
            if not x:
                print("have no cache!")
                top1_list = top3(1)
                x = cros_view(date1 = [""] , date2 = [""] ,cli = top1_list,pro =[""],cam = [""],g1 = [""],g2 = [""], g3 = [""],med = [""],lin =[""],pay=[""],reg = [""],ord = [""] )
                cache.set("top1_cache_cros",x,3600)
        elif mod[0] == "fb":
            x = cache.get("top1_cache_fb")
            if not x:
                print("have no cache!")
                top1_list = top3(1)
                x = fb_view(date1 = [""] , date2 = [""] ,cli = top1_list,pro =[""],cam = [""],g1 = [""],g2 = [""], g3 = [""],med = [""],lin = [""])
                cache.set("top1_cache_fb",x,3600)
        elif mod[0] == "line":
            x = cache.get("top1_cache_line")
            if not x:
                print("have no cache!")
                top1_list = top3(1)
                x = line_view(date1 = [""] , date2 = [""] ,cli = top1_list,pro =[""],cam = [""],g1 = [""],g2 = [""], g3 = [""],med = [""],lin = [""])
                cache.set("top1_cache_line",x,3600)

    elif mod[0] == "cros":
        x = cros_view(date1 = splitList[0] , date2 = splitList[1] ,cli = splitList[2],pro =splitList[3],cam = splitList[4],g1 = splitList[5],g2 = splitList[6], g3 = splitList[7],med = splitList[8],lin =splitList[9],pay=splitList[10],reg = splitList[11],ord = splitList[12] )
    elif mod[0] == "fb":
        x = fb_view(date1 = splitList[0] , date2 = splitList[1] ,cli = splitList[2],pro =splitList[3],cam = splitList[4],g1 = splitList[5],g2 = splitList[6], g3 = splitList[7],med = splitList[8],lin =splitList[9])
    elif mod[0] == "line":
        x = line_view(date1 = splitList[0] , date2 = splitList[1] ,cli = splitList[2],pro =splitList[3],cam = splitList[4],g1 = splitList[5],g2 = splitList[6], g3 = splitList[7],med = splitList[8],lin =splitList[9])
    else:
        x = cros_view(date1 = splitList[0] , date2 = splitList[1] ,cli = splitList[2],pro =splitList[3],cam = splitList[4],g1 = splitList[5],g2 = splitList[6], g3 = splitList[7],med = splitList[8],lin =splitList[9],pay=splitList[10],reg = splitList[11],ord = splitList[12] )
    
    to_excel(mod[0],x,request.user)
    filepath = os.path.join("./download/"+str(request.user)+".xlsx")
    response = HttpResponse(open(filepath,'rb'),content_type="application/xlsx")
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(str(request.user)+".xlsx")
    return response

    
    date_1 = request.GET.getlist("date1","")
    date_2 = request.GET.getlist("date2","")
    cli1 = request.GET.getlist("clientname","")
    pro1 = request.GET.getlist("productname","")
    cam1 = request.GET.getlist("campaign","")
    ga1 = request.GET.getlist("ga1","")
    ga2 = request.GET.getlist("ga2","")
    ga3 = request.GET.getlist("ga3","")
    med1 = request.GET.getlist("media","")
    lin1 = request.GET.getlist("link_type","")
    payMeth = request.GET.getlist("paymethod","")
    regu = request.GET.getlist("regular","")
    orderT = request.GET.getlist("ordertype","")
    splitList = [date_1,date_2,cli1,pro1,cam1,ga1,ga2,ga3,med1,lin1]
    
    for i in range(10):
        try:
            splitList[i] = splitList[i][0].split(",")
        except IndexError:
            continue
    
    x = line_view(date1 = splitList[0] , date2 = splitList[1] ,cli = splitList[2],pro =splitList[3],cam = splitList[4],g1 = splitList[5],g2 = splitList[6], g3 = splitList[7],med = splitList[8],lin =splitList[9])
    
    # ensure_ascii=False 處理編碼問題
    return HttpResponse(json.dumps(x,ensure_ascii=False), content_type='application/json')
#需再精簡

#身分確認api

def log_in(request):
    print(request.method == "POST")
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = auth.authenticate(request, username = username,password = password)
    print(user,username,password)
    if user is not None:
        auth.login(request,user)
        status = {"success": 1}
    else:
        status = {"success": 0}
    return HttpResponse(json.dumps(status,ensure_ascii=False), content_type='application/json')

def check(request):
    print(request.user)
    if request.user.is_authenticated:
        status = {"success": 1}
    else:
        status = {"success": 0}
    return HttpResponse(json.dumps(status,ensure_ascii=False), content_type='application/json')

def log_out(request):
    auth.logout(request)
    status = {"success": 1}
    return HttpResponse(json.dumps(status,ensure_ascii=False), content_type='application/json')

#testing

def fb_only(request):
    
    date_1 = request.GET.getlist("date1","")
    date_2 = request.GET.getlist("date2","")
    cli1 = request.GET.getlist("clientname","")
    pro1 = request.GET.getlist("productname","")
    acc1 = request.GET.getlist("accountname","")

    gro1 = request.GET.getlist('grouptype',"")
    cam1 = request.GET.getlist("campaignname","")
    lin1 = request.GET.getlist("link_type","")
    asn = request.GET.getlist("adsetname","")
    an = request.GET.getlist("adname","")

    ga1 = request.GET.getlist("ga1","")
    ga2 = request.GET.getlist("ga2","")
    ga3 = request.GET.getlist("ga3","")
    
    
    splitList = [date_1,date_2,cli1,pro1,acc1,gro1,cam1,lin1,asn,an,ga1,ga2,ga3]
    
    for i in range(13):
        try:
            splitList[i] = splitList[i][0].split(",")
        except IndexError:
            continue
    
    x = fb_view(date1 = splitList[0] , date2 = splitList[1] ,cli = splitList[2],pro =splitList[3],acc = splitList[4],gro = splitList[5] ,cam = splitList[6],lin = splitList[7],asn = splitList[8], an = splitList[9],g1 = splitList[10],g2 = splitList[11], g3 = splitList[12])
    
    # ensure_ascii=False 處理編碼問題
    return HttpResponse(json.dumps(x,ensure_ascii=False), content_type='application/json')


def cros_api(request):

    #get https arguments
    date_1 = request.GET.getlist("date1","")
    date_2 = request.GET.getlist("date2","")
    cli1 = request.GET.getlist("clientname","")
    pro1 = request.GET.getlist("productname","")
    cam1 = request.GET.getlist("campaign","")
    ga1 = request.GET.getlist("ga1","")
    ga2 = request.GET.getlist("ga2","")
    ga3 = request.GET.getlist("ga3","")
    med1 = request.GET.getlist("media","")
    lin1 = request.GET.getlist("link_type","")
    payMeth = request.GET.getlist("paymethod","")
    regu = request.GET.getlist("regular","")
    orderT = request.GET.getlist("ordertype","")
    orderStatus = request.GET.getlist("order_status","")
    orderPath = request.GET.getlist("order_path","")
    delFlag = request.GET.getlist("del_flag","")
    margin = int(request.GET.get("margin",""))
    
    #put arguments in splList
    splitList = [date_1,date_2,cli1,pro1,cam1,ga1,ga2,ga3,med1,lin1,payMeth,regu,orderT,orderStatus,orderPath,delFlag]
    #split the elements in splitList 
    for i in range(16):
        try:
            splitList[i] = splitList[i][0].split(",")
        except IndexError:
            splitList[i] = [""]
            continue
    for i in range(len(splitList[11])):
        if splitList[11][i] == "定期":
            splitList[11][i] = "1"
        elif splitList[11][i] == "都度":
            splitList[11][i] = "0"
    
    
    #call function from models.py
    x = cros_view(date1 = splitList[0] , date2 = splitList[1] ,cli = splitList[2],pro =splitList[3],cam = splitList[4],g1 = splitList[5],g2 = splitList[6], g3 = splitList[7],med = splitList[8],lin =splitList[9],pay=splitList[10],reg = splitList[11],ord = splitList[12],ordS = splitList[13],ordP = splitList[14],delF = splitList[15],marg = margin )

    # ensure_ascii=False 處理編碼問題
    return HttpResponse(json.dumps(x,ensure_ascii=False), content_type='application/json')


def line_only(request):
    
    date_1 = request.GET.getlist("date1","")
    date_2 = request.GET.getlist("date2","")
    cli1 = request.GET.getlist("clientname","")
    pro1 = request.GET.getlist("productname","")
    acc1 = request.GET.getlist("accountname","")

    gro1 = request.GET.getlist('grouptype',"")
    cam1 = request.GET.getlist("campaignname","")
    lin1 = request.GET.getlist("link_type","")
    asn = request.GET.getlist("adsetname","")
    an = request.GET.getlist("adname","")

    ga1 = request.GET.getlist("ga1","")
    ga2 = request.GET.getlist("ga2","")
    ga3 = request.GET.getlist("ga3","")
    
    
    splitList = [date_1,date_2,cli1,pro1,acc1,gro1,cam1,lin1,asn,an,ga1,ga2,ga3]
    
    for i in range(13):
        try:
            splitList[i] = splitList[i][0].split(",")
        except IndexError:
            continue
    
    x = line_view(date1 = splitList[0] , date2 = splitList[1] ,cli = splitList[2],pro =splitList[3],acc = splitList[4],gro = splitList[5] ,cam = splitList[6],lin = splitList[7],asn = splitList[8], an = splitList[9],g1 = splitList[10],g2 = splitList[11], g3 = splitList[12])
    
    # ensure_ascii=False 處理編碼問題
    return HttpResponse(json.dumps(x,ensure_ascii=False), content_type='application/json')


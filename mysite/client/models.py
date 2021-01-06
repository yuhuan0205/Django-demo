# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from datetime import datetime,date
import datetime as dt
import operator
from django.db.models import Q
from functools import reduce
import pandas as pd
import copy
import time
from django.contrib.auth import authenticate, login

class ClientInfo(models.Model):
    serial_no = models.AutoField(db_column='Serial_NO', primary_key=True)  # Field name made lowercase.
    client_name = models.TextField(db_column='Client_Name', blank=True, null=True)  # Field name made lowercase.
    show_client_name = models.TextField(db_column='Show_Client_Name', blank=True, null=True)  # Field name made lowercase.
    client_name_cht = models.TextField(db_column='Client_Name_CHT', blank=True, null=True)  # Field name made lowercase.
    client_name_jp = models.TextField(db_column='Client_Name_JP', blank=True, null=True)  # Field name made lowercase.
    client_name_en = models.TextField(db_column='Client_Name_EN', blank=True, null=True)  # Field name made lowercase.
    status = models.TextField(db_column='Status', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'client_info'

class ClientProduct(models.Model):
    serial_no = models.AutoField(db_column='Serial_NO', primary_key=True)  # Field name made lowercase.
    client_name = models.TextField(db_column='Client_Name', blank=True, null=True)  # Field name made lowercase.
    product_name = models.TextField(db_column='Product_Name', blank=True, null=True)  # Field name made lowercase.
    show_client_name = models.TextField(db_column='Show_Client_Name', blank=True, null=True)  # Field name made lowercase.
    unit_price = models.IntegerField(db_column='Unit_Price', blank=True, null=True)  # Field name made lowercase.
    industry_type = models.TextField(db_column='Industry_Type', blank=True, null=True)  # Field name made lowercase.
    product_type = models.TextField(db_column='Product_Type', blank=True, null=True)  # Field name made lowercase.
    hash_tag = models.TextField(db_column='Hash_Tag', blank=True, null=True)  # Field name made lowercase.
    status = models.TextField(db_column='Status', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'client_product'

class CrosOrder(models.Model):
    no = models.CharField(primary_key=True, max_length=32)
    order_id = models.CharField(max_length=15)
    customer_id = models.CharField(max_length=10)
    order_status = models.IntegerField()
    order_price = models.IntegerField()
    del_flg = models.IntegerField()
    pay_method = models.IntegerField()
    pickup_method = models.IntegerField()
    regular = models.IntegerField()
    regular_times = models.IntegerField()
    campaign = models.CharField(max_length=50)
    promotion_code = models.CharField(max_length=30)
    buy_date = models.DateTimeField()
    cancel_date = models.DateTimeField()
    transfer_date = models.DateTimeField()
    real_transfer_date = models.DateTimeField()
    booking_return_date = models.DateTimeField()
    return_status = models.IntegerField()
    return_in_warehouse_date = models.DateTimeField()
    order_type = models.CharField(max_length=10)
    ga1 = models.TextField()
    ga2 = models.TextField()
    ga3 = models.TextField()
    apply_id = models.CharField(max_length=15)
    new_oto = models.IntegerField()
    cross_sell = models.IntegerField()
    repeat_click_lp = models.IntegerField()
    multi_buy_lp = models.IntegerField()
    order_path = models.CharField(max_length=10)
    invoice_date = models.DateTimeField()
    birth_month = models.IntegerField()
    sourcetype = models.CharField(db_column='SourceType', max_length=20)  # Field name made lowercase.
    sourcesubtype = models.CharField(db_column='SourceSubType', max_length=10)  # Field name made lowercase.
    clientname = models.CharField(db_column='ClientName', max_length=30)  # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', max_length=256)  # Field name made lowercase.
    accountname = models.CharField(db_column='AccountName', max_length=100)  # Field name made lowercase.
    stadatetime = models.DateTimeField(db_column='StaDateTime')  # Field name made lowercase.
    media = models.CharField(max_length=20)
    link_type = models.CharField(max_length=7)
    sex = models.CharField(max_length=10)
    birth = models.DateTimeField()
    referer = models.TextField()
    user_agent = models.TextField()

    class Meta:
        managed = False
        db_table = 'cros_order'

class CrosOrderShort(models.Model):
    no = models.CharField(primary_key=True, max_length=32)
    order_id = models.CharField(max_length=15)
    customer_id = models.CharField(max_length=10)
    order_status = models.IntegerField()
    order_price = models.IntegerField()
    del_flg = models.IntegerField()
    pay_method = models.IntegerField()
    pickup_method = models.IntegerField()
    regular = models.IntegerField()
    regular_times = models.IntegerField()
    campaign = models.CharField(max_length=50)
    promotion_code = models.CharField(max_length=30)
    cancel_date = models.DateTimeField()
    ordertype = models.CharField(db_column='order_type',max_length=10)
    ga1 = models.TextField()
    ga2 = models.TextField()
    ga3 = models.TextField()
    order_path = models.CharField(max_length=10)
    birth_month = models.IntegerField()
    clientname = models.CharField(db_column='ClientName', max_length=30)  # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', max_length=256)  # Field name made lowercase.
    accountname = models.CharField(db_column='AccountName', max_length=100)  # Field name made lowercase.
    stadatetime = models.DateTimeField(db_column='StaDateTime')  # Field name made lowercase.
    media = models.CharField(max_length=20)
    link_type = models.CharField(max_length=7)
    sex = models.CharField(max_length=10)
    birth = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cros_order_short'

class FbUniversalAd(models.Model):
    no = models.CharField(primary_key=True, max_length=32)
    ad_id = models.CharField(max_length=25)
    impressions = models.IntegerField()
    clicks = models.IntegerField()
    cv = models.IntegerField()
    cost = models.IntegerField()
    clientname = models.CharField(db_column='ClientName', max_length=30)  # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', max_length=256)  # Field name made lowercase.
    accountname = models.CharField(db_column='AccountName', max_length=100)  # Field name made lowercase.
    industrytype = models.CharField(db_column='IndustryType', max_length=10)  # Field name made lowercase.
    stadatetime = models.DateTimeField(db_column='StaDateTime')  # Field name made lowercase.
    group_type = models.CharField(max_length=5)
    campaign_id = models.CharField(max_length=25)
    campaign_name = models.CharField(max_length=100)
    ad_set_id = models.CharField(max_length=25)
    ad_set_name = models.CharField(max_length=256)
    ad_name = models.CharField(max_length=256)
    link_type = models.CharField(max_length=7)
    ga1 = models.TextField()
    ga2 = models.TextField()
    ga3 = models.TextField()

    class Meta:
        managed = False
        db_table = 'fb_universal_ad'

class FbUniversal(models.Model):
    no = models.CharField(primary_key=True, max_length=32)
    ad_id = models.CharField(max_length=25)
    impressions = models.IntegerField()
    clicks = models.IntegerField()
    cv = models.IntegerField()
    cost = models.IntegerField()
    clientname = models.CharField(db_column='ClientName', max_length=30)  # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', max_length=256)  # Field name made lowercase.
    accountname = models.CharField(db_column='AccountName', max_length=100)  # Field name made lowercase.
    industrytype = models.CharField(db_column='IndustryType', max_length=10)  # Field name made lowercase.
    stadatetime = models.DateTimeField(db_column='StaDateTime')  # Field name made lowercase.
    ad_time = models.CharField(max_length=25)
    group_type = models.CharField(max_length=5)
    campaign_id = models.CharField(max_length=25)
    campaign_name = models.CharField(max_length=100)
    campaign_status = models.CharField(max_length=10)
    campaign_objective = models.CharField(max_length=25)
    buying_type = models.CharField(max_length=15)
    campaign_spend_limit = models.CharField(max_length=10)
    campaign_daily_budget = models.IntegerField()
    campaign_lifetime_budget = models.IntegerField()
    campaign_bid_strategy = models.CharField(max_length=50)
    ad_set_id = models.CharField(max_length=25)
    ad_set_run_status = models.CharField(max_length=10)
    ad_set_name = models.CharField(max_length=256)
    ad_set_daily_budget = models.IntegerField()
    link_object_id = models.CharField(max_length=25)
    optimized_conversion_tracking_pixels = models.CharField(max_length=25)
    optimized_event = models.CharField(max_length=30)
    link = models.TextField()
    countries = models.CharField(max_length=10)
    gender = models.CharField(max_length=20)
    age_min = models.IntegerField()
    age_max = models.IntegerField()
    custom_audiences = models.TextField()
    excluded_custom_audiences = models.TextField()
    flexible_inclusions = models.TextField()
    flexible_exclusions = models.TextField()
    publisher_platforms = models.CharField(max_length=255)
    facebook_positions = models.CharField(max_length=255)
    instagram_positions = models.CharField(max_length=255)
    audience_network_positions = models.CharField(max_length=255)
    messenger_positions = models.CharField(max_length=255)
    device_platforms = models.CharField(max_length=30)
    optimization_goal = models.CharField(max_length=30)
    bid_amount = models.IntegerField()
    ad_set_bid_strategy = models.CharField(max_length=50)
    ad_status = models.CharField(max_length=10)
    ad_name = models.CharField(max_length=256)
    title = models.TextField()
    body = models.TextField()
    link_type = models.CharField(max_length=7)
    ga1 = models.TextField()
    ga2 = models.TextField()
    ga3 = models.TextField()

    class Meta:
        managed = False
        db_table = 'fb_universal'

class FbUniversalAd(models.Model):
    no = models.AutoField(primary_key=True)
    ad_id = models.CharField(max_length=25, blank=True, null=True)
    impressions = models.IntegerField(blank=True, null=True)
    clicks = models.IntegerField(blank=True, null=True)
    cv = models.IntegerField(blank=True, null=True)
    cost = models.IntegerField(blank=True, null=True)
    clientname = models.CharField(db_column='ClientName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    accountname = models.CharField(db_column='AccountName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    industrytype = models.CharField(db_column='IndustryType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    stadatetime = models.DateTimeField(db_column='StaDateTime', blank=True, null=True)  # Field name made lowercase.
    group_type = models.CharField(max_length=5, blank=True, null=True)
    campaign_id = models.CharField(max_length=25, blank=True, null=True)
    campaign = models.CharField(db_column='Campaign_Name',max_length=100, blank=True, null=True)
    ad_set_id = models.CharField(max_length=25, blank=True, null=True)
    ad_set_name = models.CharField(max_length=100, blank=True, null=True)
    ad_name = models.CharField(max_length=100, blank=True, null=True)
    link_type = models.CharField(max_length=7, blank=True, null=True)
    ga1 = models.TextField(blank=True, null=True)
    ga2 = models.TextField(blank=True, null=True)
    ga3 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fb_universal_ad'

class LineUniversal(models.Model):
    no = models.CharField(primary_key=True, max_length=32)
    ad_id = models.CharField(max_length=25)
    stadatetime = models.DateTimeField(db_column='StaDateTime')  # Field name made lowercase.
    adaccount_id = models.CharField(max_length=20)
    campaign_id = models.CharField(max_length=20)
    campaign_name = models.CharField(max_length=100)
    campaign_status = models.CharField(max_length=10)
    adgroup_id = models.CharField(max_length=20)
    adgroup_name = models.CharField(max_length=256)
    campaign_objective = models.CharField(max_length=30)
    campaign_spend_limit = models.CharField(max_length=10)
    budget_type = models.CharField(max_length=20)
    monthly_budget = models.IntegerField()
    lifetime_budget = models.IntegerField()
    ad_group_status = models.CharField(max_length=10)
    bidding_amount_configuration = models.CharField(max_length=100)
    optimize_for = models.CharField(max_length=20)
    payment_method = models.CharField(max_length=40)
    bid_amount = models.IntegerField()
    max_cpc = models.FloatField()
    max_cpa = models.FloatField()
    daily_budget = models.IntegerField()
    gender = models.CharField(max_length=20)
    age_min = models.IntegerField()
    age_max = models.IntegerField()
    user_os = models.CharField(max_length=100)
    user_os_version_min = models.CharField(max_length=100)
    user_os_version_max = models.CharField(max_length=100)
    include_audiences_id = models.TextField()
    exclude_audiences_id = models.TextField()
    ad_format = models.CharField(max_length=20)
    ad_name = models.CharField(max_length=256)
    impression = models.IntegerField()
    clicks = models.IntegerField()
    cv = models.IntegerField()
    cost = models.FloatField()
    currency = models.CharField(max_length=10)
    industrytype = models.CharField(db_column='IndustryType', max_length=10)  # Field name made lowercase.
    group_type = models.CharField(max_length=5)
    link_type = models.CharField(max_length=7)
    clientname = models.CharField(db_column='ClientName', max_length=30)  # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', max_length=256)  # Field name made lowercase.
    accountname = models.CharField(db_column='AccountName', max_length=100)  # Field name made lowercase.
    ad_status = models.CharField(max_length=10)
    image_id = models.CharField(max_length=20)
    video_id = models.CharField(max_length=20)
    title = models.TextField()
    description = models.TextField()
    click_url = models.TextField()
    ga1 = models.TextField()
    ga2 = models.TextField()
    ga3 = models.TextField()

    class Meta:
        managed = False
        db_table = 'line_universal'

class LineUniversalAd(models.Model):
    no = models.CharField(primary_key=True, max_length=32)
    ad_id = models.CharField(max_length=25)
    stadatetime = models.DateTimeField(db_column='StaDateTime')  # Field name made lowercase.
    adaccount_id = models.CharField(max_length=20)
    campaign_id = models.CharField(max_length=20)
    campaign = models.CharField(db_column='Campaign_Name',max_length=100)
    adgroup_id = models.CharField(max_length=20)
    adgroup_name = models.CharField(max_length=256)
    ad_name = models.CharField(max_length=256)
    impressions = models.IntegerField(db_column='impression')
    clicks = models.IntegerField()
    cv = models.IntegerField()
    cost = models.FloatField()
    industrytype = models.CharField(db_column='IndustryType', max_length=10)  # Field name made lowercase.
    group_type = models.CharField(max_length=5)
    link_type = models.CharField(max_length=7)
    clientname = models.CharField(db_column='ClientName', max_length=30)  # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', max_length=256)  # Field name made lowercase.
    accountname = models.CharField(db_column='AccountName', max_length=100)  # Field name made lowercase.
    image_id = models.CharField(max_length=20)
    video_id = models.CharField(max_length=20)
    ga1 = models.TextField()
    ga2 = models.TextField()
    ga3 = models.TextField()

    class Meta:
        managed = False
        db_table = 'line_universal_ad'



#統計客戶&產品別

def get_info_cros(df,df_len):

    df1 = pd.DataFrame(df)

    info_list=[[],[],[],[],[],[],[],[]] # cli_name, pro_name, campaign, Ga1, Ga2, Ga3, media, link_type


    info_list[0]= set(df1["clientname"])
        
    info_list[1]= set(df1["productname"])

    info_list[2]= set(df1["media"])
            
    info_list[3]= set(df1["campaign"])

    info_list[4]= set(df1["ga1"])
            
    info_list[5]= set(df1["ga2"])
            
    info_list[6]= set(df1["ga3"])
            
    info_list[7]= set(df1["link_type"])

    """
    for i in range(df_len):
        if df[i]["clientname"] not in info_list[0] and df[i]["clientname"] != None:
            info_list[0].append(df[i]["clientname"])
        
        if df[i]["productname"] not in info_list[1] and df[i]["productname"] != None:
            info_list[1].append(df[i]["productname"])
            
        if df[i]["campaign"] not in info_list[2] and df[i]["campaign"] != None:
            info_list[2].append(df[i]["campaign"])

        if df[i]["ga1"] not in info_list[3] and df[i]["ga1"] != None:
            info_list[3].append(df[i]["ga1"])
            
        if df[i]["ga2"] not in info_list[4] and df[i]["ga2"] != None:
            info_list[4].append(df[i]["ga2"])
            
        if df[i]["ga3"] not in info_list[5] and df[i]["ga3"] != None:
            info_list[5].append(df[i]["ga3"])
        try:
            if df[i]["media"] not in info_list[6] and df[i]["media"] != None :
                info_list[6].append(df[i]["media"])
        except KeyError:
                pass
            
        if df[i]["link_type"] not in info_list[7] and df[i]["link_type"] != None:
            info_list[7].append(df[i]["link_type"])
        """   
    for i in range(len(info_list)):
        info_list[i] = list(info_list[i])

    return info_list


    
def top3(n):
    st =time.time()
    date1 = [""]
    date2 = [""]
    date1[0] = datetime.today() - dt.timedelta(days = 200)
    date2[0] = datetime.today()

    df = list(CrosOrderShort.objects.filter(stadatetime__date__range=[date1[0],date2[0]]).values())

    
    df_len = len(df)
    
    info_list = get_info(df,df_len)
    cli_name = info_list[0]
    pro_name = info_list[1]

    sales_ranking = []
    sales_ranking_sort = []
    top3_list = []

    for i in cli_name:
        sales = 0
        for j in range(df_len):
            if df[j]["clientname"] == i:
                sales+= df[j]['order_price']
        sales_ranking.append(sales)
        sales_ranking_sort.append(sales)
        sales = 0
    sales_ranking_sort.sort()
    sales_ranking_sort.reverse()
    for k in range(n):
        top3_list.append(cli_name[sales_ranking.index(sales_ranking_sort[k])])

    """
    #匯出json格式
    df = list(CrosOrder.objects.filter(clientname__in = top3_list ,stadatetime__date__range=[date1[0],date2[0]],order_status="900").values().order_by("clientname","stadatetime","ga3"))
    df_len = len(df)
    info_list = get_info(df,df_len)

    df_json_list_all = []

    df_json_list_all.append({"clients":info_list[0],"products":info_list[1],"campaign":info_list[2],"ga1":info_list[3],"ga2":info_list[4],"ga3":info_list[5],"media":info_list[6],"link_type":info_list[7]})

    df_json_list_day = json_cros(df,df_len,date1,date2)
    df_json_list_all.append(df_json_list_day)
    
    df_json_list_mon = json_month_cros(df_json_list_day)
    df_json_list_all.append(df_json_list_mon)

    df_json_list_sea = json_season_cros(df_json_list_day)
    df_json_list_all.append(df_json_list_sea)
    """
    print(time.time()-st)
    return top3_list




def data_view():
    
    df = ClientProduct.objects.all()
    df = list(df.values())
    return df


#下載excel檔功能
def to_excel(mode,x,username):
    df_list = []
    
    if mode == "cros":
        col = ['clientname','productname','date','cv','profit','unitprice','ordertype','regular']#'新規','既存','都度','定期']
        for i in range(3):
            df_list.append(pd.DataFrame(columns=col))
            df_ord_list = [[],[]]
            df_reg_list = [[],[]]
            for j in range(len(x[i+1])):
                df_list[i].loc[j] = x[i+1][j]
                df_ord_list[0].append(x[i+1][j]['ordertype'][0])
                df_ord_list[1].append(x[i+1][j]['ordertype'][1])
                df_reg_list[0].append(x[i+1][j]['regular'][0])
                df_reg_list[1].append(x[i+1][j]['regular'][1])
            df_list[i]['新規'] = df_ord_list[0]
            df_list[i]['既存'] = df_ord_list[1]
            df_list[i]['都度'] = df_reg_list[1]
            df_list[i]['定期'] = df_reg_list[0]
            df_list[i] = df_list[i].drop('ordertype',axis = 1)
            df_list[i] = df_list[i].drop('regular',axis = 1)

    elif mode == "fb" or mode == "line":
        col = ['clientname','productname','date','impressions','clicks','cv','cost','ctr','cvr','cpc','cpm','cpo']
        for i in range(3):
            df_list.append(pd.DataFrame(columns=col))
            for j in range(len(x[i+1])):
                df_list[i].loc[j] = x[i+1][j]
                

    if mode == "cros":
        df_list[0].fillna(0, inplace=True)
        df_total = df_list[0].groupby("clientname").sum()
        df_total['unitprice'] = df_total['profit']/df_total['cv']
        df_list.append(df_total)
    else:
        df_list[0].fillna(0, inplace=True)
        df_total = df_list[0].groupby("clientname").sum()
        df_total["ctr"] = (df_total["clicks"]/df_total["impressions"]) *100
        df_total["cvr"] = (df_total["cv"]/df_total["clicks"]) *100
        df_total["cpc"] = df_total["cost"]/df_total["clicks"]
        df_total["cpm"] = df_total["cost"]/df_total["impressions"] *1000
        df_total["cpo"] = df_total["cost"]/df_total["cv"]
        df_list.append(df_total)
    with pd.ExcelWriter("./download/"+ str(username) +".xlsx") as writer:
        df_list[3].to_excel(writer,sheet_name="total")
        df_list[0].to_excel(writer,sheet_name="days")
        df_list[1].to_excel(writer,sheet_name="month")
        df_list[2].to_excel(writer,sheet_name="season")

#日期格式函式
def dateToDf(date1,date2):
    if date1 == ['']:
        date1[0] = datetime.today() - dt.timedelta(days = 30)
    else:
        date1[0] = datetime.strptime(date1[0],"%Y-%m-%d")

    if date2 == ['']:
        date2[0] = datetime.today()
    else:
        date2[0] = datetime.strptime(date2[0],"%Y-%m-%d")

    if date1[0] > date2[0]:
        tmp = date1[0]
        date1[0] = date2[0]
        date2[0] = tmp
    return date1,date2

#資料庫搜尋函式
def queryCros(date1,date2,cli,pro,cam,g1,g2,g3,med,lin,pay,reg,ord,ordS,ordP,delF):
    if len(cli) >1:
        query_cli = Q(clientname__in = cli)
        #query_cli = reduce(operator.or_,(Q(clientname__icontains = i )for i in cli))
    elif cli[0] == "":
        query_cli = Q()
    else:
        query_cli = Q(clientname__icontains =cli[0])

    if len(pro) >1:
        query_pro = reduce(operator.or_,(Q(productname__icontains = i )for i in pro))
    elif pro[0] == "":
        query_pro = Q()
    else:
        query_pro = Q(productname__icontains =pro[0])
    
    if len(cam) >1:
        query_cam = reduce(operator.or_,(Q(campaign__icontains = i )for i in cam))
    elif cam[0] == "":
        query_cam = Q()
    else:
        query_cam = Q(campaign__icontains =cam[0])

    if len(g1) >1:
        query_g1 = reduce(operator.or_,(Q(ga1__icontains = i )for i in g1))
    elif g1[0] == "":
        query_g1 = Q()
    else:
        query_g1 = Q(ga1__icontains =g1[0])

    if len(g2) >1:
        query_g2 = reduce(operator.or_,(Q(ga2__icontains = i )for i in g2))
    elif g2[0] == "":
        query_g2 = Q()
    else:
        query_g2 = Q(ga2__icontains =g2[0])

    if len(g3) >1:
        query_g3 = reduce(operator.or_,(Q(ga3__icontains = i )for i in g3))
    elif g3[0] == "":
        query_g3 = Q()
    else:
        query_g3 = Q(ga3__icontains =g3[0])

    if len(med) >1:
        query_med = reduce(operator.or_,(Q(media__icontains = i )for i in med))
    elif med[0] == "":
        query_med = Q()
    else:
        query_med = Q(media__icontains =med[0])
    
    if len(lin) >1:
        query_lin = reduce(operator.or_,(Q(link_type__icontains = i )for i in lin))
    elif lin[0] == "":
        query_lin = Q()
    else:
        query_lin = Q(link_type__icontains =lin[0])
    
    if len(pay) >1:
        query_pay = reduce(operator.or_,(Q(pay_method__icontains = i )for i in pay))
    elif pay[0] == "":
        query_pay = Q()
    else:
        query_pay = Q(pay_method__icontains =pay[0])
    
    if len(reg) >1:
        query_reg = reduce(operator.or_,(Q(regular__icontains = i )for i in reg))
    elif reg[0] == "":
        query_reg = Q()
    else:
        query_reg = Q(regular__icontains =reg[0])
    
    if len(ord) >1:
        query_ord = reduce(operator.or_,(Q(ordertype__icontains = i )for i in ord))
    elif ord[0] == "":
        query_ord = Q()
    else:
        query_ord = Q(ordertype__icontains =ord[0])

    if len(ordS) >1:
        query_ordS = reduce(operator.or_,(Q(order_status__icontains = i )for i in ordS))
    elif ordS[0] == "":
        query_ordS = Q()
    else:
        query_ordS = Q(order_status__icontains =ordS[0])

    if len(ordP) >1:
        query_ordP = reduce(operator.or_,(Q(order_path__icontains = i )for i in ordP))
    elif ordP[0] == "":
        query_ordP = Q()
    else:
        query_ordP = Q(order_path__icontains =ordP[0])

    if len(delF) >1:
        query_delF = reduce(operator.or_,(Q(del_flg__icontains = i )for i in delF))
    elif delF[0] == "":
        query_delF = Q()
    else:
        query_delF = Q(del_flg__icontains =delF[0])
    

    df = list(CrosOrderShort.objects.filter(query_cli,query_pro,query_cam,query_g1,query_g2,query_g3,query_med,query_pay,query_reg,query_ord,query_ordS,query_ordP,query_delF,stadatetime__date__range=[date1[0],date2[0]]).values().order_by("clientname","stadatetime","ga3"))
    #print(CrosOrderShort.objects.filter(query_cli,query_pro,query_cam,query_g1,query_g2,query_g3,query_med,query_pay,query_reg,query_ord,query_ordS,query_ordP,query_delF,stadatetime__date__range=[date1[0],date2[0]]).values().query)
    return df

def queryFB(date1,date2,cli,pro,acc,gro,cam,g1,g2,g3,lin,asn,an):
    #st = time.time()
    if len(cli) >1:
        query_cli = Q(clientname__in = cli)
        #query_cli = reduce(operator.or_,(Q(clientname__icontains = i )for i in cli))
    elif cli[0] == "":
        query_cli = Q()
    else:
        query_cli = Q(clientname__icontains =cli[0])

    if len(pro) >1:
        query_pro = reduce(operator.or_,(Q(productname__in = i )for i in pro))
    elif pro[0] == "":
        query_pro = Q()
    else:
        query_pro = Q(productname__icontains =pro[0])

    if len(acc) >1:
        query_acc = reduce(operator.or_,(Q(accountname__in = i )for i in acc))
    elif acc[0] == "":
        query_acc = Q()
    else:
        query_acc = Q(accountname__icontains =acc[0])

    if len(gro) >1:
        query_gro = reduce(operator.or_,(Q(group_type__in = i )for i in gro))
    elif gro[0] == "":
        query_gro = Q()
    else:
        query_gro = Q(group_type__icontains =gro[0])
    
    if len(cam) >1:
        query_cam = reduce(operator.or_,(Q(campaign__in = i )for i in cam))
    elif cam[0] == "":
        query_cam = Q()
    else:
        query_cam = Q(campaign__icontains =cam[0])

    if len(g1) >1:
        query_g1 = reduce(operator.or_,(Q(ga1__in = i )for i in g1))
    elif g1[0] == "":
        query_g1 = Q()
    else:
        query_g1 = Q(ga1__in =g1[0])

    if len(g2) >1:
        query_g2 = reduce(operator.or_,(Q(ga2__in = i )for i in g2))
    elif g2[0] == "":
        query_g2 = Q()
    else:
        query_g2 = Q(ga2__in =g2[0])

    if len(g3) >1:
        query_g3 = reduce(operator.or_,(Q(ga3__in = i )for i in g3))
    elif g3[0] == "":
        query_g3 = Q()
    else:
        query_g3 = Q(ga3__in =g3[0])

    if len(asn) >1:
        query_asn = reduce(operator.or_,(Q(ad_set_name__in = i )for i in asn))
    elif asn[0] == "":
        query_asn = Q()
    else:
        query_asn = Q(ad_set_name__icontains = asn[0])

    if len(an) >1:
        query_an = reduce(operator.or_,(Q(ad_name__in = i )for i in an))
    elif an[0] == "":
        query_an = Q()
    else:
        query_an = Q(ad_name__icontains =an[0])

    if len(lin) >1:
        query_lin = reduce(operator.or_,(Q(link_type__in = i )for i in lin))
    elif lin[0] == "":
        query_lin = Q()
    else:
        query_lin = Q(link_type__icontains =lin[0])
    #print(V_fb_universal.objects.filter(query_cli,query_pro,query_acc,query_gro,query_cam,query_g1,query_g2,query_g3,query_asn,query_an,query_lin,stadatetime__date__range=[date1[0],date2[0]]).values().order_by("clientname","stadatetime").query)
    #df = FbUniversal.objects.filter(query_cli,query_pro,query_acc,query_gro,query_cam,query_g1,query_g2,query_g3,query_asn,query_an,query_lin,stadatetime__date__range=[date1[0],date2[0]]).values().order_by("clientname","stadatetime")
    df = list(FbUniversalAd.objects.filter(query_cli,query_pro,query_acc,query_gro,query_cam,query_g1,query_g2,query_g3,query_asn,query_an,query_lin,stadatetime__date__range=[date1[0],date2[0]]).values(
    ).order_by("productname","stadatetime"))
    #print(FbUniversalAd.objects.filter(query_cli,query_pro,query_acc,query_gro,query_cam,query_g1,query_g2,query_g3,query_asn,query_an,query_lin,stadatetime__date__range=[date1[0],date2[0]]).values(
    #).query)

    return df  

def queryLine(date1,date2,cli,pro,acc,gro,cam,g1,g2,g3,lin,asn,an):
    #st = time.time()
    if len(cli) >1:
        query_cli = Q(clientname__in = cli)
        #query_cli = reduce(operator.or_,(Q(clientname__icontains = i )for i in cli))
    elif cli[0] == "":
        query_cli = Q()
    else:
        query_cli = Q(clientname__icontains =cli[0])

    if len(pro) >1:
        query_pro = reduce(operator.or_,(Q(productname__in = i )for i in pro))
    elif pro[0] == "":
        query_pro = Q()
    else:
        query_pro = Q(productname__icontains =pro[0])

    if len(acc) >1:
        query_acc = reduce(operator.or_,(Q(accountname__in = i )for i in acc))
    elif acc[0] == "":
        query_acc = Q()
    else:
        query_acc = Q(accountname__icontains =acc[0])

    if len(gro) >1:
        query_gro = reduce(operator.or_,(Q(group_type__in = i )for i in gro))
    elif gro[0] == "":
        query_gro = Q()
    else:
        query_gro = Q(group_type__icontains =gro[0])
    
    if len(cam) >1:
        query_cam = reduce(operator.or_,(Q(campaign__in = i )for i in cam))
    elif cam[0] == "":
        query_cam = Q()
    else:
        query_cam = Q(campaign__icontains =cam[0])

    if len(g1) >1:
        query_g1 = reduce(operator.or_,(Q(ga1__in = i )for i in g1))
    elif g1[0] == "":
        query_g1 = Q()
    else:
        query_g1 = Q(ga1__in =g1[0])

    if len(g2) >1:
        query_g2 = reduce(operator.or_,(Q(ga2__in = i )for i in g2))
    elif g2[0] == "":
        query_g2 = Q()
    else:
        query_g2 = Q(ga2__in =g2[0])

    if len(g3) >1:
        query_g3 = reduce(operator.or_,(Q(ga3__in = i )for i in g3))
    elif g3[0] == "":
        query_g3 = Q()
    else:
        query_g3 = Q(ga3__in =g3[0])

    if len(asn) >1:
        query_asn = reduce(operator.or_,(Q(adgroup_name__in = i )for i in asn))
    elif asn[0] == "":
        query_asn = Q()
    else:
        query_asn = Q(adgroup_name__icontains = asn[0])

    if len(an) >1:
        query_an = reduce(operator.or_,(Q(ad_name__in = i )for i in an))
    elif an[0] == "":
        query_an = Q()
    else:
        query_an = Q(ad_name__icontains =an[0])

    if len(lin) >1:
        query_lin = reduce(operator.or_,(Q(link_type__in = i )for i in lin))
    elif lin[0] == "":
        query_lin = Q()
    else:
        query_lin = Q(link_type__icontains =lin[0])
    #print(V_fb_universal.objects.filter(query_cli,query_pro,query_acc,query_gro,query_cam,query_g1,query_g2,query_g3,query_asn,query_an,query_lin,stadatetime__date__range=[date1[0],date2[0]]).values().order_by("clientname","stadatetime").query)
    #df = FbUniversal.objects.filter(query_cli,query_pro,query_acc,query_gro,query_cam,query_g1,query_g2,query_g3,query_asn,query_an,query_lin,stadatetime__date__range=[date1[0],date2[0]]).values().order_by("clientname","stadatetime")
    df = list(LineUniversalAd.objects.filter(query_cli,query_pro,query_acc,query_gro,query_cam,query_g1,query_g2,query_g3,query_asn,query_an,query_lin,stadatetime__date__range=[date1[0],date2[0]]).values(
    ).order_by("productname","stadatetime"))
    #print(FbUniversalAd.objects.filter(query_cli,query_pro,query_acc,query_gro,query_cam,query_g1,query_g2,query_g3,query_asn,query_an,query_lin,stadatetime__date__range=[date1[0],date2[0]]).values(
    #).query)

    return df  


'''
def queryForDB(date1,date2,cli,pro,cam,g1,g2,g3,med,lin,pay,reg,ord):
    if len(cli) >1:
        query_cli = Q(clientname__in = cli)
        #query_cli = reduce(operator.or_,(Q(clientname__icontains = i )for i in cli))
    elif cli[0] == "":
        query_cli = Q()
    else:
        query_cli = Q(clientname__icontains =cli[0])

    if len(pro) >1:
        query_pro = reduce(operator.or_,(Q(productname__icontains = i )for i in pro))
    elif pro[0] == "":
        query_pro = Q()
    else:
        query_pro = Q(productname__icontains =pro[0])
    
    if len(cam) >1:
        query_cam = reduce(operator.or_,(Q(campaign__icontains = i )for i in cam))
    elif cam[0] == "":
        query_cam = Q()
    else:
        query_cam = Q(campaign__icontains =cam[0])

    if len(g1) >1:
        query_g1 = reduce(operator.or_,(Q(ga1__icontains = i )for i in g1))
    elif g1[0] == "":
        query_g1 = Q()
    else:
        query_g1 = Q(ga1__icontains =g1[0])

    if len(g2) >1:
        query_g2 = reduce(operator.or_,(Q(ga2__icontains = i )for i in g2))
    elif g2[0] == "":
        query_g2 = Q()
    else:
        query_g2 = Q(ga2__icontains =g2[0])

    if len(g3) >1:
        query_g3 = reduce(operator.or_,(Q(ga3__icontains = i )for i in g3))
    elif g3[0] == "":
        query_g3 = Q()
    else:
        query_g3 = Q(ga3__icontains =g3[0])

    if len(med) >1:
        query_med = reduce(operator.or_,(Q(media__icontains = i )for i in med))
    elif med[0] == "":
        query_med = Q()
    else:
        query_med = Q(media__icontains =med[0])
    """
    if len(lin) >1:
        query_lin = reduce(operator.or_,(Q(link_type__icontains = i )for i in lin))
    elif lin[0] == "":
        query_lin = Q()
    else:
        query_lin = Q(link_type__icontains =lin[0])
    """
    if len(pay) >1:
        query_pay = reduce(operator.or_,(Q(pay_method__icontains = i )for i in pay))
    elif pay[0] == "":
        query_pay = Q()
    else:
        query_pay = Q(pay_method__icontains =pay[0])
    
    if len(reg) >1:
        query_reg = reduce(operator.or_,(Q(regular__icontains = i )for i in reg))
    elif reg[0] == "":
        query_reg = Q()
    else:
        query_reg = Q(regular__icontains =reg[0])
    
    if len(ord) >1:
        query_ord = reduce(operator.or_,(Q(order_type__icontains = i )for i in ord))
    elif ord[0] == "":
        query_ord = Q()
    else:
        query_ord = Q(order_type__icontains =ord[0])

    df = list(CrosOrderShort.objects.filter(query_cli,query_pro,query_cam,query_g1,query_g2,query_g3,query_med,query_pay,query_reg,query_ord,stadatetime__date__range=[date1[0],date2[0]],order_status="900").values().order_by("clientname","stadatetime","ga3"))
    
    return df

def queryForDB_fb(date1,date2,cli,pro,cam,g1,g2,g3,med,lin):
    if len(cli) >1:
        query_cli = Q(clientname__in = cli)
        #query_cli = reduce(operator.or_,(Q(clientname__icontains = i )for i in cli))
    elif cli[0] == "":
        query_cli = Q()
    else:
        query_cli = Q(clientname__icontains =cli[0])

    if len(pro) >1:
        query_pro = reduce(operator.or_,(Q(productname__icontains = i )for i in pro))
    elif pro[0] == "":
        query_pro = Q()
    else:
        query_pro = Q(productname__icontains =pro[0])
    
    if len(cam) >1:
        query_cam = reduce(operator.or_,(Q(campaign__icontains = i )for i in cam))
    elif cam[0] == "":
        query_cam = Q()
    else:
        query_cam = Q(campaign__icontains =cam[0])

    if len(g1) >1:
        query_g1 = reduce(operator.or_,(Q(ga1__icontains = i )for i in g1))
    elif g1[0] == "":
        query_g1 = Q()
    else:
        query_g1 = Q(ga1__icontains =g1[0])

    if len(g2) >1:
        query_g2 = reduce(operator.or_,(Q(ga2__icontains = i )for i in g2))
    elif g2[0] == "":
        query_g2 = Q()
    else:
        query_g2 = Q(ga2__icontains =g2[0])

    if len(g3) >1:
        query_g3 = reduce(operator.or_,(Q(ga3__icontains = i )for i in g3))
    elif g3[0] == "":
        query_g3 = Q()
    else:
        query_g3 = Q(ga3__icontains =g3[0])

    if len(med) >1:
        query_med = reduce(operator.or_,(Q(media__icontains = i )for i in med))
    elif med[0] == "":
        query_med = Q()
    else:
        query_med = Q(media__icontains =med[0])
    """
    if len(lin) >1:
        query_lin = reduce(operator.or_,(Q(link_type__icontains = i )for i in lin))
    elif lin[0] == "":
        query_lin = Q()

    else:
        query_lin = Q(link_type__icontains =lin[0])
    """
    #print(V_facebook.objects.filter(query_cli,query_pro,query_cam,query_g1,query_g2,query_g3,query_med,query_lin,stadatetime__date__range=[date1[0],date2[0]]).query)
    df = list(FbUniversalAd.objects.filter(query_cli,query_pro,query_cam,query_g1,query_g2,query_g3,stadatetime__date__range=[date1[0],date2[0]]).values().order_by("clientname","stadatetime"))
    return df

def queryForDB_line(date1,date2,cli,pro,cam,g1,g2,g3,med,lin):
    if len(cli) >1:
        query_cli = Q(clientname__in = cli)
        #query_cli = reduce(operator.or_,(Q(clientname__icontains = i )for i in cli))
    elif cli[0] == "":
        query_cli = Q()
    else:
        query_cli = Q(clientname__icontains =cli[0])

    if len(pro) >1:
        query_pro = reduce(operator.or_,(Q(productname__icontains = i )for i in pro))
    elif pro[0] == "":
        query_pro = Q()
    else:
        query_pro = Q(productname__icontains =pro[0])
    
    if len(cam) >1:
        query_cam = reduce(operator.or_,(Q(campaign__icontains = i )for i in cam))
    elif cam[0] == "":
        query_cam = Q()
    else:
        query_cam = Q(campaign__icontains =cam[0])

    if len(g1) >1:
        query_g1 = reduce(operator.or_,(Q(ga1__icontains = i )for i in g1))
    elif g1[0] == "":
        query_g1 = Q()
    else:
        query_g1 = Q(ga1__icontains =g1[0])

    if len(g2) >1:
        query_g2 = reduce(operator.or_,(Q(ga2__icontains = i )for i in g2))
    elif g2[0] == "":
        query_g2 = Q()
    else:
        query_g2 = Q(ga2__icontains =g2[0])

    if len(g3) >1:
        query_g3 = reduce(operator.or_,(Q(ga3__icontains = i )for i in g3))
    elif g3[0] == "":
        query_g3 = Q()
    else:
        query_g3 = Q(ga3__icontains =g3[0])

    if len(med) >1:
        query_med = reduce(operator.or_,(Q(media__icontains = i )for i in med))
    elif med[0] == "":
        query_med = Q()
    else:
        query_med = Q(media__icontains =med[0])
    """
    if len(lin) >1:
        query_lin = reduce(operator.or_,(Q(link_type__icontains = i )for i in lin))
    elif lin[0] == "":
        query_lin = Q()
    else:
        query_lin = Q(link_type__icontains =lin[0])
    """

    df = list(LineUniversalAd.objects.filter(query_cli,query_pro,query_cam,query_g1,query_g2,query_g3,query_med,stadatetime__date__range=[date1[0],date2[0]]).values().order_by("clientname","stadatetime","ga3"))
    return df
'''
# 分天加總

def json_Line(df,df_len,date1,date2):
    
    #st = time.time()
        #同日期加總
    df_json_list = []
    #第一筆為資訊包
    df_json = {'industrytype':"",'clientname':"",'productname':"",'date':"","impressions":"","clicks":"",'cv':"","cost":"","ctr":"","cvr":"","cpc":"","cpm":"","cpo":""}
    constrct_list =[date1[0].date(),df[0]["productname"]]
    impressions = 0
    clicks = 0
    cv = 0
    cost = 0

    for i in range(df_len):
        #最後一筆的情況
        #會出現極端狀況，當最後一筆資料為獨立資料時，會出現怪狀況，這個等之後再討論


        if constrct_list[0] != df[i]["stadatetime"].date() and i==0:
            dateRange = -(constrct_list[0] - df[i]["stadatetime"].date()).days
                
            for j in range(dateRange):
                df_json_list.append({'industrytype':df[i]["industrytype"],'clientname':df[i]["clientname"],'productname':df[i]["productname"],'date':str(constrct_list[0]+ dt.timedelta(days=j)),"impressions":0,"clicks":0,'cv':0,'cost':0,'ctr':0,"cvr":0,"cpc":0,"cpm":0,"cpo":0})

            df_json = {'industrytype':"",'clientname':"",'productname':"",'date':"","impressions":"","clicks":"",'cv':"","cost":"","ctr":"","cvr":"","cpc":"","cpm":"","cpo":""}
            impressions = df[i]["impressions"]
            clicks = df[i]["clicks"]
            cv = df[i]["cv"]
            cost = df[i]["cost"]
            
            constrct_list[0] = df[i]["stadatetime"].date()
    
        elif constrct_list[0] == df[i]["stadatetime"].date() and constrct_list[1] == df[i]["productname"] :
            impressions += df[i]["impressions"]
            clicks += df[i]["clicks"]
            cv += df[i]["cv"]
            cost += df[i]["cost"]
        else:
            df_json['industrytype'] = df[i-1]["industrytype"]
            df_json['clientname'] = df[i-1]["clientname"]
            df_json['productname'] = df[i-1]["productname"]
            df_json['date'] = str(constrct_list[0])
            df_json['impressions'] = impressions
            df_json['clicks'] = clicks
            df_json['cv'] = cv
            df_json['cost'] = cost
            
            try:
                df_json['cvr'] = (cv/clicks)*100
                df_json['cpc'] = cost/clicks
            except ZeroDivisionError:
                df_json['cvr'] = 0
                df_json['cpc'] = 0
            try:
                df_json['ctr'] = (clicks/impressions)*100
                df_json['cpm'] = (cost/impressions)*1000
            except ZeroDivisionError:
                df_json['ctr'] = 0
                df_json['cpm'] = 0
            try:
                df_json['cpo'] = cost/cv
            except ZeroDivisionError:
                df_json['cpo'] = 0    
            df_json_list.append(df_json)

            if constrct_list[0] ==(df[i]["stadatetime"].date() - dt.timedelta(days=1)) and constrct_list[1] == df[i]["productname"] :
                #Reset
                df_json = {'industrytype':"",'clientname':"",'productname':"",'date':"","impressions":"","clicks":"",'cv':"","cost":"","ctr":"","cvr":"","cpc":"","cpm":"","cpo":""}
                impressions = df[i]["impressions"]
                clicks = df[i]["clicks"]
                cv = df[i]["cv"]
                cost = df[i]["cost"]
           
                constrct_list[0] = df[i]["stadatetime"].date()
            #加入空值
            elif constrct_list[0] != (df[i]["stadatetime"].date() - dt.timedelta(days=1)) and constrct_list[1] == df[i]["productname"]:
                
                dateRange = -(constrct_list[0] - df[i]["stadatetime"].date()).days
                
                for j in range(dateRange-1):
                    df_json_list.append({'industrytype':df[i]["industrytype"],'clientname':df[i]["clientname"],'productname':df[i]["productname"],'date':str(constrct_list[0]+ dt.timedelta(days=j+1)),"impressions":0,"clicks":0,'cv':0,'cost':0,'ctr':0,"cvr":0,"cpc":0,"cpm":0,"cpo":0})

                df_json = {'industrytype':"",'clientname':"",'productname':"",'date':"","impressions":"","clicks":"",'cv':"","cost":"","ctr":"","cvr":"","cpc":"","cpm":"","cpo":""}
                impressions = df[i]["impressions"]
                clicks = df[i]["clicks"]
                cv = df[i]["cv"]
                cost = df[i]["cost"]  
                constrct_list[0] = df[i]["stadatetime"].date()
            else:
                
                df_json = {'industrytype':"",'clientname':"",'productname':"",'date':"","impressions":"","clicks":"",'cv':"","cost":"","ctr":"","cvr":"","cpc":"","cpm":"","cpo":""}
                constrct_list[0] = df[i]["stadatetime"].date()
                constrct_list[1] = df[i]["productname"]
                impressions = df[i]["impressions"]
                clicks = df[i]["clicks"]
                cv = df[i]["cv"]
                cost = df[i]["cost"]

        if i == (df_len-1):
            df_json['industrytype'] = df[i]["industrytype"]
            df_json['clientname'] = df[i]["clientname"]
            df_json['productname'] = df[i]["productname"]
            df_json['date'] = str(df[i]["stadatetime"])[:10]
            df_json['impressions'] = impressions
            df_json['clicks'] = clicks
            df_json['cv'] = cv
            df_json['cost'] = cost
            try:
                df_json['cvr'] = (cv/clicks)*100
                df_json['cpc'] = cost/clicks
            except ZeroDivisionError:
                df_json['cvr'] = 0
                df_json['cpc'] = 0
            try:
                df_json['ctr'] = (clicks/impressions)*100
                df_json['cpm'] = (cost/impressions)*1000
            except ZeroDivisionError:
                df_json['ctr'] = 0
                df_json['cpm'] = 0
            try:
                df_json['cpo'] = cost/cv
            except ZeroDivisionError:
                df_json['cpo'] = 0    

            df_json_list.append(df_json)
            break
    #print(time.time() - st)
    return df_json_list

def json_FB(df,df_len,date1,date2):
    
    #st = time.time()
        #同日期加總
    df_json_list = []
    #第一筆為資訊包
    df_json = {'industrytype':"",'clientname':"",'productname':"",'date':"","impressions":"","clicks":"",'cv':"","cost":"","ctr":"","cvr":"","cpc":"","cpm":"","cpo":""}
    constrct_list =[date1[0].date(),df[0]["productname"]]
    impressions = 0
    clicks = 0
    cv = 0
    cost = 0

    for i in range(df_len):
        #最後一筆的情況
        #會出現極端狀況，當最後一筆資料為獨立資料時，會出現怪狀況，這個等之後再討論


        if constrct_list[0] != df[i]["stadatetime"].date() and i==0:
            dateRange = -(constrct_list[0] - df[i]["stadatetime"].date()).days
                
            for j in range(dateRange):
                df_json_list.append({'industrytype':df[i]["industrytype"],'clientname':df[i]["clientname"],'productname':df[i]["productname"],'date':str(constrct_list[0]+ dt.timedelta(days=j)),"impressions":0,"clicks":0,'cv':0,'cost':0,'ctr':0,"cvr":0,"cpc":0,"cpm":0,"cpo":0})

            df_json = {'industrytype':"",'clientname':"",'productname':"",'date':"","impressions":"","clicks":"",'cv':"","cost":"","ctr":"","cvr":"","cpc":"","cpm":"","cpo":""}
            impressions = df[i]["impressions"]
            clicks = df[i]["clicks"]
            cv = df[i]["cv"]
            cost = df[i]["cost"]
            
            constrct_list[0] = df[i]["stadatetime"].date()
    
        elif constrct_list[0] == df[i]["stadatetime"].date() and constrct_list[1] == df[i]["productname"] :
            impressions += df[i]["impressions"]
            clicks += df[i]["clicks"]
            cv += df[i]["cv"]
            cost += df[i]["cost"]
        else:
            df_json['industrytype'] = df[i-1]["industrytype"]
            df_json['clientname'] = df[i-1]["clientname"]
            df_json['productname'] = df[i-1]["productname"]
            df_json['date'] = str(constrct_list[0])
            df_json['impressions'] = impressions
            df_json['clicks'] = clicks
            df_json['cv'] = cv
            df_json['cost'] = cost
            
            try:
                df_json['cvr'] = (cv/clicks)*100
                df_json['cpc'] = cost/clicks
            except ZeroDivisionError:
                df_json['cvr'] = 0
                df_json['cpc'] = 0
            try:
                df_json['ctr'] = (clicks/impressions)*100
                df_json['cpm'] = (cost/impressions)*1000
            except ZeroDivisionError:
                df_json['ctr'] = 0
                df_json['cpm'] = 0
            try:
                df_json['cpo'] = cost/cv
            except ZeroDivisionError:
                df_json['cpo'] = 0    
            df_json_list.append(df_json)

            if constrct_list[0] ==(df[i]["stadatetime"].date() - dt.timedelta(days=1)) and constrct_list[1] == df[i]["productname"] :
                #Reset
                df_json = {'industrytype':"",'clientname':"",'productname':"",'date':"","impressions":"","clicks":"",'cv':"","cost":"","ctr":"","cvr":"","cpc":"","cpm":"","cpo":""}
                impressions = df[i]["impressions"]
                clicks = df[i]["clicks"]
                cv = df[i]["cv"]
                cost = df[i]["cost"]
           
                constrct_list[0] = df[i]["stadatetime"].date()
            #加入空值
            elif constrct_list[0] != (df[i]["stadatetime"].date() - dt.timedelta(days=1)) and constrct_list[1] == df[i]["productname"]:
                
                dateRange = -(constrct_list[0] - df[i]["stadatetime"].date()).days
                
                for j in range(dateRange-1):
                    df_json_list.append({'industrytype':df[i]["industrytype"],'clientname':df[i]["clientname"],'productname':df[i]["productname"],'date':str(constrct_list[0]+ dt.timedelta(days=j+1)),"impressions":0,"clicks":0,'cv':0,'cost':0,'ctr':0,"cvr":0,"cpc":0,"cpm":0,"cpo":0})

                df_json = {'industrytype':"",'clientname':"",'productname':"",'date':"","impressions":"","clicks":"",'cv':"","cost":"","ctr":"","cvr":"","cpc":"","cpm":"","cpo":""}
                impressions = df[i]["impressions"]
                clicks = df[i]["clicks"]
                cv = df[i]["cv"]
                cost = df[i]["cost"]  
                constrct_list[0] = df[i]["stadatetime"].date()
            else:
                
                df_json = {'industrytype':"",'clientname':"",'productname':"",'date':"","impressions":"","clicks":"",'cv':"","cost":"","ctr":"","cvr":"","cpc":"","cpm":"","cpo":""}
                constrct_list[0] = df[i]["stadatetime"].date()
                constrct_list[1] = df[i]["productname"]
                impressions = df[i]["impressions"]
                clicks = df[i]["clicks"]
                cv = df[i]["cv"]
                cost = df[i]["cost"]

        if i == (df_len-1):
            df_json['industrytype'] = df[i]["industrytype"]
            df_json['clientname'] = df[i]["clientname"]
            df_json['productname'] = df[i]["productname"]
            df_json['date'] = str(df[i]["stadatetime"])[:10]
            df_json['impressions'] = impressions
            df_json['clicks'] = clicks
            df_json['cv'] = cv
            df_json['cost'] = cost
            try:
                df_json['cvr'] = (cv/clicks)*100
                df_json['cpc'] = cost/clicks
            except ZeroDivisionError:
                df_json['cvr'] = 0
                df_json['cpc'] = 0
            try:
                df_json['ctr'] = (clicks/impressions)*100
                df_json['cpm'] = (cost/impressions)*1000
            except ZeroDivisionError:
                df_json['ctr'] = 0
                df_json['cpm'] = 0
            try:
                df_json['cpo'] = cost/cv
            except ZeroDivisionError:
                df_json['cpo'] = 0    

            df_json_list.append(df_json)
            break
    #print(time.time() - st)
    return df_json_list

def json_Cros(df,df_len,date1,date2,marg):
    #同日期加總
    df_json_list = []
    #第一筆為資訊包
    df_json = {'clientname':"",'productname':"",'date':"",'cv':"",'profit':"",'unitprice':"","ordertype":"","regular":""}
    constrct_list =[date1[0].date(),df[0]["clientname"]]
    i_list = []
    cv = 0
    profit = 0
    orderTypeInfo = [0,0] #新規,既存
    regularInfo = [0,0]   #都度,定期

    for i in range(df_len):
        
        if constrct_list[0] != df[i]["stadatetime"].date() and i==0:
            dateRange = -(constrct_list[0] - df[i]["stadatetime"].date()).days
                
            for j in range(dateRange):
                df_json_list.append({'clientname':df[i]["clientname"],'productname':df[i]["productname"],'date':str(constrct_list[0]+ dt.timedelta(days=j)),'cv':0,'profit':0,'unitprice':0,"ordertype":[0,0],"regular":[0,0]})

            df_json = {'clientname':"",'productname':"",'date':"",'cv':"",'profit':"",'unitprice':"","ordertype":"","regular":""}
            cv = 1
            profit = df[i]["order_price"]
            orderTypeInfo = [0,0] 
            regularInfo = [0,0]   
            if df[i]["ordertype"] == "新規":
                orderTypeInfo[0]+=1
            elif df[i]["ordertype"] == "既存":
                orderTypeInfo[1]+=1                
            if df[i]["regular"] == 1:
                regularInfo[0]+=1
            elif df[i]["regular"] == 0: #定期
                regularInfo[1]+=1
            constrct_list[0] = df[i]["stadatetime"].date()
    
        elif constrct_list[0] == df[i]["stadatetime"].date() and constrct_list[1] == df[i]["clientname"] :
            
            cv+=1
            profit+=df[i]["order_price"]
            #新規既存判斷
            if df[i]["ordertype"] == "新規":
                orderTypeInfo[0]+=1
            elif df[i]["ordertype"] == "既存":
                orderTypeInfo[1]+=1
            #定期都度判斷
            if df[i]["regular"] == 1:
                regularInfo[0]+=1
            elif df[i]["regular"] == 0:
                regularInfo[1]+=1

            
        else:
            
            df_json['clientname'] = df[i-1]["clientname"]
            df_json['productname'] = df[i-1]["productname"]
            df_json['date'] = str(constrct_list[0])
            df_json['cv'] = cv
            df_json['profit'] = profit/((100-marg)/100)
            df_json['ordertype'] = orderTypeInfo
            df_json['regular'] = regularInfo
            
            try:
                df_json['unitprice'] = profit/((100-marg)/100)/cv
            except ZeroDivisionError:
                df_json['unitprice'] =0
            df_json_list.append(df_json)

            if constrct_list[0] ==(df[i]["stadatetime"].date() - dt.timedelta(days=1)) and constrct_list[1] == df[i]["clientname"] :
                #Reset
                df_json = {'clientname':"",'productname':"",'date':"",'cv':"",'profit':"",'unitprice':"","ordertype":"","regular":""}
                cv = 1
                profit = df[i]["order_price"]
                orderTypeInfo = [0,0] 
                regularInfo = [0,0]   
                if df[i]["ordertype"] == "新規":
                    orderTypeInfo[0]+=1
                elif df[i]["ordertype"] == "既存":
                    orderTypeInfo[1]+=1                
                if df[i]["regular"] == 1:
                    regularInfo[0]+=1
                elif df[i]["regular"] == 0:
                    regularInfo[1]+=1
                constrct_list[0] = df[i]["stadatetime"].date()
            #加入空值
            elif constrct_list[0] != (df[i]["stadatetime"].date() - dt.timedelta(days=1)) and constrct_list[1] == df[i]["clientname"]:
                
                dateRange = -(constrct_list[0] - df[i]["stadatetime"].date()).days
                
                for j in range(dateRange-1):
                    df_json_list.append({'clientname':df[i]["clientname"],'productname':df[i]["productname"],'date':str(constrct_list[0]+ dt.timedelta(days=j+1)),'cv':0,'profit':0,'unitprice':0,"ordertype":[0,0],"regular":[0,0]})

                df_json = {'clientname':"",'productname':"",'date':"",'cv':"",'profit':"",'unitprice':"","ordertype":"","regular":""}
                cv = 1
                profit = df[i]["order_price"]
                orderTypeInfo = [0,0] 
                regularInfo = [0,0]   
                if df[i]["ordertype"] == "新規":
                    orderTypeInfo[0]+=1
                elif df[i]["ordertype"] == "既存":
                    orderTypeInfo[1]+=1                
                if df[i]["regular"] == 1:
                    regularInfo[0]+=1
                elif df[i]["regular"] == 0:
                    regularInfo[1]+=1
                constrct_list[0] = df[i]["stadatetime"].date()
            else:
                
                df_json = {'clientname':"",'productname':"",'date':"",'cv':"",'profit':"",'unitprice':"","ordertype":"","regular":""}
                constrct_list[0] = df[i]["stadatetime"].date()
                constrct_list[1] = df[i]["clientname"]
                cv = 1
                profit = df[i]["order_price"]
                orderTypeInfo = [0,0] 
                regularInfo = [0,0]   

                if df[i]["ordertype"] == "新規":
                    orderTypeInfo[0]+=1
                elif df[i]["ordertype"] == "既存":
                    orderTypeInfo[1]+=1                
                if df[i]["regular"] == 1:
                    regularInfo[0]+=1
                elif df[i]["regular"] == 0:
                    regularInfo[1]+=1
        if i == (df_len-1):
            df_json['clientname'] = df[i]["clientname"]
            df_json['productname'] = df[i]["productname"]
            df_json['date'] = str(df[i]["stadatetime"])[:10]
            df_json['cv'] = cv
            df_json['profit'] = profit/((100-marg)/100)
            df_json['ordertype'] = orderTypeInfo
            df_json['regular'] = regularInfo

            try:
                df_json['unitprice'] = profit/((100-marg)/100)/cv
            except ZeroDivisionError:
                df_json['unitprice'] =0
            df_json_list.append(df_json)
            break

    return df_json_list


# 分月

def json_month_Line(df_json_list):
    df = copy.deepcopy(df_json_list)
    df_json_list = []
    df_json = {'industrytype':"",'clientname':"",'productname':"",'date':"","impressions":"","clicks":"",'cv':"","cost":"","ctr":"","cvr":"","cpc":"","cpm":"","cpo":""}
    constrct_list =[df[0]["date"][:7],df[0]["productname"]]
    impressions = 0
    clicks = 0
    cv = 0
    cost = 0
    for i in range(len(df)):

        if constrct_list[0] == df[i]["date"][:7] and constrct_list[1] == df[i]["productname"] :
            impressions += df[i]["impressions"]
            clicks += df[i]["clicks"]
            cv += df[i]["cv"]
            cost += df[i]["cost"]
        else:
            df_json['industrytype'] = df[i-1]["industrytype"]
            df_json['clientname'] = df[i-1]["clientname"]
            df_json['productname'] = df[i-1]["productname"]
            df_json['date'] = constrct_list[0]
            df_json['impressions'] = impressions
            df_json['clicks'] = clicks
            df_json['cv'] = cv
            df_json['cost'] = cost
            
            try:
                df_json['cvr'] = (cv/clicks)*100
                df_json['cpc'] = cost/clicks
            except ZeroDivisionError:
                df_json['cvr'] = 0
                df_json['cpc'] = 0
            try:
                df_json['ctr'] = (clicks/impressions)*100
                df_json['cpm'] = (cost/impressions)*1000
            except ZeroDivisionError:
                df_json['ctr'] = 0
                df_json['cpm'] = 0
            try:
                df_json['cpo'] = cost/cv
            except ZeroDivisionError:
                df_json['cpo'] = 0    
            df_json_list.append(df_json)

            df_json = {'industrytype':"",'clientname':"",'productname':"",'date':"","impressions":"","clicks":"",'cv':"","cost":"","ctr":"","cvr":"","cpc":"","cpm":"","cpo":""}
            constrct_list[0] = df[i]["date"][:7]
            constrct_list[1] = df[i]["productname"]
            impressions = df[i]["impressions"]
            clicks = df[i]["clicks"]
            cv = df[i]["cv"]
            cost = df[i]["cost"]
        if i == len(df)-1:
            df_json['industrytype'] = df[i]["industrytype"]
            df_json['clientname'] = df[i]["clientname"]
            df_json['productname'] = df[i]["productname"]
            df_json['date'] = str(df[i]["date"])[:7]
            df_json['impressions'] = impressions
            df_json['clicks'] = clicks
            df_json['cv'] = cv
            df_json['cost'] = cost
            try:
                df_json['cvr'] = (cv/clicks)*100
                df_json['cpc'] = cost/clicks
            except ZeroDivisionError:
                df_json['cvr'] = 0
                df_json['cpc'] = 0
            try:
                df_json['ctr'] = (clicks/impressions)*100
                df_json['cpm'] = (cost/impressions)*1000
            except ZeroDivisionError:
                df_json['ctr'] = 0
                df_json['cpm'] = 0
            try:
                df_json['cpo'] = cost/cv
            except ZeroDivisionError:
                df_json['cpo'] = 0    

            df_json_list.append(df_json)
            break
    return df_json_list

def json_month_FB(df_json_list):
    df = copy.deepcopy(df_json_list)
    df_json_list = []
    df_json = {'industrytype':"",'clientname':"",'productname':"",'date':"","impressions":"","clicks":"",'cv':"","cost":"","ctr":"","cvr":"","cpc":"","cpm":"","cpo":""}
    constrct_list =[df[0]["date"][:7],df[0]["productname"]]
    impressions = 0
    clicks = 0
    cv = 0
    cost = 0
    for i in range(len(df)):

        if constrct_list[0] == df[i]["date"][:7] and constrct_list[1] == df[i]["productname"] :
            impressions += df[i]["impressions"]
            clicks += df[i]["clicks"]
            cv += df[i]["cv"]
            cost += df[i]["cost"]
        else:
            df_json['industrytype'] = df[i-1]["industrytype"]
            df_json['clientname'] = df[i-1]["clientname"]
            df_json['productname'] = df[i-1]["productname"]
            df_json['date'] = constrct_list[0]
            df_json['impressions'] = impressions
            df_json['clicks'] = clicks
            df_json['cv'] = cv
            df_json['cost'] = cost
            
            try:
                df_json['cvr'] = (cv/clicks)*100
                df_json['cpc'] = cost/clicks
            except ZeroDivisionError:
                df_json['cvr'] = 0
                df_json['cpc'] = 0
            try:
                df_json['ctr'] = (clicks/impressions)*100
                df_json['cpm'] = (cost/impressions)*1000
            except ZeroDivisionError:
                df_json['ctr'] = 0
                df_json['cpm'] = 0
            try:
                df_json['cpo'] = cost/cv
            except ZeroDivisionError:
                df_json['cpo'] = 0    
            df_json_list.append(df_json)

            df_json = {'industrytype':"",'clientname':"",'productname':"",'date':"","impressions":"","clicks":"",'cv':"","cost":"","ctr":"","cvr":"","cpc":"","cpm":"","cpo":""}
            constrct_list[0] = df[i]["date"][:7]
            constrct_list[1] = df[i]["productname"]
            impressions = df[i]["impressions"]
            clicks = df[i]["clicks"]
            cv = df[i]["cv"]
            cost = df[i]["cost"]
        if i == len(df)-1:
            df_json['industrytype'] = df[i]["industrytype"]
            df_json['clientname'] = df[i]["clientname"]
            df_json['productname'] = df[i]["productname"]
            df_json['date'] = str(df[i]["date"])[:7]
            df_json['impressions'] = impressions
            df_json['clicks'] = clicks
            df_json['cv'] = cv
            df_json['cost'] = cost
            try:
                df_json['cvr'] = (cv/clicks)*100
                df_json['cpc'] = cost/clicks
            except ZeroDivisionError:
                df_json['cvr'] = 0
                df_json['cpc'] = 0
            try:
                df_json['ctr'] = (clicks/impressions)*100
                df_json['cpm'] = (cost/impressions)*1000
            except ZeroDivisionError:
                df_json['ctr'] = 0
                df_json['cpm'] = 0
            try:
                df_json['cpo'] = cost/cv
            except ZeroDivisionError:
                df_json['cpo'] = 0    

            df_json_list.append(df_json)
            break
    return df_json_list

def json_month_Cros(df_json_list):
    df = copy.deepcopy(df_json_list)
    df_json_list = []
    df_json = {'clientname':"",'productname':"",'date':"",'cv':"",'profit':"",'unitprice':"","ordertype":"","regular":""}
    constrct_list =[df[0]["date"][:7],df[0]["clientname"]]
    cv = 0
    profit = 0
    orderTypeInfo = [0,0] #新規,既存
    regularInfo = [0,0]
    for i in range(len(df)):
        if i == len(df)-1:
            df_json['clientname'] = df[i]["clientname"]
            df_json['productname'] = df[i]["productname"]
            df_json['date'] = str(df[i]["date"])[:7]
            df_json['cv'] = cv+df[i]["cv"]
            df_json['profit'] = profit+df[i]["profit"]
            orderTypeInfo[0]+=df[i]["ordertype"][0]
            orderTypeInfo[1]+=df[i]["ordertype"][1]
            df_json['ordertype'] = orderTypeInfo
            regularInfo[0]+=df[i]["regular"][0]
            regularInfo[1]+=df[i]["regular"][1]
            df_json['regular'] = regularInfo

            try:
                df_json['unitprice'] = profit/cv
            except ZeroDivisionError:
                df_json['unitprice'] =0
            df_json_list.append(df_json)
            break
        elif constrct_list[0] == df[i]["date"][:7] and constrct_list[1] == df[i]["clientname"] :
            cv+=df[i]["cv"]
            profit+=df[i]["profit"]
            #新規既存判斷
            
            orderTypeInfo[0]+=df[i]["ordertype"][0]
            
            orderTypeInfo[1]+=df[i]["ordertype"][1]
            #定期都度判斷
            
            regularInfo[0]+=df[i]["regular"][0]
            
            regularInfo[1]+=df[i]["regular"][1]
            
        else:
            df_json['clientname'] = df[i-1]["clientname"]
            df_json['productname'] = df[i-1]["productname"]
            df_json['date'] = constrct_list[0]
            df_json['cv'] = cv
            df_json['profit'] = profit
            df_json['ordertype'] = orderTypeInfo
            df_json['regular'] = regularInfo
            
            try:
                df_json['unitprice'] = profit/cv
            except ZeroDivisionError:
                df_json['unitprice'] =0
            df_json_list.append(df_json)

            df_json = {'clientname':"",'productname':"",'date':"",'cv':"",'profit':"",'unitprice':"","ordertype":"","regular":""}
            constrct_list[0] = df[i]["date"][:7]
            constrct_list[1] = df[i]["clientname"]
            cv = df[i]["cv"]
            profit = df[i]["profit"]
            orderTypeInfo = [0,0] 
            regularInfo = [0,0]   
        
            orderTypeInfo[0]+=df[i]["ordertype"][0]
            
            orderTypeInfo[1]+=df[i]["ordertype"][1]
            #定期都度判斷
            
            regularInfo[0]+=df[i]["regular"][0]
            
            regularInfo[1]+=df[i]["regular"][1]
    
    return df_json_list


# 分季

def json_season_Line(df_json_list):
    season = {"01":"Q1","02":"Q1","03":"Q1","04":"Q2","05":"Q2","06":"Q2","07":"Q3","08":"Q3","09":"Q3","10":"Q4","11":"Q4","12":"Q4"}
    df = copy.deepcopy(df_json_list)
    df_json_list = []
    df_json = {'industrytype':"",'clientname':"",'productname':"",'date':"","impressions":"","clicks":"",'cv':"","cost":"","ctr":"","cvr":"","cpc":"","cpm":"","cpo":""}
    constrct_list =[df[0]["date"][:4]+"-"+season[df[0]["date"][5:7]],df[0]["productname"]] #1?0?
    impressions = 0
    clicks = 0
    cv = 0
    cost = 0
    for i in range(len(df)):
        
        df[i]["date"] = df[i]["date"][:4]+"-"+season[df[i]["date"][5:7]]

        if constrct_list[0] == df[i]["date"] and constrct_list[1] == df[i]["productname"] :
            impressions += df[i]["impressions"]
            clicks += df[i]["clicks"]
            cv += df[i]["cv"]
            cost += df[i]["cost"]
        else:
            df_json['industrytype'] = df[i-1]["industrytype"]
            df_json['clientname'] = df[i-1]["clientname"]
            df_json['productname'] = df[i-1]["productname"]
            df_json['date'] = constrct_list[0]
            df_json['impressions'] = impressions
            df_json['clicks'] = clicks
            df_json['cv'] = cv
            df_json['cost'] = cost
            
            try:
                df_json['cvr'] = (cv/clicks)*100
                df_json['cpc'] = cost/clicks
            except ZeroDivisionError:
                df_json['cvr'] = 0
                df_json['cpc'] = 0
            try:
                df_json['ctr'] = (clicks/impressions)*100
                df_json['cpm'] = (cost/impressions)*1000
            except ZeroDivisionError:
                df_json['ctr'] = 0
                df_json['cpm'] = 0
            try:
                df_json['cpo'] = cost/cv
            except ZeroDivisionError:
                df_json['cpo'] = 0    
            df_json_list.append(df_json)

            df_json = {'industrytype':"",'clientname':"",'productname':"",'date':"","impressions":"","clicks":"",'cv':"","cost":"","ctr":"","cvr":"","cpc":"","cpm":"","cpo":""}
            constrct_list[0] = df[i]["date"]
            constrct_list[1] = df[i]["productname"]
            impressions = df[i]["impressions"]
            clicks = df[i]["clicks"]
            cv = df[i]["cv"]
            cost = df[i]["cost"]

        if i == len(df)-1:
            df_json['industrytype'] = df[i]["industrytype"]
            df_json['clientname'] = df[i]["clientname"]
            df_json['productname'] = df[i]["productname"]
            df_json['date'] = df[i]["date"]
            df_json['impressions'] = impressions + df[i]["impressions"]
            df_json['clicks'] = clicks 
            df_json['cv'] = cv 
            df_json['cost'] = cost 
            try:
                df_json['cvr'] = (cv/clicks)*100
                df_json['cpc'] = cost/clicks
            except ZeroDivisionError:
                df_json['cvr'] = 0
                df_json['cpc'] = 0
            try:
                df_json['ctr'] = (clicks/impressions)*100
                df_json['cpm'] = (cost/impressions)*1000
            except ZeroDivisionError:
                df_json['ctr'] = 0
                df_json['cpm'] = 0
            try:
                df_json['cpo'] = cost/cv
            except ZeroDivisionError:
                df_json['cpo'] = 0    

            df_json_list.append(df_json)
            break
    return df_json_list

def json_season_FB(df_json_list):
    season = {"01":"Q1","02":"Q1","03":"Q1","04":"Q2","05":"Q2","06":"Q2","07":"Q3","08":"Q3","09":"Q3","10":"Q4","11":"Q4","12":"Q4"}
    df = copy.deepcopy(df_json_list)
    df_json_list = []
    df_json = {'industrytype':"",'clientname':"",'productname':"",'date':"","impressions":"","clicks":"",'cv':"","cost":"","ctr":"","cvr":"","cpc":"","cpm":"","cpo":""}
    constrct_list =[df[0]["date"][:4]+"-"+season[df[0]["date"][5:7]],df[0]["productname"]] #1?0?
    impressions = 0
    clicks = 0
    cv = 0
    cost = 0
    for i in range(len(df)):
        
        df[i]["date"] = df[i]["date"][:4]+"-"+season[df[i]["date"][5:7]]

        if constrct_list[0] == df[i]["date"] and constrct_list[1] == df[i]["productname"] :
            impressions += df[i]["impressions"]
            clicks += df[i]["clicks"]
            cv += df[i]["cv"]
            cost += df[i]["cost"]
        else:
            df_json['industrytype'] = df[i-1]["industrytype"]
            df_json['clientname'] = df[i-1]["clientname"]
            df_json['productname'] = df[i-1]["productname"]
            df_json['date'] = constrct_list[0]
            df_json['impressions'] = impressions
            df_json['clicks'] = clicks
            df_json['cv'] = cv
            df_json['cost'] = cost
            
            try:
                df_json['cvr'] = (cv/clicks)*100
                df_json['cpc'] = cost/clicks
            except ZeroDivisionError:
                df_json['cvr'] = 0
                df_json['cpc'] = 0
            try:
                df_json['ctr'] = (clicks/impressions)*100
                df_json['cpm'] = (cost/impressions)*1000
            except ZeroDivisionError:
                df_json['ctr'] = 0
                df_json['cpm'] = 0
            try:
                df_json['cpo'] = cost/cv
            except ZeroDivisionError:
                df_json['cpo'] = 0    
            df_json_list.append(df_json)

            df_json = {'industrytype':"",'clientname':"",'productname':"",'date':"","impressions":"","clicks":"",'cv':"","cost":"","ctr":"","cvr":"","cpc":"","cpm":"","cpo":""}
            constrct_list[0] = df[i]["date"]
            constrct_list[1] = df[i]["productname"]
            impressions = df[i]["impressions"]
            clicks = df[i]["clicks"]
            cv = df[i]["cv"]
            cost = df[i]["cost"]

        if i == len(df)-1:
            df_json['industrytype'] = df[i]["industrytype"]
            df_json['clientname'] = df[i]["clientname"]
            df_json['productname'] = df[i]["productname"]
            df_json['date'] = df[i]["date"]
            df_json['impressions'] = impressions + df[i]["impressions"]
            df_json['clicks'] = clicks 
            df_json['cv'] = cv 
            df_json['cost'] = cost 
            try:
                df_json['cvr'] = (cv/clicks)*100
                df_json['cpc'] = cost/clicks
            except ZeroDivisionError:
                df_json['cvr'] = 0
                df_json['cpc'] = 0
            try:
                df_json['ctr'] = (clicks/impressions)*100
                df_json['cpm'] = (cost/impressions)*1000
            except ZeroDivisionError:
                df_json['ctr'] = 0
                df_json['cpm'] = 0
            try:
                df_json['cpo'] = cost/cv
            except ZeroDivisionError:
                df_json['cpo'] = 0    

            df_json_list.append(df_json)
            break
    return df_json_list

def json_season_Cros(df_json_list):
    season = {"01":"Q1","02":"Q1","03":"Q1","04":"Q2","05":"Q2","06":"Q2","07":"Q3","08":"Q3","09":"Q3","10":"Q4","11":"Q4","12":"Q4"}
    df = copy.deepcopy(df_json_list)
    df_json_list = []
    df_json = {'clientname':"",'productname':"",'date':"",'cv':"",'profit':"",'unitprice':"","ordertype":"","regular":""}
    constrct_list =[df[0]["date"][:4]+"-"+season[df[0]["date"][5:7]],df[0]["clientname"]]
    cv = 0
    profit = 0
    orderTypeInfo = [0,0] #新規,既存
    regularInfo = [0,0]
    for i in range(len(df)):
        
        df[i]["date"] = df[i]["date"][:4]+"-"+season[df[i]["date"][5:7]]
        if i == len(df)-1:
            df_json['clientname'] = df[i]["clientname"]
            df_json['productname'] = df[i]["productname"]
            df_json['date'] = df[i]["date"]
            df_json['cv'] = cv+df[i]["cv"]
            df_json['profit'] = profit+df[i]["profit"]
            orderTypeInfo[0]+=df[i]["ordertype"][0]
            orderTypeInfo[1]+=df[i]["ordertype"][1]
            df_json['ordertype'] = orderTypeInfo
            regularInfo[0]+=df[i]["regular"][0]
            regularInfo[1]+=df[i]["regular"][1]
            df_json['regular'] = regularInfo
            try:
                df_json['unitprice'] = profit/cv
            except ZeroDivisionError:
                df_json['unitprice'] =0

            df_json_list.append(df_json)
            break
        elif constrct_list[0] == df[i]["date"] and constrct_list[1] == df[i]["clientname"] :
            cv+=df[i]["cv"]
            profit+=df[i]["profit"]
            #新規既存判斷
            orderTypeInfo[0]+=df[i]["ordertype"][0]
            
            orderTypeInfo[1]+=df[i]["ordertype"][1]
            #定期都度判斷
            
            regularInfo[0]+=df[i]["regular"][0]
            
            regularInfo[1]+=df[i]["regular"][1]
        else:
            df_json['clientname'] = df[i-1]["clientname"]
            df_json['productname'] = df[i-1]["productname"]
            df_json['date'] = constrct_list[0]
            df_json['cv'] = cv
            df_json['profit'] = profit
            df_json['ordertype'] = orderTypeInfo
            df_json['regular'] = regularInfo
            
            try:
                df_json['unitprice'] = profit/cv
            except ZeroDivisionError:
                df_json['unitprice'] =0

            df_json_list.append(df_json)

            df_json = {'clientname':"",'productname':"",'date':"",'cv':"",'profit':"",'unitprice':"","ordertype":"","regular":""}
            constrct_list[0] = df[i]["date"]
            constrct_list[1] = df[i]["clientname"]
            cv = df[i]["cv"]
            profit = df[i]["profit"]
            orderTypeInfo = [0,0] 
            regularInfo = [0,0]   

            orderTypeInfo[0]+=df[i]["ordertype"][0]
            
            orderTypeInfo[1]+=df[i]["ordertype"][1]
            #定期都度判斷
            
            regularInfo[0]+=df[i]["regular"][0]
            
            regularInfo[1]+=df[i]["regular"][1]

    return df_json_list




# main 
# cli_name, pro_name, campaign, Ga1, Ga2, Ga3, media, link_type
def cros_view(date1,date2,cli,pro,cam,g1,g2,g3,med,lin,pay,reg,ord,ordS,ordP,delF,marg):

    date1,date2 = dateToDf(date1,date2)    
    
    #篩選條件寫入
    df = queryCros(date1,date2,cli,pro,cam,g1,g2,g3,med,lin,pay,reg,ord,ordS,ordP,delF)
    
    df_len = len(df)

    #如果df沒有資料，則回傳空的json檔
    if df_len == 0:
        df_json_list = [{"clients":"","products":"","campaign":"","ga1":"","ga2":"","ga3":"","media":"","link_type":""},{'clientname':"",'productname':"",'date':"",'cv':"",'profit':"",'unitprice':"","ordertype":"","regular":""}]
        return df_json_list

    info_list = get_info_cros(df,df_len)

    df_json_list_all = []

    df_json_list_all.append({"clients":info_list[0],"products":info_list[1],"campaign":info_list[2],"ga1":info_list[3],"ga2":info_list[4],"ga3":info_list[5],"media":info_list[6],"link_type":info_list[7]})

    df_json_list_day = json_Cros(df,df_len,date1,date2,marg)
    df_json_list_all.append(df_json_list_day)
    
    df_json_list_mon = json_month_Cros(df_json_list_day)
    df_json_list_all.append(df_json_list_mon)

    df_json_list_sea = json_season_Cros(df_json_list_day)
    df_json_list_all.append(df_json_list_sea)

    return df_json_list_all
"""
def fb_view(date1,date2,cli,pro,cam,g1,g2,g3,med,lin):
    
    date1,date2 = dateToDf(date1,date2)
    
    #篩選條件寫入
    
    df = queryForDB_fb(date1,date2,cli,pro,cam,g1,g2,g3,med,lin)
    

    
    df_len = len(df)
    
    #如果df沒有資料，則回傳空的json檔

    if df_len == 0:
        df_json_list = [{"clients":"","products":"","campaign":"","ga1":"","ga2":"","ga3":"","media":"","link_type":""},{'clientname':"",'productname':"",'date':"","impressions":"","clicks":"",'cv':"","cost":"","ctr":"","cvr":"","cpc":"","cpm":"","cpo":""}]
        return df_json_list

    
    info_list = get_info(df,df_len)
    

    df_json_list_all = []
    
    df_json_list_all.append({"clients":info_list[0],"products":info_list[1],"campaign":info_list[2],"ga1":info_list[3],"ga2":info_list[4],"ga3":info_list[5],"media":info_list[6],"link_type":info_list[7]})
    
    df_json_list_day = json_fb(df,df_len,date1,date2)
    df_json_list_all.append(df_json_list_day)
    
    
    df_json_list_mon = json_month_lineFb(df_json_list_day)
    df_json_list_all.append(df_json_list_mon)
    
    
    df_json_list_sea = json_season_lineFb(df_json_list_day)
    df_json_list_all.append(df_json_list_sea)
    

    return df_json_list_all
"""

def line_view(date1,date2,cli,pro,acc,gro,cam,g1,g2,g3,lin,asn,an):
    
    date1,date2 = dateToDf(date1,date2)
   
    #篩選條件寫入
    
    df = queryLine(date1,date2,cli,pro,acc,gro,cam,g1,g2,g3,lin,asn,an)
    

    
    df_len = len(df)
    
    #如果df沒有資料，則回傳空的json檔
    

    if df_len == 0:
        df_json_list = [{"industrytype":"","clients":"","products":"","accountname":"","campaign":"","ga1":"","ga2":"","ga3":"","group_type":"","link_type":"","ad_set_name":"","ad_name":""},{'clientname':"",'productname':"",'date':"","impressions":"","clicks":"",'cv':"","cost":"","ctr":"","cvr":"","cpc":"","cpm":"","cpo":""}]
        return df_json_list

    
    info_list = get_info_Line(df,df_len)

    df_json_list_all = []
    
    df_json_list_all.append({"industrytype":info_list[0],"clients":info_list[1],"products":info_list[2],"accountname":info_list[3],"campaign":info_list[4],"ga1":info_list[5],"ga2":info_list[6],"ga3":info_list[7],"group_type":info_list[8],"link_type":info_list[9],"ad_set_name":info_list[10],"ad_name":info_list[11]})
    
    df_json_list_day = json_Line(df,df_len,date1,date2)
    df_json_list_all.append(df_json_list_day)
    
    
    
    
    df_json_list_mon = json_month_Line(df_json_list_day)
    df_json_list_all.append(df_json_list_mon)
    
    
    df_json_list_sea = json_season_Line(df_json_list_day)
    df_json_list_all.append(df_json_list_sea)
    
    
    return df_json_list_all


def fb_view(date1,date2,cli,pro,acc,gro,cam,g1,g2,g3,lin,asn,an):
    
    date1,date2 = dateToDf(date1,date2)
   
    #篩選條件寫入
    
    df = queryFB(date1,date2,cli,pro,acc,gro,cam,g1,g2,g3,lin,asn,an)
    

    
    df_len = len(df)
    
    #如果df沒有資料，則回傳空的json檔
    

    if df_len == 0:
        df_json_list = [{"industrytype":"","clients":"","products":"","accountname":"","campaign":"","ga1":"","ga2":"","ga3":"","group_type":"","link_type":"","ad_set_name":"","ad_name":""},{'clientname':"",'productname':"",'date':"","impressions":"","clicks":"",'cv':"","cost":"","ctr":"","cvr":"","cpc":"","cpm":"","cpo":""}]
        return df_json_list

    
    info_list = get_info_FB(df,df_len)

    df_json_list_all = []
    
    df_json_list_all.append({"industrytype":info_list[0],"clients":info_list[1],"products":info_list[2],"accountname":info_list[3],"campaign":info_list[4],"ga1":info_list[5],"ga2":info_list[6],"ga3":info_list[7],"group_type":info_list[8],"link_type":info_list[9],"ad_set_name":info_list[10],"ad_name":info_list[11]})
    
    df_json_list_day = json_FB(df,df_len,date1,date2)
    df_json_list_all.append(df_json_list_day)
    
    
    
    
    df_json_list_mon = json_month_FB(df_json_list_day)
    df_json_list_all.append(df_json_list_mon)
    
    
    df_json_list_sea = json_season_FB(df_json_list_day)
    df_json_list_all.append(df_json_list_sea)
    
    
    return df_json_list_all






#testing


def get_info_FB(df,df_len):
    
    df1 = pd.DataFrame(df)

    info_list=[[],[],[],[],[],[],[],[],[],[],[],[],[]] # cli_name, pro_name, campaign, Ga1, Ga2, Ga3, media, link_type

    info_list[0]= set(df1["industrytype"])

    info_list[1]= set(df1["clientname"])
        
    info_list[2]= set(df1["productname"])

    info_list[3]= set(df1["accountname"])
            
    info_list[4]= set(df1["campaign"])

    info_list[5]= set(df1["ga1"])
            
    info_list[6]= set(df1["ga2"])
            
    info_list[7]= set(df1["ga3"])
            
    info_list[8]= set(df1["group_type"])
            
    info_list[9]= set(df1["link_type"])

    info_list[10]= set(df1["ad_set_name"])

    info_list[11]= set(df1["ad_name"])
    

    for i in range(len(info_list)):
        info_list[i] = list(info_list[i])

    return info_list



def get_info_Line(df,df_len):
    
    df1 = pd.DataFrame(df)

    info_list=[[],[],[],[],[],[],[],[],[],[],[],[],[]] # cli_name, pro_name, campaign, Ga1, Ga2, Ga3, media, link_type

    info_list[0]= set(df1["industrytype"])

    info_list[1]= set(df1["clientname"])
        
    info_list[2]= set(df1["productname"])

    info_list[3]= set(df1["accountname"])
            
    info_list[4]= set(df1["campaign"])

    info_list[5]= set(df1["ga1"])
            
    info_list[6]= set(df1["ga2"])
            
    info_list[7]= set(df1["ga3"])
            
    info_list[8]= set(df1["group_type"])
            
    info_list[9]= set(df1["link_type"])

    info_list[10]= set(df1["adgroup_name"])

    info_list[11]= set(df1["ad_name"])
    

    for i in range(len(info_list)):
        info_list[i] = list(info_list[i])

    return info_list




def top3_ver2(n):

    date1 = [""]
    date2 = [""]
    date1[0] = datetime.today() - dt.timedelta(days = 200)
    date2[0] = datetime.today()

    st = time.time()
    df = pd.DataFrame(CrosOrder.objects.filter(stadatetime__date__range=[date1[0],date2[0]]).values())
    
    df_len = len(df)

    print(time.time() - st)
    st = time.time()
    cli_name = list(set(df['clientname']))
    #pro_name = info_list[1]
    print(time.time() - st)
    st = time.time()
    df1 = df.groupby('clientname').sum().sort_values('order_price',ascending=False)[:3]
    print(time.time() - st)

    return df1





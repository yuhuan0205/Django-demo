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


class V_facebook(models.Model):
    ad_id = models.TextField(db_column='Ad_ID',blank=True, null=True)
    stadatetime = models.DateTimeField(db_column='StaDateTime', blank=True, null=True)
    ad_time = models.TextField(db_column='Ad_Time', blank=True, null=True)
    campaign_name = models.TextField(db_column='Campaign_Name', blank=True, null=True)
    ad_group_name = models.TextField(db_column='Ad_Group_Name', blank=True, null=True)
    ad_name = models.TextField(db_column='Ad_Name', blank=True, null=True)
    ad_status = models.TextField(db_column='Ad_Status', blank=True, null=True)
    impressions = models.IntegerField(db_column='Impressions', blank=True, null=True)
    clicks = models.IntegerField(db_column='Clicks', blank=True, null=True)
    cv = models.IntegerField(db_column='CV', blank=True, null=True)
    cost = models.IntegerField(db_column='Cost', blank=True, null=True)
    media = models.CharField(db_column='media', max_length=255, blank=True, null=True)
    group_type = models.CharField(db_column='group_type', max_length=255, blank=True, null=True)
    ad_set_daily_budget = models.IntegerField(db_column='Ad_Set_Daily_Budget', blank=True, null=True)
    link = models.TextField(db_column='Link', blank=True, null=True)
    countries = models.TextField(db_column='Countries', blank=True, null=True)
    cities = models.TextField(db_column='Cities', blank=True, null=True)
    regions = models.TextField(db_column='Regions', blank=True, null=True)
    zi_p = models.TextField(db_column='Zip', blank=True, null=True)
    addresses = models.TextField(db_column='Addresses', blank=True, null=True)
    gender = models.TextField(db_column='Gender', blank=True, null=True)
    age_min = models.IntegerField(db_column='Age_Min', blank=True, null=True)
    age_max = models.IntegerField(db_column='Age_Max', blank=True, null=True)
    title = models.TextField(db_column='Title', blank=True, null=True)
    body = models.TextField(db_column='Body', blank=True, null=True)
    link_type = models.CharField(db_column='link_type', max_length=255, blank=True, null=True)
    sourceType = models.CharField(db_column='SourceType', max_length=255, blank=True, null=True)
    sourceSubType = models.CharField(db_column='SourceSubType', max_length=255, blank=True, null=True)
    clientName = models.CharField(db_column='ClientName', max_length=255, blank=True, null=True)
    productName = models.CharField(db_column='ProductName', max_length=255, blank=True, null=True)
    accountName = models.CharField(db_column='AccountName', max_length=255, blank=True, null=True)
    ga1 = models.TextField(db_column='GA1', blank=True, null=True)  
    ga2 = models.TextField(db_column='GA2', blank=True, null=True)  
    ga3 = models.TextField(db_column='GA3', blank=True, null=True)

    class Meta:
        managed = False
        db_table = "v_facebook"

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
    no = models.AutoField(db_column='No', primary_key=True)  # Field name made lowercase.
    order_id = models.TextField(db_column='Order_ID', blank=True, null=True)  # Field name made lowercase.
    customer_id = models.TextField(db_column='Customer_ID', blank=True, null=True)  # Field name made lowercase.
    order_status = models.TextField(db_column='Order_Status', blank=True, null=True)  # Field name made lowercase.
    order_price = models.IntegerField(db_column='Order_Price', blank=True, null=True)  # Field name made lowercase.
    del_flg = models.TextField(blank=True, null=True)
    pay_method = models.TextField(db_column='Pay_Method', blank=True, null=True)  # Field name made lowercase.
    pickup_method = models.TextField(db_column='Pickup_Method', blank=True, null=True)  # Field name made lowercase.
    regular = models.TextField(db_column='Regular', blank=True, null=True)  # Field name made lowercase.
    regular_times = models.IntegerField(db_column='Regular_Times', blank=True, null=True)  # Field name made lowercase.
    campaign = models.TextField(db_column='Campaign', blank=True, null=True)  # Field name made lowercase.
    promotion_code = models.TextField(db_column='Promotion_Code', blank=True, null=True)  # Field name made lowercase.
    buy_date = models.DateTimeField(db_column='Buy_Date', blank=True, null=True)  # Field name made lowercase.
    cancel_date = models.DateTimeField(db_column='Cancel_Date', blank=True, null=True)  # Field name made lowercase.
    transfer_date = models.DateTimeField(db_column='Transfer_Date', blank=True, null=True)  # Field name made lowercase.
    real_transfer_date = models.DateTimeField(db_column='Real_Transfer_Date', blank=True, null=True)  # Field name made lowercase.
    booking_return_date = models.DateTimeField(db_column='Booking_Return_Date', blank=True, null=True)  # Field name made lowercase.
    return_status = models.TextField(db_column='Return_Status', blank=True, null=True)  # Field name made lowercase.
    return_in_warehouse_date = models.DateTimeField(db_column='Return_In_Warehouse_Date', blank=True, null=True)  # Field name made lowercase.
    order_type = models.TextField(db_column='Order_Type', blank=True, null=True)  # Field name made lowercase.
    ga1 = models.TextField(db_column='GA1', blank=True, null=True)  # Field name made lowercase.
    ga2 = models.TextField(db_column='GA2', blank=True, null=True)  # Field name made lowercase.
    ga3 = models.TextField(db_column='GA3', blank=True, null=True)  # Field name made lowercase.
    paypal_transaction_id = models.TextField(db_column='PayPal_Transaction_ID', blank=True, null=True)  # Field name made lowercase.
    apply_id = models.TextField(blank=True, null=True)
    newoto = models.TextField(db_column='NewOTO', blank=True, null=True)  # Field name made lowercase.
    cross_sell = models.TextField(db_column='Cross_Sell', blank=True, null=True)  # Field name made lowercase.
    repeat_click_lp = models.TextField(db_column='Repeat_Click_LP', blank=True, null=True)  # Field name made lowercase.
    multi_buy_lp = models.TextField(db_column='Multi_Buy_LP', blank=True, null=True)  # Field name made lowercase.
    order_path = models.TextField(db_column='Order_Path', blank=True, null=True)  # Field name made lowercase.
    invoice_date = models.DateTimeField(db_column='Invoice_Date', blank=True, null=True)  # Field name made lowercase.
    birth_month = models.TextField(blank=True, null=True)
    sourcetype = models.CharField(db_column='SourceType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sourcesubtype = models.CharField(db_column='SourceSubType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    clientname = models.CharField(db_column='ClientName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    accountname = models.CharField(db_column='AccountName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    stadatetime = models.DateTimeField(db_column='StaDateTime', blank=True, null=True)  # Field name made lowercase.
    media = models.CharField(max_length=255, blank=True, null=True)
    link_type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cros_order'


class CrosWeb(models.Model):
    no = models.AutoField(db_column='No', primary_key=True)  # Field name made lowercase.
    ga1 = models.TextField(db_column='GA1', blank=True, null=True)  # Field name made lowercase.
    ga2 = models.TextField(db_column='GA2', blank=True, null=True)  # Field name made lowercase.
    ga3 = models.TextField(db_column='GA3', blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    visitors = models.IntegerField(db_column='Visitors', blank=True, null=True)  # Field name made lowercase.
    cv = models.IntegerField(db_column='CV', blank=True, null=True)  # Field name made lowercase.
    cvr = models.FloatField(db_column='CVR', blank=True, null=True)  # Field name made lowercase.
    profit = models.IntegerField(db_column='Profit', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.IntegerField(db_column='UnitPrice', blank=True, null=True)  # Field name made lowercase.
    sourcetype = models.CharField(db_column='SourceType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sourcesubtype = models.CharField(db_column='SourceSubType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    clientname = models.CharField(db_column='ClientName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    accountname = models.CharField(db_column='AccountName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    stadatetime = models.DateTimeField(db_column='StaDateTime', blank=True, null=True)  # Field name made lowercase.
    media = models.CharField(max_length=255, blank=True, null=True)
    link_type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cros_web'


class FbMaterial(models.Model):
    no = models.AutoField(db_column='No', primary_key=True)  # Field name made lowercase.
    ad_id = models.TextField(db_column='Ad_ID', blank=True, null=True)  # Field name made lowercase.
    start_date = models.DateTimeField(db_column='Start_Date', blank=True, null=True)  # Field name made lowercase.
    end_date = models.DateTimeField(db_column='End_Date', blank=True, null=True)  # Field name made lowercase.
    ad_name = models.TextField(db_column='Ad_Name', blank=True, null=True)  # Field name made lowercase.
    ad_time = models.TextField(db_column='Ad_Time', blank=True, null=True)  # Field name made lowercase.
    campaign_name = models.TextField(db_column='Campaign_Name', blank=True, null=True)  # Field name made lowercase.
    ad_group_name = models.TextField(db_column='Ad_Group_Name', blank=True, null=True)  # Field name made lowercase.
    ad_status = models.TextField(db_column='Ad_Status', blank=True, null=True)  # Field name made lowercase.
    impressions = models.IntegerField(db_column='Impressions', blank=True, null=True)  # Field name made lowercase.
    clicks = models.IntegerField(db_column='Clicks', blank=True, null=True)  # Field name made lowercase.
    result = models.IntegerField(db_column='Result', blank=True, null=True)  # Field name made lowercase.
    cv_type = models.TextField(db_column='CV_Type', blank=True, null=True)  # Field name made lowercase.
    buy_content = models.IntegerField(db_column='Buy_Content', blank=True, null=True)  # Field name made lowercase.
    cv = models.IntegerField(db_column='CV', blank=True, null=True)  # Field name made lowercase.
    cost = models.IntegerField(db_column='Cost', blank=True, null=True)  # Field name made lowercase.
    cpo = models.FloatField(db_column='CPO', blank=True, null=True)  # Field name made lowercase.
    roas_of_buy = models.FloatField(db_column='Roas_Of_Buy', blank=True, null=True)  # Field name made lowercase.
    roas_of_website_buy = models.FloatField(db_column='Roas_Of_Website_Buy', blank=True, null=True)  # Field name made lowercase.
    sourcetype = models.CharField(db_column='SourceType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sourcesubtype = models.CharField(db_column='SourceSubType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    clientname = models.CharField(db_column='ClientName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    accountname = models.CharField(db_column='AccountName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    stadatetime = models.DateTimeField(db_column='StaDateTime', blank=True, null=True)  # Field name made lowercase.
    media = models.CharField(max_length=255, blank=True, null=True)
    group_type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fb_material'


class FbSystem(models.Model):
    ad_id = models.TextField(db_column='Ad_ID', blank=True, null=True)  # Field name made lowercase.
    campaign_id = models.TextField(db_column='Campaign_ID', blank=True, null=True)  # Field name made lowercase.
    campaign_name = models.TextField(db_column='Campaign_Name', blank=True, null=True)  # Field name made lowercase.
    campaign_status = models.TextField(db_column='Campaign_Status', blank=True, null=True)  # Field name made lowercase.
    campaign_objective = models.TextField(db_column='Campaign_Objective', blank=True, null=True)  # Field name made lowercase.
    buying_type = models.TextField(db_column='Buying_Type', blank=True, null=True)  # Field name made lowercase.
    campaign_spend_limit = models.TextField(db_column='Campaign_Spend_Limit', blank=True, null=True)  # Field name made lowercase.
    campaign_daily_budget = models.IntegerField(db_column='Campaign_Daily_Budget', blank=True, null=True)  # Field name made lowercase.
    campaign_lifetime_budget = models.IntegerField(db_column='Campaign_Lifetime_Budget', blank=True, null=True)  # Field name made lowercase.
    campaign_bid_strategy = models.TextField(db_column='Campaign_Bid_Strategy', blank=True, null=True)  # Field name made lowercase.
    ad_set_id = models.TextField(db_column='Ad_Set_ID', blank=True, null=True)  # Field name made lowercase.
    ad_set_run_status = models.TextField(db_column='Ad_Set_Run_Status', blank=True, null=True)  # Field name made lowercase.
    ad_set_name = models.TextField(db_column='Ad_Set_Name', blank=True, null=True)  # Field name made lowercase.
    ad_set_time_start = models.DateTimeField(db_column='Ad_Set_Time_Start', blank=True, null=True)  # Field name made lowercase.
    ad_set_time_stop = models.DateTimeField(db_column='Ad_Set_Time_Stop', blank=True, null=True)  # Field name made lowercase.
    ad_set_daily_budget = models.IntegerField(db_column='Ad_Set_Daily_Budget', blank=True, null=True)  # Field name made lowercase.
    link_object_id = models.TextField(db_column='Link_Object_ID', blank=True, null=True)  # Field name made lowercase.
    optimized_conversion_tracking_pixels = models.TextField(db_column='Optimized_Conversion_Tracking_Pixels', blank=True, null=True)  # Field name made lowercase.
    optimized_event = models.TextField(db_column='Optimized_Event', blank=True, null=True)  # Field name made lowercase.
    link = models.TextField(db_column='Link', blank=True, null=True)  # Field name made lowercase.
    countries = models.TextField(db_column='Countries', blank=True, null=True)  # Field name made lowercase.
    cities = models.TextField(db_column='Cities', blank=True, null=True)  # Field name made lowercase.
    regions = models.TextField(db_column='Regions', blank=True, null=True)  # Field name made lowercase.
    zip = models.TextField(db_column='Zip', blank=True, null=True)  # Field name made lowercase.
    addresses = models.TextField(db_column='Addresses', blank=True, null=True)  # Field name made lowercase.
    gender = models.TextField(db_column='Gender', blank=True, null=True)  # Field name made lowercase.
    age_min = models.IntegerField(db_column='Age_Min', blank=True, null=True)  # Field name made lowercase.
    age_max = models.IntegerField(db_column='Age_Max', blank=True, null=True)  # Field name made lowercase.
    custom_audiences = models.TextField(db_column='Custom_Audiences', blank=True, null=True)  # Field name made lowercase.
    excluded_custom_audiences = models.TextField(db_column='Excluded_Custom_Audiences', blank=True, null=True)  # Field name made lowercase.
    flexible_inclusions = models.TextField(db_column='Flexible_Inclusions', blank=True, null=True)  # Field name made lowercase.
    flexible_exclusions = models.TextField(db_column='Flexible_Exclusions', blank=True, null=True)  # Field name made lowercase.
    publisher_platforms = models.TextField(db_column='Publisher_Platforms', blank=True, null=True)  # Field name made lowercase.
    facebook_positions = models.TextField(db_column='Facebook_Positions', blank=True, null=True)  # Field name made lowercase.
    instagram_positions = models.TextField(db_column='Instagram_Positions', blank=True, null=True)  # Field name made lowercase.
    audience_network_positions = models.TextField(db_column='Audience_Network_Positions', blank=True, null=True)  # Field name made lowercase.
    messenger_positions = models.TextField(db_column='Messenger_Positions', blank=True, null=True)  # Field name made lowercase.
    device_platforms = models.TextField(db_column='Device_Platforms', blank=True, null=True)  # Field name made lowercase.
    optimization_goal = models.TextField(db_column='Optimization_Goal', blank=True, null=True)  # Field name made lowercase.
    bid_amount = models.IntegerField(db_column='Bid_Amount', blank=True, null=True)  # Field name made lowercase.
    ad_set_bid_strategy = models.TextField(db_column='Ad_Set_Bid_Strategy', blank=True, null=True)  # Field name made lowercase.
    ad_status = models.TextField(db_column='Ad_Status', blank=True, null=True)  # Field name made lowercase.
    preview_link = models.TextField(db_column='Preview_Link', blank=True, null=True)  # Field name made lowercase.
    instagram_preview_link = models.TextField(db_column='Instagram_Preview_Link', blank=True, null=True)  # Field name made lowercase.
    ad_name = models.TextField(db_column='Ad_Name', blank=True, null=True)  # Field name made lowercase.
    title = models.TextField(db_column='Title', blank=True, null=True)  # Field name made lowercase.
    body = models.TextField(db_column='Body', blank=True, null=True)  # Field name made lowercase.
    sourcetype = models.CharField(db_column='SourceType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sourcesubtype = models.CharField(db_column='SourceSubType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    clientname = models.CharField(db_column='ClientName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    accountname = models.CharField(db_column='AccountName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    media = models.CharField(max_length=255, blank=True, null=True)
    group_type = models.CharField(max_length=255, blank=True, null=True)
    link_type = models.CharField(max_length=255, blank=True, null=True)
    ga1 = models.TextField(db_column='GA1', blank=True, null=True)  # Field name made lowercase.
    ga2 = models.TextField(db_column='GA2', blank=True, null=True)  # Field name made lowercase.
    ga3 = models.TextField(db_column='GA3', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fb_system'


class GaEvent(models.Model):
    no = models.AutoField(db_column='No', primary_key=True)  # Field name made lowercase.
    eventaction = models.TextField(db_column='EventAction', blank=True, null=True)  # Field name made lowercase.
    sourcemedia = models.TextField(db_column='SourceMedia', blank=True, null=True)  # Field name made lowercase.
    campaign = models.TextField(db_column='Campaign', blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    eventcategory = models.TextField(db_column='EventCategory', blank=True, null=True)  # Field name made lowercase.
    eventlabel = models.TextField(db_column='EventLabel', blank=True, null=True)  # Field name made lowercase.
    totalevents = models.IntegerField(db_column='TotalEvents', blank=True, null=True)  # Field name made lowercase.
    uniqueevents = models.IntegerField(db_column='UniqueEvents', blank=True, null=True)  # Field name made lowercase.
    eventvalue = models.FloatField(db_column='EventValue', blank=True, null=True)  # Field name made lowercase.
    avgeventvalue = models.FloatField(db_column='AvgEventValue', blank=True, null=True)  # Field name made lowercase.
    users = models.IntegerField(db_column='Users', blank=True, null=True)  # Field name made lowercase.
    newusers = models.IntegerField(db_column='NewUsers', blank=True, null=True)  # Field name made lowercase.
    sessions = models.IntegerField(db_column='Sessions', blank=True, null=True)  # Field name made lowercase.
    percentnewsessions = models.TextField(db_column='PercentNewSessions', blank=True, null=True)  # Field name made lowercase.
    bouncerate = models.TextField(db_column='BounceRate', blank=True, null=True)  # Field name made lowercase.
    pageviewspersession = models.FloatField(db_column='PageviewsPerSession', blank=True, null=True)  # Field name made lowercase.
    avgsessionduration = models.TextField(db_column='AvgSessionDuration', blank=True, null=True)  # Field name made lowercase.
    goal_conversionrate = models.TextField(db_column='Goal_ConversionRate', blank=True, null=True)  # Field name made lowercase.
    goal_completions = models.IntegerField(db_column='Goal_Completions', blank=True, null=True)  # Field name made lowercase.
    goal_value = models.IntegerField(db_column='Goal_Value', blank=True, null=True)  # Field name made lowercase.
    sourcetype = models.CharField(db_column='SourceType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sourcesubtype = models.CharField(db_column='SourceSubType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    clientname = models.CharField(db_column='ClientName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    accountname = models.CharField(db_column='AccountName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    stadatetime = models.DateTimeField(db_column='StaDateTime', blank=True, null=True)  # Field name made lowercase.
    media = models.CharField(max_length=255, blank=True, null=True)
    link_type = models.CharField(max_length=255, blank=True, null=True)
    ga1 = models.TextField(db_column='GA1', blank=True, null=True)  # Field name made lowercase.
    ga2 = models.TextField(db_column='GA2', blank=True, null=True)  # Field name made lowercase.
    ga3 = models.TextField(db_column='GA3', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ga_event'


class GaSource(models.Model):
    no = models.AutoField(db_column='No', primary_key=True)  # Field name made lowercase.
    landingpagepath = models.TextField(db_column='LandingPagePath', blank=True, null=True)  # Field name made lowercase.
    sourcemedia = models.TextField(db_column='SourceMedia', blank=True, null=True)  # Field name made lowercase.
    campaign = models.TextField(db_column='Campaign', blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    users = models.IntegerField(db_column='Users', blank=True, null=True)  # Field name made lowercase.
    newusers = models.IntegerField(db_column='NewUsers', blank=True, null=True)  # Field name made lowercase.
    sessions = models.IntegerField(db_column='Sessions', blank=True, null=True)  # Field name made lowercase.
    percentnewsessions = models.TextField(db_column='PercentNewSessions', blank=True, null=True)  # Field name made lowercase.
    bouncerate = models.TextField(db_column='BounceRate', blank=True, null=True)  # Field name made lowercase.
    pageviewspersession = models.FloatField(db_column='PageviewsPerSession', blank=True, null=True)  # Field name made lowercase.
    avgsessionduration = models.TextField(db_column='AvgSessionDuration', blank=True, null=True)  # Field name made lowercase.
    goal_conversionrate = models.TextField(db_column='Goal_ConversionRate', blank=True, null=True)  # Field name made lowercase.
    goal_completions = models.IntegerField(db_column='Goal_Completions', blank=True, null=True)  # Field name made lowercase.
    goal_value = models.IntegerField(db_column='Goal_Value', blank=True, null=True)  # Field name made lowercase.
    sourcetype = models.CharField(db_column='SourceType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sourcesubtype = models.CharField(db_column='SourceSubType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    clientname = models.CharField(db_column='ClientName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    accountname = models.CharField(db_column='AccountName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    stadatetime = models.DateTimeField(db_column='StaDateTime', blank=True, null=True)  # Field name made lowercase.
    media = models.CharField(max_length=255, blank=True, null=True)
    link_type = models.CharField(max_length=255, blank=True, null=True)
    ga1 = models.TextField(db_column='GA1', blank=True, null=True)  # Field name made lowercase.
    ga2 = models.TextField(db_column='GA2', blank=True, null=True)  # Field name made lowercase.
    ga3 = models.TextField(db_column='GA3', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ga_source'


class LineEffect(models.Model):
    no = models.AutoField(primary_key=True)
    ad_id = models.TextField(blank=True, null=True)
    day = models.DateTimeField(blank=True, null=True)
    adaccount_name = models.TextField(blank=True, null=True)
    adaccount_id = models.TextField(blank=True, null=True)
    campaign_name = models.TextField(blank=True, null=True)
    campaign_id = models.TextField(blank=True, null=True)
    campaign_objective = models.TextField(db_column='campaign_Objective', blank=True, null=True)  # Field name made lowercase.
    adgroup_name = models.TextField(blank=True, null=True)
    adgroup_id = models.TextField(blank=True, null=True)
    ad_name = models.TextField(blank=True, null=True)
    impression = models.IntegerField(blank=True, null=True)
    viewable_impression = models.IntegerField(blank=True, null=True)
    clicks = models.IntegerField(blank=True, null=True)
    ctr = models.TextField(db_column='CTR', blank=True, null=True)  # Field name made lowercase.
    cpc = models.FloatField(db_column='CPC', blank=True, null=True)  # Field name made lowercase.
    cv = models.IntegerField(db_column='CV', blank=True, null=True)  # Field name made lowercase.
    cvr = models.TextField(db_column='CVR', blank=True, null=True)  # Field name made lowercase.
    cpa = models.FloatField(db_column='CPA', blank=True, null=True)  # Field name made lowercase.
    cost = models.FloatField(blank=True, null=True)
    currency = models.TextField(blank=True, null=True)
    video_completions = models.IntegerField(db_column='Video_completions', blank=True, null=True)  # Field name made lowercase.
    installs_clicks = models.IntegerField(db_column='Installs_clicks', blank=True, null=True)  # Field name made lowercase.
    install_rate_clicks = models.FloatField(db_column='Install_rate_clicks', blank=True, null=True)  # Field name made lowercase.
    open = models.IntegerField(db_column='Open', blank=True, null=True)  # Field name made lowercase.
    open_rate = models.TextField(db_column='Open_rate', blank=True, null=True)  # Field name made lowercase.
    cost_per_open = models.FloatField(db_column='cost_per_Open', blank=True, null=True)  # Field name made lowercase.
    view_home = models.IntegerField(db_column='View_home', blank=True, null=True)  # Field name made lowercase.
    view_home_rate = models.TextField(db_column='View_home_rate', blank=True, null=True)  # Field name made lowercase.
    cost_per_view_home = models.FloatField(db_column='cost_per_View_home', blank=True, null=True)  # Field name made lowercase.
    view_category = models.IntegerField(db_column='View_category', blank=True, null=True)  # Field name made lowercase.
    viewcategory_rate = models.TextField(db_column='Viewcategory_rate', blank=True, null=True)  # Field name made lowercase.
    cost_per_view_category = models.FloatField(db_column='cost_per_View_category', blank=True, null=True)  # Field name made lowercase.
    view_item = models.IntegerField(db_column='View_item', blank=True, null=True)  # Field name made lowercase.
    view_item_rate = models.TextField(db_column='View_item_rate', blank=True, null=True)  # Field name made lowercase.
    cost_per_view_item = models.FloatField(db_column='cost_per_View_item', blank=True, null=True)  # Field name made lowercase.
    search = models.IntegerField(db_column='Search', blank=True, null=True)  # Field name made lowercase.
    search_rate = models.TextField(db_column='Search_rate', blank=True, null=True)  # Field name made lowercase.
    cost_per_search = models.FloatField(db_column='cost_per_Search', blank=True, null=True)  # Field name made lowercase.
    add_to_cart = models.IntegerField(db_column='Add_to_cart', blank=True, null=True)  # Field name made lowercase.
    add_to_cart_rate = models.TextField(db_column='Add_to_cart_rate', blank=True, null=True)  # Field name made lowercase.
    cost_per_add_to_cart = models.FloatField(db_column='cost_per_Add_to_cart', blank=True, null=True)  # Field name made lowercase.
    purchase = models.IntegerField(db_column='Purchase', blank=True, null=True)  # Field name made lowercase.
    purchase_rate = models.TextField(db_column='Purchase_rate', blank=True, null=True)  # Field name made lowercase.
    cost_per_purchase = models.FloatField(db_column='cost_per_Purchase', blank=True, null=True)  # Field name made lowercase.
    level_achieved = models.IntegerField(db_column='Level_achieved', blank=True, null=True)  # Field name made lowercase.
    level_achieved_rate = models.TextField(db_column='Level_achieved_rate', blank=True, null=True)  # Field name made lowercase.
    cost_per_level_achieved = models.FloatField(db_column='cost_per_Level_achieved', blank=True, null=True)  # Field name made lowercase.
    tutorial_complete = models.IntegerField(db_column='Tutorial_complete', blank=True, null=True)  # Field name made lowercase.
    tutorial_complete_rate = models.TextField(db_column='Tutorial_complete_rate', blank=True, null=True)  # Field name made lowercase.
    cost_per_tutorial_complete = models.FloatField(db_column='cost_per_Tutorial_complete', blank=True, null=True)  # Field name made lowercase.
    sourcetype = models.CharField(db_column='SourceType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sourcesubtype = models.CharField(db_column='SourceSubType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    clientname = models.CharField(db_column='ClientName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    accountname = models.CharField(db_column='AccountName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    stadatetime = models.DateTimeField(db_column='StaDateTime', blank=True, null=True)  # Field name made lowercase.
    media = models.CharField(max_length=255, blank=True, null=True)
    group_type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'line_effect'


class LineMaterial(models.Model):
    ad_id = models.CharField(db_column='Ad_ID', max_length=25, blank=True, null=True)  # Field name made lowercase.
    ad_account_id = models.TextField(db_column='Ad_account_ID', blank=True, null=True)  # Field name made lowercase.
    campaign_id = models.TextField(db_column='Campaign_ID', blank=True, null=True)  # Field name made lowercase.
    campaign_name = models.TextField(db_column='Campaign_name', blank=True, null=True)  # Field name made lowercase.
    campaign_status = models.TextField(db_column='Campaign_status', blank=True, null=True)  # Field name made lowercase.
    campaign_objective = models.TextField(db_column='Campaign_objective', blank=True, null=True)  # Field name made lowercase.
    start_date = models.DateTimeField(db_column='Start_date', blank=True, null=True)  # Field name made lowercase.
    end_date = models.DateTimeField(db_column='End_date', blank=True, null=True)  # Field name made lowercase.
    campaign_spend_limit = models.TextField(db_column='Campaign_spend_limit', blank=True, null=True)  # Field name made lowercase.
    budget_type = models.TextField(db_column='Budget_type', blank=True, null=True)  # Field name made lowercase.
    monthly_budget = models.IntegerField(db_column='Monthly_budget', blank=True, null=True)  # Field name made lowercase.
    lifetime_budget = models.IntegerField(db_column='Lifetime_budget', blank=True, null=True)  # Field name made lowercase.
    ad_group_id = models.TextField(db_column='Ad_group_ID', blank=True, null=True)  # Field name made lowercase.
    ad_group_name = models.TextField(db_column='Ad_group_name', blank=True, null=True)  # Field name made lowercase.
    ad_group_status = models.TextField(db_column='Ad_group_status', blank=True, null=True)  # Field name made lowercase.
    bidding_amount_configuration = models.TextField(db_column='Bidding_amount_configuration', blank=True, null=True)  # Field name made lowercase.
    optimize_for = models.TextField(db_column='Optimize_for', blank=True, null=True)  # Field name made lowercase.
    payment_method = models.TextField(db_column='Payment_method', blank=True, null=True)  # Field name made lowercase.
    bid_amount = models.FloatField(db_column='Bid_amount', blank=True, null=True)  # Field name made lowercase.
    max_cpc = models.FloatField(db_column='Max_CPC', blank=True, null=True)  # Field name made lowercase.
    max_cpa = models.FloatField(db_column='Max_CPA', blank=True, null=True)  # Field name made lowercase.
    daily_budget = models.IntegerField(db_column='Daily_budget', blank=True, null=True)  # Field name made lowercase.
    gender = models.TextField(db_column='Gender', blank=True, null=True)  # Field name made lowercase.
    age_min = models.IntegerField(db_column='Age_min', blank=True, null=True)  # Field name made lowercase.
    age_max = models.IntegerField(db_column='Age_max', blank=True, null=True)  # Field name made lowercase.
    user_os = models.TextField(db_column='User_os', blank=True, null=True)  # Field name made lowercase.
    user_os_version_min = models.TextField(db_column='User_os_version_min', blank=True, null=True)  # Field name made lowercase.
    user_os_version_max = models.TextField(db_column='User_os_version_max', blank=True, null=True)  # Field name made lowercase.
    include_audiences_id = models.TextField(db_column='Include_audiences_ID', blank=True, null=True)  # Field name made lowercase.
    exclude_audiences_id = models.TextField(db_column='Exclude_audiences_ID', blank=True, null=True)  # Field name made lowercase.
    ad_name = models.TextField(db_column='Ad_name', blank=True, null=True)  # Field name made lowercase.
    ad_status = models.TextField(db_column='Ad_status', blank=True, null=True)  # Field name made lowercase.
    ad_format = models.TextField(db_column='Ad_format', blank=True, null=True)  # Field name made lowercase.
    image_id = models.TextField(db_column='Image_ID', blank=True, null=True)  # Field name made lowercase.
    video_id = models.TextField(db_column='Video_ID', blank=True, null=True)  # Field name made lowercase.
    title = models.TextField(db_column='Title', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    call_to_action = models.TextField(db_column='Call_to_action', blank=True, null=True)  # Field name made lowercase.
    landing_page = models.TextField(db_column='Landing_page', blank=True, null=True)  # Field name made lowercase.
    click_url = models.TextField(db_column='Click_URL', blank=True, null=True)  # Field name made lowercase.
    sourcetype = models.CharField(db_column='SourceType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sourcesubtype = models.CharField(db_column='SourceSubType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    clientname = models.CharField(db_column='ClientName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    accountname = models.CharField(db_column='AccountName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    media = models.CharField(max_length=255, blank=True, null=True)
    group_type = models.CharField(max_length=255, blank=True, null=True)
    link_type = models.CharField(max_length=255, blank=True, null=True)
    ga1 = models.TextField(db_column='GA1', blank=True, null=True)  # Field name made lowercase.
    ga2 = models.TextField(db_column='GA2', blank=True, null=True)  # Field name made lowercase.
    ga3 = models.TextField(db_column='GA3', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'line_material'

#統計客戶&產品別
def get_info(df,df_len):
    info_list=[[],[],[],[],[],[],[],[]] # cli_name, pro_name, campaign, Ga1, Ga2, Ga3, media, link_type

    for i in range(df_len):
        if df[i]["clientname"] not in info_list[0]:
            info_list[0].append(df[i]["clientname"])
        if df[i]["productname"] not in info_list[1]:
            info_list[1].append(df[i]["productname"])
        if df[i]["campaign"] not in info_list[2]:
            info_list[2].append(df[i]["campaign"])
        if df[i]["ga1"] not in info_list[3]:
            info_list[3].append(df[i]["ga1"])
        if df[i]["ga2"] not in info_list[4]:
            info_list[4].append(df[i]["ga2"])
        if df[i]["ga3"] not in info_list[5]:
            info_list[5].append(df[i]["ga3"])
        if df[i]["media"] not in info_list[6]:
            info_list[6].append(df[i]["media"])
        if df[i]["link_type"] not in info_list[7]:
            info_list[7].append(df[i]["link_type"])
        
    return info_list


def top3():
    date1 = datetime.today() - dt.timedelta(days = 100)
    date2 = datetime.today()
    df = CrosWeb.objects.filter(date__date__range=[date1,date2]).values()

    df_len = len(df)

    cli_name,pro_name = get_info(df,df_len)

    sales_ranking = []
    sales_ranking_sort = []
    top3_list = []

    for i in cli_name:
        sales = 0
        for j in range(df_len):
            if df[j]["clientname"] == i:
                sales+= df[j]['profit']
        sales_ranking.append(sales)
        sales_ranking_sort.append(sales)
        sales = 0
    sales_ranking_sort.sort()
    sales_ranking_sort.reverse()
    for k in range(3):
        top3_list.append(cli_name[sales_ranking.index(sales_ranking_sort[k])])


    #匯出json格式
    df = CrosWeb.objects.filter(clientname__in = top3_list ,date__date__range=[date1,date2]).values()
    df_len = len(df)
    cli_name,pro_name = get_info(df,df_len)

    df_json_list = []
    df_json_list.append({"clients":cli_name,"products":pro_name})
    df_json = {'clientname':"",'productname':"",'date':"",'visitors':"",'cv':"",'profit':"",'cvr':"",'unitprice':""}
    i_date = df[0]["date"]

    i_cli = df[0]["clientname"]
    i_list = []
    cv = 0
    profit = 0
    visitors = 0

    for i in range(df_len):
        if i == (df_len-1):
            df_json['clientname'] = df[i]["clientname"]
            df_json['productname'] = df[i]["productname"]
            df_json['date'] = str(df[i]["date"])[:10]
            df_json['visitors'] = visitors
            df_json['cv'] = cv
            df_json['profit'] = profit
            try:
                df_json['cvr'] = cv/visitors
            except ZeroDivisionError:
                df_json['cvr'] =0
            try:
                df_json['unitprice'] = profit/cv
            except ZeroDivisionError:
                df_json['unitprice'] =0
            df_json_list.append(df_json)
            break

        elif i_cli == df[i]['clientname'] and i_date == df[i]["date"]:

            cv+=df[i]["cv"]
            profit+=df[i]["profit"]
            visitors+=df[i]['visitors']
        else:

            df_json['clientname'] = df[i-1]["clientname"]
            df_json['productname'] = df[i-1]["productname"]
            df_json['date'] = str(df[i-1]["date"])[:10]
            df_json['visitors'] = visitors
            df_json['cv'] = cv
            df_json['profit'] = profit
            try:
                df_json['cvr'] = cv/visitors
            except ZeroDivisionError:
                df_json['cvr'] =0
            try:
                df_json['unitprice'] = profit/cv
            except ZeroDivisionError:
                df_json['unitprice'] =0
            df_json_list.append(df_json)

            #Reset
            df_json = {'clientname':"",'productname':"",'date':"",'visitors':"",'cv':"",'profit':"",'cvr':"",'unitprice':""}
            i_date= df[i]["date"]
            i_cli = df[i]["clientname"]
            cv = df[i]["cv"]
            profit = df[i]["profit"]
            visitors =df[i]["visitors"]

    return df_json_list



"""
def data_view(ind,pro,cli):
    if ind ==[""] and pro ==[""] and cli ==[""]:
        df = ClientProduct.objects.all()
    elif ind ==[""] and pro ==[""]:
        df = ClientProduct.objects.filter(clientname__in = cli)
    elif ind ==[""] and cli ==[""]:
        df = ClientProduct.objects.filter(productname__in = pro)
    elif pro ==[""] and cli ==[""]:
        df = ClientProduct.objects.filter(industrytype__in = ind)
    elif ind ==[""] :
        df = ClientProduct.objects.filter(productname__in = pro, clientname__in = cli)
    elif pro ==[""] :
        df = ClientProduct.objects.filter(industrytype__in = ind , clientname__in = cli)
    elif cli ==[""] :
        df = ClientProduct.objects.filter(industrytype__in = ind ,productname__in = pro)
    else :
        df = ClientProduct.objects.filter(industrytype__in = ind ,productname__in = pro, clientname__in = cli)

    df = list(df.values())
    return df
"""
def data_view():
    print("data sent")
    df = ClientProduct.objects.all()
    df = list(df.values())
    return df

"""
#從前端接收
def cros_view(date1,date2,cli,pro):

    if date1 == ['']:
        date1[0] = datetime.today() - dt.timedelta(days = 100)
    else:
        date1[0] = datetime.strptime(date1[0],"%Y-%m-%d")

    if date2 == ['']:
        date2[0] = datetime.today()
    else:
        date2[0] = datetime.strptime(date2[0],"%Y-%m-%d")

#日期順序防呆

    if date1[0] > date2[0]:
        tmp = date1[0]
        date1[0] = date2[0]
        date2[0] = tmp

    #確認商品數量
    if len(pro) >1:
        query = reduce(operator.or_,(Q(productname__icontains = i )for i in pro))
        #query2 = reduce(operator.or_,(Q(productname__icontains = i )for i in pro))
        #query3 = reduce(operator.or_,(Q(productname__icontains = i )for i in pro))
        #query4 ....
        df = CrosWeb.objects.filter(query,date__date__range=[date1[0],date2[0]]).values()
    else:
        df = CrosWeb.objects.filter(clientname__in = cli,date__date__range=[date1[0],date2[0]]).values()

    df_len = len(df)
#如果df沒有資料，則回傳空的json檔
    if df_len == 0:
        df_json_list = [{'clientname':"",'productname':"",'date':"",'visitors':"",'cv':"",'profit':"",'cvr':"",'unitprice':""}]
        return df_json_list

    cli_name,pro_name = get_info(df,df_len)

    #同日期加總
    df_json_list = []
    df_json_list.append({"clients":cli_name,"products":pro_name})
    df_json = {'clientname':"",'productname':"",'date':"",'visitors':"",'cv':"",'profit':"",'cvr':"",'unitprice':""}
    i_date = df[0]["date"]

    i_cli = df[0]["clientname"]
    i_list = []
    cv = 0
    profit = 0
    visitors = 0

    for i in range(df_len):
        if i == (df_len-1):
            df_json['clientname'] = df[i]["clientname"]
            df_json['productname'] = df[i]["productname"]
            df_json['date'] = str(df[i]["date"])[:10]
            df_json['visitors'] = visitors
            df_json['cv'] = cv
            df_json['profit'] = profit
            try:
                df_json['cvr'] = cv/visitors
            except ZeroDivisionError:
                df_json['cvr'] =0
            try:
                df_json['unitprice'] = profit/cv
            except ZeroDivisionError:
                df_json['unitprice'] =0
            df_json_list.append(df_json)
            break

        elif i_cli == df[i]['clientname'] and i_date == df[i]["date"]:

            cv+=df[i]["cv"]
            profit+=df[i]["profit"]
            visitors+=df[i]['visitors']
        else:

            df_json['clientname'] = df[i-1]["clientname"]
            df_json['productname'] = df[i-1]["productname"]
            df_json['date'] = str(df[i-1]["date"])[:10]
            df_json['visitors'] = visitors
            df_json['cv'] = cv
            df_json['profit'] = profit
            try:
                df_json['cvr'] = cv/visitors
            except ZeroDivisionError:
                df_json['cvr'] =0
            try:
                df_json['unitprice'] = profit/cv
            except ZeroDivisionError:
                df_json['unitprice'] =0
            df_json_list.append(df_json)

            #Reset
            df_json = {'clientname':"",'productname':"",'date':"",'visitors':"",'cv':"",'profit':"",'cvr':"",'unitprice':""}
            i_date= df[i]["date"]
            i_cli = df[i]["clientname"]
            cv = df[i]["cv"]
            profit = df[i]["profit"]
            visitors =df[i]["visitors"]

    return df_json_list

#x = cl.cros_view(["2019-02-05"],["2019-08-10"],pro = ["Macchia Label潤澤透顏持妝精華粉底"],cli = ["JIMOS"])
"""

"""


import operator
from django.db.models import Q
from functools import reduce

q = ['x', 'y', 'z']
query = reduce(operator.or_, (Q(first_name__contains = item) for item in q))
result = User.objects.filter(query)
"""

#下載excel檔功能
def to_excel(x):
    col = ["clientname",'productname','date','visitors','cv','profit','cvr','unitprice']
    df = pd.DataFrame(columns=col)
    for i in range(1,len(x)):
        df.loc[i-1] = list(x[i].values())
    df.to_excel("./download/qwe.xlsx")

#日期格式函式
def dateToDf(date1,date2):
    if date1 == ['']:
        date1[0] = datetime.today() - dt.timedelta(days = 100)
    else:
        date1[0] = datetime.strptime(date1[0],"%Y-%m-%d")

    if date2 == ['']:
        date2[0] = datetime.today()
    else:
        date2[0] = datetime.strptime(date2[0],"%Y-%m-%d")

#日期順序防呆

    if date1[0] > date2[0]:
        tmp = date1[0]
        date1[0] = date2[0]
        date2[0] = tmp
    return date1,date2

#資料庫搜尋函式
def queryForDB(date1,date2,cli,pro,cam,g1,g2,g3,med,lin,pay,reg,ord):
    if len(cli) >1:
        query_cli = reduce(operator.or_,(Q(clientname__icontains = i )for i in cli))
    else:
        query_cli = Q(clientname__icontains =cli[0])

    if len(pro) >1:
        query_pro = reduce(operator.or_,(Q(productname__icontains = i )for i in pro))
    else:
        query_pro = Q(productname__icontains =pro[0])
    
    if len(cam) >1:
        query_cam = reduce(operator.or_,(Q(campaign__icontains = i )for i in cam))
    else:
        query_cam = Q(campaign__icontains =cam[0])

    if len(g1) >1:
        query_g1 = reduce(operator.or_,(Q(ga1__icontains = i )for i in g1))
    else:
        query_g1 = Q(ga1__icontains =g1[0])

    if len(g2) >1:
        query_g2 = reduce(operator.or_,(Q(ga2__icontains = i )for i in g2))
    else:
        query_g2 = Q(ga2__icontains =g2[0])

    if len(g3) >1:
        query_g3 = reduce(operator.or_,(Q(ga3__icontains = i )for i in g3))
    else:
        query_g3 = Q(ga3__icontains =g3[0])

    if len(med) >1:
        query_med = reduce(operator.or_,(Q(media__icontains = i )for i in med))
    else:
        query_med = Q(media__icontains =med[0])

    if len(lin) >1:
        query_lin = reduce(operator.or_,(Q(link_type__icontains = i )for i in lin))
    else:
        query_lin = Q(link_type__icontains =lin[0])

    if len(pay) >1:
        query_pay = reduce(operator.or_,(Q(pay_method__icontains = i )for i in pay))
    else:
        query_pay = Q(pay_method__icontains =pay[0])
    
    if len(reg) >1:
        query_reg = reduce(operator.or_,(Q(regular__icontains = i )for i in reg))
    else:
        query_reg = Q(regular__icontains =reg[0])
    
    if len(ord) >1:
        query_ord = reduce(operator.or_,(Q(order_type__icontains = i )for i in ord))
    else:
        query_ord = Q(order_type__icontains =ord[0])


    df = CrosOrder.objects.filter(query_cli,query_pro,query_cam,query_g1,query_g2,query_g3,query_med,query_lin,query_pay,query_reg,query_ord,stadatetime__date__range=[date1[0],date2[0]],order_status="900").values()
    df = df.order_by("clientname","stadatetime","ga3")
    return df

#從前端接收
# cli_name, pro_name, campaign, Ga1, Ga2, Ga3, media, link_type
def cros_view(date1,date2,cli,pro,cam,g1,g2,g3,med,lin,pay,reg,ord):

    date1,date2 = dateToDf(date1,date2)    

    #篩選條件寫入
    df = queryForDB(date1,date2,cli,pro,cam,g1,g2,g3,med,lin,pay,reg,ord)
    
    df_len = len(df)

#如果df沒有資料，則回傳空的json檔
    if df_len == 0:
        df_json_list = [{"clients":"","products":"","campaign":"","ga1":"","ga2":"","ga3":"","media":"","link_type":""},{'clientname':"",'productname':"",'date':"",'cv':"",'profit':"",'unitprice':"","ordertype":"","regular":""}]
        return df_json_list

    info_list = get_info(df,df_len)

    #同日期加總
    df_json_list = []
    #第一筆為資訊包
    df_json_list.append({"clients":info_list[0],"products":info_list[1],"campaign":info_list[2],"ga1":info_list[3],"ga2":info_list[4],"ga3":info_list[5],"media":info_list[6],"link_type":info_list[7]})
    df_json = {'clientname':"",'productname':"",'date':"",'cv':"",'profit':"",'unitprice':"","ordertype":"","regular":""}
    constrct_list =[date1[0].date(),df[0]["clientname"]]
    i_list = []
    cv = 0
    profit = 0
    orderTypeInfo = [0,0] #新規,既存
    regularInfo = [0,0]   #都度,定期

    for i in range(df_len):
        #最後一筆的情況
        #會出現極端狀況，當最後一筆資料為獨立資料時，會出現怪狀況，這個等之後再討論
        if i == (df_len-1):
            df_json['clientname'] = df[i]["clientname"]
            df_json['productname'] = df[i]["productname"]
            df_json['date'] = str(df[i]["stadatetime"])[:10]
            df_json['cv'] = cv
            df_json['profit'] = profit
            df_json['ordertype'] = orderTypeInfo
            df_json['regular'] = regularInfo

            try:
                df_json['unitprice'] = profit/cv
            except ZeroDivisionError:
                df_json['unitprice'] =0
            df_json_list.append(df_json)
            break
        elif constrct_list[0] != df[i]["stadatetime"].date() and i==0:
            dateRange = -(constrct_list[0] - df[i]["stadatetime"].date()).days
                
            for j in range(dateRange):
                df_json_list.append({'clientname':df[i]["clientname"],'productname':df[i]["productname"],'date':str(constrct_list[0]+ dt.timedelta(days=j)),'cv':0,'profit':0,'unitprice':0,"ordertype":[0,0],"regular":[0,0]})

            df_json = {'clientname':"",'productname':"",'date':"",'cv':"",'profit':"",'unitprice':"","ordertype":"","regular":""}
            cv = 1
            profit = df[i]["order_price"]
            orderTypeInfo = [0,0] 
            regularInfo = [0,0]   
            if df[i]["order_type"] == "新規":
                orderTypeInfo[0]+=1
            elif df[i]["order_type"] == "既存":
                orderTypeInfo[1]+=1                
            if df[i]["regular"] == "1":
                regularInfo[0]+=1
            elif df[i]["regular"] == "0": #定期
                regularInfo[1]+=1
            constrct_list[0] = df[i]["stadatetime"].date()
    
        elif constrct_list[0] == df[i]["stadatetime"].date() and constrct_list[1] == df[i]["clientname"] :
            
            cv+=1
            profit+=df[i]["order_price"]
            #新規既存判斷
            if df[i]["order_type"] == "新規":
                orderTypeInfo[0]+=1
            elif df[i]["order_type"] == "既存":
                orderTypeInfo[1]+=1
            #定期都度判斷
            if df[i]["regular"] == "1":
                regularInfo[0]+=1
            elif df[i]["regular"] == "0":
                regularInfo[1]+=1

            
        else:
            
            df_json['clientname'] = df[i-1]["clientname"]
            df_json['productname'] = df[i-1]["productname"]
            df_json['date'] = str(constrct_list[0])
            df_json['cv'] = cv
            df_json['profit'] = profit
            df_json['ordertype'] = orderTypeInfo
            df_json['regular'] = regularInfo
            
            try:
                df_json['unitprice'] = profit/cv
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
                if df[i]["order_type"] == "新規":
                    orderTypeInfo[0]+=1
                elif df[i]["order_type"] == "既存":
                    orderTypeInfo[1]+=1                
                if df[i]["regular"] == "1":
                    regularInfo[0]+=1
                elif df[i]["regular"] == "0":
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
                if df[i]["order_type"] == "新規":
                    orderTypeInfo[0]+=1
                elif df[i]["order_type"] == "既存":
                    orderTypeInfo[1]+=1                
                if df[i]["regular"] == "1":
                    regularInfo[0]+=1
                elif df[i]["regular"] == "0":
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

                if df[i]["order_type"] == "新規":
                    orderTypeInfo[0]+=1
                elif df[i]["order_type"] == "既存":
                    orderTypeInfo[1]+=1                
                if df[i]["regular"] == "1":
                    regularInfo[0]+=1
                elif df[i]["regular"] == "0":
                    regularInfo[1]+=1


    return df_json_list

#x = cl.cros_view(["2019-02-05"],["2019-08-10"],pro = ["Macchia Label潤澤透顏持妝精華粉底"],cli = ["JIMOS"])


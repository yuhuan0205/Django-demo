# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Fbtest(models.Model):
    no = models.IntegerField(primary_key=True)
    ad_id = models.CharField(max_length=25)
    impressions = models.IntegerField()
    clicks = models.IntegerField()
    cv = models.IntegerField()
    cost = models.IntegerField()
    clientname = models.CharField(db_column='ClientName', max_length=30)  # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', max_length=100)  # Field name made lowercase.
    accountname = models.CharField(db_column='AccountName', max_length=100)  # Field name made lowercase.
    industrytype = models.CharField(db_column='IndustryType', max_length=10)  # Field name made lowercase.
    stadatetime = models.DateTimeField(db_column='StaDateTime')  # Field name made lowercase.
    group_type = models.CharField(max_length=5)
    campaign_name = models.CharField(max_length=100)
    buying_type = models.CharField(max_length=15)
    ad_set_name = models.CharField(max_length=100)
    ad_name = models.CharField(max_length=100)
    link_type = models.CharField(max_length=7)
    ga1 = models.TextField()
    ga2 = models.TextField()
    ga3 = models.TextField()

    class Meta:
        managed = False
        db_table = 'FBtest'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


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


class CrosOrderOld(models.Model):
    no = models.AutoField(db_column='No', primary_key=True)  # Field name made lowercase.
    order_id = models.TextField(db_column='Order_ID')  # Field name made lowercase.
    customer_id = models.TextField(db_column='Customer_ID')  # Field name made lowercase.
    order_status = models.TextField(db_column='Order_Status')  # Field name made lowercase.
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
        db_table = 'cros_order_old'


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
    order_type = models.CharField(max_length=10)
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


class CrosWeb(models.Model):
    no = models.BigIntegerField(primary_key=True)
    ga1 = models.TextField()
    ga2 = models.TextField()
    ga3 = models.TextField()
    w_date = models.DateTimeField()
    visitors = models.IntegerField()
    cv = models.IntegerField()
    cvr = models.FloatField()
    profit = models.IntegerField()
    unit_price = models.FloatField()
    sourcetype = models.CharField(db_column='SourceType', max_length=20)  # Field name made lowercase.
    sourcesubtype = models.CharField(db_column='SourceSubType', max_length=10)  # Field name made lowercase.
    clientname = models.CharField(db_column='ClientName', max_length=30)  # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', max_length=256)  # Field name made lowercase.
    accountname = models.CharField(db_column='AccountName', max_length=100)  # Field name made lowercase.
    stadatetime = models.DateTimeField(db_column='StaDateTime')  # Field name made lowercase.
    media = models.CharField(max_length=20)
    link_type = models.CharField(max_length=7)

    class Meta:
        managed = False
        db_table = 'cros_web'


class CrosWebOld(models.Model):
    no = models.IntegerField(db_column='No', primary_key=True)  # Field name made lowercase.
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
        db_table = 'cros_web_old'


class CrosWebShort(models.Model):
    no = models.BigIntegerField(primary_key=True)
    ga1 = models.TextField()
    ga2 = models.TextField()
    ga3 = models.TextField()
    visitors = models.IntegerField()
    cv = models.IntegerField()
    profit = models.IntegerField()
    unit_price = models.FloatField()
    clientname = models.CharField(db_column='ClientName', max_length=30)  # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', max_length=256)  # Field name made lowercase.
    accountname = models.CharField(db_column='AccountName', max_length=100)  # Field name made lowercase.
    stadatetime = models.DateTimeField(db_column='StaDateTime')  # Field name made lowercase.
    media = models.CharField(max_length=20)
    link_type = models.CharField(max_length=7)

    class Meta:
        managed = False
        db_table = 'cros_web_short'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class FbMaterial(models.Model):
    no = models.IntegerField(db_column='No')  # Field name made lowercase.
    ad_id = models.TextField(db_column='Ad_ID', blank=True, null=True)  # Field name made lowercase.
    ad_id_new = models.TextField(db_column='Ad_ID_New', blank=True, null=True)  # Field name made lowercase.
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
    clientname = models.CharField(db_column='ClientName', max_length=255)  # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    accountname = models.CharField(db_column='AccountName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    stadatetime = models.DateTimeField(db_column='StaDateTime', blank=True, null=True)  # Field name made lowercase.
    media = models.CharField(max_length=255, blank=True, null=True)
    group_type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fb_material'


class FbSystem(models.Model):
    ad_id = models.CharField(db_column='Ad_ID', primary_key=True, max_length=30)  # Field name made lowercase.
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


class FbUniversalAdOld(models.Model):
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
    campaign_name = models.CharField(max_length=100, blank=True, null=True)
    ad_set_id = models.CharField(max_length=25, blank=True, null=True)
    ad_set_name = models.CharField(max_length=100, blank=True, null=True)
    ad_name = models.CharField(max_length=100, blank=True, null=True)
    link_type = models.CharField(max_length=7, blank=True, null=True)
    ga1 = models.TextField(blank=True, null=True)
    ga2 = models.TextField(blank=True, null=True)
    ga3 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fb_universal_ad_old'


class FbUniversalOld(models.Model):
    no = models.AutoField(primary_key=True)
    ad_id = models.CharField(max_length=25)
    impressions = models.IntegerField()
    clicks = models.IntegerField()
    cv = models.IntegerField()
    cost = models.IntegerField()
    clientname = models.CharField(db_column='ClientName', max_length=30)  # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', max_length=100)  # Field name made lowercase.
    accountname = models.CharField(db_column='AccountName', max_length=100)  # Field name made lowercase.
    industrytype = models.CharField(db_column='IndustryType', max_length=10)  # Field name made lowercase.
    stadatetime = models.DateTimeField(db_column='StaDateTime')  # Field name made lowercase.
    group_type = models.CharField(max_length=5)
    campaign_id = models.CharField(max_length=25)
    campaign_name = models.CharField(max_length=100)
    campaign_status = models.CharField(max_length=10)
    campaign_objective = models.CharField(max_length=25)
    buying_type = models.CharField(max_length=15)
    campaign_daily_budget = models.IntegerField()
    ad_set_id = models.CharField(max_length=25)
    ad_set_run_status = models.CharField(max_length=10)
    ad_set_name = models.CharField(max_length=100)
    ad_set_daily_budget = models.IntegerField()
    link = models.TextField()
    gender = models.CharField(max_length=7)
    age_min = models.IntegerField()
    age_max = models.IntegerField()
    publisher_platforms = models.CharField(max_length=255)
    facebook_positions = models.CharField(max_length=255)
    instagram_positions = models.CharField(max_length=255)
    audience_network_positions = models.CharField(max_length=255)
    messenger_positions = models.CharField(max_length=255)
    device_platforms = models.CharField(max_length=30)
    optimization_goal = models.CharField(max_length=30)
    bid_amount = models.IntegerField()
    ad_status = models.CharField(max_length=10)
    ad_name = models.CharField(max_length=100)
    title = models.TextField()
    body = models.TextField()
    link_type = models.CharField(max_length=7)
    ga1 = models.TextField()
    ga2 = models.TextField()
    ga3 = models.TextField()

    class Meta:
        managed = False
        db_table = 'fb_universal_old'


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
    no = models.IntegerField()
    ad_id = models.TextField(blank=True, null=True)
    ad_id_new = models.TextField(blank=True, null=True)
    day = models.DateTimeField(blank=True, null=True)
    adaccount_name = models.TextField(blank=True, null=True)
    adaccount_id = models.TextField(blank=True, null=True)
    campaign_name = models.TextField(blank=True, null=True)
    campaign_id = models.TextField(blank=True, null=True)
    campaign_objective = models.TextField(blank=True, null=True)
    adgroup_name = models.TextField(blank=True, null=True)
    adgroup_id = models.TextField(blank=True, null=True)
    ad_name = models.TextField(blank=True, null=True)
    impression = models.IntegerField(blank=True, null=True)
    viewable_impression = models.IntegerField(blank=True, null=True)
    clicks = models.IntegerField(blank=True, null=True)
    ctr = models.TextField(blank=True, null=True)
    cpc = models.FloatField(blank=True, null=True)
    cv = models.IntegerField(blank=True, null=True)
    cvr = models.TextField(blank=True, null=True)
    cpa = models.FloatField(blank=True, null=True)
    cost = models.FloatField(blank=True, null=True)
    currency = models.TextField(blank=True, null=True)
    video_completions = models.IntegerField(blank=True, null=True)
    installs_clicks = models.IntegerField(blank=True, null=True)
    install_rate_clicks = models.FloatField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    open_rate = models.TextField(blank=True, null=True)
    cost_per_open = models.FloatField(blank=True, null=True)
    view_home = models.IntegerField(blank=True, null=True)
    view_home_rate = models.TextField(blank=True, null=True)
    cost_per_view_home = models.FloatField(blank=True, null=True)
    view_category = models.IntegerField(blank=True, null=True)
    viewcategory_rate = models.TextField(blank=True, null=True)
    cost_per_view_category = models.FloatField(blank=True, null=True)
    view_item = models.IntegerField(blank=True, null=True)
    view_item_rate = models.TextField(blank=True, null=True)
    cost_per_view_item = models.FloatField(blank=True, null=True)
    search = models.IntegerField(blank=True, null=True)
    search_rate = models.TextField(blank=True, null=True)
    cost_per_search = models.FloatField(blank=True, null=True)
    add_to_cart = models.IntegerField(blank=True, null=True)
    add_to_cart_rate = models.TextField(blank=True, null=True)
    cost_per_add_to_cart = models.FloatField(blank=True, null=True)
    purchase = models.IntegerField(blank=True, null=True)
    purchase_rate = models.TextField(blank=True, null=True)
    cost_per_purchase = models.FloatField(blank=True, null=True)
    level_achieved = models.IntegerField(blank=True, null=True)
    level_achieved_rate = models.TextField(blank=True, null=True)
    cost_per_level_achieved = models.FloatField(blank=True, null=True)
    tutorial_complete = models.IntegerField(blank=True, null=True)
    tutorial_complete_rate = models.TextField(blank=True, null=True)
    cost_per_tutorial_complete = models.FloatField(blank=True, null=True)
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
    ad_id = models.CharField(primary_key=True, max_length=30)
    ad_account_id = models.TextField(blank=True, null=True)
    campaign_id = models.TextField(blank=True, null=True)
    campaign_name = models.TextField(blank=True, null=True)
    campaign_status = models.TextField(blank=True, null=True)
    campaign_objective = models.TextField(blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    campaign_spend_limit = models.TextField(blank=True, null=True)
    budget_type = models.TextField(blank=True, null=True)
    monthly_budget = models.IntegerField(blank=True, null=True)
    lifetime_budget = models.IntegerField(blank=True, null=True)
    ad_group_id = models.TextField(blank=True, null=True)
    ad_group_name = models.TextField(blank=True, null=True)
    ad_group_status = models.TextField(blank=True, null=True)
    bidding_amount_configuration = models.TextField(blank=True, null=True)
    optimize_for = models.TextField(blank=True, null=True)
    payment_method = models.TextField(blank=True, null=True)
    bid_amount = models.FloatField(blank=True, null=True)
    max_cpc = models.FloatField(blank=True, null=True)
    max_cpa = models.FloatField(blank=True, null=True)
    daily_budget = models.IntegerField(blank=True, null=True)
    gender = models.TextField(blank=True, null=True)
    age_min = models.IntegerField(blank=True, null=True)
    age_max = models.IntegerField(blank=True, null=True)
    user_os = models.TextField(blank=True, null=True)
    user_os_version_min = models.TextField(blank=True, null=True)
    user_os_version_max = models.TextField(blank=True, null=True)
    include_audiences_id = models.TextField(blank=True, null=True)
    exclude_audiences_id = models.TextField(blank=True, null=True)
    ad_name = models.TextField(blank=True, null=True)
    ad_status = models.TextField(blank=True, null=True)
    ad_format = models.TextField(blank=True, null=True)
    image_id = models.TextField(blank=True, null=True)
    video_id = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    call_to_action = models.TextField(blank=True, null=True)
    landing_page = models.TextField(blank=True, null=True)
    click_url = models.TextField(blank=True, null=True)
    sourcetype = models.CharField(db_column='SourceType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sourcesubtype = models.CharField(db_column='SourceSubType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    clientname = models.CharField(db_column='ClientName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    accountname = models.CharField(db_column='AccountName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    media = models.CharField(max_length=255, blank=True, null=True)
    group_type = models.CharField(max_length=255, blank=True, null=True)
    link_type = models.CharField(max_length=255, blank=True, null=True)
    ga1 = models.TextField(blank=True, null=True)
    ga2 = models.TextField(blank=True, null=True)
    ga3 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'line_material'


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
    campaign_name = models.CharField(max_length=100)
    adgroup_id = models.CharField(max_length=20)
    adgroup_name = models.CharField(max_length=256)
    ad_name = models.CharField(max_length=256)
    impression = models.IntegerField()
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


class LineUniversalOld(models.Model):
    no = models.BigIntegerField(primary_key=True)
    ad_id = models.CharField(max_length=25, blank=True, null=True)
    stadatetime = models.DateTimeField(db_column='StaDateTime', blank=True, null=True)  # Field name made lowercase.
    adaccount_id = models.CharField(max_length=20)
    campaign_id = models.CharField(max_length=20)
    campaign_name = models.CharField(max_length=100)
    adgroup_id = models.CharField(max_length=20)
    adgroup_name = models.CharField(max_length=256)
    ad_name = models.CharField(max_length=256)
    impression = models.IntegerField(blank=True, null=True)
    clicks = models.IntegerField(blank=True, null=True)
    cv = models.IntegerField(blank=True, null=True)
    cost = models.FloatField(blank=True, null=True)
    industrytype = models.CharField(db_column='IndustryType', max_length=10)  # Field name made lowercase.
    group_type = models.CharField(max_length=5)
    link_type = models.CharField(max_length=7)
    clientname = models.CharField(db_column='ClientName', max_length=30)  # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', max_length=100)  # Field name made lowercase.
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
        db_table = 'line_universal_old'

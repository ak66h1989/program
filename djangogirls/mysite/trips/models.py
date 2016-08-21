# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = True
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    username = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = True
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_session'


class Forr(models.Model):
    年月日 = models.DateField(blank=True, null=True)
    證券代號 = models.TextField(blank=True, null=True)
    time = models.FloatField(blank=True, null=True)
    成交股數 = models.FloatField(blank=True, null=True)
    成交筆數 = models.FloatField(blank=True, null=True)
    成交金額 = models.FloatField(blank=True, null=True)
    開盤價 = models.FloatField(blank=True, null=True)
    最高價 = models.FloatField(blank=True, null=True)
    最低價 = models.FloatField(blank=True, null=True)
    收盤價 = models.FloatField(blank=True, null=True)
    漲跌_field = models.TextField(db_column='漲跌(+/-)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    漲跌價差 = models.FloatField(blank=True, null=True)
    最後揭示買價 = models.FloatField(blank=True, null=True)
    最後揭示買量 = models.FloatField(blank=True, null=True)
    最後揭示賣價 = models.FloatField(blank=True, null=True)
    最後揭示賣量 = models.FloatField(blank=True, null=True)
    本益比 = models.FloatField(blank=True, null=True)
    殖利率_field = models.FloatField(db_column='殖利率(%)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    股價淨值比 = models.FloatField(blank=True, null=True)
    自營商_自行買賣_賣出股數 = models.FloatField(db_column='自營商(自行買賣)賣出股數', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    自營商_自行買賣_買賣超股數 = models.FloatField(db_column='自營商(自行買賣)買賣超股數', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    自營商_自行買賣_買進股數 = models.FloatField(db_column='自營商(自行買賣)買進股數', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    自營商_避險_賣出股數 = models.FloatField(db_column='自營商(避險)賣出股數', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    自營商_避險_買賣超股數 = models.FloatField(db_column='自營商(避險)買賣超股數', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    自營商_避險_買進股數 = models.FloatField(db_column='自營商(避險)買進股數', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    自營商賣出股數 = models.FloatField(blank=True, null=True)
    自營商買賣超股數 = models.FloatField(blank=True, null=True)
    自營商買進股數 = models.FloatField(blank=True, null=True)
    外資鉅額交易 = models.TextField(blank=True, null=True)
    外資買進股數 = models.FloatField(blank=True, null=True)
    外資賣出股數 = models.FloatField(blank=True, null=True)
    外資買賣超股數 = models.FloatField(blank=True, null=True)
    投信鉅額交易 = models.TextField(blank=True, null=True)
    投信買進股數 = models.FloatField(blank=True, null=True)
    投信賣出股數 = models.FloatField(blank=True, null=True)
    投信買賣超股數 = models.FloatField(blank=True, null=True)
    基本每股盈餘_元_field = models.FloatField(db_column='基本每股盈餘（元）', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    每股參考淨值 = models.FloatField(blank=True, null=True)
    流動比率 = models.FloatField(blank=True, null=True)
    負債佔資產比率 = models.FloatField(blank=True, null=True)
    權益報酬率 = models.FloatField(blank=True, null=True)
    毛利率 = models.FloatField(blank=True, null=True)
    營業利益率 = models.FloatField(blank=True, null=True)
    綜合稅後純益率 = models.FloatField(blank=True, null=True)
    grow_s = models.FloatField(blank=True, null=True)
    grow_hy = models.FloatField(blank=True, null=True)
    grow_y = models.FloatField(blank=True, null=True)
    grow = models.FloatField(blank=True, null=True)
    本期綜合損益總額_wma = models.FloatField(db_column='本期綜合損益總額.wma', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    本期綜合損益總額_ma = models.FloatField(db_column='本期綜合損益總額.ma', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    profitbility = models.FloatField(blank=True, null=True)
    investment = models.FloatField(blank=True, null=True)
    建材營造類指數 = models.FloatField(blank=True, null=True)
    漲跌點數 = models.FloatField(blank=True, null=True)
    漲跌百分比_field = models.FloatField(db_column='漲跌百分比(%)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    建材營造類報酬指數 = models.FloatField(blank=True, null=True)
    r漲跌點數 = models.FloatField(blank=True, null=True)
    r漲跌百分比_field = models.FloatField(db_column='r漲跌百分比(%)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    lnmo = models.FloatField(blank=True, null=True)
    lnr = models.FloatField(blank=True, null=True)
    lnr025 = models.FloatField(blank=True, null=True)
    lnr05 = models.FloatField(blank=True, null=True)
    lnr1 = models.FloatField(blank=True, null=True)
    lnr2 = models.FloatField(blank=True, null=True)
    lnr3 = models.FloatField(blank=True, null=True)
    lnr6 = models.FloatField(blank=True, null=True)
    r025 = models.FloatField(blank=True, null=True)
    r05 = models.FloatField(blank=True, null=True)
    r1 = models.FloatField(blank=True, null=True)
    r2 = models.FloatField(blank=True, null=True)
    r3 = models.FloatField(blank=True, null=True)
    r6 = models.FloatField(blank=True, null=True)
    r025_s = models.FloatField(db_column='r025.s', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    r05_s = models.FloatField(db_column='r05.s', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    r1_s = models.FloatField(db_column='r1.s', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    r2_s = models.FloatField(db_column='r2.s', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    r3_s = models.FloatField(db_column='r3.s', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    r6_s = models.FloatField(db_column='r6.s', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    h_l = models.FloatField(blank=True, null=True)
    p = models.FloatField(db_column='P', blank=True, null=True)  # Field name made lowercase.
    pch = models.FloatField(blank=True, null=True)
    ch = models.FloatField(blank=True, null=True)
    ch_u = models.FloatField(blank=True, null=True)
    ch_d = models.FloatField(blank=True, null=True)
    rsi = models.FloatField(blank=True, null=True)
    ma5 = models.FloatField(db_column='MA5', blank=True, null=True)  # Field name made lowercase.
    ma20 = models.FloatField(db_column='MA20', blank=True, null=True)  # Field name made lowercase.
    ma60 = models.FloatField(db_column='MA60', blank=True, null=True)  # Field name made lowercase.
    ma120 = models.FloatField(db_column='MA120', blank=True, null=True)  # Field name made lowercase.
    max9 = models.FloatField(blank=True, null=True)
    min9 = models.FloatField(blank=True, null=True)
    ema12 = models.FloatField(db_column='EMA12', blank=True, null=True)  # Field name made lowercase.
    ema26 = models.FloatField(db_column='EMA26', blank=True, null=True)  # Field name made lowercase.
    dif = models.FloatField(db_column='DIF', blank=True, null=True)  # Field name made lowercase.
    macd = models.FloatField(db_column='MACD', blank=True, null=True)  # Field name made lowercase.
    macd1 = models.FloatField(db_column='MACD1', blank=True, null=True)  # Field name made lowercase.
    osc = models.FloatField(db_column='OSC', blank=True, null=True)  # Field name made lowercase.
    rsv = models.FloatField(blank=True, null=True)
    k = models.FloatField(blank=True, null=True)
    d = models.FloatField(blank=True, null=True)
    p1 = models.FloatField(db_column='P1', blank=True, null=True)  # Field name made lowercase.
    mavg = models.FloatField(blank=True, null=True)
    up = models.FloatField(blank=True, null=True)
    dn = models.FloatField(blank=True, null=True)
    pctb = models.FloatField(db_column='pctB', blank=True, null=True)  # Field name made lowercase.
    c_up = models.FloatField(blank=True, null=True)
    c_dn = models.FloatField(blank=True, null=True)
    std5 = models.FloatField(blank=True, null=True)
    std10 = models.FloatField(blank=True, null=True)
    std20 = models.FloatField(blank=True, null=True)
    twii = models.FloatField(db_column='TWII', blank=True, null=True)  # Field name made lowercase.
    sse = models.FloatField(db_column='SSE', blank=True, null=True)  # Field name made lowercase.
    hsi = models.FloatField(db_column='HSI', blank=True, null=True)  # Field name made lowercase.
    sti = models.FloatField(db_column='STI', blank=True, null=True)  # Field name made lowercase.
    n225 = models.FloatField(db_column='N225', blank=True, null=True)  # Field name made lowercase.
    axjo = models.FloatField(db_column='AXJO', blank=True, null=True)  # Field name made lowercase.
    gspc = models.FloatField(db_column='GSPC', blank=True, null=True)  # Field name made lowercase.
    ixic = models.FloatField(db_column='IXIC', blank=True, null=True)  # Field name made lowercase.
    gdaxi = models.FloatField(db_column='GDAXI', blank=True, null=True)  # Field name made lowercase.
    ftse = models.FloatField(db_column='FTSE', blank=True, null=True)  # Field name made lowercase.
    stoxx50e = models.FloatField(db_column='STOXX50E', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'forr'


class Forr1(models.Model):
    年月日 = models.DateField(blank=True, primary_key=True)
    證券代號 = models.TextField(blank=True, primary_key=True)
    time = models.FloatField(blank=True, null=True)
    成交股數 = models.FloatField(blank=True, null=True)
    成交筆數 = models.FloatField(blank=True, null=True)
    成交金額 = models.FloatField(blank=True, null=True)
    開盤價 = models.FloatField(blank=True, null=True)
    最高價 = models.FloatField(blank=True, null=True)
    最低價 = models.FloatField(blank=True, null=True)
    收盤價 = models.FloatField(blank=True, null=True)
    漲跌_field = models.TextField(db_column='漲跌(+/-)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    漲跌價差 = models.FloatField(blank=True, null=True)
    最後揭示買價 = models.FloatField(blank=True, null=True)
    最後揭示買量 = models.FloatField(blank=True, null=True)
    最後揭示賣價 = models.FloatField(blank=True, null=True)
    最後揭示賣量 = models.FloatField(blank=True, null=True)
    本益比 = models.FloatField(blank=True, null=True)
    殖利率_field = models.FloatField(db_column='殖利率(%)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    股價淨值比 = models.FloatField(blank=True, null=True)
    自營商_自行買賣_賣出股數 = models.FloatField(db_column='自營商(自行買賣)賣出股數', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    自營商_自行買賣_買賣超股數 = models.FloatField(db_column='自營商(自行買賣)買賣超股數', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    自營商_自行買賣_買進股數 = models.FloatField(db_column='自營商(自行買賣)買進股數', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    自營商_避險_賣出股數 = models.FloatField(db_column='自營商(避險)賣出股數', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    自營商_避險_買賣超股數 = models.FloatField(db_column='自營商(避險)買賣超股數', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    自營商_避險_買進股數 = models.FloatField(db_column='自營商(避險)買進股數', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    自營商賣出股數 = models.FloatField(blank=True, null=True)
    自營商買賣超股數 = models.FloatField(blank=True, null=True)
    自營商買進股數 = models.FloatField(blank=True, null=True)
    外資鉅額交易 = models.TextField(blank=True, null=True)
    外資買進股數 = models.FloatField(blank=True, null=True)
    外資賣出股數 = models.FloatField(blank=True, null=True)
    外資買賣超股數 = models.FloatField(blank=True, null=True)
    投信鉅額交易 = models.TextField(blank=True, null=True)
    投信買進股數 = models.FloatField(blank=True, null=True)
    投信賣出股數 = models.FloatField(blank=True, null=True)
    投信買賣超股數 = models.FloatField(blank=True, null=True)
    基本每股盈餘_元_field = models.FloatField(db_column='基本每股盈餘（元）', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    每股參考淨值 = models.FloatField(blank=True, null=True)
    流動比率 = models.FloatField(blank=True, null=True)
    負債佔資產比率 = models.FloatField(blank=True, null=True)
    權益報酬率 = models.FloatField(blank=True, null=True)
    毛利率 = models.FloatField(blank=True, null=True)
    營業利益率 = models.FloatField(blank=True, null=True)
    綜合稅後純益率 = models.FloatField(blank=True, null=True)
    grow_s = models.FloatField(blank=True, null=True)
    grow_hy = models.FloatField(blank=True, null=True)
    grow_y = models.FloatField(blank=True, null=True)
    grow = models.FloatField(blank=True, null=True)
    本期綜合損益總額_wma = models.FloatField(db_column='本期綜合損益總額.wma', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    本期綜合損益總額_ma = models.FloatField(db_column='本期綜合損益總額.ma', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    profitbility = models.FloatField(blank=True, null=True)
    investment = models.FloatField(blank=True, null=True)
    建材營造類指數 = models.FloatField(blank=True, null=True)
    漲跌點數 = models.FloatField(blank=True, null=True)
    漲跌百分比_field = models.FloatField(db_column='漲跌百分比(%)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    建材營造類報酬指數 = models.FloatField(blank=True, null=True)
    r漲跌點數 = models.FloatField(blank=True, null=True)
    r漲跌百分比_field = models.FloatField(db_column='r漲跌百分比(%)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    lnmo = models.FloatField(blank=True, null=True)
    lnr = models.FloatField(blank=True, null=True)
    lnr025 = models.FloatField(blank=True, null=True)
    lnr05 = models.FloatField(blank=True, null=True)
    lnr1 = models.FloatField(blank=True, null=True)
    lnr2 = models.FloatField(blank=True, null=True)
    lnr3 = models.FloatField(blank=True, null=True)
    lnr6 = models.FloatField(blank=True, null=True)
    r025 = models.FloatField(blank=True, null=True)
    r05 = models.FloatField(blank=True, null=True)
    r1 = models.FloatField(blank=True, null=True)
    r2 = models.FloatField(blank=True, null=True)
    r3 = models.FloatField(blank=True, null=True)
    r6 = models.FloatField(blank=True, null=True)
    r025_s = models.FloatField(db_column='r025.s', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    r05_s = models.FloatField(db_column='r05.s', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    r1_s = models.FloatField(db_column='r1.s', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    r2_s = models.FloatField(db_column='r2.s', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    r3_s = models.FloatField(db_column='r3.s', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    r6_s = models.FloatField(db_column='r6.s', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    h_l = models.FloatField(blank=True, null=True)
    p = models.FloatField(db_column='P', blank=True, null=True)  # Field name made lowercase.
    pch = models.FloatField(blank=True, null=True)
    ch = models.FloatField(blank=True, null=True)
    ch_u = models.FloatField(blank=True, null=True)
    ch_d = models.FloatField(blank=True, null=True)
    rsi = models.FloatField(blank=True, null=True)
    ma5 = models.FloatField(db_column='MA5', blank=True, null=True)  # Field name made lowercase.
    ma20 = models.FloatField(db_column='MA20', blank=True, null=True)  # Field name made lowercase.
    ma60 = models.FloatField(db_column='MA60', blank=True, null=True)  # Field name made lowercase.
    ma120 = models.FloatField(db_column='MA120', blank=True, null=True)  # Field name made lowercase.
    max9 = models.FloatField(blank=True, null=True)
    min9 = models.FloatField(blank=True, null=True)
    ema12 = models.FloatField(db_column='EMA12', blank=True, null=True)  # Field name made lowercase.
    ema26 = models.FloatField(db_column='EMA26', blank=True, null=True)  # Field name made lowercase.
    dif = models.FloatField(db_column='DIF', blank=True, null=True)  # Field name made lowercase.
    macd = models.FloatField(db_column='MACD', blank=True, null=True)  # Field name made lowercase.
    macd1 = models.FloatField(db_column='MACD1', blank=True, null=True)  # Field name made lowercase.
    osc = models.FloatField(db_column='OSC', blank=True, null=True)  # Field name made lowercase.
    rsv = models.FloatField(blank=True, null=True)
    k = models.FloatField(blank=True, null=True)
    d = models.FloatField(blank=True, null=True)
    p1 = models.FloatField(db_column='P1', blank=True, null=True)  # Field name made lowercase.
    mavg = models.FloatField(blank=True, null=True)
    up = models.FloatField(blank=True, null=True)
    dn = models.FloatField(blank=True, null=True)
    pctb = models.FloatField(db_column='pctB', blank=True, null=True)  # Field name made lowercase.
    c_up = models.FloatField(blank=True, null=True)
    c_dn = models.FloatField(blank=True, null=True)
    std5 = models.FloatField(blank=True, null=True)
    std10 = models.FloatField(blank=True, null=True)
    std20 = models.FloatField(blank=True, null=True)
    twii = models.FloatField(db_column='TWII', blank=True, null=True)  # Field name made lowercase.
    sse = models.FloatField(db_column='SSE', blank=True, null=True)  # Field name made lowercase.
    hsi = models.FloatField(db_column='HSI', blank=True, null=True)  # Field name made lowercase.
    sti = models.FloatField(db_column='STI', blank=True, null=True)  # Field name made lowercase.
    n225 = models.FloatField(db_column='N225', blank=True, null=True)  # Field name made lowercase.
    axjo = models.FloatField(db_column='AXJO', blank=True, null=True)  # Field name made lowercase.
    gspc = models.FloatField(db_column='GSPC', blank=True, null=True)  # Field name made lowercase.
    ixic = models.FloatField(db_column='IXIC', blank=True, null=True)  # Field name made lowercase.
    gdaxi = models.FloatField(db_column='GDAXI', blank=True, null=True)  # Field name made lowercase.
    ftse = models.FloatField(db_column='FTSE', blank=True, null=True)  # Field name made lowercase.
    stoxx50e = models.FloatField(db_column='STOXX50E', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'forr1'
    def __str__(self):
        return self.年月日

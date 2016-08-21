# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        
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
        
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        
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
        
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        
        db_table = 'django_session'


class Forr(models.Model):
    �~��� = models.DateField(blank=True, null=True)
    �Ҩ�N�� = models.TextField(blank=True, null=True)
    time = models.FloatField(blank=True, null=True)
    ����Ѽ� = models.FloatField(blank=True, null=True)
    ���浧�� = models.FloatField(blank=True, null=True)
    ������B = models.FloatField(blank=True, null=True)
    �}�L�� = models.FloatField(blank=True, null=True)
    �̰��� = models.FloatField(blank=True, null=True)
    �̧C�� = models.FloatField(blank=True, null=True)
    ���L�� = models.FloatField(blank=True, null=True)
    ���^_field = models.TextField(db_column='���^(+/-)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ���^���t = models.FloatField(blank=True, null=True)
    �̫ᴦ�ܶR�� = models.FloatField(blank=True, null=True)
    �̫ᴦ�ܶR�q = models.FloatField(blank=True, null=True)
    �̫ᴦ�ܽ�� = models.FloatField(blank=True, null=True)
    �̫ᴦ�ܽ�q = models.FloatField(blank=True, null=True)
    ���q�� = models.FloatField(blank=True, null=True)
    �ާQ�v_field = models.FloatField(db_column='�ާQ�v(%)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �ѻ��b�Ȥ� = models.FloatField(blank=True, null=True)
    �����_�ۦ�R��_��X�Ѽ� = models.FloatField(db_column='�����(�ۦ�R��)��X�Ѽ�', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    �����_�ۦ�R��_�R��W�Ѽ� = models.FloatField(db_column='�����(�ۦ�R��)�R��W�Ѽ�', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    �����_�ۦ�R��_�R�i�Ѽ� = models.FloatField(db_column='�����(�ۦ�R��)�R�i�Ѽ�', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    �����_���I_��X�Ѽ� = models.FloatField(db_column='�����(���I)��X�Ѽ�', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    �����_���I_�R��W�Ѽ� = models.FloatField(db_column='�����(���I)�R��W�Ѽ�', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    �����_���I_�R�i�Ѽ� = models.FloatField(db_column='�����(���I)�R�i�Ѽ�', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ����ӽ�X�Ѽ� = models.FloatField(blank=True, null=True)
    ����ӶR��W�Ѽ� = models.FloatField(blank=True, null=True)
    ����ӶR�i�Ѽ� = models.FloatField(blank=True, null=True)
    �~��d�B��� = models.TextField(blank=True, null=True)
    �~��R�i�Ѽ� = models.FloatField(blank=True, null=True)
    �~���X�Ѽ� = models.FloatField(blank=True, null=True)
    �~��R��W�Ѽ� = models.FloatField(blank=True, null=True)
    ��H�d�B��� = models.TextField(blank=True, null=True)
    ��H�R�i�Ѽ� = models.FloatField(blank=True, null=True)
    ��H��X�Ѽ� = models.FloatField(blank=True, null=True)
    ��H�R��W�Ѽ� = models.FloatField(blank=True, null=True)
    �򥻨C�Ѭվl_��_field = models.FloatField(db_column='�򥻨C�Ѭվl�]���^', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �C�ѰѦҲb�� = models.FloatField(blank=True, null=True)
    �y�ʤ�v = models.FloatField(blank=True, null=True)
    �t�Ŧ��겣��v = models.FloatField(blank=True, null=True)
    �v�q���S�v = models.FloatField(blank=True, null=True)
    ��Q�v = models.FloatField(blank=True, null=True)
    ��~�Q�q�v = models.FloatField(blank=True, null=True)
    ��X�|��¯q�v = models.FloatField(blank=True, null=True)
    grow_s = models.FloatField(blank=True, null=True)
    grow_hy = models.FloatField(blank=True, null=True)
    grow_y = models.FloatField(blank=True, null=True)
    grow = models.FloatField(blank=True, null=True)
    ������X�l�q�`�B_wma = models.FloatField(db_column='������X�l�q�`�B.wma', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ������X�l�q�`�B_ma = models.FloatField(db_column='������X�l�q�`�B.ma', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    profitbility = models.FloatField(blank=True, null=True)
    investment = models.FloatField(blank=True, null=True)
    �ا���y������ = models.FloatField(blank=True, null=True)
    ���^�I�� = models.FloatField(blank=True, null=True)
    ���^�ʤ���_field = models.FloatField(db_column='���^�ʤ���(%)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �ا���y�����S���� = models.FloatField(blank=True, null=True)
    r���^�I�� = models.FloatField(blank=True, null=True)
    r���^�ʤ���_field = models.FloatField(db_column='r���^�ʤ���(%)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
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
        
        db_table = 'forr'


class Forr1(models.Model):
    index = models.IntegerField(blank=True, null=True)
    �~��� = models.DateField(blank=True, null=True)
    �Ҩ�N�� = models.TextField(blank=True, null=True)
    time = models.FloatField(blank=True, null=True)
    ����Ѽ� = models.FloatField(blank=True, null=True)
    ���浧�� = models.FloatField(blank=True, null=True)
    ������B = models.FloatField(blank=True, null=True)
    �}�L�� = models.FloatField(blank=True, null=True)
    �̰��� = models.FloatField(blank=True, null=True)
    �̧C�� = models.FloatField(blank=True, null=True)
    ���L�� = models.FloatField(blank=True, null=True)
    ���^_field = models.TextField(db_column='���^(+/-)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ���^���t = models.FloatField(blank=True, null=True)
    �̫ᴦ�ܶR�� = models.FloatField(blank=True, null=True)
    �̫ᴦ�ܶR�q = models.FloatField(blank=True, null=True)
    �̫ᴦ�ܽ�� = models.FloatField(blank=True, null=True)
    �̫ᴦ�ܽ�q = models.FloatField(blank=True, null=True)
    ���q�� = models.FloatField(blank=True, null=True)
    �ާQ�v_field = models.FloatField(db_column='�ާQ�v(%)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �ѻ��b�Ȥ� = models.FloatField(blank=True, null=True)
    �����_�ۦ�R��_��X�Ѽ� = models.FloatField(db_column='�����(�ۦ�R��)��X�Ѽ�', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    �����_�ۦ�R��_�R��W�Ѽ� = models.FloatField(db_column='�����(�ۦ�R��)�R��W�Ѽ�', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    �����_�ۦ�R��_�R�i�Ѽ� = models.FloatField(db_column='�����(�ۦ�R��)�R�i�Ѽ�', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    �����_���I_��X�Ѽ� = models.FloatField(db_column='�����(���I)��X�Ѽ�', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    �����_���I_�R��W�Ѽ� = models.FloatField(db_column='�����(���I)�R��W�Ѽ�', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    �����_���I_�R�i�Ѽ� = models.FloatField(db_column='�����(���I)�R�i�Ѽ�', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ����ӽ�X�Ѽ� = models.FloatField(blank=True, null=True)
    ����ӶR��W�Ѽ� = models.FloatField(blank=True, null=True)
    ����ӶR�i�Ѽ� = models.FloatField(blank=True, null=True)
    �~��d�B��� = models.TextField(blank=True, null=True)
    �~��R�i�Ѽ� = models.FloatField(blank=True, null=True)
    �~���X�Ѽ� = models.FloatField(blank=True, null=True)
    �~��R��W�Ѽ� = models.FloatField(blank=True, null=True)
    ��H�d�B��� = models.TextField(blank=True, null=True)
    ��H�R�i�Ѽ� = models.FloatField(blank=True, null=True)
    ��H��X�Ѽ� = models.FloatField(blank=True, null=True)
    ��H�R��W�Ѽ� = models.FloatField(blank=True, null=True)
    �򥻨C�Ѭվl_��_field = models.FloatField(db_column='�򥻨C�Ѭվl�]���^', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �C�ѰѦҲb�� = models.FloatField(blank=True, null=True)
    �y�ʤ�v = models.FloatField(blank=True, null=True)
    �t�Ŧ��겣��v = models.FloatField(blank=True, null=True)
    �v�q���S�v = models.FloatField(blank=True, null=True)
    ��Q�v = models.FloatField(blank=True, null=True)
    ��~�Q�q�v = models.FloatField(blank=True, null=True)
    ��X�|��¯q�v = models.FloatField(blank=True, null=True)
    grow_s = models.FloatField(blank=True, null=True)
    grow_hy = models.FloatField(blank=True, null=True)
    grow_y = models.FloatField(blank=True, null=True)
    grow = models.FloatField(blank=True, null=True)
    ������X�l�q�`�B_wma = models.FloatField(db_column='������X�l�q�`�B.wma', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ������X�l�q�`�B_ma = models.FloatField(db_column='������X�l�q�`�B.ma', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    profitbility = models.FloatField(blank=True, null=True)
    investment = models.FloatField(blank=True, null=True)
    �ا���y������ = models.FloatField(blank=True, null=True)
    ���^�I�� = models.FloatField(blank=True, null=True)
    ���^�ʤ���_field = models.FloatField(db_column='���^�ʤ���(%)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �ا���y�����S���� = models.FloatField(blank=True, null=True)
    r���^�I�� = models.FloatField(blank=True, null=True)
    r���^�ʤ���_field = models.FloatField(db_column='r���^�ʤ���(%)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
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
        
        db_table = 'forr1'


class PollsChoice(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField()
    question = models.ForeignKey('PollsQuestion', models.DO_NOTHING)

    class Meta:
        
        db_table = 'polls_choice'


class PollsQuestion(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

    class Meta:
        
        db_table = 'polls_question'

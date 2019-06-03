from __future__ import unicode_literals
from django.db import models

# Create your models here.
import phonenumbers
from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.conf import settings
from django.utils import timezone





class ERCTransaction(TimeStampedModel):
    """This one is used to capture the response from the API.
    It is expected that this table shall be insert only mostly
    """
    target = models.CharField(max_length=100)
    status = models.CharField(max_length=20,null=True, blank=True)
    phone_number = models.CharField(max_length=13,null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    product_id = models.CharField(max_length=100,null=True, blank=True)
    reference = models.CharField(max_length=255,null=True, blank=True)
    code = models.CharField(max_length=100,null=True, blank=True)
    paid_amount = models.IntegerField(null=True, blank=True)
    paid_currency = models.CharField(max_length=50,null=True, blank=True)
    topup_amount = models.IntegerField(null=True, blank=True)
    topup_currency = models.CharField(max_length=50,null=True, blank=True)
    time = models.DateTimeField(auto_now_add=True)
    country = models.CharField(max_length=100,null=True, blank=True)
    operator_name = models.CharField(max_length=100,null=True, blank=True)
    completed_in = models.CharField(max_length=100, null=True, blank=True)
    customer_reference = models.CharField(max_length=100, null=True, blank=True)
    api_transactionid = models.CharField(max_length=100, null=True, blank=True)
    pin_based = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return "Airtime Recharge For {} on {}".format(self.target,self.time)


# {"status":201,"message":"Operation Successful, Recharge created, Reference : 7b3c03c0-9280-11e8-9cc6-2db20206c01a","reference":"7b3c03c0-9280-11e8-9cc6-2db20206c01a","code":"RECHARGE_COMPLETE","paid_amount":97,"paid_currency":"NGN","topup_amount":100,"topup_currency":"NGN","target":"2347033288348","product_id":"MFIN-5-OR","time":"2018-07-28T16:08:36.540Z","country":"Nigeria","operator_name":"MTN","completed_in":982,"customer_reference":null,"api_transactionid":"80062496","pin_based":false}















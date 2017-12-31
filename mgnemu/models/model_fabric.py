# -*- coding: utf-8 -*-

"""
Model fabric is used to generate modles.

"""

from mgnemu.models.discount import Discount
from mgnemu.models.payment_type import PaymentType
from mgnemu.models.check_line import CheckLine
from mgnemu.models.check_comment import CheckComment
from mgnemu.models.sales_types import DISCOUNT
from mgnemu.models.sales_types import CHECK_LINE
from mgnemu.models.sales_types import PAYMENT
from mgnemu.models.sales_types import COMMENT_TYPE
from mgnemu.models.sales_types import PAYMENT


class ModelFabric(object):

    def __init__(self):
        pass

    def get_model(self, data):
        keys = list(data.keys())

        if DISCOUNT in keys:
            return Discount(data[DISCOUNT])
        elif CHECK_LINE in keys:
            return CheckLine(data[CHECK_LINE])
        elif PAYMENT in keys:
            return PaymentType(data[PAYMENT])
        elif COMMENT_TYPE in keys:
            return CheckComment(data[COMMENT_TYPE])
        else:
            return None

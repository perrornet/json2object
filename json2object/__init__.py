# -*- coding:utf-8 -*-
"""将json转换成类属性
usage:
   >>> import json2object
   >>> data = {"12":{"class": b"{\"66\": [1, 2, 3, {\"33\": \"88\"}]}"}}
   >>> data = json2obj.js2obj(data)
   >>> data
    <JsonToObject attr_12={'class': b'{"66": [1, 2, 3, {"33": "88"}]}'},>
    >>> data.attr_12
    <JsonToObject _class=b'{"66": [1, 2, 3, {"33": "88"}]}',>
    >>> data.attr_12._class.attr_66
    [1, 2, 3, <JsonToObject attr_33=88,>]
"""
from .api import JsonToObject as _JsonToObject


def js2obj(item):
    return _JsonToObject(item)

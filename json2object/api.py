# -*- coding:utf-8 -*-
import json
import keyword


class JsonToObject:
    """将json转换成类属性"""

    def __init__(self, item, decoding='utf-8', keyword_str='_', identifier="attr"):
        """
        :param item: 需要转换的json type: str, bytes, dict
        :param decoding: 如果是bytes类型那么其中如要转码的编码 type: str
        :param keyword_str: 如果json中有python的关键字, 会自动在加上这个前缀 type: str
        :param identifier: 如果json中有不能转换成python标识符, 会自动在加上这个前缀 type: str
        """
        
        self.__data = None
        JsonToObject.__decoding = decoding
        if isinstance(item, str):
            self.__data = json.loads(item)
        elif isinstance(item, bytes):
            self.__data = json.loads(item.decode(decoding))
        elif isinstance(item, dict):
            self.__data = item
        else:
            raise TypeError("只接受 dict或者str、bytes类型的json, 但是传入类型为{}".format(type(item)))
        self.__item = dict(self.__data)
        for key in dict(self.__data):
            if not key.isidentifier():
                self.__data["{}_{}".format(identifier, key)] = self.__data[key]
                self.__data.pop(key)
            elif keyword.iskeyword(key):
                self.__data["{}{}".format(keyword_str, key)] = self.__data[key]
                self.__data.pop(key)

    def to_dict(self):
        """返回未经过转义的dict"""
        return self.__item

    def __repr__(self):
        if not self.__data:
            return "<JsonToObject None>"
        s = ''
        count = 0
        for i in self.__data:
            if count == 3:
                break
            s += "{}={},".format(i, self.__data[i])
            count += 1
        return "<JsonToObject {}>".format(s)

    def __getattr__(self, name):
        return self._build(self.__data[name])

    @classmethod
    def _build(cls, obj):
        if isinstance(obj, str):
            try:
                obj = json.loads(obj)
            except json.JSONDecodeError:
                pass
        if isinstance(obj, bytes):
            try:
                obj = json.loads(obj.decode(cls.__decoding))
            except json.JSONDecodeError:
                pass
        if isinstance(obj, dict):
            return cls(obj)
        elif isinstance(obj, list):
            data = []
            for i in obj:
                if isinstance(i, (int, float)):
                    data.append(i)
                else:
                    data.append(cls(i))
            return data
        else:
            return obj

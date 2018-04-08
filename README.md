# json2object
完善《流畅的python》一书中的例子, 实现json访问类似js中的访问方式, 改进了输入str、bytes类型json也可以进行解析
使用:
```python
   >>> import json2object
   >>> data = {"12":{"class": b"{\"66\": [1, 2, 3, {\"33\": \"88\"}]}"}}
   >>> data = json2object.js2obj(data)
   >>> data
    <JsonToObject attr_12={'class': b'{"66": [1, 2, 3, {"33": "88"}]}'},>
   >>> data.attr_12
    <JsonToObject _class=b'{"66": [1, 2, 3, {"33": "88"}]}',>
   >>> data.attr_12._class.attr_66
    [1, 2, 3, <JsonToObject attr_33=88,>]
```
仅仅支持python 3
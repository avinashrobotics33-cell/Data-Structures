Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> s={10,20,30,10,20,30}
>>> type(s)
<class 'set'>
>>> s={10,20,30,10,20,30}
>>> s
{10, 20, 30}
>>> s1={30,10,20,10}
>>> s1
{10, 20, 30}
>>> s[0]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    s[0]
TypeError: 'set' object is not subscriptable
>>> s[1:]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    s[1:]
TypeError: 'set' object is not subscriptable
>>> s
{10, 20, 30}
>>> s.append('amx')
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    s.append('amx')
AttributeError: 'set' object has no attribute 'append'
>>> s.add('amx')
>>> s
{'amx', 10, 20, 30}
>>> s.remove(30)
>>> s
{'amx', 10, 20}
>>> s1={'narayan','amx','shiv','mark','alex'}
>>> s1
{'shiv', 'amx', 'mark', 'alex', 'narayan'}

Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> t=tuple
>>> t=()
>>> type(t)
<class 'tuple'>
>>> t=(10,20.30,40)
>>> t(0)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    t(0)
TypeError: 'tuple' object is not callable
>>> t1=t
>>> t1=(10,'amxwam',True,5.8,10)
>>> t1
(10, 'amxwam', True, 5.8, 10)
>>> t1(0)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    t1(0)
TypeError: 'tuple' object is not callable
>>> t1[0]
10
>>> t1[0:3]
(10, 'amxwam', True)
>>> t1[0:4]
(10, 'amxwam', True, 5.8)
>>> t1
(10, 'amxwam', True, 5.8, 10)
>>> t
(10, 20.3, 40)
>>> t[0]
10
>>> t[0]=100
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    t[0]=100
TypeError: 'tuple' object does not support item assignment

Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
r=range
r=range(10)
type(r)
<class 'range'>
r
range(0, 10)
range(10.0,10.5)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    range(10.0,10.5)
TypeError: 'float' object cannot be interpreted as an integer
>>> r
range(0, 10)
>>> for i in r: print(i)
... 
0
1
2
3
4
5
6
7
8
9
>>> r[0]
0
>>> r[4]
4
>>> r[0:3]
range(0, 3)
>>> range(100)
range(0, 100)
>>> range(10,30)
range(10, 30)
>>> range(50)
range(0, 50)
>>> range(10,50)
range(10, 50)
>>> range(10,50,5)
range(10, 50, 5)
>>> for i in range(10,50,5)
SyntaxError: expected ':'
>>> print(i)
9
>>> for i in range(10,50,10)                                                                                                                                                                  print(i)
SyntaxError: invalid syntax
>>> r
range(0, 10)
>>> range(10,50,5)
range(10, 50, 5)
>>> r
range(0, 10)
>>> for i in range(10,50,5)
SyntaxError: expected ':'
>>> for i in range(10:50:5)
SyntaxError: invalid syntax

Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
l = list
>>> l = [ ]
>>> type(l)
<class 'list'>
>>> print(type(l))
<class 'list'>
>>> l
[]
>>> l.append(10)
>>> l.append(20)
>>> l.append(30)
>>> l.append(10)
>>> l
[10, 20, 30, 10]
>>> l.append('amx')
>>> l.append('8.0')
>>> l.append(None)
>>> print(l)
[10, 20, 30, 10, 'amx', '8.0', None]
>>> l.remove('amx')
>>> l
[10, 20, 30, 10, '8.0', None]
>>> l[0]
10
>>> l[2]
30
>>> l[1]
20
>>> l[2:5]
[30, 10, '8.0']
>>> l[-1]
>>> 
>>> l[-1]
>>> l[-2]
'8.0'
>>> l[-1]
>>> 
>>> l[-3]
10
>>> l[1:4}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> l[1:4]
[20, 30, 10]
>>> l[0]
10
>>> l[0]=200
>>> l
[200, 20, 30, 10, '8.0', None]



l=list
l=[]
l
[]
print(type(l))
<class 'list'>
l=[10,20.3,40]
l
[10, 20.3, 40]
l[0:]
[10, 20.3, 40]
l[:-2]
[10]
l[:]
[10, 20.3, 40]
l[1:]
[20.3, 40]
l[:1]
[10]
l[:-2]
[10]












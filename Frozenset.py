Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> fs=frozenset
>>> fs
<class 'frozenset'>
>>> s2=frozenset
>>> s2
<class 'frozenset'>
>>> s2={10,20,30,40}
>>> s2
{40, 10, 20, 30}
>>> fs=frozenset(s2)
>>> fs
frozenset({40, 10, 20, 30})
>>> type(fs)
<class 'frozenset'>
>>> fs.add(50)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    fs.add(50)
AttributeError: 'frozenset' object has no attribute 'add'
>>> fs.remove(50)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    fs.remove(50)
AttributeError: 'frozenset' object has no attribute 'remove'

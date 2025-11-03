Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> d={100:'amx',200:'shiva',300:'narayan'}
>>> d
{100: 'amx', 200: 'shiva', 300: 'narayan'}
>>> type(d)
<class 'dict'>
>>> d1={}
>>> d1
{}
>>> print(type(d1))
<class 'dict'>
>>> d2={}
>>> d2
{}
>>> d2[100]='abc'
>>> d2[200]='shiv'
>>> d2
{100: 'abc', 200: 'shiv'}
>>> d2[100]='xxx'
>>> d2
{100: 'xxx', 200: 'shiv'}
>>> del d2[100]
>>> d2
{200: 'shiv'}

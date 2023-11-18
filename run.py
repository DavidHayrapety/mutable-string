from package import MutableString

string = MutableString('01234')


# __getitem__
print('__getitem__(item)')
print(f'{string[2:]=}', end='\n\n')

# __setitem__
print('__setitem__(item, value)')
string[0] = 'd'
print(f"string[0]='d'\n{string=}", end='\n\n')

# __str__
print('__str__()')
print(f'{string.__str__()=}', end='\n\n')

# __len__
print('__len__()')
print(f'{string.__len__()=}', end='\n\n')

# __iter__
print('__iter__()')
iter_item = string.__iter__()
for k, v in enumerate(iter_item):
    print(f'{k}=>{v}, ', end='')
print('\n\n')

# __repr__
print('__repr__()')
print(f'{string.__repr__()=}', end='\n\n')

# __add__
print('__add__(string)')
print('string+" asd d9v"')
string.__add__(" asd d9v")
print(f'{string=}', end='\n\n')

# title
print('title()')
print('string.title()')
string.title()
print(f'{string=}', end='\n\n')

# capitalize
print('capitalize()')
print('string.capitalize()')
string.capitalize()
print(f'{string=}', end='\n\n')

# center
print('center(width, fill=None)')
print('string.center(30, "|")')
string.center(30, "|")
print(f'{string=}', end='\n\n')

# upper
print('upper()')
print('string.upper()')
string.upper()
print(f'{string=}', end='\n\n')

# lower
print('lower()')
print('string.lower()')
string.lower()
print(f'{string=}', end='\n\n')

# startswith
print('startswith(string)')
print(f'{string.startswith("||||")=}', end='\n\n')

# endswith
print('endswith(string)')
print(f'{string.endswith("V")=}', end='\n\n')

# find
print('find(string, start=None, end=None)')
print(f'{string.find("|", start=9, end=None)=}', end='\n\n')

# rfind
print('rfind(s, start=None, end=None)')
print(f'{string.rfind("|", start=9, end=None)=}', end='\n\n')

# index
print('index(string, start=None, end=None)')
print(f'{string.index("|", start=None, end=9)=}', end='\n\n')

# rindex
print('rindex(string, start=None, end=None)')
print(f'{string.rindex(" ", start=None, end=15)=}', end='\n\n')

# split
print('split(symbol)')
print(f'{string.split(" ")=}', end='\n\n')

# replace
print('replace(old, new)')
print('string.replace("D", "000", 1)')
string.replace("D", "000", 1)
print(f'{string=}', end='\n\n')

# rreplace
print('rreplace(old, new)')
print('string.rreplace("D", "000")')
string.rreplace("D", "000")
print(f'{string=}', end='\n\n')

# isdigit
print('isdigit()')
print(f'{string.isdigit()=}', end='\n\n')

# isalpha
print('isalpha()')
print(f'{string.isalpha()=}', end='\n\n')

# isalnum
print('isalnum()')
print(f'{string.isalnum()=}', end='\n\n')

# islower
print('islower()')
print(f'{string.islower()=}', end='\n\n')

# isupper
print('isupper()')
print(f'{string.isupper()=}', end='\n\n')

# isspace
print('isspace()')
print(f'{string.isspace()=}', end='\n\n')

# istitle
print('istitle()')
print(f'{string.istitle()=}', end='\n\n')

# join
print('join(array)')
print(string.join(['*', '&']), end='\n\n')

# format
print('format(* args, ** kwargs)')
new_str = MutableString("My name is {fname}, I'm {age}")
print(f'{new_str=}')
new_str.format(fname="John", age=36)
print('new_str.format(fname = "John", age = 36)')
print(f'{new_str=}', end='\n\n')

# ord
print('ord(c)')
print(f'{ord(MutableString("r"))=}', end='\n\n')

# chr
print('chr(d)')
print(f'{chr(89)=}', end='\n\n')

# count
print('count(self, string, start=None, end=None)')
print(f'{string.count("|", start=None, end=None)=}', end='\n\n')

# lstrip
print('lstrip(c=None)')
print('string.lstrip()')
string.lstrip('|')
print(f'{string=}', end='\n\n')

# rstrip
print('rstrip(c=None)')
print('string.rstrip()')
string.rstrip('|')
print(f'{string=}', end='\n\n')

# strip
print('strip(c=None)')
print('string.strip()')
string.strip('0V9 ')
print(f'{string=}', end='\n\n')

# __delitem__
print('__delitem__(index)')
print('__delitem__(1)')
string.__delitem__(1)
print(f'{string=}', end='\n\n')

# __iadd__
print('__iadd__(string)')
print('string+"SP"')
string.__iadd__("SP")
print(f'{string=}', end='\n\n')

# __reversed__)
print('__reversed__()')
print('print(string.__reversed__())')
print(f'{string.__reversed__()=}', end='\n\n')

# append
print('append(value)')
print('string.append("#")')
string.append('#')
print(f'{string=}', end='\n\n')

# insert
print('insert(index, value)')
print('string.insert(2, " ")')
string.insert(2, " ")
print(f'{string=}', end='\n\n')

# pop
print('pop(index=-1)')
print('print(string.pop(3))')
print(string.pop(3))
print(f'{string=}', end='\n\n')

# remove
print('remove(value)')
print('string.remove("SS")')
string.remove('SS')
print(f'{string=}', end='\n\n')

# reverse
print('reverse()')
print('string.reverse()')
string.reverse()
print(f'{string=}', end='\n\n')

# clear
print('clear()')
print('string.clear()')
string.clear()
print('string=""')

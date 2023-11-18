from collections.abc import MutableSequence


class MutableString(MutableSequence, str):

    def __init__(self, s):
        if type(s) is not str:
            raise TypeError("Inapproopriate argument type")
        self.string = s

    # Magic methods

    def __getitem__(self, item):
        return self.string[item]

    def __setitem__(self, item, value):
        list_str = list(self.string)
        list_str[item] = value
        self.string = ''.join(list_str)

    def __str__(self):
        return self.string

    def __len__(self):
        return len(self.string)

    def __iter__(self):
        return iter(self.string)

    def __repr__(self):
        return self.string

    def __add__(self, string):
        self.string +=str(string)
        return self.string

    # Abstract methods

    def __delitem__(self,index):
        sample=list(self.string)
        del sample[index]
        self.string=''.join(sample)

    def __iadd__(self, string):
        self.string+=str(string)
        return self.string
    
    def __reversed__(self):
        return self.string[::-1]
    
    def append(self, value):
        self.string+=value
        return self.string

    def clear(self):
        self.string=''
        return None

    def insert(self, index, value):
        sample=list(self.string)
        sample.insert(index, value)
        self.string=''.join(sample)

    def pop(self, index=-1):
        sample=list(self.string)
        value=sample.pop(index)
        self.string=''.join(sample)
        return value

    def remove(self, value):
        self.string=self.string.replace(value,'', 1)
        return self.string
    
    def reverse(self):
        self.string=self.string[::-1]
        return self.string
    
    def count(self, value):
        main_len=len(self.string)
        val_len=len(value)
        diff_len=main_len-len(self.string.replace(value,''))
        count=diff_len//val_len
        return count

    # Methods

    def title(self):
        self.string = self.string.title()
        return self.string

    def capitalize(self):
        self.string = self.string.capitalize()
        return self.string

    def center(self, width, fill=None):
        self.string = self.string.center(width, fill)
        return self.string

    def upper(self):
        self.string = self.string.upper()
        return self.string

    def lower(self):
        self.string = self.string.upper()
        return self.string

    def startswith(self, string):
        return self.string.startswith(string)

    def endswith(self, string):
        return self.string.endswith(string)

    def find(self, string, start=None, end=None):
        return self.string.find(string, start, end)

    def rfind(self, string, start=None, end=None):
        return self.string.rfind(string, start, end)

    def index(self, string, start=None, end=None):
        return self.string.index(string, start, end)

    def rindex(self, string, start=None, end=None):
        return self.string.rindex(string, start, end)

    def split(self, symbol):
        return self.string.split(symbol)

    def replace(self, old, new, count=None):
        if count:
            self.string = self.string.replace(old, new, count)
            return self.string
        self.string = self.string.replace(old, new)
        return self.string

    def rreplace(self, old, new, count=None):
        if count:
            self.string = self.string[::-1].replace(old, new, count)[::-1]
            return self.string
        self.string = self.string[::-1].replace(old, new)[::-1]
        return self.string

    def isdigit(self):
        return self.string.isdigit()

    def isalpha(self):
        return self.string.isalpha()

    def isalnum(self):
        return self.string.isalnum()

    def islower(self):
        return self.string.islower()

    def isupper(self):
        return self.string.isupper()

    def isspace(self):
        return self.string.isspace()

    def istitle(self):
        return self.string.istitle()

    def join(self, array):
        return self.string.join(array)

    def format(self, * args, ** kwargs):
        self.string = self.string.format(*args, **kwargs)
        return self.string

    def count(self, string, start=None, end=None):
        return self.string.count(string, start, end)

    def strip(self, c=None):
        self.string = self.string.strip(c)
        return self.string

    def lstrip(self, c=None):
        self.string = self.string.lstrip(c)
        return self.string

    def rstrip(self, c=None):
        self.string = self.string.rstrip(c)
        return self.string

class MutableString:

    def __init__(self, s):
        if type(s) is not str:
            raise Exception
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
        self.string = self.string+string
        return self.string

    # Methods

    def title(self):
        self.string = self.string.title()
        return self.string

    def capitalize(self):
        self.string = self.string.capitalize()
        return self.string

    def center(self, width, fill=None):
        self.string = self.string.center(width, fill="")
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
        return self.string.find(string, start=None, end=None)

    def rfind(self, string, start=None, end=None):
        return self.string.rfind(string, start=None, end=None)

    def index(self, string, start=None, end=None):
        return self.string.index(self, string, start=None, end=None)

    def rindex(self, string, start=None, end=None):
        return self.string.rindex(self, string, start=None, end=None)

    def split(self, symbol):
        return self.string.split(symbol)

    def replace(self, old, new):
        self.string = self.string.replace(old, new)
        return self.string

    def rreplace(self, old, new):
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
        self.string=self.string.format(*args,**kwargs)
        return self.string
    
    def ord(self, c):
        return ord(c)
    
    def chr(self, d):
        return chr(d)

    def count(self, string, start=None, end=None):
        return self.string.count(string, start=None, end=None)
    
    def strip(self, c=None):
        self.string=self.string.strip(c)
        return self.string
    
    def lstrip(self, c=None):
        self.string=self.string.lstrip(c)
        return self.string
    
    def rstrip(self, c=None):
        self.string=self.string.rstrip(c)
        return self.string

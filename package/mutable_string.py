class MutableString :

    def __init__(self, s):
        self.string=s

    def __getitem__(self, item):
        # TODO: validation
        return self.string[item]
    
    def __setitem__(self, item, value):
        if type(item) is not int:    
            raise TypeError('Need to write an int for the index')
        list_str=list(self.string)
        list_str[item]=value
        self.string=''.join(list_str)

    def __str__(self):
        return self.string
    
    def __len__(self):
        return len(self.string)
    
    def __iter__(self):
        pass # TODO

    def __repr__(self):
        return self.string
    
    def __add__(self, string):
        # TODO: validation
        self.string=self.string+string

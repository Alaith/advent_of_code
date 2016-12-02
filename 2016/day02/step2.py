import sys

class Pad(object):

    _digits = [[None,None,1,None,None],
               [None,2,3,4,None],
               [5,6,7,8,9],
               [None,'A','B','C',None],
               [None,None,'D',None,None]]
    
    def __init__(self):
        self.column = 1
        self.row = 1
    
    def getlocation(self):
        return Pad._digits[self.row][self.column]

    def U(self):
        if self.row == 0:
            pass
        elif Pad._digits[self.row-1][self.column] is None:
            pass
        else:
            self.row -= 1

    def D(self):
        if self.row == 4:
            pass
        elif Pad._digits[self.row+1][self.column] is None:
            pass
        else:
            self.row += 1

    def L(self):
        if self.column == 0:
            pass
        elif Pad._digits[self.row][self.column-1] is None:
            pass
        else:
            self.column -= 1

    def R(self):
        if self.column == 4:
            pass
        elif Pad._digits[self.row][self.column+1] is None:
            pass
        else:
            self.column += 1

p = Pad()
a = ''
for line in sys.stdin.readlines():
    for c in line.strip():
        getattr(p,c)()
    a += str(p.getlocation())

print a

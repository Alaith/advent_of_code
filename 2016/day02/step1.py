import sys

class Pad(object):
    ''' 1 2 3
        4 5 6
        7 8 9'''

    _digits = [[1,2,3],[4,5,6],[7,8,9]]
    
    def __init__(self):
        self.column = 1
        self.row = 1
    
    def getlocation(self):
        return Pad._digits[self.row][self.column]

    def U(self):
        if self.row == 0:
            pass
        else:
            self.row -= 1
    
    def D(self):
        if self.row == 2:
            pass
        else:
            self.row += 1

    def L(self):
        if self.column == 0:
            pass
        else:
            self.column -= 1

    def R(self):
        if self.column == 2:
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

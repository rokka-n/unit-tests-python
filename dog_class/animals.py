import os

class animal(object):

    # initialize things during class creation
    def __init__(self, name):
        self.name  = name
        self.tricks = []

    # adds a trick
    def add_trick(self, trick):
        self.tricks.append(trick)

    # returns all tricks
    def print_tricks(self):
        print 'x = {}'.format(self.tricks)
        return self.tricks

    # checks if a dir is empty
    def dempty(self, dir):
        if os.path.exists(dir):
            if os.listdir(dir) == []:
                return True
            else:
                return False
        else:
            return False

e = animal('Wut')
print(e.name)

e.add_trick('Sit!')
print(e.dempty('/tmp1'))

var = e.print_tricks()

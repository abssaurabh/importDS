'''this program is not working correctly in this form so far; need to work on it'''

import math

class XORListNodes:
    def __init__(self):
        self.ptrdiff = None
        self.data = None

    def set_ptrdiff(self,prev,next):
        self.ptrdiff = math.trunc(prev) ^ math.trunc(next)

    def set_data(self,value):
        self.data = value

    def get_data(self):
        return self.data

    def get_ptrdiff(self):
        return self.ptrdiff

class XORList:
    def __init__(self):
        print "This list only allows adding elements at the beginning"
        self.head = None

    def add__elem_atbeg(self,newnode):
        if self.head is None:
            self.head = newnode
            self.head.set_ptrdiff(0,0)
        else:
            newnode.set_ptrdiff(0,self.head)
            self.head = newnode

    def show_list(self):
        temp = self.head
        elem_list = []
        while temp is not None:
            elem_list.append(str(temp.get_data()))
            prev = temp
            temp = temp.ptrdiff ^ math.trunc(prev)
        return '--'.join(elem_list)


    def edit_list(self):
        add = 1
        while add:
            value = int(raw_input("Enter node value: "))
            newnode = XORListNodes()
            newnode.set_data(value)
            self.add__elem_atbeg(newnode)
            print "List looks like\n:%s" %self.show_list()
            add = int(raw_input("Continue adding (1/0) ? "))

try:
    list = XORList()
    list.edit_list()

except(KeyboardInterrupt,SystemExit):
    print "Exiting as requested"
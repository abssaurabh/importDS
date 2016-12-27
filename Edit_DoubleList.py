from DoubleNode import *

'''be especially careful while deleting when node is the last one or the first
    also while adding keep track of prev and temp: need two pointers
    '''

class DoubleList:
    def __init__(self):
        print "Welcome and create your double list here \n1. add at beg\n2. add at end" \
              "\n3. add in between\n4. remove an element\n 5.remove element at position"
        self.head = None

    def add_elem_atbeg(self, newnode):
        if self.head is None:
            self.head = newnode
        else:
            newnode.setNext(self.head)
            self.head.set_prev(newnode)
            self.head = newnode


    def add_elem_atend(self, newnode):
        if self.head is None:
            self.head = newnode
        else:
            prev = temp = self.head
            while temp is not None:
                prev = temp
                temp = temp.getNext()
            prev.setNext(newnode)
            newnode.set_prev(prev)

    def remove_an_elem_val(self):
        if self.head is None:
            print "List is empty"
            return

        value = int(raw_input("Enter the element to be removed"))
        if self.head.data == value:
            self.head = self.head.getNext()
            # if there is only single element left in the list
            # self.head will become None and hence its prev should not be accessed
            if self.head:
                self.head.prev.set_prev(None)
        else:
            temp = self.head
            while temp is not None and temp.data != value:
                temp = temp.getNext()
            if temp is None:
                print "Element is not present in the list"
            else:
                temp.get_prev().setNext(temp.getNext())
                # check if the element to be deleted is not the last element
                # in which case it's next will be None
                if temp.getNext():
                    temp.getNext().set_prev(temp.get_prev())

    def remove_an_elem_pos(self):
        pos = int(raw_input("enter the position of node to be deleted"))
        if pos == 1:
            self.head = self.head.getNext()
            if self.head:
                self.head.set_prev(None)
        else:
            prev = temp = self.head
            while pos > 1 and temp is not None:
                prev = temp
                temp = temp.getNext()
                pos -= 1
            if temp is None:
                print "Node is position falls outside list length"
            else:
                prev.setNext(temp.getNext())
                if temp.getNext():
                    temp.getNext().set_prev(prev)

    def add_elem_inbetween(self, newnode):
        pos = int(raw_input("Enter the position you want the node to take: "))
        if self.head is None:
            print "List is empty"
        elif pos == 1:
            self.add_elem_atbeg(newnode)
        else:
            prev = temp = self.head
            while pos > 1 and temp is not None:
                prev = temp
                temp = temp.getNext()
                pos -= 1
            if pos > 1 or temp is None:
                print "List length does not contain that position"
            else:
                prev.setNext(newnode)
                newnode.setNext(temp)
                newnode.set_prev(prev)
                temp.set_prev(newnode)

    def show_list(self):
        if self.head is None:
            return "<Empty>"
        elements = []
        temp = self.head
        while temp is not None:
            elements.append(str(temp.data))
            temp = temp.getNext()
        return '<-->'.join(elements)

    def add_elements(self, choice):
        data = int(raw_input("Enter node data:"))
        new_node = DoubleNode()
        new_node.setData(data)

        if choice == 1:
            self.add_elem_atbeg(new_node)
        if choice == 2:
            self.add_elem_atend(new_node)
        if choice == 3:
            self.add_elem_inbetween(new_node)

    def remove_elements(self,choice):
        if choice == 4:
            self.remove_an_elem_val()
        else:
            self.remove_an_elem_pos()

    def edit_double_list(self):
        edit = 1
        while int(edit):
            choice = int(raw_input("Enter your edit choice: "))
            if choice in [1, 2, 3]:
                  self.add_elements(choice)
            elif choice in [4,5]:
                self.remove_elements(choice)

            print "List looks like:\n%s" %self.show_list()
            edit = raw_input("Keep on editing (1/0) ?  ")
try:
    dlist = DoubleList()
    dlist.edit_double_list()

except (KeyboardInterrupt, SystemExit):
    print '\nAs Requested: Exiting the program'

from Node import *


class List:
    def __init__(self):
        print 'Editing a linked list\n1.Add at beginning\n2.add at end\n' \
              '3.insert in between\n4. remove an element\n5. remove element at a position '
        self.head = None

    def remove_elem_withval(self,elem):

        if self.head.getData() == elem:
            self.head = self.head.getNext()

        else:
            temp = prev = self.head

            while temp is not None and temp.getData() != elem :
                prev = temp
                temp = temp.getNext()

            if temp is None:
                print 'Element is not found in the list'
            else:
                prev.setNext(temp.getNext())

    def remove_elem_atpos(self,pos):
        temp = prev = self.head
        if pos == 1:
            prev = prev.getNext()
            self.head = prev
        else:
            while temp is not None and pos > 1:
                prev = temp
                temp = temp.getNext()
                pos -= 1
            if temp is None:
                print 'Element position is out of range'
            else:
                prev.setNext(temp.getNext())


    def addatbeg_node(self, new_node):
        new_node.setNext(self.head)
        self.head = new_node

    def addatend_node(self, new_node):
        temp = self.head
        while temp.getNext() is not None:
            temp = temp.getNext()
        temp.setNext(new_node)

    def insert_node(self, new_node, pos):
        if pos == 1:
            print "Choose to add at beginning option"
            return
        temp = self.head
        prev = self.head
        while pos > 1 and temp is not None:
            prev = temp
            temp = temp.getNext()
            pos -= 1
        if temp is None:
            print 'Position is more than items in list; choose add at end if you want to add at the end'
        else:
            prev.setNext(new_node)
            new_node.setNext(temp)

    def add_node(self, new_node, choice):
        if choice == 1:
            self.addatbeg_node(new_node)
        elif choice == 2:
            self.addatend_node(new_node)
        elif choice == 3:
            pos = raw_input('Enter position of node:')
            self.insert_node(new_node, int(pos))

    def remove_elem(self,choice):
        if self.is_list_empty():
            print 'List is empty'
            return
        if choice == 4:
            data = raw_input("Enter node value :")
            self.remove_elem_withval(int(data))
        elif choice == 5:
            pos = raw_input('Enter node position: ')
            self.remove_elem_atpos(int(pos))

    def is_list_empty(self):
        return self.head is None

    def show_list(self):
        if self.is_list_empty():
            return '(Empty)'
        else:
            temp = self.head
            list_string = []
            while temp is not None:
                list_string.append(str(temp.getData()))
                temp = temp.getNext()
            return '-->'.join(list_string)


    def edit_list(self):
        edit = 1
        while edit:
            choice = int(raw_input("Choose node action ?"))
            if choice in [1,2,3]:
                new_node = Node()
                data = raw_input("Enter node value :")
                new_node.setData(int(data))
                self.add_node(new_node, choice)
            elif choice in [4,5]:
                self.remove_elem(choice)
            else:
                print 'Make a valid choice'

            print 'List looks like:\n %s' % self.show_list()
            edit = int(raw_input('Keep on editing (1/0)?'))
            if edit:
                continue
            else:
                print "You chose to stop the editing"
                return self

#uncomment to execute the program
'''try:
    new_list = List()
    self = new_list.edit_list()
except (KeyboardInterrupt, SystemExit):
    print '\nAs Requested: Exiting the program'
'''
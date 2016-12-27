# this class defines the properties and behaviours for the
# node of a singly linked list

class Node:
    def __init__(self):
        self.next = None
        self.data = None

    def getData(self):
        return self.data

    def setData(self,node_data):
        self.data = node_data

    def getNext(self):
        return self.next

    def setNext(self,next_node):
        self.next = next_node

    def hasNext(self):
        return self.next is not None


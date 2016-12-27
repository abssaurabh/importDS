import Node


# inherits the node class for a singly linked list
class DoubleNode(Node.Node):
    def __init__(self):
        Node.Node.__init__(self)
        self.prev = None

    def get_prev(self):
        return self.prev

    def set_prev(self,prev_node):
        self.prev = prev_node

    def has_prev(self):
        return self.prev is not None




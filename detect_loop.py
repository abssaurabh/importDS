# detect loop in the list

from Edit_List import *

def show_cyclic_loop(temp_list):
    #shows the elements in the list maximum upto 10 items at one time
    count = 10
    elements = []
    pos = temp_list.head
    while count:
        elements.append(str(pos.getData()))
        pos = pos.getNext()
        count -= 1
    print "-->".join(elements)


def detect_loop(temp_list):
    slow_ptr = fast_ptr = temp_list.head
    while slow_ptr and fast_ptr:
        slow_ptr = slow_ptr.getNext()
        if fast_ptr.getNext():
            fast_ptr = fast_ptr.getNext().getNext()
        if slow_ptr == fast_ptr:
            print "loop is detected. meeting point node has data: %d" %slow_ptr.getData()
            return
    if slow_ptr is None:
        print "List is all straight up. No loops detected."


def get_nth_node(temp_list,pos):
    node = temp_list.head
    while pos > 1:
        node = node.getNext()
        pos -= 1
    return node

def create_loop(temp_list):
    print "Enter the loop points: node2-->node1"
    pos1_count = int(raw_input('Enter the first node: '))
    pos2_count = int(raw_input('Enter the second node: '))
    pos1 = get_nth_node(temp_list,pos1_count)
    print "first node data: %d" %pos1.getData()
    pos2 = get_nth_node(temp_list, pos2_count)
    print "second node data: %d" %pos2.getData()
    print "setting the loop from node2 to node1"
    pos2.setNext(pos1)
    print "Showing the looped list in succession upto 10 items maximum"
    show_cyclic_loop(temp_list)
    detect_loop(temp_list)

try:
    new_list = List()
    new_list = new_list.edit_list()
    create_loop(new_list)
    #detect_loop(new_list)
except(SystemExit,KeyboardInterrupt):
    print 'Normal termination of the code'

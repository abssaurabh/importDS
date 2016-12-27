from Edit_List import *


def return_nth_node_end(self,pos):
    lag_ptr = self.head
    lead_ptr = self.head


    while pos>=1 and lead_ptr is not None:
        lead_ptr = lead_ptr.getNext()
        pos -= 1
    if lead_ptr is None and pos:
        print "List is not long enough for that position"
    else:
        while lead_ptr is not None:
            lead_ptr = lead_ptr.getNext()
            lag_ptr = lag_ptr.getNext()
        return lag_ptr.getData()
try:
    new_list = List()
    new_list = new_list.edit_list()
    while True:
        pos = int(raw_input("Enter the position you want: "))
        print "Oks this is the data we got for you %d" %return_nth_node_end(new_list,pos)
except:
    print "Exited the program !! "


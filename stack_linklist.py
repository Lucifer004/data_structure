class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class link_list:
    def __init__(self):
        self.start = None

    def pop_node(self):
        if self.start.next == None:
            print('\nThe link-list is empty!. Hence value of the HEAD is NULL')
            return None
        else:
            temp = self.start
            #if the element is not first node.
            prev = None#store the entry of previous node.
            while temp and temp.next!=None:
                prev = temp
                temp = temp.next
            
            if temp is None:
                print('\nelement not found in the list')
                return None
            prev.next = None
            temp = None

                
    def get_stack(self):
        if self.start.next==None:
            print('list is empty')
        else:
            temp = self.start
            while temp.next is not None:
                print(temp.data,end=' ')
                temp=temp.next
            print(temp.data,end=' ')
            
    def push_node(self,value):
        new_node = node(value)
        if self.start==None: #if there is no node present at start, hence start is the first node.
            self.start=new_node
        else:
            temp = self.start #here temp is refer to start, insted of travering start node we will travesrse temp.
            while temp.next!=None:
                temp = temp.next
            temp.next = new_node #inser new_node at the end of the link-list

if __name__ == "__main__":
    mylist = link_list()
    mylist.push_node(1)
    mylist.push_node(2)
    mylist.push_node(3)
    print('link-list STACK after insertion--' )
    mylist.get_stack()
    mylist.pop_node()# pop the node to be deleted-->
    print('\nlink-list STACK after POP--' )
    mylist.get_stack()
    
    
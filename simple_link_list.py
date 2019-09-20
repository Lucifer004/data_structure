#node[data,next]->node[data,next]->node[data,None](last element of the list)


class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class link_list:
    def __init__(self):
        self.start = None

    def delete_node(self,value):
        if self.start == None:
            print('The link-list is empty!')
        else:
            temp = self.start
            if temp and temp.data == value:#if the deletion element is first node, move the head to next_node and set the previous node to None.
                self.start = temp.next
                temp = None
            else:#if the element is not first node.
                prev = None
                while temp and temp.data!=value:
                    prev = temp
                    temp = temp.next
                
                if temp is None:
                    print('\nelement %s not found in the list'%(value))
                    return None
                prev.next = temp.next
                temp = None

                
    def view(self):
        if self.start==None:
            print('list is empty')
        else:
            temp = self.start
            while temp.next is not None:
                print(temp.data,end=' ')
                temp=temp.next
            print(temp.data,end=' ')
    def insert_node(self,value):
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
    mylist.insert_node(1)
    mylist.insert_node(2)
    mylist.insert_node(4)
    mylist.insert_node(5)
    print('link-list after insertion--' )
    mylist.view()
    mylist.delete_node(6)# enter the node to be deleted-->
    print('\nlink-list after deleting the node--')
    mylist.view()
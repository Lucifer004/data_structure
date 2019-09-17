#node[data,next]->node[data,next]->node[data,None](last element of the list)


class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class link_list:
    def __init__(self):
        self.start = None

    def delete_node(self):
        if self.start == None:
            print('The link-list is empty!')
        else:
            temp = self.start
            while temp.next!= None:
                temp = temp.next
            temp.next=None

    def view(self):
        if self.start==None:
            print('list is empty')
        else:
            temp = self.start
            while temp.next!=None:
                print(temp.data,end=' ')
                temp=temp.next
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
    mylist.view()
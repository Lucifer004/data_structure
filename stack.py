#Basics of Stack

#operations of the Stack - 
# create - creation of stack
# push - inserting the element into the stack. eg. push(element)
# pop - deletion/fetch the element.
# traverse - just displaying all the elements of the stack.
# isEmpty() - [optional]
# isFull - [optional]
# sizeOf - [optional] how many elements are present into the stack

class stack:
    
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)
        print('element %s inserted into stack.'%(element))
    
    def pop(self):
        top = len(self.stack)
        print('element %s got poped out'%(self.stack[top-1]))
        self.stack.remove(self.stack[top-1])
        return self.stack
        
    def is_empty(self):
        if self.stack == []:
            print('stack is empty')

    def is_full(self):
        if not self.stack == []:
            print('stack is Full')

    def get_stack(self):
        return self.stack

if __name__ == "__main__":
    
    stk = stack()
    stk.push(1)
    stk.push(2)
    stk.push(3)
    res = stk.get_stack()
    print(res)
    res = stk.pop()
    print(res)
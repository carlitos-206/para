#this is a singly link list in python script 


class SLNode:
    def __init__(self, val):
        self.value =val
        self.next = None


class SList:
    def __init__(self):
        self.head=None
    def add_to_front(self, val):
        new_node=SLNode(val)
        current_head =self.head
        new_node.next=current_head
        self.head=new_node
        return self

    def print_values(self):
        if self.head==None:
            print("List is Empty")
        runner =self.head
        while(runner !=None):
            the_list=[]
            the_list.append(runner.value)
            print(the_list)
            runner=runner.next
        return self
    
    def add_to_back(self, val):
        if self.head==None:
            self.add_to_front(val)
            return self
        new_node=SLNode(val)
        runner=self.head
        while(runner.next != None):
            runner=runner.next
        runner.next=new_node
        return self
    def remove_from_front(self):
        if self.head==None:
            print("List is empty")
            return self
        else:
            temp = self.head
            print(f"the first value of '{temp.value}'  is being removed")
            self.head= self.head.next
            temp = None
            return self
    def remove_from_back(self):
        if self.head==None:
            print(f"List is empty")
            return self
        elif self.head.next==None:
            print(f"list only contained 1 value of {self.head.value}")
            self.head=None
            return self
        else:
            runner=self.head
            while(runner !=None):
                runner=runner.next
            runner=None
            return self
    def remove_val(self, val):
        temp=self.head
        if self.head.value == val:
            self.head=self.head.next
            print(f"the value of {temp.value} has been deleted")
            temp=None
            return self
        runner=self.head
        while(temp !=None):
            if temp.value==val:
                break
            prev = temp
            temp = temp.next
        if(temp==None):
            return
        prev.next =temp.next
        print(f"the value of {temp.value} has been deleted")
        temp=None
        return self
test=SList()
test.add_to_front(7).add_to_back(34).add_to_front(25).add_to_back(21).add_to_front(15).print_values().remove_val(15).remove_val(34).print_values().remove_from_front().remove_from_back().print_values()

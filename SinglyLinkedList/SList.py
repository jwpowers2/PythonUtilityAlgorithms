# Singly Linked List
from SLNode import SLNode


class SList(object):

    def __init__(self):

        self.head = None
        self.tail = None

    def insert_after(self, preval, val):

        runner = self.head

        while(runner != None):

            if (runner.val == preval):

                temp = runner.next
                runner.next = SLNode(val)
                runner.next.next = temp
 
            runner = runner.next 

        self.tail = runner

    def insert_before(self, afterval, val):

        runner = self.head

        while(runner.next != None):

            if(runner.next.val == afterval):
                temp = runner.next
                runner.next = SLNode(val)
                runner.next.next = temp
            runner = runner.next 

        self.tail = runner

    def prepend(self,val):

        if(self.head):

            temp = self.head
            self.head = SLNode(val)
            self.head.next = temp
            return self

    def append(self,val):

        self.tail.next = SLNode(val)
        self.tail = self.tail.next
        return self

    def delete(self, val):

        runner = self.head

        while(runner.next != None):

            if(runner.next.val == val):
                if (runner.next.next): 
                    
                    runner.next = runner.next.next
                else:
                    runner.next = None
                    self.tail = runner
                    return
            runner = runner.next 

        self.tail = runner

    def print_all_vals(self):

        runner = self.head
        while(runner != None):
            print(runner.val)
            runner = runner.next 

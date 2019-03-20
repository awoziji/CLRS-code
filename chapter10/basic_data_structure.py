# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 09:30:26 2019

@author: win 10
"""

class Queue(object):
    tail = 0
    head = 0
    length = 0
    data = []
    
    def __init__(self,init_list):
        self.data = init_list
        self.tail = len(self.data)
        self.head = 0
        self.data = self.data * 2
        self.length = len(self.data)
    
    def __getitem__(self,n):
        return self.data[n]
    def __setitem__(self,n,value):
        self.data[n] = value

def enqueue(q,x):
    q[q.tail] = x
    if(q.tail == q.length):
        q.tail = 1
    else:
        q.tail = q.tail + 1

def dequeue(q):
    x = q[q.head]
    if q.head == q.length:
        q.head = 1
    else:
        q.head = q.head + 1
    return x        
    
        
aa = Queue([1,2,3,4,5,6,7,8,9])
print(aa[0])


class Node(object):
    key = ""
    prev = None
    next = None
    
    def __init__(self,key):
        self.key = key

class LinkedList(object):
    head = None
    
    def __init__(self,head):
        self.head = head
        
        
def list_search(l,k):
    x = l.head
    while x != None and x.key != k:
        x = x.next
    return x

def list_insert(l,x):
    x.next = l.head
    if l.head != None:
        l.head.prev = x
    l.head = x
    x.prev = None

def list_delete(l,x):
    if x.prev != None:
        x.prev.next = x.next
    else:
        l.head = x.next
    if x.next != None:
        x.next.prev = x.prev


head = Node("0");
l = LinkedList(head)
node_1 = Node("1")
node_2 = Node("2")
node_3 = Node("3")
list_insert(l,node_1)
list_insert(l,node_2)
list_insert(l,node_3)
result = list_search(l,"1")
list_delete(l,node_2)



#哨兵
class LinkedListNil(object):
    nil = Node("")
    
    def __init__(self):
        self.nil.next = self.nil
        self.nil.prev = self.nil


def list_search_nil(l,k):
    x = l.nil.next
    while x != l.nil and x.key != k:
        x = x.next
    return x

def list_insert_nil(l,x):
    x.next = l.nil.next
    l.nil.next.prev = x
    l.nil.next = x
    x.prev = l.nil

def list_delete_nil(l,x):
    x.prev.next = x.next
    x.next.prev = x.prev
        

l_nil = LinkedListNil()
node_0 = Node("0")
node_1 = Node("4")
node_2 = Node("5")
node_3 = Node("6")
node_4 = Node("7")
list_insert_nil(l_nil,node_0)
list_insert_nil(l_nil,node_1)
list_insert_nil(l_nil,node_2)
list_insert_nil(l_nil,node_3)
list_insert_nil(l_nil,node_4)
result = list_search_nil(l_nil,"4")
list_delete_nil(l_nil,node_2)

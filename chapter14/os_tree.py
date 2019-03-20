# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 19:34:38 2019

@author: steven
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 10:41:24 2019

@author: steven
"""

RED = 1
BLACK = 2


class OSRBTree:
    def __init__(self):
        self.nil = OSRBTreeNode(0,0)
        self.root = self.nil

class OSRBTreeNode:
    def __init__(self, x,size):
        self.key = x
        self.left = None
        self.right = None
        self.p = None
        self.color = BLACK
        self.size = size

def inorder_tree_walk(x):
        if x != None:
            inorder_tree_walk(x.left)
            print(x.key,"----")
            if x.key != 0:
                print ('key:', x.key, 'parent:', x.p.key, 'color:', x.color)
            inorder_tree_walk(x.right)

def tree_minimum(x):
    while x.left != T.nil:
        x = x.left
    return x


def os_select(x,i):
    if x.left != T.nil:
        r = x.left.size + 1
    else:
        r = 1    
    if i == r:
        return x
    elif i < r:
        return os_select(x.left,i)
    else:
        return os_select(x.right,i-r)

def os_rank(T,x):
    r = x.left.size + 1
    y = x
    while y != T.root:
        if y == y.p.right:
            r = r + y.p.left.size + 1
        y = y.p
    return r

    

def left_rotate(T,x):
    y = x.right
    x.right = y.left
    if y.left != T.nil:
        y.left.p = x
    y.p = x.p
    if x.p == T.nil:
        T.root = y
    elif x == x.p.left:
        x.p.left = y
    else:
        x.p.right = y
    y.left = x
    x.p = y
    y.size = x.size
    x.size = x.left.size + x.right.size + 1

def right_rotate(T,y):
    x = y.left
    y.left = x.right
    if x.right != T.nil:
        x.right.p = y
    x.p = y.p
    if y.p == T.nil:
        T.root = x
    elif y == y.p.left:
        y.p.left = x
    else:
        y.p.right = x
    x.right = y
    y.p = x
    x.size = y.size
    y.size = y.left.size + y.right.size + 1

def rb_insert(T,z):
    y = T.nil
    x = T.root
    while x != T.nil:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.p = y
    if y == T.nil:
        T.root = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z
    z.left = T.nil
    z.right = T.nil
    z.color = RED
    s = z.p
    if T.root == z:
        T.root.size = T.root.size + 1
    else:
        while s != T.root:
            s.size = s.size + 1
            s = s.p
        T.root.size = T.root.size + 1    
    rb_insert_fixup(T,z)
    

def rb_insert_fixup(T,z):
    while z.p.color == RED:
        if z.p == z.p.p.left:
            y = z.p.p.right
            if y.color == RED:
                z.p.color = BLACK
                y.color = BLACK
                z.p.p.color = RED
                z = z.p.p
            else:
                if z == z.p.right:
                    z = z.p
                    left_rotate(T,z)
                z.p.color = BLACK
                z.p.p.color = RED
                right_rotate(T,z.p.p)
        else:
            y = z.p.p.left
            if y.color == RED:
                z.p.color = BLACK
                y.color = BLACK
                z.p.p.color = RED
                z = z.p.p
            else:
                if z == z.p.left:
                    z = z.p
                    right_rotate(T,z)
                z.p.color = BLACK
                z.p.p.color = RED
                left_rotate(T,z.p.p)
    T.root.color = BLACK


def rb_transplant(T,u,v):
    if u.p == T.nil:
        T.root = v
    elif u == u.p.left:
        u.p.left = v
    else:
        u.p.right = v
    v.p = u.p    

def rb_delete(T,z):
    if z == T.root:
        T.root.size = T.root.size - 1
    else:
        s = z.p
        while s != T.root:
            s.size = s.size - 1
            s = s.p
        T.root.size = T.root.size - 1    
    
    y = z
    y.original_color = y.color
    if z.left == T.nil:
        x = z.right
        rb_transplant(T,z,z.right)
    elif z.right == T.nil:
        x = z.left
        rb_transplant(T,z,z.left)
    else:
        y = tree_minimum(z.right)
        y.original_color = y.color
        x = y.right
        if y.p == z:
           x.p = y
        else:
           print(y.key,type(y.right),"****") 
           rb_transplant(T,y,y.right)
           y.right = z.right
           y.right.p = y
        rb_transplant(T,z,y)
        y.left = z.left
        y.left.p = y
        y.color = z.color
    if y.original_color == BLACK:
        rb_delete_fixup(T,x)

def rb_delete_fixup(T,x):
    while x != T.root and x.color == BLACK:
        if x == x.p.left:
            w = x.p.right
            if w.color == RED:
                w.color = BLACK
                x.p.color = RED
                left_rotate(T,x.p)
                w = x.p.right
            if w.left.color == BLACK and w.right.color == BLACK:
                w.color = RED
                x = x.p
            else:
                if w.right.color == BLACK:
                    w.left.color = BLACK
                    w.color = RED
                    right_rotate(T,w)
                    w = x.p.right
                w.color = x.p.color
                x.p.color = BLACK
                w.right.color = BLACK
                left_rotate(T,x.p)
                x = T.root
        else:
            w = x.p.left
            if w.color == RED:
                w.color = BLACK
                x.p.color = RED
                right_rotate(T,x.p)
                w = x.p.left
            if w.right.color == BLACK and w.left.color == BLACK:
                w.color = RED
                x = x.p
            else:
                if w.left.color == BLACK:
                    w.right.color = BLACK
                    w.color = RED
                    left_rotate(T,w)
                    w = x.p.left
                w.color = x.p.color
                x.p.color = BLACK
                w.left.color = BLACK
                right_rotate(T,x.p)
                x = T.root
    x.color = BLACK


nodes = [11,2,14,1,7,15,5,8,4]
T = OSRBTree()
for node in nodes:
    rb_insert(T,OSRBTreeNode(node,1))
            
   


inorder_tree_walk(T.root)

print("#########################")
rb_delete(T,T.root)
print ('after delete')
inorder_tree_walk(T.root)

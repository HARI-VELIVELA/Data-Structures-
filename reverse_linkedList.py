#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def print_helper(self,node,name):
    if node is None:
        print(name+ ": None")
    else:
        print(name + ":" + node.data)
        
def reverse_iterative:
    previousNode = None
    currentNode = self.head
    while currentNode:
        nxt = currentNode.next
        currentNode.next = previousNode
        self.print_helper(previousNode,"PREV")
        self.print_helper(currentNode,"CURRENT")
        self.print_helper(nxt,"NEXT")
        print("\n")
        previousNode = currentNode
        currentNode = nxt
    self.head = previousNode

            
        


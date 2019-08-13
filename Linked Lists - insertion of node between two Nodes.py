#!/usr/bin/env python
# coding: utf-8

# In[17]:


# create nodes
# create linked lists
# add nodes to linked lists
# print the linked lists


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode
            
    def printList(self):
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            
            print(currentNode.data)
            currentNode = currentNode.next
            
    def atBigin(self,newData):
        newNode  = newData
        newNode.next = self.head
        self.head = newNode
            
    def betweenNodes(self,newData,position):
        currentNode = self.head
        currentPosition = 0
        while True:
            if currentPosition == position:
                previousNode.next = newData
                newData.next = currentNode
                break
            
            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition += 1
        newNode = newData
        

firstNode = Node("seed")
LL = LinkedList()
LL.insert(firstNode)
secondNode = Node("sprout")
LL.insert(secondNode)
thirdNode = Node("plnat")
LL.insert(thirdNode)
fourthNode = Node("tree")
LL.insert(fourthNode)
zeroNode = Node("soil & water")
LL.atBigin(zeroNode)
threeFourNode = Node("flowers")
LL.betweenNodes(threeFourNode,4)
fourFiveNode = Node("Fruits")
LL.betweenNodes(fourFiveNode,5)



LL.printList()


# In[ ]:





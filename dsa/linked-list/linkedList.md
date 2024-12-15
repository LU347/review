# Singly Linked List Implementation

First we need to create a class for the ListNode class, which would contain a value and a pointer to the next node. 

```
class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node
```

Example:

```
ListNode() #Creates a node with a default value of 0 and a pointer to None
```

Now, we need to create a LinkedList class. A LinkedList consists of a head, which dictates the start of the list and the end of the list is called a tail.

```
class LinkedList:
    self.head = ListNode()
    self.tail = self.head
```

When the linked list is initialized, it will have a dummy node with a value of 0 and a pointer to None. The head and tail will both be None/Null

The function below returns the value at the ith node (0-indexed).
```
#in LinkedList class
    def get(self, index: int) -> int:  #will return the value of the ith node
        cur = self.head  #starts at the head of the linked list
        i = 0
        while cur:           #will keep iterating until it is None
            if i == index:
                return cur.val  #returns the value at ith index
            i += 1
            cur = cur.next
        return -1               #returns -1 if the value was not found
```

This function is supposed to insert a node at the head of the list but NeetCode's implementation shows that it points the head to the new node, instead of replacing the head with the new node. Maybe i'm interpreting it wrong but I'm pretty sure it should make the newly created node the head of the list and have it point to the old head

```
    #NeetCode's implementation
    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)       #creates a new node
        new_node.next = self.head.next    #points to the node after the head
        self.head.next = new_node         #the head points to the new node

        if not new_node.next:  # If list was empty before insertion
            self.tail = new_node

        #My implementation
        new_node = ListNode(val)     #the new node is created
        new_node.next = self.head    #points to the current head
        self.head = new_node         #new_node becomes the new head

        if self.tail is None:        #if the list was previously empty
            self.tail = new_node
```


```
    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)    #creates a new node
        self.tail.next = new_node   #update the tail's pointer to the new node
        self.tail = new_node        #the new node becomes the new tail
```

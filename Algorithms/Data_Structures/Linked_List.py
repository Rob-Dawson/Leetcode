class SinglyLinked:
    def __init__(self, val, next=None):
        self.next = next
        self.val = val

    def __str__(self):
        return str(self.val)
    

class DoublyNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
    
    def __str__(self):
        return  str(self.val)




def showAll(head):
    current = head
    while current:
        print(current)
        current = current.next

def display(head):
    current = head
    elements = []
    while current:
        elements.append(str(current.val))
        current = current.next
    print("-->".join(elements))

def search(head, val):
    current = head
    while current:
        if val == current.val:
            return f"Found {current.val}"
        current = current.next
    return False


def insert_at_beginning_DL(head, tail, val):
    tail = None
    new_node = DoublyNode(val, next=head)
    head.prev=new_node
    return new_node, tail

def insert_at_end_DL(head, tail, val):
    new_node = DoublyNode(val, prev=tail)
    tail.next = new_node
    return head, new_node

def display_DL(head):
    current = head
    elements = []
    while current:
        elements.append(str(current.val))
        current = current.next
    print(" <-> ".join(elements))

def main():
    Head = SinglyLinked(1)
    A = SinglyLinked(2)
    B = SinglyLinked(3)
    C = SinglyLinked(4)

    Head.next = A
    A.next = B
    B.next = C 


    showAll(Head)
    display(Head)
    result = search(Head, 0)
    print(result)
    result = search(Head, 3)
    print(result)

    ##Doubly Linked List
    head = tail = DoublyNode(10)

    head, tail = insert_at_beginning_DL(head=head, tail=tail, val=20)
    display_DL(head)

if __name__ == "__main__":
    main()
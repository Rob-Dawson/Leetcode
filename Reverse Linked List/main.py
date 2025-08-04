class LinkedList():
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node

def build_linked_list(nodes):
    head = LinkedList(nodes[0])
    current = head
    for val in nodes[1:]:
        current.next = LinkedList(val)
        current = current.next
    return head

def show_all(nodes):
    current = nodes
    while current:
        print(current.val)
        current = current.next

def reverse(nodes):
    prev = None
    temp = None
    current = nodes
    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp
    return prev




def main():
    head = [1,2,3,4,5]
    nodes = build_linked_list(head)
    show_all(nodes)
    nodes = reverse(nodes)
    show_all(nodes)


if __name__ == "__main__":
    main()

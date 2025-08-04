class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_linked_list(list):
    head = ListNode(list[0])
    current = head
    for val in list[1:]:
        current.next = ListNode(val)
        current = current.next
    return head
        

def deleteDuplicates(head):
    current = head
    while current and current.next:
        if current.next.val == current.val:
            current.next = current.next.next
        else:
            current = current.next
    return head

def showAll(head):
    current = head
    while current:
        print(current.val)
        current = current.next

def main():
    values = [1,1,2]
    head = build_linked_list(values)
    values = deleteDuplicates(head)
    showAll(values)

if __name__ == "__main__":
    main()
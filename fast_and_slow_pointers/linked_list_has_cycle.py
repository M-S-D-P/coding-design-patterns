class Node:
    def __init__(self, val):
        # Initialize the node with a value and a reference to the next node
        self.val = val
        self.next = None

def has_cycle(head):
    # If the list is empty or has only one element, return None
    if head is None or head.next is None:
        return None

    # Initialize two pointers, slow and fast
    slow = head
    fast = head

    # Traverse the list with two pointers
    # 'slow' moves one step at a time, 'fast' moves two steps at a time
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    # When 'fast' reaches the end, 'slow' will be at the middle
        if slow == fast:
            return True
        else:
            return False


# Create the linked list: 1 -> 2 -> 3 -> 4 -> 5
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next = head.next

# Find the middle node
has_cycle = has_cycle(head)

# Print the value of the middle node if it exists
if has_cycle:
    print(f"No cycle detected")
else:
    print("cycle detected")

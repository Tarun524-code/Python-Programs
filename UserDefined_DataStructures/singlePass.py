import LinkedList

l = LinkedList.LinkedList()
values = list(map(int, input().split()))

for v in values:
    l.insert_end(v)

l.traverse()

slow = l.head
fast = l.head.next
while fast is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next

print("Middle node value:", slow.data if slow else None)
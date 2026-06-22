import LinkedList

l = LinkedList.LinkedList()
values = list(map(int, input().split()))

for v in values:
    l.insert_end(v)
l.traverse()

prev = None
curr = l.head
while curr != None:
    n = curr.next
    curr.next = prev
    prev = curr
    curr = n 
l.head = prev

print('Reversed list:')
if l.head is None:
    print('None')
else:
    l.traverse
import LinkedList

l = LinkedList.LinkedList()
values = list(map(int, input().split()))

for v in values:
    l.insert_end(v)
l.traverse()
c = 0
curr = l.head
while curr:
    c += 1
    curr = curr.next

print('Number of nodes:', c)



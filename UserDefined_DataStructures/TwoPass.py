import LinkedList

l = LinkedList.LinkedList()
values = list(map(int, input().split()))

for v in values:
    l.insert_end(v)
l.traverse()

c = l.head
count  = 0
while c is not None:
    count = count + 1
    c = c.next
c = l.head
for _ in range(0,count//2):
    c = c.next
    


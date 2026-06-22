import LinkedList

l = LinkedList.LinkedList()
values = list(map(int, input().split()))

for v in values:
    l.insert_end(v)

l.traverse()

c = l.head
count = 0
while c is not None:
    count += 1
    c = c.next

c = l.head

for _ in range(count // 2):
    c = c.next

print("Middle node value:", c.data if c else None)
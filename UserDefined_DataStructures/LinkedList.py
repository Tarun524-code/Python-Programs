class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_head(self, x):
        t = Node(x)
        t.next = self.head
        self.head = t

    def insert_end(self, x):
        t = Node(x)
        if not self.head:
            self.head = t
            return self.head
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = t

    def insert_pos(self, x, pos):
        if pos < 0:
            return self.head
        t = Node(x)
        if pos == 0:
            t.next = self.head
            self.head = t
            return self.head
        curr = self.head
        while curr is not None and pos > 1:
            curr = curr.next
            pos -= 1
        if curr is None:
            return self.head
        t.next = curr.next
        curr.next = t

    def delete_head(self):
        if self.head is None:
            return self.head
        self.head = self.head.next

    def delete_end(self):
        if self.head is None:
            return self.head
        if self.head.next is None:
            self.head = None
            return self.head
        curr = self.head
        while curr.next.next:
            curr = curr.next
        curr.next = None

    def delete_pos(self, pos):
        if self.head is None or pos < 0:
            return self.head 
        if pos == 0:
            self.head = self.head.next
            return self.head 
        curr = self.head
        while curr is not None and pos > 1:
            curr = curr.next
            pos -= 1
        if curr is None or curr.next is None:
            return self.head 
        curr.next = curr.next.next
        return self.head 
    
    def traverse(self):
        t = self.head
        while t:
            print(t.data, end=" -> ")
            t = t.next
        print("None")

    def search(self, x):
        t = self.head
        while t:
            if t.data == x:
                return True
            t = t.next
        return False

    def search_recursive(self, root, x):
        if root is None:
            return False
        if root.data == x:
            return  True
        return  self.search_recursive(root.next, x)
if __name__ == "__main__":
    ll = LinkedList()

    while True:
        print("\nMenu:")
        print("1. Insert at head")
        print("2. Insert at end")
        print("3. Insert at position")
        print("4. Delete head")
        print("5. Delete end")
        print("6. Delete at position")
        print("7. Traverse")
        print("8. Search (iterative)")
        print("9. Search (recursive)")
        print("10. Exit")

        choice = input("Enter choice: ").strip()

        if choice == '1':
            x = int(input("Enter value: "))
            ll.insert_head(x)
        elif choice == '2':
            x = int(input("Enter value: "))
            ll.insert_end(x)
        elif choice == '3':
            x = int(input("Enter value: "))
            pos = int(input("Enter position: "))
            ll.insert_pos(x, pos)
        elif choice == '4':
            ll.delete_head()
        elif choice == '5':
            ll.delete_end()
        elif choice == '6':
            pos = int(input("Enter position: "))
            ll.delete_pos(pos)
        elif choice == '7':
            ll.traverse()
        elif choice == '8':
            x = int(input("Enter value to search: "))
            print("Found" if ll.search(x) else "Not Found")
        elif choice == '9':
            x = int(input("Enter value to search: "))
            print("Found" if ll.search_recursive(ll.head, x) else "Not Found")
        elif choice == '10':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.")

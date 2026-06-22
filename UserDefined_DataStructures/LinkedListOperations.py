import LinkedList
ll = LinkedList.LinkedList()

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

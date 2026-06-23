import BST

bst = BST.BST()
while True:
    print("\n--- Binary Search Tree Menu ---")
    print("1. Insert")
    print("2. Delete")
    print("3. InOrder Traversal")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        val = int(input("Enter value to insert: "))
        bst.root = bst.insert(bst.root, val)

    elif choice == 2:
        val = int(input("Enter value to delete: "))
        bst.root = bst.delete(bst.root, val)

    elif choice == 3:
        print("InOrder Traversal:", end=" ")
        bst.inOrder(bst.root)
        print()

    elif choice == 4:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")

def count(fname):
    f = None
    try:
        f = open(fname,"r")
        data = f.readlines()
        f.close()
        return len(data)
    except FileNotFoundError:
        print("File doesn't Exist ")
    finally:
        print("File Closed.......")

fname = input()
ans = count(fname)
print("No.of Lines: ",ans)
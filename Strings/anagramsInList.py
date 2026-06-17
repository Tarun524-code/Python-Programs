# method-1 using sorting

from collections import defaultdict

def group_by_sorting(w):
    groups = {}
    for word in w:
        key = "".join(sorted(word.lower()))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return list(groups.values())



if __name__ == "__main__":
    s= input()
    w = s.split()
    res = group_by_sorting(w)
    print(res)

from concurrent.futures import ThreadPoolExecutor
import time

def multiply(x):
    return 2*x

l=list(map(int,input().split()))

with ThreadPoolExecutor(max_workers=4) as e:
    results = e.map(multiply, l)

for result in results:
    print(result)

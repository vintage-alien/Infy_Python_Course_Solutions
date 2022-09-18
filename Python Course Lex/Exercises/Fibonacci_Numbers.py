# Write a Python function generate_fibanacci(n) to return a list of first n Fibonacci numbers.
import time

begin = time.time()
def generate_fibonacci(n):
    i, j = 0, 1
    print(i, j, end=" ")

    for m in range(n-2):
        k=i+j
        print(k, end=" ")
        i = j
        j = k


generate_fibonacci(100)

end = time.time()
print(f"\nExcecution time : {end - begin}")
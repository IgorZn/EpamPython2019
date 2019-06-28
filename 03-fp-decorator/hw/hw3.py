import time
count = 0
def collatz_steps(n, count=count):
    if n == 1:
        global a
        a = count
        return count
    elif n % 2 == 0:
        collatz_steps((n//2), count+1)
    else:
        collatz_steps((n * 3) + 1, count+1)
    return a

def collatz_steps_inline(n, c=0):
    return collatz_steps_inline(3 * n + 1 if n % 2 else int(n / 2), c=c + 1) if n != 1 else c

start = time.time()
assert collatz_steps(16) == 4
assert collatz_steps(12) == 9
assert collatz_steps(1000000) == 152
end = time.time()
print(end - start)

start = time.time()
assert collatz_steps_inline(16) == 4
assert collatz_steps_inline(12) == 9
assert collatz_steps_inline(1000000) == 152
end = time.time()
print(end - start)
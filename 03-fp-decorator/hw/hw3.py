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



assert collatz_steps(16) == 4
assert collatz_steps(12) == 9
assert collatz_steps(1000000) == 152

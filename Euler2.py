__author__ = 'Eric'
memo = {0:0, 1:1}
x=0
n=0
def fib(n):
    if not n in memo:
        memo[n]= fib(n-1) +fib(n-2)
    return memo[n]
while fib(n) < 4000000:
    if fib(n) % 2 == 0:
        x = x + fib(n)
    n = n + 1
print(x)
# Write a program to generate the first 10 numbers of the Fibonacci series.
a, b = 0, 1
fibonacci_series = []
for _ in range(10):
    fibonacci_series.append(a)
    a, b = b, a + b
print("The first 10 numbers of the Fibonacci series are:", fibonacci_series)
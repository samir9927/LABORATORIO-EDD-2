def fibonacci(n):
    fib_numbers = [0, 1]
    print(fib_numbers[-2])
    while len(fib_numbers) < n:
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
    return fib_numbers


primeros_10_fibonacci = fibonacci(10)

print("Los primeros 10 números de la serie Fibonacci son:")
print(primeros_10_fibonacci)
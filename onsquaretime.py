def onsquaretime(n):
    iterations = 0
    for i in range(0, n):
        for j in range(0, n):
            print("*", end="")
            iterations += 1
    print(" When n is", n, "the number of iterations is", iterations, "\n")
onsquaretime(5)
onsquaretime(4)
onsquaretime(3)
print("\nWith every n the time taken equals to n^2.")
print("O(n^2)")
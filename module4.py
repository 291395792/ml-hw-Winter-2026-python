# Read N
N = int(input("Enter a positive integer N: "))

numbers = []

# Read N numbers one by one
for i in range(N):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

# Read X
X = int(input("Enter X: "))

# Check if X is in the list
if X in numbers:
    print(numbers.index(X) + 1)  # index from 1 to N
else:
    print(-1)
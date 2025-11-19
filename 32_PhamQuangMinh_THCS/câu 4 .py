def la_nguyen_to(x):
    if x < 2:
        return False
  
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1

    return True

n = int(input("Nhập n: "))

print("Các số nguyên tố nhỏ hơn", n, "là:")

for i in range(2, n):
    if la_nguyen_to(i):
        print(i, end=" ")
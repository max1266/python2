#задача с монетками
n = int(input())
count = 0
for i in range(n):
    v = int(input()) ##вводим числа 0 если решка 1 если орел
    if v == 1:
        count+= 1
print(count if count<n/2 else n-count)

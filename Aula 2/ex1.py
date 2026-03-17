n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
x = [n1, n2, n3, n4]
par = 0
impar = 0
for i in x:
    if i % 2 == 0:
        par += i
    if i % 2 == 1:
        impar += i
print(par)
print(impar)
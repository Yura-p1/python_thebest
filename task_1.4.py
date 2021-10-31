number = int(input("Давай найдем в числе самую большую цифру, введи число: "))
r = -1
while number > 0:
    d = number % 10
    number //= 10
    if d > r:
        r = d
print(r)
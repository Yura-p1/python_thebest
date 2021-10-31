# version 1
number = int(input("Введи число от 1 до 9: "))
number_double = number * 11
number_triple = number * 111
print (number + number_double + number_triple)

# version 2
number = input("Введи число от 1 до 9: ")
number_double = number + number
number_triple = number_double + number
total = int(number) + int(number_double) + int(number_triple)
print(total)
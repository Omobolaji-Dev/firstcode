from math import *
print(pow(4, 5))
print(round(3.6))
print(sqrt(4))
print(floor(3.2))
print(ceil(2.2))


age = 13
print(age < 7)
print(age == 5)
print(age > 5)
print(age != 5)
print(age >= 5)
print(age <= 9)

print("Richard" > "peniel")
print("a" > "b")

a = 9 > 3
print(int(a))
richard = 18
peniel = 16
if richard > peniel:
    print("Richard is older")
else:
    print("Peniel is older")

prime_number = ["taketake", "tic a toe", "Elizabeth"]
classmates = ["richard", "peniel", "francis", "Agbadaola"]
classmates.extend(prime_number)
print(classmates)
classmates.insert(1, "olatoye")
print(classmates)
classmates.remove("taketake")
print(classmates)
classmates.sort()
print(classmates)
age = 10
name = "Richard"

def login(name):
    print('welcome'+ name)


class Richard:
    pass


login('Richard')

def login(name,age):
    print('welcome'+ name + "you are" + str(age) + "years old")

login('Richard',13)

def cube(num):
    return num*num*num
    print(cube(4))
def max_size(num1, num2, num3):
    if num1>=num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
num1= input(float('Enter your first number'))
op= input('Enter operator')
num2 = input(float('Enter your second number'))
if op =="+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)





cube(3)

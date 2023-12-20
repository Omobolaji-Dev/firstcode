'''namee= "richard"
age = 14
careerPath ="Student"
is_hardworking= True
#input statement
your_age = input("How old are you: ")
birthyear = 2023 - int(your_age)
print(birthyear)

#usingfloats in input statement

numA = float(input("firstnumber: "))
numB = float(input("secondnumber: "))
result =numA -numB
print("The result of the question is " + str(result))
#if statement
if result > 15:
    print("you passed")
else:
    print("you failed, please try again")'''
#Operation with string
interest = "I enjoy learning programming languages"
print(interest.upper())
print(interest.lower())
print(interest.find("p"))
print(interest.replace("enjoy","dislike"))

#Arithmetic

x = 5
y = 6
print(x+y)
print(y%x)
print(2**3)
#comparison and logical operation
x = 5 >2
print(x)

speedLimit = 25
if speedLimit > 70:
    print("you are overspeeding")
elif speedLimit < 40:
    print("You are causing ostruction")
else:
    print("Weldone, You are within the speedlimit")

#EVENT LOOP
num = 1
'''while num <= 10:
    sum += num
    num+=1
    print("The sum of numbers from 1 to 10 is",num)
'''
count = 1
for count in range(1,11):
    print(count)
    count += 1
# LIST
techList = ["apple","microsoft","google","samsung"]
print(techList[0:2])
techList[0]= "panasonic"
print(techList)
print(len(techList))
techList.clear()

#DICTIONARY
shoe= {"nike":20,"adidas":50,"Jordans":30}
shoe["nike"]=45
print(shoe)
#FUNCTIONS
def addList():
    print("I am chosen")
addList()

def path(a,b):
    return a*b
print(path(30,25))

#EXCEPTION
'''item = int(input("type the number: "))
print(item)
except ValueError:
print("your value is not an integer")'''

#OBJECT ORIENTED PROGRAMMING OOP
#CLASS, OBJECT AND METHODS
class animal:
    def __init__(self,breed,color):
        self.breed = breed
        self.color = color
    def run(self):
        print("running")
    def eat(self):
        print("eating")

dog = animal('husky',"white")
print(dog.breed)
print(dog.color)

class person:
    def __init__(self,name,personality):
        self.name=name
        self.personality=personality
    def greet(self):
        print("My name is ", self.name)
person1 = person("Alice","introvert")
print(person1.greet())

class Animal:
    def __init__(self,name):
        self.name =name
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        return f"{self.name} says woof"
class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow"
dog=Dog("husky")
cat=Cat("ladyJay")
print(dog.speak())
print(cat.speak())

#ACCESSING SUPERCLASS
class Bird:
    def __int__(self,name):
        self.name=name
    def speak(self):
        return f"{self.name} sings a song"
class Parrot(Bird):
    def speak(self):
        return f"{self.name} mimics human speech"
    def bird_song(self):
        return super().speak()
parrot = Parrot()
print(parrot.speak())
print(parrot.bird_song())
print("Hello World")

print("10" + "10")
print(10 + 10)

print(type(10))
print(type("10"))

x = 100


x = "120"
x = int(x)

print(x / 4)

print(12 % 5)

print(2 ** 4)
print(13 // 3)

y = 10
y += 10
print(y)

print(x == y)
print(x >= y)
try:
    x = input("enter number one ") 
    y = input("enter number two ")

    x = int(x)
    y = int(y)

    print(x + y)

    if x < y:
        print("y is bigger than x")

    elif x > y:
        print("x is bigger than y")

    else:
        print("y is equal to x")

except:
    print("something went wrong!")
i = 0


while i < 10:
    i += 1
    if i == 5:
        continue
    if i == 8:
        break
    print (i)

mylist = [1, 2, 3, "string", 5.21]
print(mylist[3])
mylist[3] = 5.6
print(mylist[3])
mylist.append(58)
print(len(mylist))
print(max(mylist))
print(min(mylist))
mylist.remove(5.21)
mylist.pop(0)
print(sorted(mylist))

x = [23, 64, 88, 24, 1]
x.sort()
print(x)

person = {'name':'rana', 'age':21, 'gender':'female'}
print(person['name'])
person['surname'] = "unal"
print(person)

def add(x, y):
    print(x + y)

add(3,164)

def mysum(*numbers):
    result = 0
    for number in numbers:
        result += number
    return result

print(mysum(10, 20, 11))

name = input()
age = int(input())

print("my name is %s and i am %d years old" % (name, age))

text = "Hello World!"
print(text.count("o"))
words = text.split(' ')
print(words)
print(text.replace("Hello", "Goodbye"))
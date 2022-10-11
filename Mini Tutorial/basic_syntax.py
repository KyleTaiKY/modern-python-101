#check type and instance type
name = "Kyle"
print(type(name))
print(isinstance(name, str))
print(type(name) == str)
print('Hi, %s.' % name)

age = 3
print(type(age))

age = float(2)
print(type(age))

#casting / parsing
number = "20"
age = int(number)
print(type(age))

print("#########################")

#or
print(0 or 1)  ## 1
print(False or 'hey')  ## 'hey'
print('hi' or 'hey')  ## 'hi'
print([] or False)  ## False
print(False or [])  ## []


def is_adult(age):
    if age > 18:
        return True
    else:
        return False


def is_adult2(age):
    return True if age > 18 else False


name = "Be\"a\\u"
print(name.upper().lower())
print("au" in name)
print(name[1:-1])

ingredients_purchased = True
meal_cooked = False

ready_to_serve = all([ingredients_purchased, meal_cooked])
print(ready_to_serve)


num1 = 2 + 3j
num2 = complex(2, 3)
print(num2.real, num2.imag)

abs(-5.5) ## 5.5
print(round(5.46, 1)) ## 5.5


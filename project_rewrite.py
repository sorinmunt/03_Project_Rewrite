
# implement the min (x, y) function for two real numbers as imputs - var 1 - without function

# num1 = float(input("Enter the first numeber: "))
# num2 = float(input("Enter the second numeber: "))



# if num1 <= num2:
#     min = num1
# else:
#     min = num2

# print("min (x, y) = " + str(min))


# implement the min (x, y) function for two real numbers as imputs - var 2 with function

def min(x, y):
    if x <= y:
        return x
    else:
        return y

x = float(input("Enter the first numeber: "))
y = float(input("Enter the second numeber: "))

print("min (x, y) = " + str(min(x, y)))



#implement the max(value_list) function for a list of numbers - var 1 - without function



# numbers = [16, 2, 3, -54, 65, -98, 45, -75, 76, 6, 256]
# numbers_count = len(numbers)


# max = -9999999999

# for index in range(numbers_count):
    
#     if numbers[index] > max:
#         max = numbers[index]

# print("max(value_list) = " + str(max))


#implement the max(value_list) function for a list of numbers - var 2 with function

def max():
    max = -9999999999
    for index in range(numbers_count):
    
        if numbers[index] > max:
            max = numbers[index]
    return max


numbers = [16, 2, 3, -54, 65, -98, 45, -75, 76, 6, 256]
numbers_count = len(numbers)

print("max(value_list) = " + str(max()))





#implement the len(value_list) function for a list of numbers or strings which returns the lenghth of the string - var 1, without function


# numbers = [16, 2, 3, -54, 65, -98, 45, -75, 76, 6, 256]

# list_count = 0

# for index in numbers:
#     list_count = list_count + 1

# print("len(value_list) = " + str(list_count))


#implement the len(value_list) function for a list of numbers or strings which returns the lenghth of the string - var 2, with function



def len_list():
    list_count = 0

    for index in numbers:
        list_count = list_count + 1
    
    return list_count


numbers = [16, 2, 3, -54, 65, -98, 45, -75, 76, 6, 256]

print("len(value_list) = " + str(len_list()))


# implement the multiply(x, y)  function for integers as inputs - var 1 - without function


# x = int(input("Enter the first integer x: "))
# y = int(input("Enter the second integer y: "))


# index = 0
# multi = 0


# for index in range(index,y):
#     multi = multi + x


# print("multiply result = " + str(multi))



#implement the multiply(x, y)  function for integers as inputs - var 2 - with function

def multiply(x, y):

    index = 0
    multi = 0

    for index in range(index, y):
        multi = multi + x

    return multi

x = int(input("Enter the first integer x: "))
y = int(input("Enter the second integer y: "))



print("multiply (x, y) = " + str(multiply(x, y)))



#implement the pow(x, y) function for real base numbers and positive integer exponents - var 1 - without function

# x = float(input("Enter the base number x: "))
# y = int(input("Enter the power number y: "))

# index = 0
# power = 1


# for index in range(index,y):
#     power = power * x
    

# print("power result = " + str(power))

#implement the pow(x, y) function for real base numbers and positive integer exponents - var 2 - with function

def pow(x, y):

    index = 0
    power = 1


    for index in range(index,y):
        power = power * x

    return power

x = float(input("Enter the base number x: "))
y = int(input("Enter the power number y: "))


print("pow(x, y) = " + str(pow(x, y)))


#implement the divmod(x, y) function for two integer numbers as inputs. It should return a tuple, the first value should be equal to the value of 
#x // y and the second value of x % y - var 1 - without function


# x = 75
# y = 3
# sum = 0

# base_division = x // y
# rest = x % y



# while sum < x:
#     sum = sum + y
#     #print("sum = " + str(sum))


# sum = sum - y
# restul = x - sum
# tuple_divmod = (sum, restul)


# print("sum_final = " + str(sum))
# print("restul = " + str(restul))
# print(tuple_divmod)


#implement the divmod(x, y) function for two integer numbers as inputs. It should return a tuple, the first value should be equal to the value of 
#x // y and the second value of x % y - var 2 - with function

def divmod(x, y):

    sum = 0

    while sum < x:
        sum = sum + y

    sum = sum - y
    return sum


x = int(input("Enter the first integer x: "))
y = int(input("Enter the second integer y: "))



tuple_divmod = (divmod(x, y), (x - (divmod(x, y))))


print(tuple_divmod)



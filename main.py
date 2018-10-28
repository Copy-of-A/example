# A user enters integers line by line. the sign of ending is "."
# A user can`t stop until at least one number is inputted.
# For given sequence of integer find an amount of equals for each number
def find_equals(myList):
    nums = {}
    for num in myList:
        if num in nums:
            nums[num] += 1
        else:
            nums[num] = 1
    return nums


print('Print numbers until \'.\'')
number_list = []
flag = True
while flag:
    x = input()
    if x == ".":
        if len(number_list) == 0:
            print("You should enter at least one number")
        else:
            flag = False
    else:
        try:
            int(x)
            number_list.append(x)
        except:
            print("It`s not a number")

for number in number_list:
    print(number, end=", ")
print()

result = find_equals(number_list)
print(result.items())




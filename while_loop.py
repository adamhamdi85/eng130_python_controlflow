#

# data = 0
#
# while data < 10:
#     print(f"it's working - >{data}")
#     if data == 5:
#          break        #key word continue
#     data += 1

#age =
# user_prompt = True
#
# while user_prompt:
#     age = input("please enter your age")
#     if age.isdigit():
#         user_prompt = False
#     else:
#         print("Please enter your age in digits only")
# print(f"your age is {age}")
# # calculate their age - year of birth etc.

def cal_Age(birth_year , current_year ):
    age = current_year - birth_year
    return age
current_year = int(input(" what is the current year?"))
birth_year = int(input(" what year was you born in?"))
print(cal_Age(birth_year , current_year))


# year = str(year)
#
# print("and you were born in {}").format(year)


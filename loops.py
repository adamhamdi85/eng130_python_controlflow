# list_data = [1, 2, 3, 4, 5]
# for number in list_data:
#     if number == 3:
#        print(number)
#     elif number > 3:
#         print(" you have passed 3")
#     else:
#         print("too soon")

# create a dictionary student_data
# iterate through the dict
# using control flow - if elif - else and for loop print all the keys
# print key with matching value
def print_key_and_values(dictionary):

    for key in dictionary:         # loops through all the items in dictionary and stores it in name
        print(key)                 # print first key
        print(dictionary[key])    # print corresponding value


student_data = {
    "name" : "Adam",
    "surname" : "Hamdi",
    "age" : "22"



}
print_key_and_values(student_data)     # calling function and giving it student dictionary
# for name in student_data()
# print(name)
# values = student_data.values()
# print(values)
# for name in student_data:
#     if name in student_data:
#         print(name, student_data[name])








# print(list_data)
# print(list_data[0])
# print(list_data[1])
# print(list_data[2])
# print(list_data[3])
# print(list_data[4])

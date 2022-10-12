list_data = [1, 2, 3, 4, 5]
for number in list_data:
    if number == 3:
       print(number)
    elif number > 3:
        print(" you have passed 3")
    else:
        print("too soon")

# create a dictionary student_data
# iterate through the dict
# using control flow - if elif - else and for loop print all the keys
# print key with matching value

student_data = {
    "name" : "Adam",
    "surname" : "Hamdi",
    "age" : "22"
}
for name in student_data:
    print(name)

for name in student_data.values():
    if name == "Adam":
        print(student_data.keys())







# print(list_data)
# print(list_data[0])
# print(list_data[1])
# print(list_data[2])
# print(list_data[3])
# print(list_data[4])

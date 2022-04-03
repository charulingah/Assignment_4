'''Write a Python program to square the elements of a list using map() function.'''

#solution with user input

list_input = input('Enter elements of a list separated by space ')         #user input
user_list = list_input.split()                                             #converts to list
list_num = list(map(int, user_list))                                       #converts list to int using map
x = map(lambda x : x**2, list_num)                                         #lambda expression to find square
print(list(x))


#Sample List: [4, 5, 2, 9]
#sample output: [16, 25, 4, 81]

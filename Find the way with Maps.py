'''Write a Python program to triple all numbers of a given list of integers. Use Python map.'''



#solution

list_input = input('Enter elements of a list separated by space ')    #user input
user_list = list_input.split()                                        #coverts to list
list_num = list(map(int, user_list))                                  #converts to int using map
x = map(lambda x : x*3, list_num)                                     #lambda expression to triple
print(list(x))



#sample list: [1, 2, 3, 4, 5, 6, 7]
#sample output : [3, 6, 9, 12, 15, 18, 21]

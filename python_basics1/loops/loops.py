grocery_list = ['bannana', 'turkey', 'apple', 'toothbrush'] #intializes a list

#for i in range() is the same thing as for i in [0,1,2,3,...]

for item in grocery_list:
    print(item) # prints the values

for item in range(len(grocery_list)):
    print(item) # print the indecies

for item in range(len(grocery_list)):
    print(grocery_list) # prints whole array, not useful

for i in range(len(grocery_list)):
    print(grocery_list[i]) #prints values, says print the indexed values

#enumrate: useful for priting out values and their indecies

for i, item in enumerate(grocery_list):
    print(i, item)

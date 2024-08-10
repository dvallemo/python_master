favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

#write for loop and while loop and enumerate for this array 

#for loop
for item in favorites:
    print(item)
#enumerate 
for idx, item in enumerate(favorites):
    print(idx, item)

#while loop
count = 0
while count < len(favorites):
    print('One of my favorite desserts is ', favorites[count])
    count += 1

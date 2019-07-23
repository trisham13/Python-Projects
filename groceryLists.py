grocery = ['milk', 'eggs', 'veggies'];
print(grocery);

add = input("What do you want to add to your list? ");
grocery.append(add);
print('Your new list is ' + str(grocery));

insertItem = grocery[2]
grocery.insert(4,insertItem);
print('I added veggies to your list again ' + str(grocery));

removeItem = input('Which item would you like to remove?');

count = grocery.count(removeItem);

if (count > 0):
    grocery.remove(removeItem);
else:
    print('This item is not in your list.');

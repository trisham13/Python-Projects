#Trisha Menon
myJewelryBox = ['earring', 'ring', 'necklace']
print('Ms. Pooja\'s jewelry box contains ')
print(myJewelryBox)

print('I have added something to Ms. Pooja\'s jewelry box. Now, it has ')
myJewelryBox.append('tiara')
for item in myJewelryBox:
    print(item)

print('I accidently broke her earring, so I took it out of her jewelry bow before she noticed. Now her box only has ')
del myJewelryBox[0]
for item in myJewelryBox:
    print(item)

print('Ms. Pooja\'s jewelry box has ' + str(len(myJewelryBox)) + ' items')

# Bonus
print('My mom has to go shopping later, so I made her a list of things she needs to buy: ')
shoppingList = ('eggs', 'bread', 'butter')
print(shoppingList)

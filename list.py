closetList = ['shoes', 'shirts', 'pants', 'jackets', 'skirts', 'underwear']
numList = [1,2,3,4,5,6,7,8,9,10,11,12]
for a in numList:
    print(a)
closetList.append('socks')
print('How many times do I have socks? ')
x = closetList.count('socks')
print(x)
for apparel in closetList:
    print(apparel)

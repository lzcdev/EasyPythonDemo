#!usr/bin/python

# This is my shopping list
shopList = ['apple', 'mango', 'carrot', 'banana']

print 'I have', len(shopList), 'items to purchase'

print 'These items are:\n',
for item in shopList:
	print item

print '\nI also have to buy rice'
shopList.append('rice')
print 'My shopping list is now', shopList

print 'I will sort my list now'
shopList.sort()
print 'Sorted shopping list is', shopList

print 'THe first item I will buy is', shopList[0]
olditem = shopList[0]
del shopList[0]
print 'I bought the', olditem
print 'My shopping list is now', shopList
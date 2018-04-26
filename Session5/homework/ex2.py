inventory = {
    'gold': 500,
    'pouch': ['flint', 'twine', 'gemstone'],
    'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}
inventory ['pocket'] = ['seashell', 'strange', 'lint'] #truy cap vao inventory > pocket
print (inventory)
inventory['backpack'].remove('dagger')
print (inventory)
# x = 8
# x = x + 50
# x += 50
inventory ['gold'] = inventory['gold'] + 50

print (inventory)

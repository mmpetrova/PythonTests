test_dict = {
    'address' : 'test_address',
    'last_name' : 'test_last_name'
}


for key in test_dict:
    print(key, test_dict.get(key))

keys = test_dict.keys()
#print(keys)
values = test_dict.values()
#print(values)
items = test_dict.items()
#print(items)

test_dict['new_pos'] = 'new_val'

test_dict.pop('address')

for key, value in items:
    print(key, value)
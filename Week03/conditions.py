x = 0
if x > 0:
    print(f'{x} is positive number')
elif x == 0:
    print(f'{x} is zero')
else:
    print(f'{x} is negative number')


'''
y = 0
check = (y > 0)
match y:
    case (y > 0):
        print(f'{y} is positive number')
    case (y == 0):
        print(f'{y} is zero')
    default:
        print(f'{y} is negative number')
'''

gender = 'Male'
pronoun = 'He' if gender == 'Male' else 'She'
print(pronoun)
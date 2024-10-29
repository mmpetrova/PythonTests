'''
def my_func(action):
    print(f'I am {action}')

my_func('a function')

##################
def calculate_weight(mass, gravity = 9.8):
    weight = mass * gravity
    return weight
print(calculate_weight(10))
print(calculate_weight(10, 10))

##################
import math
def calculate_area_circle(radius):
    area = math.pi * radius ** 2
    return area
print(calculate_area_circle(3))

##################
def calculate_volume(width, height, length):
    volume = width * height * length
    return volume

print(calculate_volume(length=14, width=100, height=25))

##################
countries = ['Finland', 'Switzerland', 'Pakistan', 'Tadjikistan']

def filter_country_by_string(substring):
    new_list = []
    for country in countries:
        if substring in country:
            new_list.append(country)
    return new_list
print(f'1st method : {filter_country_by_string('stan')}')

def filter_country_by_starting(substr):
    new_list = []
    for country in countries:
        if country.startswith(substr):
            new_list.append(country)
    return new_list, len(new_list)
print(f'2nd method : {filter_country_by_starting('F')}')

##################
def add_nums(*args):
    print(sum(args))

print(add_nums(1, 2, 3, 4, 5, 6, 7))

##################
def generate_groups(team, *args):
    return team, args

team, args = (generate_groups('Team-1', 'test1', 'test2'))
print(team)
print(args) 
'''

##################
dict = {
    'steet' : 'test street',
    'house_number' : 24
}
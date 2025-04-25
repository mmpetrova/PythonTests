import csv
import random
import string

def generate_id(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_data(num_rows):
    data = []
    for _ in range(num_rows):
        pr_id = generate_id(random.randint(1, 10))  # Short IDs
        other_columns = [random.randint(1, 100) for _ in range(7)]
        data.append([pr_id] + other_columns)
    return data

# Define the number of rows
num_rows = 120000
data = generate_data(num_rows)

# Write to CSV
with open("generated_data.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Pr_ID", "Column_2", "Column_3", "Column_4", "Column_5", "Column_6", "Column_7", "Column_8"])
    writer.writerows(data)

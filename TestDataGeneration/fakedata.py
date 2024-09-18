import random
from faker import Faker
import csv

# Initialize Faker
fake = Faker()


def generate_random_data(num_entries):
    data = []
    for i in range(num_entries):
        name = fake.name()
        phone_number = fake.phone_number()
        email = fake.email()
        gender = random.choice(['Male', 'Female', 'Other'])
        data.append({
            'name': name,
            'phone number': phone_number,
            'email': email,
            'gender': gender,
            'profession': "",
            'dob': "",
            'nationality': "",
            'province': "",
            'district': "",
            'municipality': "",
            'ward': "",
            'groupLabel': ""
        })
    return data


def save_to_csv(data, filename):
    keys = data[0].keys()
    with open(filename, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)


# Generate 100 entries of random data
num_entries = 10
random_data = generate_random_data(num_entries)

# Save the data to a CSV file
save_to_csv(random_data, '../test_data1.csv')

print(f"{num_entries} entries of random data have been generated and saved to 'test_data.csv'.")

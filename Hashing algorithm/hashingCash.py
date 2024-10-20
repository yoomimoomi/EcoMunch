import hashlib

# Function to hash the phone number
def hash_phone_number(phone_number):
    return hashlib.sha256(phone_number.encode()).hexdigest()

# This does the same thing the Credit Card algorithm does but with phone number
database = {
    '1001': hash_phone_number('5551234567'),
    '1002': hash_phone_number('5552345678'),
    '1003': hash_phone_number('5553456789'),
    '1004': hash_phone_number('5554567890')
}

def verify_container(container_id, phone_number):
    hashed_phone = hash_phone_number(phone_number)
    if container_id in database:
        stored_hash = database[container_id]
        return hashed_phone == stored_hash
    else:
        return False

# No actual data is ever being saved in the Database
test_data = [
    ('1001', '5551234567'),  # True match
    ('1008', '5558901234')   # False match
    ('1002', '5552345678'),  # True match
    ('1003', '5553456789'),  # True match
    ('1004', '5554567890'),  # True match
    ('1005', '5555678901'),  # False match
    ('1006', '5556789012'),  # False match
    ('1007', '5557890123'),  # False match
 \
]

# Check each entry
for container_id, phone_number in test_data:
    if verify_container(container_id, phone_number):
        print("Thank you for returning your container, you can opt for cash or card for your 1 dollar refund.")
    else:
        print("Thank you for keeping Governors Island clean! you can opt for cash or card for your 0.75 cent reward.")
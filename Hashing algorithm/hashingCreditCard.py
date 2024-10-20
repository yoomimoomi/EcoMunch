import hashlib

# Function to hash the credit card number
def hash_credit_card(card_number):
    return hashlib.sha256(card_number.encode()).hexdigest()


# Mock database for prototype reason (Not secured), we will not store any credit card data directly in this database
database = {
    '1001': hash_credit_card('1234567890123456'),
    '1002': hash_credit_card('2345678901234567'),
    '1003': hash_credit_card('3456789012345678'),
    '1004': hash_credit_card('4567890123456789')
}

def verify_container(container_id, card_number):
    hashed_card = hash_credit_card(card_number)
    if container_id in database:
        stored_hash = database[container_id]
        return hashed_card == stored_hash
    else:
        return False

# Sample data of containerID and Card Number 
test_data = [
    ('1001', '1234567890123456'),  # True match
    ('1002', '2345678901234567'),  # True match
    ('1007', '7890123456789012'),  # False match
    ('1003', '3456789012345678'),  # True match
    ('1004', '4567890123456789'),  # True match
    ('1005', '5678901234567890'),  # False match
    ('1006', '6789012345678901'),  # False match
    ('1008', '8901234567890123')   # False match
]

# Check each entry
for container_id, credit_card_number in test_data:
    if verify_container(container_id, credit_card_number):
        print("Thank you for returning your container, you can opt for cash or card for your 1 dollar refund.")
    else:
        print("Thank you for keeping Governors Island clean! you can opt for cash or card for your 0.75 cent reward.")

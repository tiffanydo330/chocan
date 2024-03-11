import json

def validate_member_id(member_data):
    valid_ids = ["000001", "000002"]  # Replace with the actual list of valid IDs
    for member in member_data:
        if member["id_num"] not in valid_ids:
            return False, f"Invalid ID: {member['id_num']} for member: {member['name']}"
    return True, "All member IDs are VALID"

# Load the member data from a JSON file
with open('member.json', 'r') as f:
    member_data = json.load(f)

# Validate the member IDs
is_valid, message = validate_member_id(member_data)
print(message)

# Input functions for provider after a service
def get_provider_info():
    provider_name = input("Enter Provider Name: ")
    provider_number = input("Enter Provider Number: ")
    provider_address = input("Enter Provider Address (Street, City, State, Zip Code): ")
    return provider_name, provider_number, provider_address

def get_service_details():
    date_of_service = input("Enter Date of Service (MM-DD-YYYY): ")
    date_time_received = input("Enter Date and Time Data Received by the Computer (MM-DD-YYYY HH:MM:SS): ") #DB
    member_name = input("Enter Member Name: ")
    member_number = input("Enter Member Number: ")
    service_code = input("Enter Service Code: ")
    fee_to_be_paid = input("Enter Fee to be Paid: ") # $999.99 is the max
    return date_of_service, date_time_received, member_name, member_number, service_code, fee_to_be_paid

def get_summary_info():
    total_consultations = input("Enter Total Number of Consultations with Members (3 digits): ")
    total_fee = input("Enter Total Fee for the Week: ") # $99,999.99 is the max
    return total_consultations, total_fee

# Example of using the functions in main 
'''
def main():
    provider_info = get_provider_info()
    service_details = get_service_details()
    summary_info = get_summary_info()

    # Now you can use the collected data as needed, for example, to generate a report
    # ...

if __name__ == "__main__":
    main()
'''

# Input function for adding a new memebr
def add_new_member():
    # Get the new member's details
    name = input("Enter Member Name: ")
    id_num = input("Enter Member ID Number: ")
    street = input("Enter Member Street Address: ")
    city = input("Enter Member City: ")
    state = input("Enter Member State: ")
    zip_code = input("Enter Member Zip Code: ")
    services = []  # You can modify this part to add services if needed

    new_member = {
        "name": name,
        "id_num": id_num,
        "street": street,
        "city": city,
        "state": state,
        "zip_code": zip_code,
        "services": services
    }

# Example of adding a new member to the member.json file
'''
    # Load the existing members
    with open('member.json', 'r') as f:
        members = json.load(f)

    # Add the new member
    members.append(new_member)

    # Save the updated members back to the file
    with open('member.json', 'w') as f:
        json.dump(members, f, indent=4)

    print(f"New member {name} added successfully!")

if __name__ == "__main__":
    add_new_member()
'''
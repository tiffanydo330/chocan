import json
#import Client

def validate_member_id(member_data):
    valid_ids = ["000001", "000002"]  # Replace with the actual list of valid IDs
    for member in member_data:
        try:
            id_num = int(member["id_num"])
            if str(id_num).zfill(6) not in valid_ids:
                return False, f"Invalid ID: {member['id_num']} for member: {member['name']}"
        except ValueError:
            return False, f"ID: {member['id_num']} for member: {member['name']} is not a valid integer"
    return True, "All member IDs are VALID"

# Load the member data from a JSON file
with open('member.json', 'r') as f:
    member_data = json.load(f)

# Validate the member IDs
is_valid, message = validate_member_id(member_data)
print(message)

# Input functions for provider after a service
def get_provider_info(self):
    print("Enter Provider Name: ")
    provider_name = self.__string_input(100)  # Assuming max length of 100 characters
    print("Enter Provider Number: ")
    provider_number = self.__string_input(10)  # Assuming max length of 10 characters
    print("Enter Provider Address (Street, City, State, Zip Code): ")
    provider_address = self.__string_input(200)  # Assuming max length of 200 characters
    return provider_name, provider_number, provider_address

# Input function for service details
def get_service_details(self):
    print("Enter Date of Service (MM-DD-YYYY): ")
    date_of_service = self.__string_input(10)  # Assuming max length of 10 characters for date format MM-DD-YYYY
    print("Enter Date and Time Data Received by the Computer (MM-DD-YYYY HH:MM:SS): ") 
    date_time_received = self.__string_input(19)  # Assuming max length of 19 characters for date time format MM-DD-YYYY HH:MM:SS
    print("Enter Member Name: ")
    member_name = self.__string_input(50)  # Assuming max length of 50 characters for member name
    print("Enter Member Number: ")
    member_number = self.__string_input(10)  # Assuming max length of 10 characters for member number
    print("Enter Service Code: ")
    service_code = self.__string_input(10)  # Assuming max length of 10 characters for service code
    print("Enter Fee to be Paid: ") # $999.99 is the max
    fee_to_be_paid = self.__float_input(7)  # Assuming max length of 7 characters for fee to be paid format $999.99
    return date_of_service, date_time_received, member_name, member_number, service_code, fee_to_be_paid

    # __float_input() IS WRITTEN AT THE BOTTOM OF THIS FILE. IT IS COMMENTED OUT

def get_summary_info(self):
    print("Enter Total Number of Consultations with Members (3 digits): ")
    total_consultations = self.__int_input(3)  # Assuming max length of 3 digits for total consultations
    print("Enter Total Fee for the Week: ") # $99,999.99 is the max
    total_fee = self.__float_input(9)  # Assuming max length of 9 characters for total fee format $99,999.99
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
def add_new_member(self):
    # Get the new member's details
    name = self.__string_input(50)  # Assuming max length of 50 characters for name
    id_num = self.__string_input(10)  # Assuming max length of 10 characters for ID number
    street = self.__string_input(100)  # Assuming max length of 100 characters for street address
    city = self.__string_input(50)  # Assuming max length of 50 characters for city
    state = self.__string_input(2)  # Assuming max length of 2 characters for state
    zip_code = self.__string_input(5)  # Assuming max length of 5 characters for zip code
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
# HENRY HERE IS THE FLOAT TEST I PUT IT HERE SO I WOULDN'T
# ACCIDENTALLY BREAK THE client.py FILE
'''
# float_input as a helper function for recieving float input of length size
# Privdes reuasble input option with error handling
def __float_input(self, size) -> float:
    number: float
    while True:
        try:
            number = float(self.__string_input(size))
        except ValueError as msg:
            print(f"Error: {msg}", file = sys.stderr)
            print("Please re-enter:", file = sys.stderr)
        else: break
    return number
'''
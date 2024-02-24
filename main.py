import json  # Importing the json module to work with JSON data
from data import Member, Provider  # Importing custom data models
from schema import MemberSchema, ProviderSchema  # Importing schemas for data serialization
from typing import Dict, Any  # Importing type hints for data types

def load_data_from_json(filename):
    """
    Loads data from a JSON file.

    Parameters:
    - filename (str): The name of the JSON file to load.

    Returns:
    - data (Any): The loaded JSON data.
    """
    try:
        with open(filename, 'r') as file:
            data = json.load(file)  # Load JSON data from the file
        return data
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"Error loading data from '{filename}': {e}")
        return None

def write_data_to_json(data, filename):
    """
    Writes data to a JSON file.

    Parameters:
    - data (Any): The data to write to the JSON file.
    - filename (str): The name of the JSON file to write.

    Returns:
    - None
    """
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)  # Write data to the file with indentation
    except Exception as e:
        print(f"Error writing data to '{filename}': {e}")

def main() -> None:
    """
    The main function of the program.
    """
    # Load data from JSON files
    member_data = load_data_from_json('members.json')
    provider_data = load_data_from_json('providers.json')

    # Deserialize JSON data into dictionaries
    if member_data:
        member_schema = MemberSchema(many=True)  # Create a schema for member data
        members_dict: Dict[str, Member] = {member.id_num: member for member in member_schema.load(member_data)}

    if provider_data:
        provider_schema = ProviderSchema(many=True)  # Create a schema for provider data
        providers_dict: Dict[str, Member] = {provider.id_num: provider for provider in provider_schema.load(provider_data)}

    # Modify data
    members_dict["000001"].name = "New Name"

    # Print modified member data
    print("Modified Members:")
    for id_num, member in members_dict.items():
        print("Name:", member.name)
        print("ID:", member.id_num)
        print("Services:")
        for service in member.services:
            print("- Date:", service.date)
            print("- Provider Name:", service.provider_name)
            print("- Service Name:", service.service_name)
        print()

    # Write modified data back to JSON files
    write_data_to_json(member_schema.dump(list(members_dict.values())), 'members_modified.json')
    write_data_to_json(provider_schema.dump(list(providers_dict.values())), 'providers_modified.json')

if __name__ == "__main__":
    main()  # Call the main function if the script is executed directly

import json
from data import Member, Provider
from schema import MemberSchema, ProviderSchema
# for data type declaration or whatever
from typing import Dict, Any

def load_data_from_json(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"Error writing data to'{filename}': {e}")
        return None

def write_data_to_json(data, filename):
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error writing data to'{filename}': {e}")

# the expression -> None means main returns nothing
def main() -> None:
    # Load data from JSON file
    member_data = load_data_from_json('members.json')
    provider_data = load_data_from_json('providers.json')
    
    if member_data:
        member_schema = MemberSchema(many=True)
        members_dict: Dict[str, Member] = {member.id_num: member for member in member_schema.load(member_data)}

    if provider_data:
        provider_schema = ProviderSchema(many=True)
        providers_dict: Dict[str, Member] = {provider.id_num: provider for provider in provider_schema.load(provider_data)}

    members_dict["000001"].name = "New Name"

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

    #write data back to JSON
    write_data_to_json(member_schema.dump(list(members_dict.values())), 'members_modified.json')
    write_data_to_json(provider_schema.dump(list(providers_dict.values())), 'providers_modified.json')

if __name__ == "__main__":
    main()

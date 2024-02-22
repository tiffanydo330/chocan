#main.py

from marshmallow import Schema, fields, post_load
import json
from data import *

"""
def create_member_from_data(member_data):
    return Member(member_data['name'], member_data['id_num'], member_data['street'],
                  member_data['city'], member_data['state'], member_data['zip_code'],
                  member_data['services'])

def load_members_from_json(filename):
    loaded_members_data = read_json(filename)
    loaded_members = {member['id_num']: create_member_from_data(member)
            for member in loaded_members_data}
    return loaded_members

def create_provider_from_data(provider_data):
    return Provider(provider_data['name'], provider_data['id_num'], 
                    provider_data['street'], provider_data['city'], 
                    provider_data['state'], provider_data['zip_code'], 
                    provider_data['services'], provider_data['num_consultations'], 
                    provider_data['total_wk_fee'])

def load_providers_from_json(filename):
    loaded_providers_data = read_json(filename)
    loaded_providers = {provider['id_num']: create_provider_from_data(provider)
            for provider in loaded_providers_data}
    return loaded_providers
"""

def write_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def read_json(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

def main():
    member1services = [MemberService("01-01-2001", "provider1", "service")]
    member2services = [MemberService("01-01-2001", "provider2", "service")]

    provider1services = [ProviderService("01-01-2001", "01-01-2001 07:56:30", 
                                        "jon", "001", "7", 5000)]
    provider2services = [ProviderService("01-01-2001", "01-01-2001 07:56:30", 
                                        "jane", "002", "7", 5000)]
    members = [
            Member("Member1", "001", "member 1 street", "member1 town", "OR", "89019",
                member1services),
            Member("Jane Smith", "002", "456 Oak St", "Othertown", "NY", "67890",
                member2services)
            ]

    providers = [
            Provider("Dr. Smith", "101", "789 Elm St", "Anycity", "TX", "54321",
                provider1services, 10, 1000), 
            Provider("Dr. Johnson", "102", "987 Pine St", "Othercity", "FL", "13579",
                provider2services, 8, 800)
            ]
    member_schema = MemberSchema()
    provider_schema = ProviderSchema()
    
    member_data = [member_schema.dump(member) for member in members]
    provider_data = [provider_schema.dump(provider) for provider in providers]
    """
    member_data = [member.to_dict() for member in members]
    provider_data = [provider.to_dict() for provider in providers]
    """

    write_json(member_data, 'members.json')
    write_json(provider_data, 'providers.json')
    
    loaded_members_data = read_json('members.json')
    loaded_providers_data = read_json('providers.json')

    loaded_members = [member_schema.load(member) for member in loaded_members_data]
    loaded_providers = [provider_schema.load(provider) 
                        for provider in loaded_providers_data]
    
    """
    loaded_members = load_members_from_json('members.json')
    loaded_providers = load_providers_from_json('providers.json')
    """
    """
    print("Loaded members:")
    for id_num, member in loaded_members.items():
        print(f"ID: {id_num}, Data: {member.__dict__}")

    print("Loaded providers:")
    for id_num, member in loaded_providers.items():
        print(f"ID: {id_num}, Data: {provider.__dict__}")
    """
    print("Loaded members:")
    for member in loaded_members:
        print(member.__dict__)

    print("Loaded providers:")
    for provider in loaded_providers:
        print(provider.__dict__)

if __name__ == "__main__":
    main()

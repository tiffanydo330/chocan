#main.py

#from marshmallow import Schema, fields, post_load
import json
from data import *

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

    write_json(member_data, 'members.json')
    write_json(provider_data, 'providers.json')
    
    loaded_members_data = read_json('members.json')
    loaded_providers_data = read_json('providers.json')

    loaded_members = [member_schema.load(member) for member in loaded_members_data]
    loaded_providers = [provider_schema.load(provider) 
                        for provider in loaded_providers_data]
    
    print("Loaded members:")
    for member in loaded_members:
        print(member.__dict__)

    print("Loaded providers:")
    for provider in loaded_providers:
        print(provider.__dict__)

if __name__ == "__main__":
    main()

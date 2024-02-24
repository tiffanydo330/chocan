import json
from data import Member, Provider
from schema import MemberSchema, ProviderSchema

def load_data_from_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def write_data_to_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def main():
    # Load data from JSON file
    member_data = load_data_from_json('members.json')
    provider_data = load_data_from_json('providers.json')

    # Deserialize data
    member_schema = MemberSchema(many=True)
    provider_schema = ProviderSchema(many=True)
    members = member_schema.load(member_data)
    providers = provider_schema.load(provider_data)
    
    # modifies data, should be fine with user input
    #members[0].name = "New Name"

    #members_dict = {member['id_num']: member for member in member_schema.load(member_data)}
    #members_dict = {member.id_num: member for member in member_schema.load(member_data)}
    #providers_dict = {provider.id_num: provider for provider in provider_schema.load(provider_data)}
    #members_dict["001"].name = "New Name"
    
    print("Modified Members:")
    for member in members:
        print("Name:", member.name)
        print("ID:", member.id_num)
        print("Services:")
        for service in member.services:
            print("- Date:", service.date)
            print("- Provider Name:", service.provider_name)
            print("- Service Name:", service.service_name)
        print()
    #write_data_to_json(list(members_dict.values()), 'members_modified.json')
    #write_data_to_json(list(providers_dict.values()), 'providers_modified.json')

    # write data back to JSON files
    write_data_to_json(member_schema.dump(members), 'members_modified.json')
    write_data_to_json(provider_schema.dump(providers), 'providers_modified.json')

if __name__ == "__main__":
    main()

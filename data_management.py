#data_management.py

import json  # Importing the json module to work with JSON data
from typing import Dict
from data import Member, Provider
from schema import MemberSchema, ProviderSchema  # Importing schemas for data serialization


class DataManager:
    def __init__(self):
        self.__member_data = self.load_data_from_json('members.json')
        self.__provider_data = self.load_data_from_json('providers.json')

        # Deserialize JSON data into dictionaries
        if self.__member_data:
            self.__member_schema = MemberSchema(many=True)  # Create a schema for member data
            self.__members_dict: Dict[str, Member] = {member.id_num: member for member in self.__member_schema.load(self.__member_data)}

        if self.__provider_data:
            self.__provider_schema = ProviderSchema(many=True)  # Create a schema for provider data
            self.__providers_dict: Dict[str, Provider] = {provider.id_num: provider for provider in self.__provider_schema.load(self.__provider_data)}

    def __del__(self):
        self.write_all_to_json()

    def get_member(self, member_id: str) -> Member:
        if member_id in self.__members_dict:
            return self.__members_dict[member_id]
        else:
            return None

    def get_provider(self, provider_id: str) -> Provider:
        if provider_id in self.__providers_dict:
            return self.__providers_dict[provider_id]
        else:
            return None

    def get_member_dict(self):
        return self.__members_dict

    def get_provider_dict(self):
        return self.__providers_dict

    def add_member(self, member_id: str, member: Member) -> None:
        self.__members_dict[member_id] = member

    def add_provider(self, provider_id: str, provider: Provider) -> None:
        self.__providers_dict[provider_id] = provider

    def remove_member(self, member_id: str) -> None:
        if member_id in self.__members_dict:
            del self.__members_dict[member_id]
            return 0
        else:
            return 1

    def remove_provider(self, provider_id: str) -> None:
        if provider_id in self.__providers_dict:
            del self.__providers_dict[provider_id]
            return 0
        else:
            return 1

    def modify_member(self, member_id: str, new_member_data: Member) -> None:
        if member_id in self.__members_dict:
            self.__members_dict[member_id] = new_member_data
            return 0
        else:
            return 1

    def modify_provider(self, provider_id: str, new_provider_data: Provider) -> None:
        if provider_id in self.__providers_dict:
            self.__providers_dict[provider_id] = new_provider_data
            return 0
        else:
            return 1

    def load_data_from_json(self, filename):
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

    def write_to_json(self, data, filename):
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

    def write_all_to_json(self):
        self.write_to_json(self.__member_schema.dump(list(self.__members_dict.values())), 'members_modified.json')
        self.write_to_json(self.__provider_schema.dump(list(self.__providers_dict.values())), 'providers_modified.json')

    

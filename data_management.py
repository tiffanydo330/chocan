#data_management.py

from typing import Dict
from data import Member, Provider

class DataManager:
    def __init__(self, members: Dict[str, Member], providers: Dict[str, Provider]):
        self.members = members
        self.providers = providers

    def get_member(self, member_id: str) -> Member:
        return self.members.get(member_id)

    def get_provider(self, provider_id: str) -> Provider:
        return self.providers.get(provider_id)

    def add_member(self, member_id: str, member: Member) -> None:
        self.members[member_id] = member

    def add_provider(self, provider_id: str, provider: Provider) -> None:
        self.providers[provider_id] = provider

    def remove_member(self, member_id: str) -> None:
        if member_id in self.members:
            del self.members[member_id]
            return 1
        else
            return 0

    def remove_provider(self, provider_id: str) -> None:
        if provider_id in self.providers:
            del self.providers[provider_id]

    def modify_member(self, member_id: str, new_member_data: Member) -> None:
        if member_id in self.members:
            self.members[member_id] = new_member_data

    def modify_provider(self, provider_id: str, new_provider_data: Provider) -> None:
        if provider_id in self.providers:
            self.providers[provider_id] = new_provider_data

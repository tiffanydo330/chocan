# Client class as entrypoint into the ChocAn System
# Client offers CLI menus for Managers and Providers

import sys
import time
from services import ServiceManager
from report_generator import ReportGenerator
import Carl_Swin
from main import load_data_from_json
from data import Member, Provider  # Importing custom data models
from schema import MemberSchema, ProviderSchema  # Importing schemas for data serialization
from typing import Dict, Any  # Importing type hints for data types

MP_ID_MAX = 9
S_ID_MAX = 6
COMMENT_MAX = 100

class Client:

    # Constructor creates new instances of:
    #   - member provider managemement class (Dictionaries class)
    #   - service billing class
    #   - report generator class
    def __init__(self):
        self.__service_manager = ServiceManager("services.json")
        self.__service_manager.load_services()
        self.__report_generator = ReportGenerator()

        # What follows is from main! Next, this will be maintained within its own class
        # Load data from JSON files
        self.__member_data = load_data_from_json('members.json')
        self.__provider_data = load_data_from_json('providers.json')

        # Deserialize JSON data into dictionaries
        if self.__member_data:
            self.__member_schema = MemberSchema(many=True)  # Create a schema for member data
            self.__members_dict: Dict[str, Member] = {member.id_num: member for member in self.__member_schema.load(self.__member_data)}

        if self.__provider_data:
            self.__provider_schema = ProviderSchema(many=True)  # Create a schema for provider data
            self.__providers_dict: Dict[str, Provider] = {provider.id_num: provider for provider in self.__provider_schema.load(self.__provider_data)}
            print(self.__providers_dict)
            # To be filled in upon module completion:
            # self.__mp_management = MemberProviderManagement()
    
    def __del__(self):
        self.__service_manager.save_services()
    
    # main_menu_loop function is Client's only public function
    # is called by main() upon startup to offer initial menu options
    # gives Provider, Manager, and Exit options
    def main_menu_loop(self):
        while True:
            print("\nMain Menu")
            print("----------")
            print("1. Access Provider Menu")
            print("2. Access Manager Menu")
            print("0. Exit")
            print("----------\n")
            option = self.__int_input(1)
            match option:
                case 1:
                    self.__provider_menu_loop()
                case 2:
                    self.__manager_menu_loop()
                case 0:
                    break
                case _:
                    print(f"Error: invalid option {option}")
        return
    
    # provider_menu_loop offers private access to provider menu from main_menu_loop
    # gives Provide service, Provider Dictionary, View Provider Report, and Exit options
    def __provider_menu_loop(self):
        # Maybe require provider validation here?
        # my concern is, when TA is testing, they'll have to go into the provider file to access this menu
        # maybe move provider validation for viewing specific weekly reports? IDK
        while True:
            print("\nProvider Menu")
            print("----------")
            print("1. Provide service to Member")
            print("2. Display provider directory")
            print("3. View weekly report")
            print("0. Exit")
            print("----------\n")
            option = self.__int_input(1)
            match option:
                case 1:
                    print("\nEnter member number:")
                    member_id = self.__int_input(MP_ID_MAX)
                    # VALIDATE HERE, print status
                    
                    print("\nEnter data service was provided:")
                    date = self.__time_input()

                    print("\nEnter service ID:")
                    service_id = self.__int_intput(S_ID_MAX)
                    # give option to display provider directory to find service id
                    # Validate service_id

                    print("\nWould you like to enter comments for this service? (y/n)")
                    take_comments = self.__bool_input()
                    if take_comments:
                        print("Enter comment:")
                        comment = self.__string_input(COMMENT_MAX)

                    # Now, write information to current provider entry (or maybe to disk? not sure on this one)
                case 2: 
                    print("\nServices offered:")
                    print("----------")
                    self.__service_manager.display_services()
                    print("----------\n")
                #case 3:
                    # Check if a report has been written
                    # if so, display
                    # if not, error
                case 0:
                    break
                case _:
                    print(f"Error: invalid option {option}")
        return
    
    # manager_menu_loop offers private access to manager menu from main_menu_loop
    # gives Generate Reports, Access Members, Access Providers, and Exit menu options
    def __manager_menu_loop(self):
        while True:
            print("\nManager Menu")
            print("----------")
            print("1. Manage Members")
            print("2. Manage Providers")
            print("3. Generate Weekly Reports")
            print("0. Exit")
            print("----------\n")
            option = self.__int_input(1)
            match option:
                case 1:
                    self.__manage_members_loop()
                case 2:
                    self.__manage_providers_loop()
                case 3:
                    for provider in self.__providers_dict.values():
                        self.__report_generator.generate_provider_report(provider, provider.services)

                    for member in self.__members_dict.values():
                        self.__report_generator.generate_member_report(member, member.services)

                    # Need to rename, make class
                    Carl_Swin.sum_rep_main(self.__providers_dict)

                    # Old comments, maybe still relevant
                    # Ask self.__report_generator to generate week's reports
                    # Maybe we pass in self.__mp_managemnet as an arg?
                    # Alternatively, ManagerProviderManagemnt class could contain an instnace of ReportGenerator
                    #   Downside to that is every call to ReportGenerator would have to go through MPManagement
                case 0:
                    break
                case _:
                    print(f"Error: invalid option {option}")
        return

    # manage_Memebrs_loop offers private access to in-memory members from manager_menu_loop
    # gives Add, Remove, Update, Exit options
    def __manage_members_loop(self):
        while True:
            print("\nManaging Members")
            print("----------")
            print("1. Add Member")
            print("2. Delete Member")
            print("3. Update Member")
            print("0. Exit")
            print("----------\n")
            option = self.__int_input(1)
            match option:
                #case 1: 
                    # Prompt for all relevant member data
                    # Construct new Member instance with said data
                    # Send to self.__mp_management for addition
                #case 2:
                    # Prompt for Member name/id
                    # Send to self.__mp_managment for deletion
                    # If can't find, error
                #case 3:
                    # Not sure about this one -
                    # Possibly need another function for menu to give options on WHAT to update
                    # Prompt for Member name/id
                    # Prompt for what to change and how
                    # Send to self.__mp_management for update
                    # If can't find, error
                    # If change N/A, error
                case 0:
                    break
                case _:
                    print(f"Error: invalid option {option}")
        return

    # manage_providers_loop offers private access to in-memory providers from manager_menu_loop
    # gives Add, Remove, Update, Exit options
    def __manage_providers_loop(self):
        while True:
            print("\nManaging Providers")
            print("----------")
            print("1. Add Member")
            print("2. Delete Member")
            print("3. Update Member")
            print("0. Exit")
            print("----------\n")
            option = self.__int_input(1)
            match option:
                #case 1: 
                    # Prompt for all relevant provider data
                    # Construct new Provider instance with said data
                    # Send to self.__mp_management for addition
                #case 2:
                    # Prompt for Provider name/id
                    # Send to self.__mp_managment for deletion
                    # If can't find, error
                #case 3:
                    # Not sure about this one -
                    # Possibly need another function for menu to give options on WHAT to update
                    # Prompt for Provider name/id
                    # Prompt for what to change and how
                    # Send to self.__mp_management for update
                    # If can't find, error
                    # If change N/A, error
                case 0:
                    break
                case _:
                    print(f"Error: invalid option {option}")
        return

    # bool_input as a helper function for recieving boolean input
    # Provides reusable input option with error handling 
    def __bool_input(self) -> bool:
        ret_val: bool
        while True:
            buffer = input()
            match buffer:
                case "Y" | "y" | "Yes" | "yes" | "True" | "true":
                    ret_val = True
                    break
                case "N" | "n" | "No" | "no" | "False" | "false":
                    ret_val = False
                    break
                case _:
                    print(f"Error: invalid boolean input '{buffer}'", file = sys.stderr)
                    print("Please re-enter (y/n):", file = sys.stderr)
        return ret_val

    # string_input as a helper function for recieving string input of length size
    # Provides reusable input option with error handling
    def __string_input(self, size: int) -> str:
        buffer: str
        while True:
            buffer = input()
            if len(buffer) > size:
                print(f"Error: Input {size} characters max, but {len(buffer)} characters given", file = sys.stderr)
                print("Please re-enter:", file = sys.stderr)
            elif len(buffer) <= 0:
                print("Error: Input must include at least one character", file = sys.stderr)
                print("Please re-enter:", file = sys.stderr)
            else: break
        return buffer


    # int_input as a helper function for recieving integer input of length size
    # Privdes reuasble input option with error handling
    def __int_input(self, size) -> int:
        number: int
        while True:
            try:
                number = int(self.__string_input(size))
            except ValueError as msg:
                print(f"Error: {msg}", file = sys.stderr)
                print("Please re-enter:", file = sys.stderr)
            else: break
        return number 


    # time_input as a helper function for recieving mm-dd-yyy input as a string
    # Provides reuasble input option with error handling
    def __time_input(self) -> str:
        while True:
            time_string = input()
            try:
                current_time = time.strptime(time_string, "%m-%d-%Y")
            except ValueError:
                print(f"Error: time input '{time_string}' does not match format MM-DD-YYYY", file = sys.stderr)
            else:
                break
        return time.strftime("%m-%d-%Y", current_time)


# Initial testing:
def main():
    client = Client()
    client.main_menu_loop()

if __name__ == "__main__":
    main()
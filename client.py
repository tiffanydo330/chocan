# Client class as entrypoint into the ChocAn System
# Client offers CLI menus for Managers and Providers

import sys
import time
from services import ServiceManager
from report_generator import ReportGenerator
import Carl_Swin
from data import Member, Provider  # Importing custom data models
from typing import Dict, Any  # Importing type hints for data types
from data_management import DataManager

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
        self.__data_manager = DataManager()

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
                    self.__data_manager.generate_reports()
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
                case 1: 
                    # Prompt for all relevant member data
                    # Construct new Member instance with said data
                    # Send to self.__mp_management for addition
                    print("Full Name?: ")
                    temp_name = self.__string_input(80)
                    print("ID Number?: ")
                    temp_id = self.__string_input(6)
                    print("Street Address?: ")
                    temp_street = self.__string_input(100)
                    print("City?: ")
                    temp_city = self.__string_input(100)
                    print("State? (Full): ")
                    temp_state = self.__string_input(100)
                    print("Zip Code?: ")
                    temp_zip = self.__string_input(9)
                    new_member_data = Member(temp_name, temp_id, temp_street, temp_city,
                                             temp_state, temp_zip, services = [])
                    self.__data_manager.add_member(temp_id, new_member_data)
                    print("Member added!\n")
                    self.test_print(self.__data_manager.get_member_dict()) #TODO delete

                case 2:
                    # Prompt for Member name/id
                    print("Member ID to delete?: ")
                    id_to_delete = self.__string_input(6)
                    # Send to self.__mp_managment for deletion
                    # If can't find, error
                    if (self.__data_manager.remove_member(id_to_delete) == 1):
                        print(f"{id_to_delete} not found!\n") # TODO better error handling
                        break
                    else:
                        print(f"{id_to_delete} deleted!\n")
                    self.test_print(self.__data_manager.get_member_dict()) #TODO delete
                        
                case 3:
                    # Not sure about this one -
                    # Possibly need another function for menu to give options on WHAT to update
                    # Prompt for Member name/id
                    print("Member ID to modify?: ")
                    id_to_modify = self.__string_input(6)
                    
                    temp_member = self.__data_manager.get_member(id_to_modify)
                    if (temp_member == None):
                        print(f"{id_to_modify} not found!\n")
                        break
                    # Prompt for what to change and how
                    self.__modify_menu(id_to_modify, temp_member)
                    self.__data_manager.modify_member(id_to_modify, temp_member) 
                    # Send to self.__mp_management for update
                    # If can't find, error
                    # If change N/A, error
                    self.test_print(self.__data_manager.get_member_dict()) #TODO delete
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
            print("1. Add Provider")
            print("2. Delete Provider")
            print("3. Update Provider")
            print("0. Exit")
            print("----------\n")
            option = self.__int_input(1)
            match option:
                case 1: 
                    # Prompt for all relevant provider data
                    # Construct new Provider instance with said data
                    # Send to self.__mp_management for addition
                    print("Full Name?: ")
                    temp_name = self.__string_input(80)
                    print("ID Number?: ")
                    temp_id = self.__string_input(6)
                    print("Street Address?: ")
                    temp_street = self.__string_input(100)
                    print("City?: ")
                    temp_city = self.__string_input(100)
                    print("State? (Full): ")
                    temp_state = self.__string_input(100)
                    print("Zip Code?: ")
                    temp_zip = self.__string_input(9)
                    print("# of Consultations?: ")
                    temp_consultations = self.__int_input(3)
                    print("Total Weekly Fee?: ")
                    temp_total = self.__float_input(11)
                    new_provider_data = Provider(temp_name, temp_id, temp_street, 
                            temp_city, temp_state, temp_zip, services = [],
                            num_consultations = temp_consultations, 
                            total_wk_fee = temp_total)
                    self.__data_manager.add_provider(temp_id, new_provider_data)
                    print("Provider added!\n")
                    self.test_print(self.__data_manager.get_provider_dict()) #TODO delete
                case 2:
                    # Prompt for Provider name/id
                    # Send to self.__mp_managment for deletion
                    # If can't find, error
                    print("Provider ID to delete?: ")
                    id_to_delete = self.__string_input(6)
                    # Send to self.__mp_managment for deletion
                    # If can't find, error
                    if (self.__data_manager.remove_provider(id_to_delete) == 1):
                        print(f"{id_to_delete} not found!\n") # TODO better error handling MAYBE... can probably just forget about it
                        break
                    else:
                        print(f"{id_to_delete} deleted!\n")
                    self.test_print(self.__data_manager.get_provider_dict()) #TODO delete
                        
                case 3:
                    # Not sure about this one -
                    # Possibly need another function for menu to give options on WHAT to update
                    # Prompt for Provider name/id
                    # Prompt for what to change and how
                    print("Provider ID to modify?: ")
                    id_to_modify = self.__string_input(6)
                    
                    temp_provider = self.__data_manager.get_provider(id_to_modify)
                    if (temp_provider == None):
                        print(f"{id_to_modify} not found!\n")
                        break
                    # Prompt for what to change and how
                    self.__modify_menu(id_to_modify, temp_provider)
                    self.__data_manager.modify_provider(id_to_modify, temp_provider) 
                    # Send to self.__mp_management for update
                    # If can't find, error
                    # If change N/A, error
                    self.test_print(self.__data_manager.get_provider_dict()) #TODO delete
                case 0:
                    break
                case _:
                    print(f"Error: invalid option {option}")
        return

    def __modify_menu(self, id_num, person_to_modify):
        id_flag = 0
        while True:
            if (id_flag > 0):
                print(f"\nModifying ID: {person_to_modify.id_num}")
            else:
                print(f"\nModifying ID: {id_num}")
            print("----------")
            print(f"1. Change Name        ({person_to_modify.name})")
            print(f"2. Change ID Number   ({person_to_modify.id_num})")
            print(f"3. Change Street      ({person_to_modify.street}) ")
            print(f"4. Change City        ({person_to_modify.city})")
            print(f"5. Change State       ({person_to_modify.state})")
            print(f"6. Change Zip Code    ({person_to_modify.zip_code})")
            print(f"7. Modify Services") # TODO Coming soon!!! (tm)
            if (isinstance(person_to_modify, Provider)):
                    print(f"8. Change # of Consultations  ({person_to_modify.num_consultations})")
                    print(f"9. Change Weekly Total Fee    ({person_to_modify.total_wk_fee})")
            print("0. Exit")
            print("----------\n")
            option = self.__int_input(1)
            match option:
                case 1:
                    print("New Name?: ")
                    person_to_modify.name = self.__string_input(80)
                case 2:
                    print("New ID?: ")
                    person_to_modify.id_num = self.__string_input(6)
                    id_flag += 1
                case 3:
                    print("New Street?: ")
                    person_to_modify.street = self.__string_input(100)
                case 4:
                    print("New City?: ")
                    person_to_modify.city = self.__string_input(100)
                case 5:
                    print("New State?: ")
                    person_to_modify.state = self.__string_input(100)
                case 6:
                    print("New Zip Code?: ")
                    person_to_modify.zip_code = self.__string_input(9)
                case 7:
                    # TODO maybe modify services too? add/delete/modify
                    break
                case 8 if isinstance(person_to_modify, Provider):
                    print("New # of Consultations?: ")
                    person_to_modify.num_consultations = self.__int_input(3)
                case 9 if isinstance(person_to_modify, Provider):
                    print("New Total Weekly Fee?: ")
                    person_to_modify.total_wk_fee = self.__int_input(11)
                case 0:
                    break
                case _:
                    print(f"Error: invalid option {option}")
        return

   def test_print(self, dictionary):
        is_member = isinstance(next(iter(dictionary.values())), Member)
        if is_member:
            for id_num, member in dictionary.items():
                print("Name:", member.name)
                print("ID:", member.id_num)
                print("Street:", member.street)
                print("City:", member.city)
                print("State:", member.state)
                print("Zip Code:", member.zip_code)
                print("Services:")
                for service in member.services:
                    print("- Date:", service.date)
                    print("- Provider Name:", service.provider_name)
                    print("- Service Name:", service.service_name)
                print()
        else:
            for id_num, provider in dictionary.items():
                print("Name:", provider.name)
                print("ID:", provider.id_num)
                print("Street:", provider.street)
                print("City:", provider.city)
                print("State:", provider.state)
                print("Zip Code:", provider.zip_code)
                print("Services:")
                for service in provider.services:
                    print("- Date & Time:", service.date_and_time)
                    print("- Member Name:", service.member_name)
                    print("- Member Number:", service.member_number)
                    print("- Service Code:", service.service_code)
                    print("- Fee:", service.fee)
                print()



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

    # float_input as a helper function for recieving float input of length size
    # Privdes reuasble input option with error handling
    #CAREFUL with decimals here! they cound as +1 size
    def __float_input(self, size) -> float:
        number: float
        while True:
            try:
                number = float(self.__string_input(size))
            except ValueError as msg:
                print(f"Error: {msg}", file=sys.stderr)
                print("Please re-enter:", file=sys.stderr)
            else:
                break
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



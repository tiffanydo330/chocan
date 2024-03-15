#from data import Member, Provider  # Importing custom data models
#from schema import MemberSchema, ProviderSchema  # Importing schemas for data serialization
#from typing import Dict, Any  # Importing type hints for data types

from client import *

def main() -> None:
    """
    The main function of the program.
    """

    client = Client()
    client.main_menu_loop()

if __name__ == "__main__":
    main()  # Call the main function if the script is executed directly

import os
import pathlib
from data import Member, Provider, MemberService, ProviderService

# Display total amount of services for the week with the following info for each provider: provider name, provider number, and the amount to be transferred
# Since this data is the same as EFT data, also create EFT files each including provider name, provider number, and the amount to be transferred

# Call this function in main where every you need it to generate Summary Reports and EFT files
def sum_rep_main(providers_dict):
    total_wk_fee = 0
    Dir = make_dir("EFT")
    if (Dir == 0):
        DestPath = pathlib.Path(os.getcwd() + "/EFT/")
        TotalDest = pathlib.Path(os.getcwd() + "/EFT/EFT_Total")
        TotalFD = open(TotalDest, "w")

    for id_num, Prov in providers_dict.items():
        print_format(id_num, Prov)
        if (Dir == 0): 
            EFT_file(DestPath, Prov, id_num, TotalFD)
        total_wk_fee += Prov.total_wk_fee

    print("Totaled fee for every provider:", total_wk_fee)
    if (Dir == 0): 
        TotalFD.write("Total: $" + str(total_wk_fee))
        TotalFD.close()

    return 0

# Create EFT files and write data to them
def EFT_file(DestPath, Prov, id_num, TotalFD):
    Dest = pathlib.Path(str(DestPath) + "/" + str(id_num))

    try: FD = open(str(Dest), "w")
    except:
        print("Error creating file for ID: ", str(id_num))
        return 3

    try: 
        FD.write(Prov.name + "\a" + Prov.id_num + "\a" + str(Prov.total_wk_fee))
        FD.close()
    except:
        print("Error writing data to EFT file ID: ", str(id_num))
        return 2

    try: TotalFD.write(Prov.name + "\a" + Prov.id_num + "\a" + str(Prov.total_wk_fee) + "\n")
    except:
        print("Error creating file directory: ", Dest)
        return 1

    return 0

def print_format(id_num, Prov):
    try:
        print("Name:", Prov.name)
        print("ID:", Prov.id_num)
        print("Fee:", Prov.total_wk_fee)
        print()
        return 0
    except:
        print("Unable to display for provider ID:", id_num)
        return 1

# Creates the EFT directory to store all the EFT files
def make_dir(DirStr):
    try:
        os.makedirs(DirStr, exist_ok=True)
        return 0
    except:
        print("Error creating directory:", DirStr)
        return 1
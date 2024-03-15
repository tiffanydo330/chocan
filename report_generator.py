import os
import pathlib
import json
from data import Member, Provider, MemberService, ProviderService
from datetime import datetime

# Report Generator class for writing provider, member, and service data to .json reports
# Accessed by user via the Manager menu in main
class ReportGenerator:
    def __init__(self):
        pass

    # formatting to be used in provider report method
    def format_provider_field(self, value, length, is_numeric=False):
        if is_numeric:
            value = str(value).zfill(length)
        return str(value)[:length].ljust(length)

    # to generate the provider report and put it into a json file
    def generate_provider_report(self, provider, provider_services):
        if not provider.name or not provider.name.strip() or not provider.name.replace(" ", "").isalpha():  # all reports must at least have the provider name and name must be valid
            print("Invalid provider name. Unable to generate report.")
            return None

        try:
            report_data = {
                "Provider Name": self.format_provider_field(provider.name, 25),
                "Provider Number": self.format_provider_field(provider.id_num, 9, is_numeric=True),
                "Provider Street Address": self.format_provider_field(provider.street, 25),
                "Provider City": self.format_provider_field(provider.city, 14),
                "Provider State": self.format_provider_field(provider.state, 2),
                "Provider Zip Code": self.format_provider_field(provider.zip_code, 5, is_numeric=True),
                "Services": [],
                "Total Number of Consultations": self.format_provider_field(len(provider_services), 3, is_numeric=True),
                "Total Fee for the Week": self.format_provider_field(sum(service.fee for service in provider_services), 10, is_numeric=True)
            }

            # for the services array 
            for service in provider_services:
                service_date = datetime.strptime(service.date, "%m-%d-%Y") if isinstance(service.date, str) else service.date
                service_date_time = datetime.strptime(service.date_and_time, "%m-%d-%Y %H:%M:%S") if isinstance(service.date_and_time, str) else service.date_and_time
                service_data = {
                    "Date of Service": self.format_provider_field(service_date.strftime("%m-%d-%Y"), 10),
                    "Date/Time Data Received": self.format_provider_field(service_date_time.strftime("%m-%d-%Y %H:%M:%S"), 19),
                    "Member Name": self.format_provider_field(service.member_name, 25),
                    "Member Number": self.format_provider_field(service.member_number, 9, is_numeric=True),
                    "Service Code": self.format_provider_field(service.service_code, 6, is_numeric=True),
                    "Fee to be paid": self.format_provider_field(service.fee, 7, is_numeric=True)
                }
                report_data["Services"].append(service_data)

            file_name = f"{provider.name.replace(' ', '_')}.json"
            with open(file_name, 'w') as json_file:
                json.dump(report_data, json_file, indent=4)

            return file_name
        except Exception as e:
            print(f"An error occurred while generating the report for provider {provider.name}: {e}")
            return None
        
    # to generate the provider report and put it into a json file
    def generate_member_report(self, member, member_services):
        if not member.name or not member.name.strip() or not member.name.replace(" ", "").isalpha():  # all reports must at least have the provider name and name must be valid
            print("Invalid provider name. Unable to generate report.")
            return None

        try:
            report_data = {
                "Member Name": self.format_provider_field(member.name, 25),
                "Member Number": self.format_provider_field(member.id_num, 9, is_numeric=True),
                "Member Street Address": self.format_provider_field(member.street, 25),
                "Member City": self.format_provider_field(member.city, 14),
                "Member State": self.format_provider_field(member.state, 2),
                "Member Zip Code": self.format_provider_field(member.zip_code, 5, is_numeric=True),
                "Services": [],
                "Total Number of Consultations": self.format_provider_field(len(member_services), 3, is_numeric=True),
            }

            # for the services array 
            for service in member_services:
                service_date = datetime.strptime(service.date, "%m-%d-%Y") if isinstance(service.date, str) else service.date
                service_data = {
                    "Date of Service": self.format_provider_field(service_date.strftime("%m-%d-%Y"), 10),
                    "Provider Name": self.format_provider_field(service.provider_name, 25),
                    "Service Name": self.format_provider_field(service.service_name, 20),
                }  
                report_data["Services"].append(service_data)

            file_name = f"{member.name.replace(' ', '_')}.json"
            with open(file_name, 'w') as json_file:
                json.dump(report_data, json_file, indent=4)

            return file_name
        except Exception as e:
            print(f"An error occurred while generating the report for provider {provider.name}: {e}")
            return None
        

    #Display total amount of services for the week with the following info for each provider: provider name, provider number, and the amount to be transferred
    # Since this data is the same as EFT data, also create EFT files each including provider name, provider number, and the amount to be transferred

    # Call this function in main where every you need it to generate Summary Reports and EFT files
    def sum_rep_main(self, providers_dict):
        total_wk_fee = 0
        Dir = self.make_dir("EFT")
        if (Dir == 0):
            DestPath = pathlib.Path(os.getcwd() + "/EFT/")
            TotalDest = pathlib.Path(os.getcwd() + "/EFT/EFT_Total")
            TotalFD = open(TotalDest, "w")

        for id_num, Prov in providers_dict.items():
            self.print_format(id_num, Prov)
            if (Dir == 0): 
                self.EFT_file(DestPath, Prov, id_num, TotalFD)
            total_wk_fee += Prov.total_wk_fee

        print("Totaled fee for every provider:", total_wk_fee)
        if (Dir == 0): 
            TotalFD.write("Total: $" + str(total_wk_fee))
            TotalFD.close()

        return 0

    # Create EFT files and write data to them
    def EFT_file(self, DestPath, Prov, id_num, TotalFD):
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

    def print_format(self, id_num, Prov):
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
    def make_dir(self, DirStr):
        try:
            os.makedirs(DirStr, exist_ok=True)
            return 0
        except:
            print("Error creating directory:", DirStr)
            return 1
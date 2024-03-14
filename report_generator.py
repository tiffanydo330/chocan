
import json

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
                service_data = {
                    "Date of Service": self.format_provider_field(service.date, 10),
                    "Date/Time Data Received": self.format_provider_field(service.date_and_time, 19),
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
                service_data = {
                    "Date of Service": self.format_provider_field(service.date, 10),
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
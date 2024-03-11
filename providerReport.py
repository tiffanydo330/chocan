import json
# formatting to be used in provider report method
def format_field(value, length, is_numeric=False):
    if is_numeric:
        value = str(value).zfill(length)
    return str(value)[:length].ljust(length)

# to generate the provider report and put it into a json file
def generate_provider_report(provider, provider_services):
    if not provider.name or not provider.name.strip() or not provider.name.replace(" ", "").isalpha():  # all reports must at least have the provider name and name must be valid
        print("Invalid provider name. Unable to generate report.")
        return None

    try:
        report_data = {
            "Provider Name": format_field(provider.name, 25),
            "Provider Number": format_field(provider.id_num, 9, is_numeric=True),
            "Provider Street Address": format_field(provider.street, 25),
            "Provider City": format_field(provider.city, 14),
            "Provider State": format_field(provider.state, 2),
            "Provider Zip Code": format_field(provider.zip_code, 5, is_numeric=True),
            "Services": [],
            "Total Number of Consultations": format_field(len(provider_services), 3, is_numeric=True),
            "Total Fee for the Week": format_field(sum(service.fee for service in provider_services), 10, is_numeric=True)
        }

        # for the services array 
        for service in provider_services:
            service_data = {
                "Date of Service": format_field(service.date, 10),
                "Date/Time Data Received": format_field(service.date_and_time, 19),
                "Member Name": format_field(service.member_name, 25),
                "Member Number": format_field(service.member_number, 9, is_numeric=True),
                "Service Code": format_field(service.service_code, 6, is_numeric=True),
                "Fee to be paid": format_field(service.fee, 7, is_numeric=True)
            }
            report_data["Services"].append(service_data)

        file_name = f"{provider.name.replace(' ', '_')}.json"
        with open(file_name, 'w') as json_file:
            json.dump(report_data, json_file, indent=4)

        return file_name
    except Exception as e:
        print(f"An error occurred while generating the report for provider {provider.name}: {e}")
        return None

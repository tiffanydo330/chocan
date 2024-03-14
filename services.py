import json

class ServiceManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.services = []
        self.load_services()

    def load_services(self):
        try:
            with open(self.file_path, 'r') as file:
                self.services = json.load(file)
        except FileNotFoundError:
            self.services = []
    
    def add_service(self, service_code, name, cost):
        self.services.append({
            "service_code": service_code,
            "name": name,
            "cost": cost
        })
        self.save_services()

    def remove_service(self, service_code):
        self.services = [service for service in self.services if service['service_code'] != service_code]
        self.save_services()

    def display_services(self):
        for service in self.services:
            print(f"Service Code: {service['service_code']}, Name: {service['name']}, Cost: {service['cost']}")

    def save_services(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.services, file, indent=4)

    #def main():
    #    sm = ServiceManager("services.json")
    #    sm.display_services()
    #
    #if __name__ == "__main__":
    #    main()
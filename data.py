from marshmallow import Schema, fields, post_load
from datetime import datetime

class Person:
    def __init__(self, name, id_num, street, city, state, zip_code):
        self.name = name
        self.id_num = id_num
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code

class Member(Person):
    def __init__(self, name, id_num, street, city, state, zip_code, services):
        super().__init__(name, id_num, street, city, state, zip_code)
        self.services = services

class Provider(Person):
    def __init__(self, name, id_num, street, city, state, zip_code,
                 services, num_consultations, total_wk_fee):
        super().__init__(name, id_num, street, city, state, zip_code)
        self.services = services
        self.num_consultations = num_consultations
        self.total_wk_fee = total_wk_fee

class Service:
    def __init__(self, date):
        self.date = date

class MemberService(Service):
    def __init__(self, date, provider_name, service_name):
        super().__init__(date)
        self.provider_name = provider_name
        self.service_name = service_name

class ProviderService(Service):
    def __init__(self, date, date_and_time, member_name, member_number, service_code,
                 fee):
        super().__init__(date)
        self.date_and_time = date_and_time
        self.member_name = member_name
        self.member_number = member_number
        self.service_code = service_code
        self.fee = fee

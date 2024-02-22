#filename:   data.py
#summary:    This file is responsible for setting up the core class heirarchy that will
#            be used for most(all?) information that is necessary to be stored and
#            managed by the ChocAn system.

# the person class will be responsible for the data that both members & providers share

#import numpy 

from marshmallow import Schema, fields, post_load

class Person:
    def __init__(self, name, id_num, street, city, state, zip_code):
        self.name = name
        self.id_num = id_num
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code

class PersonSchema(Schema):
    name = fields.Str()
    id_num = fields.Str()
    street = fields.Str()
    city = fields.Str()
    state = fields.Str()
    zip_code = fields.Str()

class Member(Person):
    def __init__(self, name, id_num, street, city, state, zip_code, services):
        super().__init__(name, id_num, street, city, state, zip_code)
        self.services = services 

class MemberSchema(PersonSchema):
    services = fields.List(fields.Str())
            
    @post_load
    def make_member(self, data, **kwargs):
        return Member(**data)

class Provider(Person):
    def __init__(self, name, id_num, street, city, state, zip_code, 
            services, num_consultations, total_wk_fee):
        super().__init__(name, id_num, street, city, state, zip_code)
        self.services = services
        self.num_consultations = num_consultations
        self.total_wk_fee = total_wk_fee
class ProviderSchema(PersonSchema):
    services = fields.Nested('ProviderServiceSchema', many=True)
    num_consultations = fields.Integer()
    total_wk_fee = fields.Float()

    @post_load
    def make_provider(self, data, **kwargs):
        return Provider(**data)

class Service:
    def __init__(self, date):
        self.date = date

class ServiceSchema(Schema):
    date = fields.Date(format='%m-%d-%Y')

    @post_load
    def make_service(self, data, **kwargs):
        return Service(**data)

class MemberService(Service):
    def __init__(self, date, provider_name, service_name):
        super().__init__(date)
        self.provider_name = provider_name
        self.service_name = service_name

class MemberServiceSchema(ServiceSchema):
    provider_name = fields.Str()
    service_name = fields.Str()

    @post_load
    def make_member_service(self, data, **kwargs):
        return MemberService(**data)

class ProviderService(Service):
    def __init__(self, date, date_and_time, member_name, member_number, service_code, 
                 fee):
        super().__init__(date)
        self.date_and_time = date_and_time
        self.member_name = member_name
        self.member_number = member_number
        self.service_code = service_code
        self.fee = fee

class ProviderServiceSchema(ServiceSchema):
    date_and_time = fields.DateTime(format='%m-%d-%Y %H:%M:%S')
    member_name = fields.Str()
    member_number = fields.Str()
    service_code = fields.Str()
    fee = fields.Float()

    @post_load
    def make_provider_service(self, data, **kwargs):
        return ProviderService(**data)

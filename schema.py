from marshmallow import Schema, fields, post_load
from data import Member, Provider, MemberService, ProviderService

class PersonSchema(Schema):
    name = fields.Str()
    id_num = fields.Str()
    street = fields.Str()
    city = fields.Str()
    state = fields.Str()
    zip_code = fields.Str()

class MemberSchema(PersonSchema):
    services = fields.List(fields.Nested("MemberServiceSchema"))

    @post_load
    def make_member(self, data, **kwargs):
        return Member(**data)

class ProviderSchema(PersonSchema):
    services = fields.List(fields.Nested("ProviderServiceSchema"))
    num_consultations = fields.Int()
    total_wk_fee = fields.Float()

    @post_load
    def make_provider(self, data, **kwargs):
        return Provider(**data)

class ServiceSchema(Schema):
    date = fields.Date(format="%m-%d-%Y")

class MemberServiceSchema(ServiceSchema):
    provider_name = fields.Str()
    service_name = fields.Str()

    @post_load
    def make_member_service(self, data, **kwargs):
        return MemberService(**data)

class ProviderServiceSchema(ServiceSchema):
    date_and_time = fields.DateTime(format="%m-%d-%YT%H:%M:%S")
    member_name = fields.Str()
    member_number = fields.Str()
    service_code = fields.Str()
    fee = fields.Float()
    num_consultations = fields.Int()
    total_fee = fields.Float()

    @post_load
    def make_provider_service(self, data, **kwargs):
        return ProviderService(**data)

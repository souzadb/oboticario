from flask_marshmallow import Schema
from marshmallow.fields import Str, Int

class DealerSchema(Schema):
    class Meta:
        fields = ["name", "cpf", "email", "password"]

    name = Str()
    cpf = Str()
    email = Str()
    password = Str()
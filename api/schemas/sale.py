from flask_marshmallow import Schema
from marshmallow.fields import Str, Int

class SaleSchema(Schema):
    class Meta:
        fields = ["cod", "value", "date", "cpf", "status"]

    cod = Int()
    value = Int()
    date = Str()
    cpf = Str()
    status = Str()
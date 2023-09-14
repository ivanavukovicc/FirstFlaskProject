from marshmallow import Schema, fields

class IzdavacSchema(Schema):
    id = fields.Integer(dump_only=True)
    ime = fields.String(required=True)
    adresa = fields.String()
    telefon = fields.String()

class BookSchema(Schema):
    id = fields.Integer(dump_only=True)
    naziv = fields.String(required=True)
    autor = fields.String()

from marshmallow import Schema, fields, validate


class UserSchema(Schema):
    name = fields.String(required=True, validate=validate.Regexp(r'^[a-zA-ZА-Яа-я\-]+$'))
    last_name = fields.String(required=True, validate=validate.Regexp(r'^[a-zA-ZА-Яа-я\-]+$'))
    token = fields.String(required=True, allow_none=False)

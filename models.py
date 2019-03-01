from coralillo import Model, fields
from main import engine


class Dog(Model):
    name = fields.Text()
    age = fields.Integer()

    class Meta:
        engine = engine

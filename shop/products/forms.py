
from wtforms import Form, BooleanField, TextAreaField, IntegerField,StringField, PasswordField, validators
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField, FileRequired 

from wtforms.validators import DataRequired,Length

class AddproductForm(Form):
    name = StringField('Name',validators= [Length(min=4, max=25),DataRequired()] )
    gender = StringField('Gender',validators= [Length(min=4, max=25)] )
   
    price = IntegerField('Price',validators= [Length(min=4, max=25)] )
    discount = IntegerField('Discount',validators= [Length(min=4, max=25)] )
    stock = IntegerField('Stock',validators= [Length(min=4, max=25)] )
    discription = TextAreaField('Discription',validators= [Length(min=4, max=25)] )
    color = TextAreaField('Colors',validators= [Length(min=4, max=25)] )

   
    image1 = FileField('Image 1', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg'], 'Images only please')])
    image2 = FileField('Image 1', validators=[ FileAllowed(['jpg', 'png', 'gif', 'jpeg'], 'Images only please')])
    image3 = FileField('Image 1', validators=[ FileAllowed(['jpg', 'png', 'gif', 'jpeg'], 'Images only please')])


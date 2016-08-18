from flask.ext.wtf import Form
from wtforms import StringField, TextField, TextAreaField, BooleanField
from wtforms.validators import Required, DataRequired, Length

class LoginForm(Form):
    openid = TextField('openid', validators = [Required()])
    remember_me = BooleanField('remember_me', default = False)

class EditForm(Form):
    nickname = StringField('nickname', validators=[DataRequired()])
    about_me = TextAreaField('about_me', validators=[Length(min=0, max=140)])
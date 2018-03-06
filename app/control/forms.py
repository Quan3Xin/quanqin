from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, ValidationError #验证信息
from app.models.model import User



class Name_Form(FlaskForm):
    name = StringField('What your name', validators=[DataRequired('plz')],

                       render_kw={
                           "required": "required",
                           "placeholder":  "plase"
                       })
    submit = SubmitField('Submit')

    password = PasswordField('password', validators=[DataRequired(message=u"密码不能为空")])


    def validate_name(self, field):
        account = field.data

        admin = User.query.filter_by(name=account).count()
        if admin == 0:
            raise ValidationError('account invalid')
class Register_Form(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    pwd = PasswordField('pwd', validators=[DataRequired()])
    submit = SubmitField('register')

    def validate_name(self, field):
        account = field.data

        admin = User.query.filter_by(name=account).count()
        if admin is not None:
            raise ValidationError('account invalid')

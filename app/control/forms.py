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


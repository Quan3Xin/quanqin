from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, ValidationError  # 验证信息
from app.models.model import User


class Name_Form(FlaskForm):
    name = StringField('What your name', validators=[DataRequired('plz')],

                       render_kw={
                           "required": "required",
                           "class": "col-sm-2 control-label",
                           "for": "formGroupInputLarge",
                           "placeholder": "请输入你的名字"
                       })
    submit = SubmitField('Submit',
                         render_kw={
                             "class": "dbtn btn-primary btn-lg btn-block"
                         })

    password = PasswordField('password', validators=[DataRequired(message=u"密码不能为空")],
                             render_kw={
                                 "required": "required",
                                 "class": "col-sm-2 control-label",
                                 "placeholder": "请输入密码"
                    })


    def validate_name(self, field):
        account = field.data

        admin = User.query.filter_by(name=account).count()
        if admin == 0:
            raise ValidationError('account invalid')


class Register_Form(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('register')

    def validate_name(self, field):
        account = field.data

        admin = User.query.filter_by(name=account).count()
        if admin != 0:
            raise ValidationError('账号存在')

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, ValidationError  # 验证信息
from app.models.model import User


class Name_Form(FlaskForm):
    name = StringField('What your name', validators=[DataRequired(message=u'内容不能不为空')],
                       # label='请输入用户名',
                       render_kw={
                           "required oninvalid": "setCustomValidity('请输入账号')",
                           "class": "control-label col",
                           "placeholder": "请输入你的名字",
                           "oninput": " setCustomValidity('')"
                       })
    submit = SubmitField('Submit',
                         render_kw={
                             "class": "btn btn-default"
                         })

    password = PasswordField('password', validators=[DataRequired(message=u"密码不能为空")],
                             #    label='请输入密码',
                             render_kw={
                                 "required oninvalid": "setCustomValidity('请输入密码')",
                                 "class": " control-label col",
                                 "placeholder": "请输入密码",
                                 "oninput": "setCustomValidity('')"
                             })

    def validate_name(self, field):
        account = field.data

        admin = User.query.filter_by(name=account).count()
        if admin == 0:
            raise ValidationError('account invalid')


class Register_Form(FlaskForm):

    name = StringField('请输入名字', validators=[DataRequired(message=u'内容不能不为空')],
                       # label='请输入用户名',
                       render_kw={
                           "required oninvalid": "setCustomValidity('请输入账号')",
                           "class": "control-label col",
                           "placeholder": "请输入你的名字",
                           "oninput": " setCustomValidity('')"
                       })
    submit = SubmitField('确定',
                         render_kw={
                             "class": "btn btn-default"
                         })

    password = PasswordField('请输入密码', validators=[DataRequired(message=u"密码不能为空")],
                             #    label='请输入密码',
                             render_kw={
                                 "required oninvalid": "setCustomValidity('请输入密码')",
                                 "class": " control-label col",
                                 "placeholder": "请输入密码",
                                 "oninput": "setCustomValidity('')"
                             })
    def validate_name(self, field):
        account = field.data

        admin = User.query.filter_by(name=account).count()
        if admin != 0:
            raise ValidationError('账号存在')

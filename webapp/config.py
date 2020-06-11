import os


basedir = os.path.abspath(os.path.dirname(__file__))

# Поместите ваш пароль от пользователя linux в .bash_profile, или введите его вручную в USER_PASSWORD
USER_PASSWORD: str = os.environ.get("USER_PASSWORD")


class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, '..', 'webapp.db')}"
    SECRET_KEY = 'asdfiwer593jnbklnsdljf9848hsjkl@33#nv'

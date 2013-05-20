import django
from django.core.validators import MaxLengthValidator
from django.db.models.signals import class_prepared
from longeruserfields.util import get_field_length


FIELDS_TO_UPDATE = ("username", "first_name", "last_name")


def longer_user_fields_signal(sender, *args, **kwargs):
    if (sender.__name__ == "User" and
        sender.__module__ == "django.contrib.auth.models"):
        patch_user_model(sender)
class_prepared.connect(longer_username_signal)


def patch_user_model(model):
    for field_name in FIELDS_TO_UPDATE:
        field = model._meta.get_field(field_name)
        field.max_length = get_field_length(field_name)

    # patch model field validator because validator doesn't change if we change
    # max_length
    for v in field.validators:
        if isinstance(v, MaxLengthValidator):
            v.limit_value = get_field_length(field_name)


from django.contrib.auth.models import User

# https://github.com/GoodCloud/django-longer-username/issues/1
# django 1.3.X loads User model before class_prepared signal is connected
# so we patch model after it's prepared

# check if User model is patched
for field_name in FIELDS_TO_UPDATE:
    field = User._meta.get_field(field_name)
    if field.max_length != get_field_length(field_name):
        patch_user_model(User)
        break

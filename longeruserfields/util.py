from django.conf import settings


FIELDS_LENGTH_SETTINGS = {
    "username": "MAX_USERNAME_LENGTH",
    "first_name": "MAX_FIRSTNAME_LENGTH",
    "last_name": "MAX_LASTNAME_LENGTH"
}


def get_field_length(field_name):
    setting_name = FIELDS_LENGTH_SETTINGS.get(field_name)
    if setting_name and hasattr(settings, setting_name):
        return getattr(settings, setting_name)
    return 255

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re


def postal_code_validation(postal_code):
    if not (re.fullmatch(r"\d\d-\d\d\d", postal_code)):
        raise ValidationError(
            _("%(postal_code)s does not match XX-XXX format"),
            code='postal_error',
            params={'postal_code': postal_code},
        )


def phone_num_valid(phone_num):
    if len(str(phone_num)) != 9:
        raise ValidationError(
            _("%(phone_num)s does not have 9 digits"),
            code='phone_error',
            params={'phone_num': phone_num},
        )

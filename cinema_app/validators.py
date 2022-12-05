from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re


def validate_postal_code(postal_code):
    if not (re.fullmatch(r"\d\d-\d\d\d", postal_code)):
        print(postal_code)
        print('invalid post code')
        raise ValidationError(
            _("%(postal_code)s does not match XX-XXX format"),
            code='postal_error',
            params={'postal_code': postal_code},
        )

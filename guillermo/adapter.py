from allauth.account.adapter import DefaultAccountAdapter
from django.forms import ValidationError


class UsernameMaxAdapter(DefaultAccountAdapter):
    def clean_username(self, username):
        if len(username) > 10:
            raise ValidationError(
                "Please enter an username of maximum 10 characters"
            )
        return DefaultAccountAdapter.clean_username(self, username)

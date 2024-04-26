from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.tokens import PasswordResetTokenGenerator # call PasswordResetTokenGenerator api from django
import six

# token generator class
class AccountActivationTokenGenerator(PasswordResetTokenGenerator): # create AccountActivationTokenGenerator implement PasswordResetTokenGenerator
    def _make_hash_value(self, user, timestamp): 
        return (
            six.text_type(user.pk) + six.text_type(timestamp) + six.text_type(user.is_active)  # generatoken by pk of user, time create token and active status of account
        )
account_activation_token = AccountActivationTokenGenerator()
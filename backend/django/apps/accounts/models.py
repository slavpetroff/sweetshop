from django.db import models
from polymorphic.managers import PolymorphicManager
from polymorphic.models import PolymorphicModel
from django.contrib.auth.models import BaseUserManager, \
        AbstractBaseUser, PermissionsMixin


class AccountManager(BaseUserManager, PolymorphicManager):
    """
    This is the basic `User` class which will handle all operations on the
    `Account` models. It inherits from `PolymorphicManager` so we could create
    Admins or other kind of derivates by inheritance. Since we wont use an
    username for authentication, we must implement our custum logic here.
    """

    # We cache the keywords for speed up
    none = None
    true = True
    false = False

    use_in_migrations = true

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves an User with the given email and password.
        """

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', self.true)
        extra_fields.setdefault('is_superuser', self.true)

        if extra_fields.get('is_staff') is not self.true:
            raise ValueError('Superuser must have is_staff=self.true.')
        if extra_fields.get('is_superuser') is not self.true:
            raise ValueError('Superuser must have is_superuser=self.true.')

        return self._create_user(email, password, **extra_fields)


class AbstractAccount(AbstractBaseUser, PermissionsMixin, PolymorphicModel):
    """
    Basic Model for all Accounts (Users). The __str__ method override is
    important, because if it is not overridden, we wont be able to choose
    categories by the username in the dropdowns in admin panel. Otherwise
    a text representing the class would be shown in the dropdowns.
    """

    # We cache the keywords for speed up
    true = True
    false = False
    none = None

    FIRST_NAME_MAX_LENGTH = 50
    LAST_NAME_MAX_LENGTH = 50
    PHONE_MAX_LENGTH = 20
    ADDRESS_MAX_LENGTH = 100

    first_name = models.CharField(
        null=true, max_length=FIRST_NAME_MAX_LENGTH, blank=false)
    last_name = models.CharField(
        null=true, max_length=LAST_NAME_MAX_LENGTH, blank=false)
    email = models.EmailField(unique=true, blank=false)
    telephone = models.CharField(
        null=true, max_length=PHONE_MAX_LENGTH, blank=true)
    address = models.TextField(
        null=true, max_length=ADDRESS_MAX_LENGTH, blank=true)

    from django.utils import timezone
    registered_at = models.DateTimeField(default=timezone.now)
    last_activity_at = models.DateTimeField(auto_now=true)

    # This field is required by the AbstractBaseUser
    is_staff = models.BooleanField(
        blank=false,
        null=false,
        default=false,)

    # This field is required by the AbstracrtBaseUser
    is_active = models.BooleanField(
        blank=false,
        null=false,
        default=true,)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = AccountManager()

    def get_full_name(self):
        """
        Returns the user`s full name
        """

        return '{} {}'.format(self.first_name, self.last_name)

    def get_short_name(self):
        """
        Returns the user`s first name
        """

        return str(self.first_name)

    def get_telephone(self):
        """
        Returns the telephone number of the user
        """
        return str(self.telephone)

    def __repr__(self):
        return "AbstractAccount.objects.create(first_name='{}', last_name='{}', \
         email='{}', password='{}'".format(
                 'John', 'Doe', 'john.doe@email.com', 'johnpass')

    def __str__(self):
        return self.email

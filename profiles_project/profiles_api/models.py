from django.db import models
from profiles_project import settings
# below ar ethe standard imports that allow us to modify standard user model
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager

# Create your models here.


class UserProfileManager(BaseUserManager):
    """
    Base user manager
    """
    # creating a user - fields requied are email and name. In case of password - it will default to None if not typed in
    def create_user(self,email,name,password=None):
        """
        create a new user
        """
        # if email was not passed
        if not email:
            raise ValueError("User has to have am email address")
        # noramlizing email - second part of email will have smaller letters
        email = self.normalize_email(email)
        # setting up model
        user = self.model(email=email,name=name)
        # enrypting password
        user.set_password(password)

        # saving the model
        user.save(using=self._db)

        # returning the newly created user
        return user

    def create_superuser(self,email,name,password):
        # create and saving a new superuser with given details
        # self is automatically passed in any class function
        # so if it is called from some other part of the code - we do not have to specified the self as it is passed
        user = self.create_user(email,name,password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)
        return user

# we are inheriting elements from what is in ()
class UserProfile(AbstractBaseUser,PermissionsMixin):
    """
    Database model for users  in the system
    """
    # max email is 255, it should be unique in the database
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    # something for permission system
    is_active = models.BooleanField(default=True)
    # below is telling us if someone is from stuff and should be able to see admin page
    is_staff = models.BooleanField(default = False)

    objects = UserProfileManager()

    # we are overwritting normal way of authentication
    # user will have to type in email instead of name
    USERNAME_FIELD='email'

    # user at least have to specify email and name
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """
        Retrieve full name of user
        """
        return self.name

    def get_short_name(self):
        """
        Retrieveing short name
        """
        return self.name

    def __str__(self):
        """
        Returning string representation of user
        """
        return self.email 


class ProfileFeedItem(models.Model):
    # keeping up status update
    # we are auth user model to not have it hardcoded so that it can be changed automatically
    user_profile = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    # adding automatically time of registration
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status_text
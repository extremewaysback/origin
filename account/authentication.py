#Create an authentication backend to let users authenticate in our site using their e-mail address instead of their username

from django.contrib.auth.models import User

class EmailAuthBackend(object):
    '''Authenticate using e-mail account'''
    def authenticate(self,username=None,password=None):
        '''Takes user credentials as parameters. Return true if the user has been authenticated, or false otherwise'''
        try:
            user=User.objects.get(email=username)#authenticate through the email
            #build-in check_password() method of the User model handles the password hashing to compare the given password againt the password stored in the database
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None
            
    def get_user(self,user_id):
        '''takes a user ID parameter and has to return a User object'''
        try:
            return User.objects.get(pk=user_id)
        except User.DoesnotExist:
            return None
 
               
                             
AUTHENTICATION_BACKENDS=(
           'django.contrib.auth.backends.ModelBackend',#used to authenticate with username and password
           'account.authentication.EmailAuthBackend',#custom EmailAuthBackend class         
)     
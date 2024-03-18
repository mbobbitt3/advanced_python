"""
This code is only meant to test auth.py 
Modify to test your code to make sure it complies
with the assignment
"""
import auth

try:
    auth.authenticator.add_user("joe", "aaawwwww1")
    print ("you are ok")
except auth.PasswordTooShort:
    print('password is too short')
except auth.PasswordMissingNumber:
    print("password missing a number")
except auth.PasswordMissingSpecialChar:
    print("password missing a Special CHar")


Sign Up With Extra Fields
So, what if I wanted to also get the user’s email address and full name upon sign up?

This strategy will work if you are using the Django user as it is, or if you have extended it using the AbstractUser or AbstractBaseUser. If you extended the Django user using a Profile model, hold tight, we will get there too.

Now we need a step further: we have to extend the UserCreationForm !!

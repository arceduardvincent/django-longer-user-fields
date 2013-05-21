**django-longer-user-fields** provides a migration and a monkeypatch to make the django auth.user fields longer, instead of the arbitrarily short 30 characters.

It allows you to update the length of the ``username``, ``first_name`` and ``last_name`` fields.
It's usefull only if you are using Django 1.4 or less. If you are using Django 1.5+ you should create a [custom user model](https://docs.djangoproject.com/en/dev/topics/auth/customizing/#auth-custom-user).

It's designed to be a simple include-and-forget project that makes a little headache go away.  Enjoy, and pull requests welcome!


Usage
=====

Step 1. Install django-longer-user-fields 
-----------------------------------------

	pip install django-longer-user-fields

You will also need to install [South](https://pypi.python.org/pypi/South/) to use the migration. 

 	pip install south




Step 2. Add ``longeruserfields`` to your installed apps
-----------------------------------------------------

Add ``longeruserfields`` to the top of your ``INSTALLED_APPS` in settings.py


	INSTALLED_APPS = ("longeruserfields",) + INSTALLED_APPS


Step 3. (Optional) Specify custom fields lengths
-------------------------------------------------

If you want to specify a custom length, add it to settings.py. The default is 255 characters.


	MAX_USERNAME_LENGTH = 100  # optional, default is 255.
	MAX_FIRSTNAME_LENGTH = 80  # optional, default is 255.
	MAX_LASTNAME_LENGTH = 80   # optional, default is 255.


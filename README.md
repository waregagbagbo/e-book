# e-book
Nutritions Academy is an institution where you can get professional education and reliable consultation by our team of certified teachers and instructors.

 Built with Django.


Features

Up-to-date dependencies
Database: sqlite
UI-Ready app, Django Native ORM
Session-Based authentication, Forms validation

Set Up Database

$ python manage.py makemigrations
$ python manage.py migrate

Start the app

$ python manage.py runserver
At this point, the app runs at http://127.0.0.1:8000/.


et Up for Windows
Install modules via VENV (windows)

$ virtualenv env
$ .\env\Scripts\activate
$ pip3 install -r requirements.txt

Set Up Database

$ python manage.py makemigrations
$ python manage.py migrate

Start the app

$ python manage.py runserver
At this point, the app runs at http://127.0.0.1:8000/.


point_right Create Users
By default, the app redirects guest users to authenticate. In order to access the private pages, follow this set up:

Start the app via python manage.py runserver
Access the registration page and create a new user:
http://127.0.0.1:8000/register/
Access the sign in page and authenticate
http://127.0.0.1:8000/login/

sparkles Code-base structure
The project is coded using a simple and intuitive structure presented below:

< PROJECT ROOT >
   |
   |-- core/                               # Implements app configuration
   |    |-- settings.py                    # Defines Global Settings
   |    |-- wsgi.py                        # Start the app in production
   |    |-- urls.py                        # Define URLs served by all apps/nodes
   |
   |-- apps/
   |    |
   |    |-- home/                          # A simple app that serve HTML files
   |    |    |-- views.py                  # Serve HTML pages for authenticated users
   |    |    |-- urls.py                   # Define some super simple routes  
   |    |
   |    |-- authentication/                # Handles auth routes (login and register)
   |    |    |-- urls.py                   # Define authentication routes  
   |    |    |-- views.py                  # Handles login and registration  
   |    |    |-- forms.py                  # Define auth forms (login and register) 
   |    |
   |    |-- static/
   |    |    |-- <css, JS, images>         # CSS files, Javascripts files
   |    |
   |    |-- templates/                     # Templates used to render pages
   |         |-- includes/                 # HTML chunks and components
   |         |    |-- navigation.html      # Top menu component
   |         |    |-- sidebar.html         # Sidebar component
   |         |    |-- footer.html          # App Footer
   |         |    |-- scripts.html         # Scripts common to all pages
   |         |
   |         |-- layouts/                   # Master pages
   |         |    |-- base-fullscreen.html  # Used by Authentication pages
   |         |    |-- base.html             # Used by common pages
   |         |
   |         |-- accounts/                  # Authentication pages
   |         |    |-- login.html            # Login page
   |         |    |-- register.html         # Register page
   |         |
   |         |-- home/                      # UI Kit Pages
   |              |-- index.html            # Index page
   |              |-- 404-page.html         # 404 page
   |              |-- *.html                # All other pages
   |
   |-- requirements.txt                     # Development modules - SQLite storage
   |
   |-- .env                                 # Inject Configuration via Environment
   |-- manage.py                            # Start the app - Django default start script
   |
   |-- ************************************************************************


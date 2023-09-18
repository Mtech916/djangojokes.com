# Notes

Status Codes
Here are the most common status codes returned by a web server along with their meanings:

200 OK.
301 Moved Permanently. The file used to be at this URL, but it isn’t anymore.
304 Not Modified. The file hasn’t changed from the last time it was sent to the client.
400 Bad Request. Something about the way the request was made has baffled the web server.
401 Unauthorized. You have to be logged in to access this file.
403 Forbidden. You can’t have this even if you are logged in.
404 Not Found. There is no file here.
500 Internal Server Error. Something went wrong on the server.
503 Service Unavailable. The web server is down or overloaded.

## To create a Virtual Environment:

- Navigate to root directory
- Terminal Command: python -m venv .venv

### To activate a venv:

- Terminal Command: source .venv/bin/activate

### Install special packages:

- Terminal Command: pip install <package> (i.e. django)

### Select Python Interpreter:

- From View menu, select Command Palette enter: "Python: Select Interpreter"
  - if no venv option given, it seems to be because the workspace isn't within the root file
- Select the version of Python your program requires and should also see the .venv within this option

### Creating a New Django Project

1 - Create a new project directory using this command: 'django-admin startproject <package_name> .' - The dot (.) at the end of django-admin startproject package_name . indicates that the project should be created in the current directory. If you leave it off, a new project directory will be created with a nested folder that has the same name, which can be confusing.

- For Example:

        django-admin startproject hello_django .
        This command creates a project like this:
        - hello_proj * project folder
            - hello_django * The python package for your new project
                - __init__.py * An empty file that turns the directory into a package.
                - asgi.py * An entry-point for ASGI-compatible web servers - not needed for this bootcamp
                - settings.py * The project's settings file
                - urls.py The projects root URL configuration file, also known as a URLConf file.
                - wsgi.py * An entry-point for WSGI-compatible web servers. It's the interface betwn the web server and the python/django app you create.
                - manage.py * The Django admin file for your project.

- To start the server, run this command:

  - python manage.py runserver

- Django Template Variable

  - {{ variable_name }}

- Django Template Tag
  - {% tag_name %}

### The shell when used within a Virtual Environment

    - python manage.py shell
    * Good to use in order to import the settings file and review/look at different variable settings in the file
        >>> from hello_django.settings import *
        >>> BASE_DIR * Webucator/Django/projects/hello_proj'
        >>> LANGUAGE_CODE * 'en-us'
        >>> ROOT_URLCONF * 'hello_django.urls'

### Creating a New App within your new Project folder

1 - Create the scaffolding of the app by running : 'python manage.py startapp <app_name>'
2 - Add the new app to the INSTALLED_APPS list in settings.py
3 - Create one or more views
4 - Configure URLs
5 - Create any necessary templates for the HTML code that renders the page.

- For Example:

  - python manage.py startapp packages
  - In settings.py: add the app to the INSTALLED_APPS variable list
  - Open pages/views.py
    - Replace the default render import with this import statement:
      -- from django.views.generic import TemplateView --
    - Below that add the following class which inherits from TemplateView
      -- class HomePageView(TemplateView):
      template_name = 'home.html'
  - Open hello_django/urls.py:
    - Add your own URL configurations to the urlpatterns list
      -- urlpatterns = [
      path('admin/', admin.site.urls),
      path('', HomePageView.as_view()), * This is the one that is added
      ]
    - Also add this import below the existing: "from pages.views import HomePageView"
  - Open settings.py:

    - Locate TEMPLATES variable
    - find the 'DIRS': [] and 'APP_DIRS': True

    - Create a new templates folder in the hello_proj directory

      - Within this folder, create a pages folder
      - and within this folder create a home.html file with starter HTML

    - Back in settings.py:
      - within the 'DIRS': add [BASE_DIR / 'templates'],

  **_ All of the above example will tell django where to look for the view page that is being requested _**

  - Open pages/views.py again:

    - change the class HomePageView to this:
      -- class HomePageView(TemplateView):
      template_name = 'pages/home.html'

  - Next, create a \_base.html file that will be able to use to extend actual view pages
    -- within templates folder - create the \_base.html file and put the home.html code into it but include some specific Django tags
    -- <title>{% block title %}{% endblock %} | Hello, Django!</title>
    </head>
    <body>
    <h1>{% block header %}Hello, Django!{% endblock %}</h1>
    <main>
    {% block main %}{% endblock %}
    </main>
  - Then replace the contents of the original home.html with this below
    -- {% extends '_base.html' %}

                 {% block title %}Home{% endblock %}
                 {% block header %}Welcome!{% endblock %}
                 {% block main %}
                     <p>Thank you for visiting our site!</p>
                 {% endblock %}

  - Create a urls.py file within the pages directory like so:
    -- from django.urls import path

         from .views import HomePageView

         app_name = 'pages' * This creates a namespace to avoid conflicts when paths from different apps within project have  same name.
         urlpatterns = [
             path('', HomePageView.as_view(), name='homepage'),
         ]

  - Modify the urls.py file within hello_django directory:
    -- import the include method from django.urls:
    from django.urls import path, include
    -- Remove the line of code importing the HomePageView
    -- Replace: path('', HomePageView.as_view()), - with: path('', include('pages.urls')),

  ### To create a new view or in this case an About Us page

        - create the view in pages/views.py
            ex: class AboutUsView(TemplateView):
                    template_name = 'pages/about_us.html'

        - make a new template within templates/pages/about_us.html
            ex: {% extends "_base.html" %}

                {% block title %}About Us{% endblock %}
                {% block header %}About Us{% endblock %}
                {% block main %}
                <p>Very interesting information about us!</p>
                {% endblock %}

        - Configure the URL in pages/urls.py
            1st - import AboutUsView: from .views import AboutUsView, HomePageView *this one already present
            2nd - path('about-us/', AboutUsView.as_view(), name='about-us'),
            Full Ex: from django.urls import path

                     from .views import AboutUsView, HomePageView

                     app_name = 'pages'
                     urlpatterns = [
                         path('', HomePageView.as_view(), name='homepage'),
                         path('about-us/', AboutUsView.as_view(), name='about-us'),
                     ]

## Creating a New Project

- From Root folder/directory

  - Create / Save Workspace as...
  - Create git repo from github.com
  - Add a README.md
  - Include a .gitignore file
  - clone the repo
  - Update the README.md file
  - perform 1st git commit
  - push initial commit

  - set up Virtual Environment
    **_ python -m venv .venv _**

  - Select View Menu in VS Code, select Command Palette
  - Enter **_ Python:Select Interpreter _** and choose the .venv option
  - if need to manual activate Virtual Environ. \*\*\* source .venv/bin/activate

  1 - From projects/djangojokes.com folder
  **_ django-admin startproject djangojokes . _** - Becomes the root project folder - Add any files I don't want kept within git version control to the .gitignore file
  2 - Add a Base Template - Create this \_base.html in the djangojokes.com/templates folder
  3 - Djangojokes/settings.py - 'DIRS': [BASE_DIR / 'templates'],
  **_ Commit changes _**

### Creating a pages App

    1 - Create the scaffolding:
        *** python manage.py startapp app_name ***
    2 - Add new app to the INSTALLED_APPS list
    3 - Create one or more Views
    4 - Configure URLs
    5 - Create and update the needed templates
        ex: templates/pages/home.html
            templates/pages/about_us.html
        * both templates extend _base.html
    **_ Commit changes _**

### Creating the Jokes App

    Scaffolding: From projects/djangojokes.com - root folder
    *** python manage.py startapp jokes
    Add jokes to INSTALLED_APPS in djangojokes.com/settings.py
        ex: # Local apps
            'jokes.apps.JokesConfig',
            'pages.apps.PagesConfig',
    Create a urls.py file within jokes/ folder
        ex: from django.urls import path

            app_name = 'jokes'
            urlpatterns = []
    Update the root folder's urls.py to hand off paths to jokes URLConf file:
        ex: from django.contrib import admin
            from django.urls import path, include

            urlpatterns = [
                path('admin/', admin.site.urls),
                path('jokes/', include('jokes.urls')),
                path('', include('pages.urls')),
            ]
    **_ Commit Changes _**

    #### Models

        - In order for the sqlite3 database or any others to initialize you have to migrate them
            *** python manage.py migrate
                - This migrates all the admin, auth, contenttypes, sessions to initalize the database
        1 - From jokes/models.py

            from django.db import models

            class Joke(models.Model):
                question = models.TextField(max_length=200)
                answer = models.TextField(max_length=100, blank=True)
                created = models.DateTimeField(auto_now_add=True)
                updated = models.DateTimeField(auto_now=True)

                def __str__(self):
                    return self.question
        2 - Since models have been changed, need to make new migration files, to do this:
            *** python manage.py makemigrations ***
            - Now run: *** python manage.py migrate *** ; again to initialize the DB with jokes

        **_ Commit Changes _**

    #### Types of Views

    Using TemplateView to create the homepage, TemplateView is class based and easier for development:
        - ListView – A view for listing objects (records in a queryset).
        - DetailView – A view for displaying details about an object (one retrieved from a queryset).
        - CreateView – A view for creating a new object.
        - UpdateView – A view for updating an object.
        - DeleteView – A view for deleting an object.

    #### Creating a ListView

    1 - Open jokes/views.py in your editor and delete the current contents.
    2 - Import ListView: *** from django.views.generic import ListView ***
    3 - Import the Joke model from models.py: *** from .models import Joke ***
    4 - Create a JokeListView view that inherits from ListView:
            class JokeListView(ListView):
                model = Joke
    5 - Configure the new path to the new view: Open jokes/urls.py
    6 - Import the JokeListView view from views.py: *** from .views import JokeListView ***
    7 - Add a new path to urlpatterns to JokeListView.as_view() at '': *** path('', JokeListView.as_view(), name='list'), ***
        - Because of the way the Class JokeListView(ListView) is written without a template name attribute, Django infers a name for the file like this app_name/model_list.html, for for JokesListView it would look like this jokes/joke_list.html
    8 - Create a jokes folder within templates/jokes: joke_list.html
        ex:
            {% extends "_base.html" %}

            {% block title %}Jokes{% endblock %}
            {% block main %}
            <h2>Jokes</h2>
            <ul class="list-group list-group-flush mb-3">
                {% for joke in joke_list %}
                <li class="list-group-item">{{ joke.question }}</li>
                {% endfor %}
            </ul>
            {% endblock %}

        **_ Commit Changes _**




# Wavey 

## Introduction
Wavey Blog is a website built in Django using Python, JavaScript, CSS and HTML. It enables users to create and share music production techniques through tutorial-style posts with other users from around the world. It is targetted towards users who enjoy making electronic music and would like to share their knowledge with others. Once users have registered and created a profile, they have the ability to create posts, as well as like and comment on others. They can upload images and videos for use on their posts, link their personal youtube accounts and other social websites.

The site provides role based permissions for users to interact with a central dataset. It includes user authentication, email validation, and Full CRUD functionality for Posts and User Profiles.

![Screenshot of homepage]()

[View the live website on Heroku]()

Please note: To open any links in this document in a new browser tab, please press CTRL + Click.

## Table of Contents
* [User Experience Design (UX)](#UX)
    * [The Strategy Plane](#The-Strategy-Plane)
        * [Site Goals](#Site-Goals)
        * [Epics](#Epics)
        * [User Stories](#User-Stories)
    * [The Scope Plane](#The-Scope-Plane)
    * [The Structure Plane](#The-Structure-Plane)
        * [Opportunities](#Opportunities)
    * [The Skeleton Plane](#The-Skeleton-Plane)
        * [Wireframes](#Wireframe-mockups)
        * [Database Schema](#Database-Schema)
    * [The Surface Plane](#The-Surface-Plane)
* [Features](#features)
* [Future Enhancements](#future-enhancements)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

## UX
### The Strategy Plane
*  Wavey is intended to be a friendly community site for users to create and share their own music production techniques with others. Users will also be able to find posts created by other users from around the world. The graphical elements and overall design of the site provide a clear and concise environment for them to focus their attention on learning.

##### The Sites Ideal User
* Music producer of any level looking to share their favourite tips, tricks and techniques with others
* Someone looking to expand their production knowledge
* Someone looking for inspiration for new things to try when creating
* Someone looking to build their social media following

#### Site Goals

* To provide users with a place to become inspired
* To provide users with a place to share their own tips and ideas
* To provide users with a place to discover new techniques and be inspired

#### Epics

8 Epics were created which were then further developed into 38 User Stories. The details on each epic, along with the user stories linked to each one can be found in the project kanban board [here](https://github.com/YesCoops/wavey-blog/projects/1)

1. Initial Django setup [#1](https://github.com/YesCoops/wavey-blog/issues/1)
2. User Profile [#2](https://github.com/YesCoops/wavey-blog/issues/2)
3. User login [#3](https://github.com/YesCoops/wavey-blog/issues/3)
4. User posts [#5](https://github.com/YesCoops/wavey-blog/issues/5)
5. Post search [#6](https://github.com/YesCoops/wavey-blog/issues/6)
6. Post viewing [#7](https://github.com/YesCoops/wavey-blog/issues/7)
7. Post interaction [#8](https://github.com/YesCoops/wavey-blog/issues/8)
8. Site Owner objectives [#4](https://github.com/YesCoops/wavey-blog/issues/4)


### User Stories

From the Epics, 38 User stories were developed. Each story was assigned a classification of Must-Have, Should-Have, Could-Have or Won't Have. Each story was also assigned user story points, based on my best estimation for the time/difficulty of completing each story. A combination of being new to story estimation, inexperience with Django and time constraints during development left me completing 61 story points from the initial total of 131. From the initial 131 points, 82 were for Could Have stories. A number of these stories were created based on an ideal scenario of building out the project whilst I knew in the time available it would be unlikely I would complete those stories. I will however revisit them at a later time for a redevelopment of the project. The full list of User Stories, seperated by those completed and those pushed to a future release is available on the project [kanban board](https://github.com/YesCoops/wavey/projects/1).

These are the user stories that were completed within the projects first release, by Epic.

1. Initial Django setup
		
2. User Profile
	
3. User login
	
4. User posts
	
5. Post management

6. Post search

7. Post viewing

8. Post interaction

9. Site owner objectives

	
### The Scope Plane

**Features planned:**
* User Profile - Create, Read, Update and Delete
* Posts - Users can create, read, update and delete their own posts
* Other Users posts - Users can read, like, and comment on other Users' posts
* Profiles - Users can view other user profiles
* Users can login to their account, change their password or their email
* Users can reset their password if they forget it
* Users can logout of their account
* Users need to be registered and logged in to create and like posts and access other users profiles.
* Responsive Design - the site needs to be fully responsive to cover a wide spectrum of screen sizes


### The Structure Plane

User Story:

> US#13 - Create a User Account - As a User I can create an account so that I can create, save and like posts

Acceptance Criteria:
* Given that I am an unregistered User, when I access the Site, then I can register as a User
* Given that I am an unregistered User, when I am on the user registration page and input a valid Username, email address and password, then the system creates me an account
* Given that I am a registered User, when I am logged into my account, then I can create my own post and see what posts I have saved
* Given that I am a registered user, When I am logged into my account, then I do not see the register button

Implementation:
* Clearly accessible call to action on homepage to register for an account
* Clearly accessible link to login or register within main navigation bar
* Easy to use User registration process
* Clear UX design, prevent unnecessary links to register as a user, if user is already logged in.

User Story:

> US#14 - Users can view their profile - As a user I can see what is in my profile so that I understand what other users can see about my profile

Acceptance Criteria:
* Given that I am logged in to my account, when I can select the option to view my profile, then I see how my profile is displayed to to other users
* Given that I am logged in to my account, when I select a username associated to a post, then I am directed to their full profile page

Implementation:
* Prevent information appearing on users' profile that other users are not allowed to see such as account information
* If information is required to be displayed that other users can not see, clearly label that information so users are aware that others can not see it.

User Story:

> US#15 - Users can edit their profile - As a User I can edit my profile so that I can keep my information up to date

Acceptance Criteria:
* Given that I am logged into my account, when I am viewing my profile, then I should be able to edit those details
* Given that I am logged into my account, when I click on the edit profile button, then I am taken to the relevant page to do so
* Given that I am not logged in to my account, when I go to any profile page, then I do not see the edit profile button
* Given that I am not logged in to my account, when I try and go directly to mine or somebody's edit profile page through their URL, then I get redirected to the login page

Implementation:
* Provide a clearly accessible button on a users profile for the profile owner only, so they can edit their profile
* Provide a simple and clear edit profile form, linked from the edit profile button

User Story:

> US#16 - Users can delete their profile - As a User I can delete my profile so that I can remove my data and posts at my request

Acceptance Criteria:
* Given that I am a registered User, when I am logged in to my account, then I have the option to delete my account
* Given that I am a registered User, when I click on the option to delete my account, then I have to confirm that I wish to do so
* Given that I am a registered User, when I have confirmed that I wish to delete my account, then my profile and all data associated with it is deleted
* Given that I am a registered User, when the account is full deleted, then I receive a confirmation that this action has taken place


Implementation:
* Provide users with an easily accessible option to delete their account
* Provide users with a secure confirmation process to confirm account deletion requests to prevent accidents
* Link all user created elements so that when a user deletes their account, all associated records are deleted.
* Provide the user with confirmation that their account and associated records have been deleted when requested.



#### Opportunities

Arising from user stories
| Opportunities | Importance | Viability / Feasibility
| ------ | :------: | :------: |
| ** Provide users the ability to create an account ** | 5 | 5 |
| ** Provide users the ability to create posts ** | 5 | 5 |
| ** Provide users the ability to edit posts ** | 5 | 5 |
| ** Provide users the ability to view posts ** | 5 | 5 |
| ** Provide users the ability to delete posts ** | 5 | 5 |
| ** Provide users the ability to edit their account ** | 5 | 5 |
| ** Provide users the ability to view other accounts ** | 5 | 5 |
| ** Provide users the ability to delete their account ** | 5 | 5 |
| ** Provide users the ability to save a post ** | 3 | 5 |
| ** Provide users the ability to access the site on any device ** | 5 | 5 |
| ** Provide users the ability to search the site for posts ** | 4 | 5 |

### The Skeleton Plane
#### Wireframe mock-ups

Wireframes were produced for each major page for desktop, mobile and tablet devices. As the site will be fully responsive, no matter the device size the user is viewing the site on, it will display accordingly.


![Home Page Wireframe]()


![Post Detail Desktop Wireframe]()


![User Profile Desktop Wireframe]()


#### Database Schema


![Database Schema Diagram]()

### The Surface Plane

#### Design


##### Typography 

##### Images



## Features
#### Home page


![Home Page]()

#### Navigation Bar
The main navigation bar appears at the top of the page, clearly displaying the main navigational links users would require.

![Logged in User Nav Bar]()

A secondary user menu is available to users who are logged into the site, users who are not logged in receive a login/register link in its place

![logged in user nave bar user menu open]()

The navigation bar and the user menu are fully responsive, adapting to narrower devices by appearing from the right hand side of the screen when the menu button is pressed.

![mobile user menu open]()

#### Footer
A common footer is utilised through out the site to encourage users to visit the social media sites of the main site. They currently direct users to the generic social media sites, all external links open in a new tab.

![footer]()


#### Post Cards

##### Standard Post Card
![Standard Post Card]()

##### Liked Post Card
![Liked Post card]()

#### User Profile

![Owner Profile Page]()

Users have access to their information by quickly visiting this page. Other users who don't own the visited profile page will also have access to other social accounts of the User. 

#### Edit Profile Page
Users have the ability to edit their profiles on the site. The edit profile page is clearly laid out, and informs the user of the characters remaining for each field.

![Edit profile page]()

#### Create/Edit Post Page
Users have the ability to create and edit their posts. The create and edit post page is clearly laid out and with the inclusion of the TinyMCE widget, easily modified if necessary. 

##### Post Form
![Post Form]()

#### Access to Edit Post and Delete Post Functionality
Only the users that create the post can edit it or delete it. If the authorised user is the post author, then the edit recipe and delete post buttons will appear in the masthead of that page.

##### Own post detail card
![Own post detail card]()


## Future Enhancements


## Testing

### Testing Strategy
I utilised a manual testing strategy for the development of the site. A full detailed breakdown of the testing procedures and methodology can be found in the testing.md file [here]().
Seperate to the functionality testing of the site, and the testing of the code, User Story tests were implemented to ensure that the acceptance criteria of the user stories listed above were met. 

#### Testing Overview

Testing was divided into different sections to ensure everything was tested individually with test cases developed for each area.

A full detailed breakdown of the testing procedures and methodology can be found in the testing.md file [here]()

#### Validator Testing


#### Notable Bugs


Development bugs: 

ISSUE - Register form was returning ValuError as didn't return HttpResponse object when invalid data was input to create a User. 
FIX - In register function the render return was incorrectly indented when the if statement wasn't met. Amending this resolved the issue and user validation was restored.

ISSUE - When submitting a new post an integrity error for a duplicate primary key was being shown. The duplicate being created was an empty string, causing an error for the super().save() method when calling the form_valid function. 
FIX - Creating a save function in the Post model which looked at the newly-created slug, stripping any empty space and replacing with a hyphen, then calling the super().save() resolved the issue.

ISSUE - When TinyMCE widget was installed in the Create Post view, when you tried to submit a post with all required fields filled the submit request was not working. 
FIX - Setting the content CharField in the Post model to blank="null" resolved the issue. 

ISSUE - Featured image field was not uploading related media to cloudinary when creating a Post, thus not replacing the masthead placeholder image as desired. 
FIX - Adding the necessary enctype="multipart/form-data" to the relevant forms sent images to cloudinary and therefore to the related post.

 

#### Technologies Used

* Python
    * The following python modules were used on this project:
        * cloudinary==1.29.0
        * dj-database-url==0.5.0
        * dj3-cloudinary-storage==0.0.6
        * Django==3.2
        * django-allauth==0.48.0
        * gunicorn==20.1.0
        * oauthlib==3.2.0
        * psycopg2==2.9.3
        * sqlparse==0.4.2

* Django
    * Django was used as the main python framework in the development of this project
    * Django AllAuth was utilised to provide enhanced user account management functionality.
* Heroku
    * Was used as the cloud based platform to deploy the site on
* Heroku PostgreSQL
    * Heroku PostgreSQL was used as the database for this project during development and in production.
* JavaScript
    * Custom JavaScript was used for the timeout of system messages presented.
* Bootstrap 5.01
    * Bootstrap was used for general layout and spacing requirements for the site.
* Font Awesome
    * Was used for access to several icons for different sections where icons were appropriate.
* CSS
    * Custom css was written for areas on the site to implement custom styling.
* Jinja/Django Templating
    * Jinja/Django templating language was utilised to insert data from the database into the sites pages. It was also utilised to perform queries on different datasets.
* HTML
    * HTML was used as the base language for the templates created for the site.
* TinyMCE
    * Used in the textareas on site where instructed to allow posts to contain external links to images and audio. 
* Summernote
    * Summernote was utilised in the inital stages of the site for use in the admin area. However, as Summernote only accepts images as its media capabilities, it was replaced for the front-end. 

#### Packages Used


#### Resources Used


##### Other Libraries Used

## Deployment

The site was deployed via Heroku, and the live link can be found here - [Wavey Blog]()

### Project Deployment

To deploy the project through Heroku I followed these steps:
* Sign up / Log in to [Heroku](https://www.heroku.com/)
* From the main Heroku Dashboard page select 'New' and then 'Create New App'
* Give the project a name - I entered wavey-blog and select a suitable region, then select create app. The name for the app must be unique.
* This will create the app within Heroku and bring you to the deploy tab. From the submenu at the top, navigate to the resources tab.
* Add the database to the app, in the add-ons section search for 'Heroku Postgres', select the package that appears and add 'Heroku Postgres' as the database
* Navigate to the setting tab, within the config vars section copy the DATABASE_URL to the clipboard for use in the Django configuration.
* Within the django app repository create a new file called env.py - within this file import the os library and set the environment variable for the DATABASE_URL pasting in the address copied from Heroku. The line should appear as os.environ["DATABASE_URL"]= "Paste the link in here"
* Add a secret key to the app using os.environ["SECRET_KEY"] = "your secret key goes here"
* Add the secret key just created to the Heroku Config Vars as SECRET_KEY for the KEY value and the secret key value you created as the VALUE
* In the settings.py file within the django app, import Path from pathlib, import os and import dj_database_url
* insert the line if os.path.isfile("env.py"): import env
* remove the insecure secret key that django has in the settings file by default and replace it with SECRET_KEY = os.environ.get('SECRET_KEY')
* replace the databases section with DATABASES = { 'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))} ensure the correct indentation for python is used.
* In the terminal migrate the models over to the new database connection
* Navigate in a browser to cloudinary, log in, or create an account and log in. 
* From the dashboard - copy the CLOUDINARY_URL to the clipboard
* in the env.py file created earlier - add os.environ["CLOUDINARY_URL"] = "paste in the Url copied to the clipboard here"
* In Heroku, add the CLOUDINARY_URL and value copied to the clipboard to the config vars
* Also add the KEY - DISABLE_COLLECTSTATIC with the Value - 1 to the config vars
* this key value pair must be removed prior to final deployment
* Add the cloudinary libraries to the list of installed apps, the order they are inserted is important, 'cloudinary_storage' goes above 'django.contrib.staitcfiles' and 'cloudinary' goes below it.
* in the Settings.py file - add the STATIC files settings - the url, storage path, directory path, root path, media url and default file storage path.
* Link the file to the templates directory in Heroku TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
* Change the templates directory to TEMPLATES_DIR - 'DIRS': [TEMPLATES_DIR]
* Add Heroku to the ALLOWED_HOSTS list the format will be the app name given in Heroku when creating the app followed by .herokuapp.com
* In your code editor, create three new top level folders, media, static, templates
* Create a new file on the top level directory - Procfile
* Within the Procfile add the code - web: guincorn PROJECT_NAME.wsgi
* In the terminal, add the changed files, commit and push to GitHub
* In Heroku, navigate to the deployment tab and deploy the branch manually - watch the build logs for any errors.
* Heroku will now build the app for you. Once it has completed the build process you will see a 'Your App Was Successfully Deployed' message and a link to the app to visit the live site.

#### Forking the repository
By forking the GitHub Repository you can make a copy of the original repository to view or change without it effecting the original repository
This can be done by
    * Log into GitHub or create an account.
    * Locate the repository at https://github.com/YesCoops/wavey.
    * At the top of the repository, on the right side of the page, select "Fork" from the buttons available.
    * A copy of the repository should now be created in your own repository.

#### Create a clone of this repository
Creating a clone enables you to make a copy of the repository at that point in time - this lets you run a copy of the project locally:
This can be done by:
* Navigate to https://github.com/
* click on the arrow on the green code button at the top of the list of files
* select the clone by https option and copy the URL it provides to the clipboard
* navigate to your code editor of choice and within the terminal change the directory to the location you want to clone the repository to.
* type 'git clone' and paste the https link you copied from github
* press enter and git will clone the repository to your local machine

### Acknowledgements

I'd like to thank the following:
* Antonio Rodrigues for all her help during this project.

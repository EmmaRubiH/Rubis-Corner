# Rubi's Corner

![amiresponsive](/static/media/ami.png)

This is a cafe website designed to display menus to costumers and allow them to make, edit and delete reservations. It's a full-stack framework project built using HTML, CSS, Python, Django and javaScript.

---

# Table of Content:

1. [UX](#ux)
   - [Strategy](#strategy)
   - [User Stories](#user-stories)
   - [Scope](#scope)
   - [Structure](#structure)
   - [Skeleton](#skeleton)
   - [color](#color)
   - [Font an Image](#font)
2. [Features](#features)
3. [Bugs](#bugs)
4. [Technologies Used](#technologies-used)
5. [Testing](#testing)
6. [Deployment](#deployment)
7. [Credits](#credits)
8. [Acknowledgements](#acknowledgements)

# UX
## Strategy:

Using the core UX principles, I first started with strategy. Thinking about what the user will be looking for in the Cafe.

The users will be looking for:
* A website that provides good information and is easy to find & concise
* A way to contact the Cafe
* A menu that shows what the cafe provides
* A booking form to make reservation, edit and delete
* An user account to log in in to make reservations
* Allow users to sign up for a newsletter

---
## User Stories:

Follow the link to find my defined user stories and their criteria [here](https://github.com/EmmaRubiH/Rubis-Corner/issues).

1. As a user I can get key information about the restaurant at the landing page so that I can spend less time search for info.
2. As a user I need to sign in so that I can make a booking.
3. As a owner I can manage all booking so that the restaurant don't get over booked.
4. As a user I can access my booking so that I can edit if needed.
5. As a user I can access my booking so that I can cancel my booking.
6. As a user I can sign up for a newsletter so that I can get info and news from the restaurant.
7. As a user I can view menu so that I can get inspiration before visit.
8. As a user I can book a table at the restaurant for date and time.
9. As a user I can see message on the site when i havesuccess with log in/sign up. 
10. As a admin user I can **log in ** so that I can access the site's backend.

---
## Scope:

* Landing page with information about the cafe.
* Menu page, with buttons to view the food and drinks menu.
* Responsive navbar that will navigate to different pages throughout the site.
* Reservation page, with a booking form.
* Register/login using Django allauth.
* Contact info and opening hours.

---
## Structure:

The information above was then used to create a structure for the website.
The site map shows how users can navigate the website intuitively.


<details><summary>Sitemap</summary>

![user](/static/media/sitemap.png)

</details>

---
## Skeleton:

Wireframes were created to set the appearance of the website. Created them using Balsamiq.

The finished project is different from the original mockup. 


<details><summary>Home Page Idea</summary>

![Home Page Idea](/static/media/startidee.png)

</details>


<details><summary>Menu Page Idea</summary>

![Menu Page Idea](/static/media/menuidee.png)

</details>


<details><summary>Book A Table Page Idea</summary>

![booking Page Idea](/static/media/bookingidee.png)

</details>


<details><summary>Home Page Idea</summary>

![Home Page Idea](/static/media/startidee.png)

</details>

<br>

### Surface:

You can see the live site here

---

## Color:

The color palette i chose for this website was grey, white and yellow. I wanted a 'clean' feel and based it on grey to keep in theme with Rubis Corner. The corners of a building can usually be concrete. I wanted the feeling of the name to follow along with the coloring and the theme in the website.While building the site I felt that the feeling could be a little dark, so I chose to add yellow to brighten it up and the feeling could be softer.

And the text colors are black and white smoke throughout the site.

![coolers](/static/media/coolors.png)

## Font:
For fonts, I chose 'Poiret One' and 'Montserrat'.

## Images:
All the images were taken from [Pixabay](https://pixabay.com/sv/).

---
<br>

# Features
There are several features on this site to help users get the most out of their visit to the website.

## General:

<details><summary>Header and Nav Bar</summary>

![Header and Nav Bar](/static/media/HeaderNav.png)

</details>

<br>

​Each page has a header and navigation bar section, located at the top of the page. The navigation bar consisted of links to Home, Menus, Book a table, Newsletter and Login page.

## Footer:

<details><summary>Footer Info</summary>

![Footer](/static/media/footer.png)

</details>

<br>

Each page contains a footer with the same information. Social media accounts (Facebook and Instagram), Opening Hours and contact info.

## Home page:

<details><summary>Main page</summary>

![Main](/static/media/homepage.png)

</details>

<br>

Here, the user gets a feel for what the cafe has to offer. Both with coloring and pictures. A picture of the cafe and a text box with information.

## Menu page:

<details><summary>Menu</summary>

![menu](/static/media/menupage.png)

</details>

<br>

Here the user/visitor can view two menus. In the cafe, there is a drink menu and a food menu. Both menus can be viewed by clicking on the buttons.

## Book a table page:

<details><summary>Booking page</summary>

![booking one](/static/media/bookingone.png)

</details>

<br>

Here the user needs to login to continue with the booking. Click on the link or go to the nav bar to continue.

<details><summary>Booking form</summary>

![booking two](/static/media/bookingtwo.png)

</details>

<br>

The user can fill in details for the booking here. Name, email and contact number,how many people, date, time, table location and occasion.

<details><summary>Booking confirmed</summary>

![booking three](/static/media/bookingthree.png)

</details>

<br>

When the booking is approved, a text page is displayed for the user. Here they can choose between going and changing their booking or viewing the menus.

## Newsletter page:

<details><summary>Newsletter</summary>

![newsletter](/static/media//newsletterpage.png)

</details>

<br>

Here the user/visitor can sign up for a newsletter.

## My Bookings page:

<details><summary>Edit/delete page</summary>

![edit](/static/media/editpage.png)

</details>

<br>

The user can change and delete their booking here.

## Register/Login and Logout:

<details><summary>Register</summary>

![register](/static/media/registerpage.png)

</details>

<details><summary>Login</summary>

![login](/static/media/loginpage.png)

</details>

<details><summary>Logout</summary>

![logout](/static/media/logoutpage.png)

</details>

<br>

Here the visitor can register. If you are already a user, you can log in. And a page to log out.

---
## Future Featurs:

Some features i would like for this app are:

* Avoid over bookings.
* Newsletter mail. After the user has signed up for the newsletter, an email should be sent with information.
* Confirmation email. An email that is sent to the user after they have made a booking, edited or canceled the reservation.

---
# Bugs

1. Had problems loading all the styling on the base.html page.
   * I hade not write the right code to the url link {% static 'css/style.css' %}. (i forgot the css)

2. Css problem. Not showing up when the site was deployed.
   * When i deployed the website to heroku, the site looked different. The CSS was not appearing.
   * I searched on the web after an explanation and ideas. Did not find an answer. But then I started to search at SLACK and found the answer.
   * I had before changed the DEBUG to 'DEVELOPMENT' in os.environ and removed DISABLE COLLECTSTAIC in heroku. What I learned now from SLACK was that I needed to write (python manage.py collectstatic --noinput) in the terminal and then commit (git push heroku).
   * And then the CSS finally worked.

3. The booking page error.
   * I had problems with booking a table page.
   * It said that the booking model did not exist.
   * I searched in slack to figure it out. And after a while I realized that I had forgotten to migrate the last migrations.

4. New uppdate coused errors
  * With the new updates for heroku, I started to have problems with my site.
  * I followed along with Code Institutes walkthrough to migrate to heroku. 
  * I did everything thoroughly one more time, then I realized that I had not saved the right URL from ElephantSQL.
  * When I now do everything the right way, it worked.

---
# Technologies Used

## Languages:
- HTML
- CSS
- Python
- JavaScript

## Frameworks, Libraries, Programs & Applications:
- Django
- PostgreSQL / ElephantSQL
- Bootstrap

---

- [Google Font](https://fonts.google.com/about) - Used the fonts linked in the header and in style.css, fonts used were Montserrat and Poiret One

- [Google Development Tools](https://developer.chrome.com/docs/devtools/) - Used as a primary method for spacing issues, finding bugs and responsiveness.

- [Font Awesome](https://fontawesome.com/v5/search) - Used for the icons on the site.

- [GitHub](https://github.com/) - Used to store code for the project after being pushed.

- [Git](https://git-scm.com/) - Used for version control by utilising the Gitpod terminal to commit to Git and Push to GitHub.

- [Gitpod](https://www.gitpod.io/) - Used as the development environment.

- [Heroku](https://dashboard.heroku.com/) - Used to deploy my application.

- [Figma](https://www.figma.com/) - Figma was used during the structure phase of this project. It was used to create a sitemap of the website.

- [Coloors](https://coolors.co/) - Used to create a colour palette for the design.

- [Cloudinary](https://cloudinary.com/) - Cloudinary was used to store the images used in this project.

- [Balsamiq](https://balsamiq.com/) - Balsamiq was used to draw initial Wireframes for this project.

- [Canva](https://www.canva.com/menus/templates/) - Used to make the menu for food and drink.

---


# Testing

## Manual Testing:

I have tested this project manually myself and have also had it tested by friends and family on multiple devices and screen sizes.

## Code Validation:

- [W3C Markup Validation Service](https://validator.w3.org/) - Used to validate all HTML

<details><summary>HTML Validation</summary>

![HTML](/static/media/HtmlV.png)

</details>

<br>

- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/#validate_by_input) - Used to validate all CSS

<details><summary>CSS Validation</summary>

![CSS](/static/media/cssV.png)

</details>

<br>

- [JSHint](https://jshint.com/) - Used to validate Js code

- [pep8 Validator](https://pep8ci.herokuapp.com/) - Tested python code online and in workspace. No errors

## Accessibility:

<details><summary>LightHouse</summary>

![lighthouse](/static/media/lighthouse.png)

</details>

---

# Deployment

## Database:

<details><summary>ElephantSQL Steps</summary>

ElephantSQL:

- To create a managed postgres datasbase go to ElephantSQL and Signup/Signin to your account.

- Name your database, choose the 'Tiny Turtle' payment plan and click 'Select Region'.

- Choose your region and then create the database.
 instance.

- In the instances page, click the name of your chosen database.

- In the details section of the following page copy the postgres url.

- You can now use this URL when linking the database to the project's GitHub repository.

</details>

## Deploying to Heroku:

<details><summary>Heroku steps</summary>

- Signup/Signin to heroku.

- Create a new app from the Heroku dashboard.

- Give the app a unique name and enter the region of operation then click 'create app'.

- From your newly created app choose the settings tab and navigate to 'Reveal Config Vars'.

- Paste the ElephantSQL Database url into the DATABASE_URL environment variable.

- Create an env.py file in the root directory of your Django project. (At the same directory level as requirements.txt and manage.py)

env.py:
- Paste the ElephantSQL url for the DATABASE_URL value.

- Add the following libraries to the settings.py file: Import Path from pathlib, dj_database_url and os.

Settings.py:
- Create a secret key to replace the insecure SECRET_KEY variable in the settings.py file. Link the secure key in env.py to the settings.py SECRET_KEY variable with the following code: SECRET_KEY = os.environ.get('SECRET_KEY')

- Add your secret key to HEROKU Config Vars.

- Link the DATABASES value to the env.py file with the following code: DATABASES = { 'default': dj_database_url.parse(os.environ.get('DATABASE_URL')) }

- You can now migrate the app models to the new database using the command: "python3 manage.py makemigrations" then Python3 manage.py migrate.

</details>

## Cloudinary:

<details><summary>Cloudinary steps</summary>

- Signup/signin to Cloudinary

- Copy the 'cloudinary url' from your account dashboard and paste it as the CLOUDINARY_URL value in env.py.

- Add the CLOUDINARY_URL to the Config Vars in Heroku.

- Also Add the DISABLE_COLLECTSTATIC Key with the value of 1

- Change the static file settings in Django by altering the following.

  * The STATIC_URL

  * STATICFILES_STORAGE

  * STATICFILES_DIRS
  * STATIC_ROOT
  * MEDIA URL
  * DEFAULT_FILE_STORAGE

Settings.py templates:

- Back nearer the top of the settings.py file add the Setting TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

- Create 3 new folders for static files, media files and HTML templates. (At the same directory level as requirements.txt and manage.py.)

- Create a Procfile(capital P) and add the following: web: gunicorn NAME_OF_THE_APP_GOES_HERE.wsgi

- Add the app name and herokuapp.com to the list of ALLOWED_HOSTS.

- Add and commit the changes to GitHub.

- Remove DISABLE_COLLECTSTATIC from Heroku Config Vars

- Deploy via the 'Deploy Main Branch' button in the Deployment page of HEROKU.

- If you recieve an success message, you can click the link provided to view the app in the web browser.

</details>

# Credits

- The initial setup of the Django project was done following the Code Institutes walkthrough project.

- Stack Overflow

- Django Docs

- Bootstrap

- Crispy Forms

- Django Allauth

- [Active_link](https://pypi.org/project/django-active-link/) - To make links active in navbar.

---

# Acknowledgements 

- I would like to thank my mentor Jubril for good feedback and support for this project.

- Thanks to Slack community

- I would like to thank my friends and family for their valued opinions and critic during the process of design and development.

---

[Back to top](#table-of-content)
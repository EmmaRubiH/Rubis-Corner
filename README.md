# Rubi's Corner

This is a cafe website designed to display menus to costumers and allow them to make, edit and delete reservations. It's a full-stack framework project built using HTML, CSS, Python, Django and javaScript.

---
# UX
## Strategy:

Using the core UX principles i first started with strategy. Thinking about what the user will be looking for in the Cafe.

The users will be looking for:
* An website that provides good information and easy to find & concise
* A way to contact the Cafe
* A menu that show what the cafe provides
* A booking form to make reservation, edit and delete
* An user account to log in in to make reservations
* Allow users to sign up for a newsletter

---
## User Stories:

Follow the link to find my defined user stories and their criterias [here](https://github.com/EmmaRubiH/Rubis-Corner/issues).

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
* Menu page, with buttons to view food and drinks menu.
* Responsive navbar that will navigate to diferent pages troughout the site.
* Reservation page, with a booking form.
* Register/login using Django allauth.
* Contact info and opening hours.

---
## Structure:

The information above was then used to create a structure for the website.
The site map showing how users can navigate the website intuitively.


<details><summary>Sitemap</summary>

![user](/static/media/sitemap.png)

</details>

---
## Skeleton:

Wireframes were created to set the appereance of the website. Created them using Balsamiq.

The finish project is different from the original mockup. 


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

The colour palette i chose for this website was grey, white and yellow. I wanted a 'clean' feel and based it on grey to keep in theme with rubis Corner. Corners of a building can usually be concrete material. I wanted the feeling of the name to follow through with the coloring and the theme in the website.
While building the site i felt that the feeling could be a little dark, so i chose to add yellow to brighten it upp and feeling could be softer.

And text colours is black and whitesmoke troughout the site.

![coolers](/static/media/coolors.png)

## Font:
For fonts i chose 'Poiret One' and 'Montserrat'.

## Images:
all the images where taken from [Pixabay](https://pixabay.com/sv/).

---
<br>

# Features
There are several features on this site to help users get the most out of their visit to the website.

## General:

<details><summary>Header and Nav Bar</summary>

![Header and Nav Bar](/static/media/HeaderNav.png)

</details>

<br>

Each page has a header and Navigation bar section, located at the top of the page. The navigation bar consisted of links to Home, Menus, Book a table, Nevsletter and Login page.

## Footer

<details><summary>Footer Info</summary>

![Footer](/static/media/footer.png)

</details>

<br>

Each page contains a footer white same information. Social media accounts (Facebook and Instagram), Opening Hours and contact info.



## Future Featurs:

Some features i would like for this app are:

* Avoid overbookings.
* Newsletter mail. After the user have sign up for newsletter, an email should bee send with information.
* Confirmation email. An email that send to the user after they have make a booking, edit or cancelled the reservation.

---
<br>

# Testing
lll

---
<br>

# Bugs

1. Had problems loading all the styling on the base.html page.
  * I hade not write the right code to the url link {% static 'css/style.css' %}. (i forgot the css)




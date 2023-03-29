# The Dragon's Flagon | Gaming Tavern

![Am I Responsive]()

**Developer: Stuart Wall**

💻 [Visit live website](https://ci-pp4-dragons-flagon-clinelly.herokuapp.com/)



## Table of Contents
  - [About](#about)
  - [User Goals](#user-goals)
  - [Site Owner Goals](#site-owner-goals)
  - [User Experience](#user-experience)
  - [User Stories](#user-stories)
  - [Design](#design)
    - [Colours](#colours)
    - [Fonts](#fonts)
    - [Structure](#structure)
      - [Website pages](#website-pages)
      - [Database](#database)
    - [Wireframes](#wireframes)
  - [Technologies Used](#technologies-used)
  - [Features](#features)
  - [Validation](#validation)
  - [Testing](#testing)
    - [Manual testing](#manual-testing)
    - [Automated testing](#automated-testing)
    - [Tests on various devices](#tests-on-various-devices)
    - [Browser compatibility](#browser-compatibility)
  - [Bugs](#bugs)
  - [Heroku Deployment](#heroku-deployment)
  - [Credits](#credits)
  - [Acknowledgements](#acknowledgements)

### About
The Dragon's Flagon is a fantasy-themed tavern. It was designed primarily as a social spot for people to eat, drink, make merry and play a variety of tabletop/card/boardgames.

<hr>

### User Goals
- To book a session at the tavern.
- To edit or delete a created booking.
- To be kept up-to-date with events.
- To view posts from the owners.
- To be able to contact the owners with questions or provide feedback.

### Site Owner Goals
- To enable users to book sessions at the tavern.
- To promote the business and attract customers.
- To keep customers up-to-date with news posts.
- To advertise events for customers to attend.
- To have an attractive and responsive website.

<hr>


## User Experience

### Target Audience
- Users wishing to book a session at the tavern.
- New and repeat customers who wish to attend different events.
- Members of the gaming community who wish to have a social hub.
- Families looking for a fun place to eat and play.

### User Requirements and Expectations
- Accessible.
- Responsive.
- Key information (contact information & opening times).
- Social media links.
- Ease of use.
- Clean design.


##### Back to [top](#table-of-contents)<hr>


## User Stories

### Users
1.	As a User I can navigate across the site so that I can move to each feature of the site easily. (Must Have).
2.	As a User I can use a navbar, footer, and social icons so that I can navigate the site, access menus, and access socials. (Must Have).
3.	As a User I can view the opening hours and contact details so that I know when the business is open and how to contact them via email, phone and socials. (Must Have).
4.	As a User I can create a booking by selecting a date and time so that I can book a session. (Must Have).
5.	As a User I can update my booking so that I can choose another available time and date. (Must Have).
6.	As a User I can delete my booking so that I can cancel my session. (Must Have).
7.	As a user I can view my booking so that I can remind myself of the date and time I have booked. (Must Have).
8.	As a User I am notified when I take an action, so that I know my action of creating, editing, or deleting a booking has been successful. (Must Have).
9.	As a User I can register when prompted so that I can make a booking if I wish. (Must Have).
10.	As a User I can register an account so that I can access more advanced features of the site. (Must Have).
11.	As a user I can login so that I can book a session, leave a review or comment on a post. (Must Have).
12.	As a user I can see my login status so that I know if I am logged in or not. (Must Have).
13.	As a User I can view the site's blog so that I can learn additional information and read articles. (Must Have).
14.	As a User I can view the food, drink and game menus so that I can decide whether visit the business. (Must Have).
15.	As a User I cannot book a date in the past so that my booking is valid. (Must have).
16.	As a User, I can view events posted by the business so that I can decide to visit on certain days. (Must Have).
17.	As a user I can see reviews left by other users so that I can see if the business is any good. (Must Have).
18.	As a user I can post a review of my experience so that I can provide feedback of my visit. (Must Have).
19.	As a user, I can comment on blog posts to provide feedback so that I can join a social network. (Must Have).
20.	As a user, I can like/unlike blog posts so that I can provide feedback the the site owner on content quality. (Should Have).

### Admin / Authorised User
21.	As an Admin / Authorised User I can log in so that I can access the back end of the site. (Must Have).
22.	As an Admin / Authorised User I can manually add a booking so that I can book a table if someone phones, or emails the business. (Should Have).
23.	As an Admin / Authorised User I can login to add, edit or remove events from the calendar so I can advertise/change new events or cancel old ones. (Must Have).
24.	As an Admin / Authorised User I can create, read, update and delete blog posts so that I can provide information and updates to the users. (Must Have).
25.	As an Admin / Authorised User I can search through bookings, blogs, and events so that I can find the information I am looking for. (Should Have).
26.	As an Admin / Authorised User I can filter bookings by date so that I can see what bookings we have for a particular day (Should Have).
27.	As an Admin / Authorised User, I can moderate reviews/comments to keep a friendly online presence and maintain a professional website. (Should Have).

### Site Owner  
23.	As a Site Owner I can provide a responsive site for my customers so that they have a good user experience. (Must Have).
24.	As a Site Owner I can validate data entered into my site so that all submitted data is correct. (Must Have).
25.	As a Site Owner I can provide a 'Contact Us' page so that users can get in touch with my business. (Must Have).
26.	As a Site Owner, I can look at feedback provided by users, through reviews, comments and direct contact, so that I can make improvements where necessary. (Must Have)


### Kanban, Epics & User Stories


<details><summary>Epics</summary>

![Epics]()

</details>

<details><summary>User Stories</summary>

![User stories]()

</details>

<details><summary>Kanban</summary>

![Kanban finish]()

</details>


##### Back to [top](#table-of-contents)<hr>


## Design

### Colours
The colour palette was found on [Coolors.co](https://coolors.co/). I chose a palette with a similar colour-scheme to the main logo of the website.
Blue buttons draw the eye of the user and uploaded cards have a parchment coloured background to fit the fantasy theme.

<details><summary>View palette</summary>
<img src="/workspace/CI_PP4_Dragons_Flagon/docs/palette.png">
</details>


### Fonts

The font chosen was Medieval Sharp from Google Fonts, as it resembles old-fashioned writing on a scroll. Cursive was chosen as a back-up font. 

### Structure

#### Website pages
The website was designed alongside standard principles to ensure users would be familiar with the layout. 
The header contains a navbar allowing users to navigate the main pages and to register/login. The navbar collapses to a menu on smaller screens.
A footer runs along the bottom of the webpages, promoting the website's social media links and more niche webpages.

Overall, the website has the following pages:
- A Home Page, providing the user with a brief description of the business. Buttons take the user to the Booking page and the Events page. Cards display user reviews and a button underneath takes users to the Review Submission page.
- An About Page, which provides the user more in-depth details about the website and the services it offers.
- The Gallery Page; which functions as a blog, allowing the site admins to publish photos/articles to the users. Clicking on a post enables users to comment on the posts.
- The Contact Page allows users to contact the site owners directly and provides direct contact details and a map to the business location.
- The Food & Drink page gives users a sample of what food/drink the tavern provides.
- The Games page provides users with a list of games the tavern has to offer.
- The Events page provides information about the regular events that take place at the tavern. A calendar provides users with dates and event names. Clicking on an event provides further details. Site admins can update/delete events.
- The User Panel page can be accessed from the header. It provides users with information about their bookings and their account information. By clicking on their booking, users can update or delete them.
- The Booking page can be accessed from the home page and allows users to book a session at the tavern.
- The Review Submission page is accessed from the home page and allows users to submit a review about their experience.

#### Database
Database schema created by using [django-extensions](https://django-extensions.readthedocs.io/en/latest/graph_models.html), pydot and [GraphVizOnline](https://dreampuf.github.io/GraphvizOnline/)

<details><summary>Show diagram</summary>
<img src="/workspace/CI_PP4_Dragons_Flagon/docs/database.png">
</details>


##### User Model
The User Model contains the following:
- user_id
- date_joined
- email
- first_name
- last_name
- is_active
- is_staff
- is_superuser
- last_login
- password
- username

##### Review Model
The Review Model contains the following:
- review_id
- author
- content
- created_on
- slug
- status
- title

##### Gallery Model
The Gallery Model contains the following:
- gallery_id
- author
- content
- created_on
- featured_image
- slug
- status
- title
- updated_on

##### Comment Model
The Comment Model contains the following:
- comment_id
- post
- approved
- body
- created_on
- name

##### TableBooking Model
The TableBooking Model contains the following:
- tablebooking_id
- user
- day
- email
- phone
- service
- time
- time_booked

##### Event Model
The Event Model contains the following:
- event_id
- description
- end_time
- start_time
- title

##### Contact Model
The Contact Model contains the following:
- message_id
- user
- created_date
- email
- message
- name
- phone

### Wireframes
The wireframes were created using Balsamiq
<details><summary></summary>
<img src="">
</details>


## Technologies Used

### Languages & Frameworks

- HTML
- CSS
- Javascript
- Python
- Django


### Libraries & Tools

- [Am I Responsive](http://ami.responsivedesign.is/)
- [Balsamiq](https://balsamiq.com/)
- [Bootstrap v5.2](https://getbootstrap.com/)
- [Cloudinary](https://cloudinary.com/)
- [Favicon.io](https://favicon.io)
- [Chrome dev tools](https://developers.google.com/web/tools/chrome-devtools/)
- [Font Awesome](https://fontawesome.com/)
- [Git](https://git-scm.com/)
- [GitHub](https://github.com/)
- [Google Fonts](https://fonts.google.com/)
- [Heroku Platform](https://id.heroku.com/login)
- [Postgres](https://www.postgresql.org/)
- [ElephantSQL](https://www.elephantsql.com/)
- [Summernote](https://summernote.org/)
- Validation:
  - [WC3 Validator](https://validator.w3.org/)
  - [Jigsaw W3 Validator](https://jigsaw.w3.org/css-validator/)
  - [Pycodestyle(PEP8)](https://pep8ci.herokuapp.com/)
  - [Lighthouse](https://developers.google.com/web/tools/lighthouse/)
  - [Wave Validator](https://wave.webaim.org/)

##### Back to [top](#table-of-contents)


## Features

### Home page



##### Back to [top](#table-of-contents)
<hr>


## Validation

The W3C Markup Validation Service was usd to validate the HTML code used in the templates. All templates returned clear with no warnings or errors.

<details><summary>Index Page</summary>
<img src="/workspace/CI_PP4_Dragons_Flagon/docs/validation/html/index.png">
</details>

<details><summary>Review Page</summary>
<img src="/workspace/CI_PP4_Dragons_Flagon/docs/validation/html/review_page.png">
</details>


<details><summary>About Page</summary>
<img src="/workspace/CI_PP4_Dragons_Flagon/docs/validation/html/about.png">
</details>

<details><summary>Gallery Page</summary>
<img src="/workspace/CI_PP4_Dragons_Flagon/docs/validation/html/gallery.png">
</details>

<details><summary>Gallery Detail Page</summary>
<img src="/workspace/CI_PP4_Dragons_Flagon/docs/validation/html/gallery_detail.png">
</details>

<details><summary>Contact Page</summary>
<img src="/workspace/CI_PP4_Dragons_Flagon/docs/validation/html/contact.png">
</details>

<details><summary>Food Menu Page</summary>
<img src="/workspace/CI_PP4_Dragons_Flagon/docs/validation/html/food_menu.png">
</details>

<details><summary>Events Page</summary>
<img src="/workspace/CI_PP4_Dragons_Flagon/docs/validation/html/event_page.png">
</details>

<details><summary>Create Event Page</summary>
<img src="/workspace/CI_PP4_Dragons_Flagon/docs/validation/html/create_event.png">
</details>

<details><summary>Edit Event Page</summary>
<img src="/workspace/CI_PP4_Dragons_Flagon/docs/validation/html/edit_event.png">
</details>

<details><summary>Delete Event Page</summary>
<img src="/workspace/CI_PP4_Dragons_Flagon/docs/validation/html/delete_event.png">
</details>

<details><summary>Game List Page</summary>
<img src="/workspace/CI_PP4_Dragons_Flagon/docs/validation/html/game_list.png">
</details>

<details><summary>Booking Page</summary>
<img src="/workspace/CI_PP4_Dragons_Flagon/docs/validation/html/booking.png">
</details>

<details><summary>Booking Submit Page</summary>
<img src="/workspace/CI_PP4_Dragons_Flagon/docs/validation/html/booking_submit.png">
</details>

<details><summary>Booking Submit (Time) Page</summary>
<img src="/workspace/CI_PP4_Dragons_Flagon/docs/validation/html/booking_submit_time.png">
</details>

<details><summary>Edit Booking Page</summary>
<img src="/workspace/CI_PP4_Dragons_Flagon/docs/validation/html/edit_booking.png">
</details>

<details><summary>Edit Booking (Time) Page</summary>
<img src="/workspace/CI_PP4_Dragons_Flagon/docs/validation/html/edit_booking_time.png">
</details>

<details><summary>Delete Booking Page</summary>
<img src="/workspace/CI_PP4_Dragons_Flagon/docs/validation/html/delete_booking.png">
</details>

<details><summary>User Panel Page</summary>
<img src="/workspace/CI_PP4_Dragons_Flagon/docs/validation/html/user_panel.png">
</details>

<hr>


### CSS Validation
The W3C Jigsaw CSS Validation Service was used to validate the CSS file used in the project. The CSS file returned clear with no errors or warnings.

<details><summary>Style.css</summary>
<img src="/workspace/CI_PP4_Dragons_Flagon/docs/validation/css.png">
</details>
<hr>

### JavaScript Validation
There are no custom JavaScript files in this project.


### PEP8 Validation
Code Institute's Python Linter App was used to check the validation of the Python code, as PEP8online is unavailable.
All custom python files reported as clear with no errors or issues.

<hr><summary>Tavern</summary><hr>

<details><summary>Admin.py</summary>
<img src="/workspace/CI_PP4_Dragons_Flagon/docs/validation/Tavern/tavern-admin-py.png">
</details>

<details><summary>Models.py</summary>
<img src="/workspace/CI_PP4_Dragons_Flagon/docs/validation/Tavern/tavern-models-py.png">
</details>

<details><summary>Urls.py</summary>
<img src="/workspace/CI_PP4_Dragons_Flagon/docs/validation/Tavern/tavern-urls-py.png">
</details>

<details><summary>Views.py</summary>
<img src="/workspace/CI_PP4_Dragons_Flagon/docs/validation/Tavern/tavern-views-py.png">
</details>

<details><summary>Forms.py</summary>
<img src="/workspace/CI_PP4_Dragons_Flagon/docs/validation/Tavern/tavern-forms-py.png">
</details>

<hr><summary>Booking</summary><hr>

<details><summary>Admin.py</summary>
<img src="/workspace/CI_PP4_Dragons_Flagon/docs/validation/Booking/booking-admin-py.png">
</details>

<details><summary>Models.py</summary>
<img src="/workspace/CI_PP4_Dragons_Flagon/docs/validation/Booking/booking-models-py.png">
</details>

<details><summary>Urls.py</summary>
<img src="/workspace/CI_PP4_Dragons_Flagon/docs/validation/Booking/booking-urls-py.png">
</details>

<details><summary>Views.py</summary>
<img src="/workspace/CI_PP4_Dragons_Flagon/docs/validation/Booking/booking-views-py.png">
</details>

<hr><summary>Contact</summary><hr>

<details><summary>Admin.py</summary>
<img src="/workspace/CI_PP4_Dragons_Flagon/docs/validation/Contact/contact-admin-py.png">
</details>

<details><summary>Models.py</summary>
<img src="/workspace/CI_PP4_Dragons_Flagon/docs/validation/Contact/contact-models-py.png">
</details>

<details><summary>Urls.py</summary>
<img src="/workspace/CI_PP4_Dragons_Flagon/docs/validation/Contact/contact-urls-py.png">
</details>

<details><summary>Views.py</summary>
<img src="/workspace/CI_PP4_Dragons_Flagon/docs/validation/Contact/contact-views-py.png">
</details>

<details><summary>Forms.py</summary>
<img src="/workspace/CI_PP4_Dragons_Flagon/docs/validation/Contact/contact-forms-py.png">
</details>


<hr><summary>Events</summary><hr>

<details><summary>Admin.py</summary>
<img src="/workspace/CI_PP4_Dragons_Flagon/docs/validation/Events/events-admin-py.png">
</details>

<details><summary>Models.py</summary>
<img src="/workspace/CI_PP4_Dragons_Flagon/docs/validation/Events/events-models-py.png">
</details>

<details><summary>Urls.py</summary>
<img src="/workspace/CI_PP4_Dragons_Flagon/docs/validation/Events/events-urls-py.png">
</details>

<details><summary>Views.py</summary>
<img src="/workspace/CI_PP4_Dragons_Flagon/docs/validation/Events/events-views-py.png">
</details>

<details><summary>Forms.py</summary>
<img src="/workspace/CI_PP4_Dragons_Flagon/docs/validation/Events/events-forms-py.png">
</details>

<details><summary>Utils.py</summary>
<img src="/workspace/CI_PP4_Dragons_Flagon/docs/validation/Events/events-utils-py.png">
</details>

### Lighthouse

Page Performance, Accessibility, Best Practice and SEO were tested using Google Lighthouse.
<br>
All templates scored above 90 on Performance and SEO. All Templates scored 83 on Best Practice due to issues Google raised with certain images, cookies and manifests.
<br>
The Gallery Detail page scored 87 on Accessibility with a warning about a conflict with the button name for the like/dislike feature for the gallery.

<details><summary>Index Page</summary>
<img src="/workspace/CI_PP4_Dragons_Flagon/docs/validation/Lighthouse/index.png">
</details>

<details><summary>Review Page</summary>
<img src="/workspace/CI_PP4_Dragons_Flagon/docs/validation/Lighthouse/review_page.png">
</details>


<details><summary>About Page</summary>
<img src="/workspace/CI_PP4_Dragons_Flagon/docs/validation/Lighthouse/about.png">
</details>

<details><summary>Gallery Page</summary>
<img src="/workspace/CI_PP4_Dragons_Flagon/docs/validation/Lighthouse/gallery.png">
</details>

<details><summary>Gallery Detail Page</summary>
<img src="/workspace/CI_PP4_Dragons_Flagon/docs/validation/Lighthouse/gallery_detail.png">
</details>

<details><summary>Contact Page</summary>
<img src="/workspace/CI_PP4_Dragons_Flagon/docs/validation/Lighthouse/contact.png">
</details>

<details><summary>Food Menu Page</summary>
<img src="/workspace/CI_PP4_Dragons_Flagon/docs/validation/Lighthouse/food_menu.png">
</details>

<details><summary>Events Page</summary>
<img src="/workspace/CI_PP4_Dragons_Flagon/docs/validation/Lighthouse/event_page.png">
</details>

<details><summary>Create Event Page</summary>
<img src="/workspace/CI_PP4_Dragons_Flagon/docs/validation/Lighthouse/create_event.png">
</details>

<details><summary>Edit Event Page</summary>
<img src="/workspace/CI_PP4_Dragons_Flagon/docs/validation/Lighthouse/edit_event.png">
</details>

<details><summary>Delete Event Page</summary>
<img src="/workspace/CI_PP4_Dragons_Flagon/docs/validation/Lighthouse/delete_event.png">
</details>

<details><summary>Game List Page</summary>
<img src="/workspace/CI_PP4_Dragons_Flagon/docs/validation/Lighthouse/game_list.png">
</details>

<details><summary>Booking Page</summary>
<img src="/workspace/CI_PP4_Dragons_Flagon/docs/validation/Lighthouse/booking.png">
</details>

<details><summary>Booking Submit Page</summary>
<img src="/workspace/CI_PP4_Dragons_Flagon/docs/validation/Lighthouse/booking_submit.png">
</details>

<details><summary>Booking Submit (Time) Page</summary>
<img src="/workspace/CI_PP4_Dragons_Flagon/docs/validation/Lighthouse/booking_submit_time.png">
</details>

<details><summary>Edit Booking Page</summary>
<img src="/workspace/CI_PP4_Dragons_Flagon/docs/validation/Lighthouse/edit_booking.png">
</details>

<details><summary>Edit Booking (Time) Page</summary>
<img src="/workspace/CI_PP4_Dragons_Flagon/docs/validation/Lighthouse/edit_booking_time.png">
</details>

<details><summary>Delete Booking Page</summary>
<img src="/workspace/CI_PP4_Dragons_Flagon/docs/validation/Lighthouse/delete_booking.png">
</details>

<details><summary>User Panel Page</summary>
<img src="/workspace/CI_PP4_Dragons_Flagon/docs/validation/Lighthouse/user_panel.png">
</details>

<hr>

### Wave
WAVE was used to test the websites accessibility.


##### Back to [top](#table-of-contents)<hr>


## Testing

1. Manual testing
2. Automated testing

### Manual testing


**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| |  |


### Automated testing




### Device Testing & Browser compatibility




##### Back to [top](#table-of-contents)<hr>


## Bugs

| **Bug** | **Fix** |
| ------- | ------- |
| |  |


##### Back to [top](#table-of-contents)<hr>


### Heroku Deployment

[Official Page](https://devcenter.heroku.com/articles/git) (Ctrl + click)
This application has been deployed from Github using Heroku. Here's how:

1. Create an account at heroku.com

2. Create an app. Give it a name such as ci-pp4-dragons-flagon (note: the name must be unique) and select a region. I set mine to Europe.

Heroku now charges for access to it's native postgres resources. I set up my project with [ElephantSQL](https://www.elephantsql.com/)

3. Go to elephantsql.com and create an account.

4. Go to your dashboard.

5. Select 'New Instance'.

6. Set up your plan: 
  - Give it a name (typically your project name)
  - Select the Tiny Turtle (free) package.
  - The Tags field can be left blank.

7. Select a Region (ideally, a data center located near you).

8. Click 'Review'.

9. Check your details are correct and click 'Create Instance'.

10. Return to the dashboard and click on the database instance name.

11. In the URL section, copy the URL to your clipboard.

12. Copy the database URL to your env.py file. It can also be set as an environmental variable in Heroku.

13. Install the plugins dj-database-url and psycopg2.

14. Run pip3 freeze > requirements.txt so both are added to the requirements.txt file.

15. Create a Procfile with the text: web: gunicorn dragonsflagon.wsgi.

16. In the settings.py ensure the connection is to the ElephantSQL database.

17. Ensure debug is set to false in the settings.py file.

18. Add localhost, and ci-pp4-dragons-flagon-clinelly.herokuapp.com to the ALLOWED_HOSTS variable in settings.py.

19. Run "python3 manage.py showmigrations" to check the status of the migrations.

20. Run "python3 manage.py migrate" to migrate the database.

21. Run "python3 manage.py createsuperuser" to create a super/admin user.

22. Install gunicorn and add it to the requirements.txt file using the command pip3 freeze > requirements.txt.

23. Disable collectstatic in Heroku before any code is pushed using the command heroku config:set DISABLE_COLLECTSTATIC=1 -a ci-pp4-dragons-flagon-clinelly.

24. Set the Config Vars in the Heroku app:
  - Your Elephant SQL Database.
  - Port 8000.
  - Your secret key.

25. Connect the app to GitHub, and enable automatic deploys from main if desired.

26. Click deploy to deploy your application to Heroku for the first time.

27. Click on the link provided to access the application.

28. If you encounter any issues accessing the build logs is a good way to troubleshoot the issue.
<hr>

### Fork Repository
In order to fork the repository, you must:

- Go to the GitHub repository.
- Click on 'Fork' button in upper right hand corner.
- Select 'Create new fork' from the drop-down menu
<hr>

### Clone Repository
You can clone the repository by following these steps:
- Going to the GitHub repository.
- Clicking the 'Code' button, loacted above the file list.
- Selecting if you prefer to clone using either HTTPS, SSH, or Github CLI.
- Clicking the copy button to copy the URL to your clipboard.
- Opening Git Bash.
- Changing the current working directory to one where you want to clone the directory to.
- Typing 'git clone' and pasting the URL from the clipboard ($ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY)
- Pressing 'Enter' to create your local clone.

The repository can be found here - https://github.com/Clinelly/CI_PP4_Dragons_Flagon

##### Back to [top](#table-of-contents)<hr>


## Credits

### Images
[Dragon’s Flagon logo](https://ih1.redbubble.net/image.1434837373.0468/flat,750x,075,f-pad,750x1000,f8f8f8.jpg)
Designed and sold on [Redbubble](https://www.redbubble.com/) by [Carl Huber](https://www.redbubble.com/people/carlhuber/shop)

Board Game Images were taken from [BoardGameGeek](https://boardgamegeek.com/)

Tavern Hero Image taken from [DDOPlayers](https://ddoplayers.com/2021/11/25/immersive-dd-inspired-restaurant-and-amusement-center-planned-in-lake-geneva/)

### Code
The code for the Events app was inspired by and modified from a tutorial by [Hui Wen]( https://www.huiwenteo.com/normal/2018/07/24/django-calendar.html)

The code for the Booking app was inspired by and modified from a tutorial by [John Abdsho Khosrowabadi](https://blog.devgenius.io/django-tutorial-on-how-to-create-a-booking-system-for-a-health-clinic-9b1920fc2b78)

The code for writing tests was inspired by a YouTube tutorial on testing by [The Dumbfounds](https://www.youtube.com/playlist?list=PLbpAWbHbi5rMF2j5n6imm0enrSD9eQUaM)

[Code Institute's](https://codeinstitute.net/) Hello Django and I Think Therefore I Blog walkthrough challenges.

[Stack Overflow](https://stackoverflow.com/) helped with answering niche questions.

[Django Documentation](https://docs.djangoproject.com/en/4.1/)

[Bootstrap Documentation](https://getbootstrap.com/docs/5.3/getting-started/introduction/)

##### Back to [top](#table-of-contents)<hr>

## Acknowledgements

### Special thanks to the following:
- My beautiful wife Megan, who's love and support has kept me going.
- My mentor Mo Shami who continually pushes me to be a better developer.
- Code Institute's fantastic tutor team, who are the fountain of all knowledge.
- The class of June '22, for their humour and insight.
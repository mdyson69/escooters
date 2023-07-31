[![Build Status](https://travis-ci.org/MD1968/e-scooters.svg?branch=master)](https://travis-ci.org/MD1968/e-scooters)

# Full Stack Frameworks Project - E Scooters

## (c) Mark Dyson

This web application is a fully fledged e commerce shop.

Link to the site: https://e-scooters.herokuapp.com

Please do not use your credit card details while checking out as I will not be sending out any products.

If you wish to try out the site you can use a test credit card. Details Below. 

Card Number: 4000 0082 6000 0000 Expiry Date: Any future date CSV: Any three numbers.


## CONCEPT:

The idea for the application followed news reports of the government looking into running trials of E-Scooters later this year. I was already researching the product to sell for the fourth project of course.
Looking at www.halfords.co.uk I realised that a good selection is already on the market.
I decided to create a project using data and photos gained from Halfords.

The course materials from the Code Institute was also very valuable as a resource and inspiration.

## WIREFRAMES:

As located in the Wireframes folder within the project.

## UI/UX:

I wanted the site to be clean, clear and concise. The general colour for the text, buttons, banners etc to be green to highlight the environmentally friendly credentials of the product available.
The page background has been coded to be white so as not to distract from the item information and page contents.
The buttons, banners have also been placed and coloured as not to distract from the overall message.

## USER STORIES

### Home page:

As a site visitor, I can search for products by entering my details

As a site visitor, I can display products filtered by size (Adult or Child)

As a site visitor, I can display products sorted by range, price and charge time.

As a site visitor, I can add my selected product to a shopping cart either by entering a number for the quantity or using a simple button for a single item.

As an admin member, I can select a product, then amend the details, or delete the item from the database.

### Checkout:

As a site visitor, I can check the cart details and amend the quantity or delete products before proceeding to make a payment.

### Payments:

As a site visitor, I can use a credit card to make a secure payment after entering my address and details.

As a visitor, I will receive an email confirming my payment details and the order information.

### Profile:

As a member, I can securely store my address and phone number to be used for future purchases.

As a member, I can review my past order details.

### Product management:

As a member, I can add, remove, delete product information from the database.

## TECHNOLOGIES USED

## Technologies

1. HTML — used to structure the content of the website (link to the documentation: https://devdocs.io/html/)
2. CSS — used for styling the website (link to the documentation: https://devdocs.io/css/)
3. Bootstrap (link to the documentation: https://getbootstrap.com)
4. Javascript — for the navigation bar (link to the documentation: https://devdocs.io/jsdoc/)
5. Python3 — (link to the documentation: https://docs.python.org/3/)
6. Django — (link to the documentation: https://docs.djangoproject.com/en/3.0/)
7. travis 
8. GitPod - Developement and Built In Testing Software
9. Grammarly 
10. Google Analytics
11. AWS

## I have used online tools to check this project. Travis, and the checker built into GitPod.

A lot of the testing was done by myself with and using online tools. 

The tools that were used are Travis, and the inbuilt checking system within GitPod.

The manual tests completed were as follows:

### General Website Functionality Tests: 

Registration:

To test this, I visited my website in the position of a user who was visiting for the first time. 
 
I first clicked on the 'Register' button in the navigation menu. Once the registration page opened, I completed the following steps.

Clicked on the 'Register' button without filling out any fields to ensure a user would not be able to register without entering their details. 
The result - It didn't allow me to register until I populated the 'Username' field.

Clicked on the 'Register' button after I populated the 'Username' field. 
The result - It didn't allow me to register until I also populated the 'Password' field.

Clicked on the 'Register' button after I populated the 'Username' and 'Password' field.
The result - It didn't allow me to register until I also populated the 'Password Confirmation' field.

Clicked on the 'Register' button after I populated the 'Username', 'Password' and 'Password Confirmation' field. 
The result - It now successfully worked and an account was registered with the username and password I set. This is all the information that is needed to use the website. Email Address and full name will be requested at the checkout page if you choose to purchase something.

To test the registration form further, 

I added a username and email that I knew was already taken to ensure that it would not let me register it. I was able to confirm that it gave me an error. 

After that test, I entered some new details and then clicked 'Register'. This registered me successfully and I was then able to access pages such as services, forum, profile and cart.

Login: To test this, I visited my website in the position of a recently registered user. Once on my website, I then proceeded to click on the 'Login' button in the navigation menu. After that, I then proceeded to enter the details I originally registered with. This then successfully logged me in.

To test this further, I entered an incorrect password and username to ensure that it would not still let me log in. I was able to confirm that it gave me an error.

Logout: To test this, I simply clicked on the 'Logout' button the navigation menu after I had logged in. This then successfully logged me out.

Password Reset: To test this, I first ensured that I was logged out of my website. Once I was sure of that, I proceeded to click on the 'Login' button in the navigation menu. Once the login page loaded, I clicked on the 'Forgotten your password?' link at the bottom of the login form. This then took me to another page, where I was able to enter my registered email address and have a password reset sent to my email. I successfully received the email and was able to update my password. Finally, I went back onto my website, loaded up the login page, added my new login details and successfully logged in.

User Restrictions on Editing/Deleting Posts/Service: To ensure that only the user who added a post or service would be able to edit/delete that post or service, I needed to add some user restrictions directly into the templates, which is what I did. To test this, I created a post and a service from 2 separate accounts. I then viewed both posts and services from different accounts to ensure that I was unable to see an edit or delete button if the post or service wasn't mine. This was the case on both accounts and this test was successful.

The browser and Mobile Responsiveness I tested the browser and mobile responsiveness in a couple of ways. The main method I used to test the responsiveness was by inspecting all the pages on Google Chrome and using the 'Toggle device toolbar' option. Using this tool I was able to test a variety of different screen sizes and how the page would look on specific mobile devices.

The second method I used was simply opening my website on different devices and ensuring it looked user-friendly.

Landing page:

I opened the site as a new visitor. Clicking on the options in the menu bar to make sure all links are working correctly
Result: Links worked and the products were sorted as planned.

Product Page:

I checked the sort by drop down and confirmed that all of the options were working correctly.
Result: Working as planned.

Then I checked that all of the buttons were functioning. 
Result: Working as planned.

Shopping Basket:

I checked that all of the information was being displayed correctly.
Result: working as planned.

Checkout:

The form validation was checked line by line:
Result: Working as planned.

Payment:

Using the UK test credit card details I tested that the process and link with stripe were all working.
Result: On the first attempt I realised that the webhook functionality was not working. After assistance from the turtors I realised that the webhook was pointing to the wrong file. This was corrected. I tested the sytem again and this was now wotking as planned. 

I received an email confirming my purchase. 


Adding A Product:

Whilst login as an Admin user I was able to see the option to add a new product. I followed the link and the form appeared as planned.
I tried to add a product without an image. The form was tested and worked correctly. I was able to add the product as planned.

However whilst trying to add a product with an image I received a 500 error. After a lot of error checking and assistance from the tutor team, I managed to resolve the issue. 
This was resolved by removing the users key from the AWS bin and creating a new version. I then update the settings in my env file and Heroku. 
Ran a new deployment and the issue was resolved. I am now able to correctly add a product with an image.


Deleting A Product:

Whilst login as an Admin user I was able to see the option to delete a product. I followed the link and the product was deleted correctly.

Amending A product:

Whilst login as an Admin user I was able to see the option to amend a product. I followed the link and the form appeared as planned.
The process for completing the form as cecked and I was able to amend the product correctly.

### OTHER CHECKS: 

The profile section has also been checked and is working as planned. 

All forms have been fully checked for content and validation. 

My PC (21" Monitor) My Laptop and Notebook My girlfriends 17" Gaming Laptop Samsung Galaxy S9 Google Pixel 4 XL iPhone 8 iPad Pro, Windows 10 and Windows 7 Professional.

Checkout When testing the checkout process, you will be prompted to enter your payment details to complete payment. Please use the card numbers mentioned in this link to test this.

During my testing of the checkout process, I used the following test details:

Card Number: 4000 0082 6000 0000 CVC: Any 3 digits Date: Any future date

My friends and family have also been heavily involved in the testing of this application.

### Bugs Discovered

During the testing process, we noticed that the webhook function from stripe was not working correctly. After receiving excellent support from the tutors.

I noticed that the link pointing from the stripe to my javascript file was not set correctly. After amending the link everything now works as planned.

I received a 500 error whilst uploading product images. Resolved by updating the AWS keys. I deleted the old key and then created a new verson. Heroku end env files were then updated.

## DEPLOYMENT

### Hosting the database.

I started by creating a new app on Heroku. Then using their dashboard I added a postgres database. My next step was to disconnect the local database and start using the new heroku one. I achieved this by installing dj-database-url and psycopg2 then changing the DATABASE setting in the settings.py file.

Remembering to remove the import env.py line! I then migrated the database on Heroku to set it up. I then had to create a new superuser.
Finally used python3 manage.py loaddata command on the console to load my data categories and data into the new database.

### Hosting The Static Files

The static files are to be stored using amazon cloud services. I set up an account with AWS and configured a 'bucket' to store things in.
Once done installed boto3 and django-storages. Both of which are used by Django to connect to remote storage.
I then had to edit settings.py again to configure it to see the new storage. I than ran collectstatic to upload the local static files to Amazon's servers.

### Deploying to Heroku

I copied the environment variables from my local environment env.py file to the settings page on Heroku. 

The site is run using a program called gunicorn so I installed that next. Heroku needs a procfile to run stuff so I had to create that as well.
Finally, I had to update the requirements.txt file, addthe 'allowed hosts' in settings.py.
Debug mode is also set to False by updating a config seng the Heroku cont
Once all of this was complete, I pushed the code to gitn deployed the branch from heroku to make the site

## FUTURE 
I would like to add Social Networking Login.

A News and Blog Section.

## CREDITS

Code Institute - Tutor Support, and Course Material (Lessions, Tutor Support and Example Code).
Bootsrap.
Font Awsome.
Google Fonts.
Halfords.

I big thank you goes to:

My Partner for her patience, support and understanding whilst studying for this project and during the planning and coding process.

The excellent tutors, mentors and online community from the Code Institute.

My friends and family for their help and feedback whilst kindly testing the application.

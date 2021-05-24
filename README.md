Welcome! [github.com](https://github.com/GiovanniSalvi/New_Library)

# UX

## I realized this project as part of the Data centric development module that I am attending at "code academy" training course.

### The App is built for a librarian or whoever is in charge to run,create or manipulate data for a library.

### I tried to make the app interface as simple and easy as possible to navigate. The homepage provides a nav-bar menu to explore the app's functionalities which I will look into more in deep further on in the User-Story paragraph, and a footer which provides social media links.

### The nav menu, footer, home-button and background image are repeated in all website pages to get app style consistent.


---


## Project's Wireframes
* [Home Desktop](https://github.com/GiovanniSalvi/New_Library/blob/master/static/wireframes/New%20Wireframe%20Desktop%20home.png)

* [Home iPad](https://github.com/GiovanniSalvi/New_Library/blob/master/static/wireframes/Home%20ipad.png)

* [Home iPhone](https://github.com/GiovanniSalvi/New_Library/blob/master/static/wireframes/Home%20iphone.png)

* [AddBook Desktop](https://github.com/GiovanniSalvi/New_Library/blob/master/static/wireframes/AddBook%20desktop.png)

* [Registration iPad](https://github.com/GiovanniSalvi/New_Library/blob/master/static/wireframes/Registration%20ipad.png)

* [AddBook iPhone](https://github.com/GiovanniSalvi/New_Library/blob/master/static/wireframes/Addbook%20iphone.png)


## Project's Mockup screenshots

* [Homepage](https://github.com/GiovanniSalvi/New_Library/blob/master/static/mockups/Homepage.png)

* [Add_book](https://github.com/GiovanniSalvi/New_Library/blob/master/static/mockups/addBook.png)

* [Register](https://github.com/GiovanniSalvi/New_Library/blob/master/static/mockups/registerUser.png)

* [Remove](https://github.com/GiovanniSalvi/New_Library/blob/master/static/mockups/removeBook.png)

* [Editbook](https://github.com/GiovanniSalvi/New_Library/blob/master/static/mockups/editBook.png)

* [Sellbook](https://github.com/GiovanniSalvi/New_Library/blob/master/static/mockups/sellBook.png)

* [Userslist](https://github.com/GiovanniSalvi/New_Library/blob/master/static/images/User-list.png)

---

## Features:

### Existing features

* Feature1: Menu-bar provides a fluid navigation through the site.

* Feature2: Homepage's body provides a background hero-image, an home-button  which redirects users to the homepage, a complete list of book titles in the database, both "available" and "sold" status ('sold' ones are supposed to be removed)and a social media links footer.

* Feature3: Homepage provides any books in the library, wrapped in a box.Clicking button "Sell" inside the box to purchase the item selected if books status is Available.

* Feature4: Add_book nav link leads to form for adding new books to the database filling all required fields.Clicking Add button at the bottom page will add a new book title in the libray.

* Feature5: Remove_book link leads to search tab input.Typing the title it'll give access to the book title requested.Click button "remove" to delete the book selected.

* Feature6: Registration link leads to form for adding new users to the database filling all required fields.Clicking Submit button will add a new user in the libray database.

* Feature7: Clicking button "Edit" inside the boxes in the homepage, which contain books titles in stock, leads users to a form to edit the item.

* Feature8: UserList link leads to a fully displayed list of all users registered in the library's database.

* Feature9: Clicking a delete button inside the box where users details are showed will remove users details from the database. 

### Features left to implement

* Implement the app, adding a login functionality for users(Librarians) in the Homepage.

* Implement the app, adding E-Commerce functionality.

* Implement the app, adding on mongo.db a new database collection with users who are supposed to run the website,a librarian or anyone working in a library, which is the reason why this app is built.

* Implement the app, adding a functionality which allows to calculate the monthly library revenue.

* Implement the app, adding an Authentication and Security functionality.

---

# Technology used:

## Programming languages

* HTML

* CSS

* JAVASCRIPT

* PYTHON3/FLASK

### Libraries

* [Bootstrap.com](https://getbootstrap.com/)

---

## Testing

### In order to navigate easily through the site:
* In the homepage, users can find all [books title](https://github.com/GiovanniSalvi/New_Library/blob/master/static/images/test%20homepage.png) in the archive.At the top of the page are displayed [navbar](https://github.com/GiovanniSalvi/New_Library/blob/master/static/images/test%20navbar.png) links to navigate through the app.
and a [search tab](https://github.com/GiovanniSalvi/New_Library/blob/master/static/images/test%20search%20tab.png) to explore site contents just below

* Add_book link leads to the [form](https://github.com/GiovanniSalvi/New_Library/blob/master/static/images/test%20add%20form.png) to adding new books to the archive

* Remove_book link leads to a [search tab](https://github.com/GiovanniSalvi/New_Library/blob/master/static/images/test%20removeBook.png) to find the book title users are supposed to be removed, clicking delete button below the book features.

* Add_user link leads to the [form](https://github.com/GiovanniSalvi/New_Library/blob/master/static/images/test%20registration.png) to adding new users to the database.

* User_list link leads to a [page](https://github.com/GiovanniSalvi/New_Library/blob/master/static/images/userList.png) where all users details in the database are displayed. Users details contained in a box include all required fields to be registered. A [delete](https://github.com/GiovanniSalvi/New_Library/blob/master/static/images/deleteButton.png) button at the bottom of the box allows to remove one's user-details to be removed.

* Every box in the homepage contains a single product.[Edit button](https://github.com/GiovanniSalvi/New_Library/blob/master/static/images/test%20button.png) positioned at the bottom of the box leads users to a [form](https://github.com/GiovanniSalvi/New_Library/blob/master/static/images/updateBook.png) to update a book.
['Sell!'button](https://github.com/GiovanniSalvi/New_Library/blob/master/static/images/test%20button.png) next to edit button leads to a [form](https://github.com/GiovanniSalvi/New_Library/blob/master/static/images/sellBooks.png) to fill with users/buyer details in order to complete purchase operation.

* The [footer](https://github.com/GiovanniSalvi/New_Library/blob/master/static/images/test%20footer.png) provides social links.

### The project has been validated and beautified using:

* HTML:

    • Base:[https://validator.w3.org/nu/](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fgithub.com%2FGiovanniSalvi%2FNew_Library%2Fblob%2Fmaster%2Ftemplates%2Fbase.html)

    • add_task:[https://validator.w3.org/nu/](https://validator.w3.org/nu/?doc=https%3A%2F%2Fgithub.com%2FGiovanniSalvi%2FNew_Library%2Fblob%2Fmaster%2Ftemplates%2Fadd_task.html#textarea)

    • book_add:[https://validator.w3.org/nu/](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fgithub.com%2FGiovanniSalvi%2FNew_Library%2Fblob%2Fmaster%2Ftemplates%2Fbook_add.html)

    • book_selling:[https://validator.w3.org/nu/](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fgithub.com%2FGiovanniSalvi%2FNew_Library%2Fblob%2Fmaster%2Ftemplates%2Fbook_selling.html)

    • edit_task:[https://validator.w3.org/nu/](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fgithub.com%2FGiovanniSalvi%2FNew_Library%2Fblob%2Fmaster%2Ftemplates%2Fedit_task.html)

    • home:[https://validator.w3.org/nu/](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fgithub.com%2FGiovanniSalvi%2FNew_Library%2Fblob%2Fmaster%2Ftemplates%2Fhome.html)

    • register:[https://validator.w3.org/nu/](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fgithub.com%2FGiovanniSalvi%2FNew_Library%2Fblob%2Fmaster%2Ftemplates%2Fregister.html)

    • remove_book:[https://validator.w3.org/nu/](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fgithub.com%2FGiovanniSalvi%2FNew_Library%2Fblob%2Fmaster%2Ftemplates%2Fremove_book.html)

    • remove:[https://validator.w3.org/nu/](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fgithub.com%2FGiovanniSalvi%2FNew_Library%2Fblob%2Fmaster%2Ftemplates%2Fremove.html)

    • sell_book:[https://validator.w3.org/nu/](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fgithub.com%2FGiovanniSalvi%2FNew_Library%2Fblob%2Fmaster%2Ftemplates%2Fsell_book.html)
    
    • task:[https://validator.w3.org/nu/](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fgithub.com%2FGiovanniSalvi%2FNew_Library%2Fblob%2Fmaster%2Ftemplates%2Ftask.html)

    • user_list: [https://validator.w3.org/nu/](https://validator.w3.org/nu/?doc=https%3A%2F%2Fgithub.com%2FGiovanniSalvi%2FNew_Library%2Fblob%2Fmaster%2Ftemplates%2Fuser_list.html)

    • user_details [https://validator.w3.org/nu/](https://validator.w3.org/nu/?doc=https%3A%2F%2Fgithub.com%2FGiovanniSalvi%2FNew_Library%2Fblob%2Fmaster%2Ftemplates%2Fuser_details.html)


* HTML: [https://webformatter.com/](https://webformatter.com/)


* CSS: [https://jigsaw.w3.org/css-validator/](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fgithub.com%2FGiovanniSalvi%2FNew_Library%2Fblob%2Fmaster%2Fstatic%2Fcss%2Fstyle.css)

* CSS: [https://webformatter.com/](https://webformatter.com/)

* JAVASCRIPT: [https://jshint.com/](https://jshint.com/)

* JAVASCRIPT:<img width="1248" alt="javascript valid" src="https://user-images.githubusercontent.com/61980577/114250922-9266ea00-999f-11eb-9628-12fd7c548bcc.png">


* JAVASCRIPT: [https://webformatter.com/](https://webformatter.com/)


* PYTHON: [http://pep8online.com/](http://pep8online.com/)
* PYTHON: <img width="1440" alt="python code Validation" src="https://user-images.githubusercontent.com/61980577/119416537-c007b880-bceb-11eb-89bc-9c802b384b04.png">


### The quality of the website was measured using Google Lighthouse:

* Chrome lighthouse Tool: <img width="1272" alt="Google lighthouse" src="https://user-images.githubusercontent.com/61980577/114251782-9d6f4980-99a2-11eb-95e0-4448a491d57b.png">

---

### User stories :

1. As a User I want navigate the site to find what I need easily.

  • In every page of the site it's possible to navigate through easily, Home button displayed at the top right leads back from every pages of the site to the Homepage.
  
  • Navigation bar is easily to find  at the top of the Homepage.

2. As a User I want to have a quick access to the page which allows me to register new customer/users in the library database.

  • Register link which leads to the form to fill(all fields are required) in order to register new potential customer to the database is in the nav-bar of the Homepage , clicking button "submit" at the bottom of the form in order to complete the operation.A flash message shows if operation is successful.

3. As a User I want to find a simple way to check the status, location and others details of the books in the library.

  • In the Homepage users can find displayed any books currently in stock.

4. As a user I want to find a clear way to add a new book in the library's database.

  • Add_book link leads users to the form(all fields are required) which allows to add new books, filling the required details of the new item,than click the button "add" at the end of the form.A flash message shows if operation is successful.

5. As a user I want to find an easy way to remove a book from the database.

  • Remove link is at the top of the page, clicking on remove navbar-link leads user to a search tab which allows to find the book by its title, if the  book status is available, so item is currently in the library, click remove button at the bottom of the box to complete the operation.A flash message shows if operation is successful.
  
 6. As a user I want to find a quick way to sell a book requested by a potential customer.
 
  • In the search_book page navigabile by search_book navbar-link from the Homepage,a search tab allows to find any book in the library, if the book selected has a status of "Available" it makes possible the item saleable, clicking the "Sell Book" button at the bottom of the box leads to a users details form to complete the purchase.A flash message shows if operation is successful.
  
 7. As a user I want to access to the social networks in order to advertise or share new info about Library catalogue.
 
  • The footer is  at the bottom of any pages and provides few links to the most popular social networks across the worls(Facebook,Twitter)and other links to important platforms like Linkedin and Youtube.

  8. As a user I want to find a quick way to edit a book-title selected.

  • In the Homepage  all books in the archive are displayed wrapped in a box,clicking on the button "edit" at the bottom of the box leads user to an editable form to complete the operation.Updates the required input fields then clicking the button "update" at the bottom of the form.A flash message shows if operation was successful.

  9. As a user I want to find all clients details.

  • User list link in the navabar leads to a fully displayed list of all users registered in the library's database, users details are contained in a box which provides first and lastname of the user, an email address , data of birth, phone nuber and a post code.Clicking on the 'delete' button inside the box allows you to remove the user from the library.A search tab, above the boxes, allows to find any users already registered in the library inserting the 'firstname' of the user, in the search tab input.
  
  
### The project has beeen designed to make pages render well on a variety of devices and window or screen sizes such as:

* Desktop: (1600x992px) Responsivness tested using ChromeDev inspector tool, as shown in the screenshot below:
<img width="1280" alt="Desktop " src="https://user-images.githubusercontent.com/61980577/114227010-aea16180-9974-11eb-95b0-3550fe140c36.png">

* Laptop: (1280x802px) Responsivness tested using ChromeDev inspector tool, as shown in the screenshot below:
<img width="778" alt="Tablet" src="https://user-images.githubusercontent.com/61980577/114227748-aeee2c80-9975-11eb-8598-fea1fe8b83fd.png">

* Tablet
 1. ipad Pro: (1024x1366px) Responsivness tested using ChromeDev inspector tool, as shown in the screenshot below:
 <img width="778" alt="iPad pro" src="https://user-images.githubusercontent.com/61980577/114226984-a6492680-9974-11eb-940d-24226f31976f.png">

 2. iPad: (768x1024px) Responsivness tested using ChromeDev inspector tool, as shown in the screenshot below:
<img width="778" alt="iPad" src="https://user-images.githubusercontent.com/61980577/114227038-ba8d2380-9974-11eb-9410-0911269a9352.png">

* Mobile
 1. Moto G4 (360x640px) Responsivness tested using ChromeDev inspector tool, as shown in the screenshot below:
 <img width="778" alt="motog4" src="https://user-images.githubusercontent.com/61980577/114226958-9fbaaf00-9974-11eb-89f8-b7d05862f566.png">

 2. Galaxy S5 (360x640px) Responsivness tested using ChromeDev inspector tool, as shown in the screenshot below:
 <img width="778" alt="Galaxy s5" src="https://user-images.githubusercontent.com/61980577/114226927-9598b080-9974-11eb-8e92-b0513b1a1ca5.png">
 
 3. Iphone 6/7/8 Plus (414x736px) Responsivness tested using ChromeDev inspector tool, as shown in the screenshot below:
 <img width="778" alt="iPhone6:7 plus" src="https://user-images.githubusercontent.com/61980577/114227118-d98bb580-9974-11eb-862f-dfa4e3cf1ca8.png">

 4. Iphone 6/7/8 (375x667px) Responsivness tested using ChromeDev inspector tool, as shown in the screenshot below:
 <img width="778" alt="iPhone 6:7" src="https://user-images.githubusercontent.com/61980577/114226911-8f0a3900-9974-11eb-9f2e-3a32f4cc0646.png">
 
 5. Iphone X (375x812px) Responsivness tested using ChromeDev inspector tool, as shown in the screenshot below:
 <img width="778" alt="iPhone x" src="https://user-images.githubusercontent.com/61980577/114227081-c8db3f80-9974-11eb-9408-d72a5b271333.png">

 6. Surface Duo (540x720px) Responsivness tested using ChromeDev inspector tool, as shown in the screenshot below:
 <img width="778" alt="surface duo" src="https://user-images.githubusercontent.com/61980577/114226917-92052980-9974-11eb-8423-20f1d81445f4.png">


---

## Deployment

### This App was deployed on Heroku server with the following steps:

* Go to [Heroku](https://id.heroku.com/login) page where you can log in or sign up for the free account than complete password and email steps.

* Once you have created an Heroku free account, click on 'Create a new app' button to create an App, then give a name to the app and select a region.


### In order to deploy the project, you need to perform some steps:

    1. Open your IDE terminal, run heroku login and fill out required fields.

    2. Add heroku git repository replacing with the name of the app.

    3. Go back to Heroku dashboard click on  Settings tab, from here you can get the Heroku git URL.

    4. Back to the IDE terminal run 'git add remote heroku'

    5. Install Gunicorn using 'pip3 install gunicorn' command, which will be necessary as part of deployment.

    6. Create a requirenments.txt file 'pip3 freeze --local > requirements.txt', so that Heroku can identify the project as a python project and commit in your local git repository.

    7. Add a Procfile using 'echo web: gunicorn app:app > Procfile' command, which contains the name of the python file that runs your application and the name of the app.

    8. Add and commit using 'git add' and 'git commit -m "message"' commands.

    9. Finally push the app to Heroku using 'git push -u origin master' command.

    10. Check if the application is running, clicking 'Open app' button top left of the page on your app Heroku dashboard.

*   For any issues with the deployment you can check files and logs with following commands: heroku run bash -a app, heroku  logs --tail.
---

## Credits


## Media

* Social-media icons were provided from:

    [fontawesome.com](https://fontawesome.com/v4.7.0/icons/)


### Image

* Hero Image provide from:

    [Hero Image](https://cdn.wallpapersafari.com/62/74/WigTJs.jpg)

---

### Bugs 

  1. Not significant bugs found.
---

### Code  

* Add_task, Register forms and JS form validation were taken  from [getbootstrap.com](https://getbootstrap.com/docs/5.0/forms/validation/) and then modified to fit with the web page needs.


















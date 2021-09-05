# Classic Novels Review
This website called Classic Novels Review is a website for book enthusiasts that provides a way for them to keep track of their favourite books through a personal account, leave reviews for others on book they have read and read reviews others have written. The name Classic Novels Review clearly states what the site is about. It is specifically geared towards classic novels that are know to many.
The purpose of this website is to provide a way for people to keep track of their favourite books, contribute to the wider community by leaving reviews and learn from other community members as well through their reviews.

## Showcase
You can view the Classic Novels Review website [here](https://classic-novels-review.herokuapp.com/get_books).

![]()

## UX

### User Stories
My goal was to create a website with a vibe that is appealing to the reader and with an intuitive design that presents the books, the sign up and log in forms, and the profile functionality in a clear manner.
My second goal was to create a website that is available wherever the user is and that works smoothly in all devices, so that they can have their personal book list available whenever they need it.

#### First Time User Goals
- As a first time user I want to be able to easily understand what services you provide.
- As a first time user I want to be able to easily understand what the membership is about.
- As a first time user I want to know tha site easily accessible, especially if I'm going to sign up.

#### Returning User Goals
- As an account holder I want to be able to update my profile when I need to.
- As an account holder I want to be able to interact with the community.
- As an account holder I want to know your website is reliable on all devices I might use.

### Wireframes
For this project I made wireframes for five webpages within the website, namely

- The Home Page
- A page to view a single book in a large mode.
- A register page
- A login page
- And the profile  page

Each of the pages has three wireframes

- One for small screens
- One for medium screens
- One for large screens

The home page lists all books on the website while the second page focuses on the synopsis of each book.
The signup and login pages basically just contain simple forms for a clean design. Finally the profile page shows each account holders personal book list.

The wireframes were created using - [InVision](https://www.invisionapp.com/). 

You can view the wireframes [here](https://dennischmielewski323696.invisionapp.com/freehand/Classic-Novels-Review-EoIn0vC2r)

### Structure
The structure of the website is laid out in such a way that the books have the main focus only a nav bar at the top for navigation though the website. 
The home page displays all books and if you create an account you get your personal book list that you can edit. 
The difference between viewing the website publically and being a member is that the member can create and edit their personal book list and also leave reviews. A non-member can only view the whole library of books without being able to edit it.

### Design
To create an appealing feel to the website, I chose a mellow theme with green and white colors with not much extra going on around the books themselves to keep the main focus on the books, which I myself would want in such a website. 
For this reason I chose to just have the name 'Classic Novels Review' as the logo.
To make the website responsive I decided to go with Boostrap5 since it is an easy framework to work with that I have prior experience with. As a detail I added smooth scrolling behavior to the website to make the user experience more pleasant and seamless.

















## Deployment
The deployment of this project was accomplished using Gitpod and Git for version control. 
I used Gitpod to write all code and push all changes made to my Github Repository using Git from the Gitpod terminal.

### Repository
If you want to view this website locally on your computer:
- Click on your preferred clone method in the upper right-hand side corner of this repository.
- Open your cloned repository in your IDE of choice.
- Run the website on a local server from there.

This project reposity is hosted on  
- [GitHub](https://github.com/) - you can find it at [this link](https://github.com/tetrapak-dev/milestone-project-3)

### Hosting Platform
This website is hosted on [Heroku](https://www.heroku.com/home) and is deployed directly from the 'master' branch. The deployed website will update automatically when new changes are committed to the master branch. 

To host this website:
- I created a requirements.txt file using the terminal command 'pip freeze > requirements.txt'.
- Then created a Procfile with the terminal command 'echo web: python app.py > Procfile'.
- I added, committed, and pushed the files to the projects Github repository.
- After that I created a new app on the Heroku website by clicking the "New" button in the dashboard.
- From within the new app I clicked on settings --> deploy --> deployment method and then selected Github to connec the app to my Github repository.
- Lastly I added the necessary config vars for 'IP', 'dabase name', 'database URI', 'port', 'secret_key' and 'key' in order to make the app able to run.

The website can be viewed [here](https://classic-novels-review.herokuapp.com/)

![showcase_classic_novels_review.png](https://github.com/tetrapak-dev/milestone-project-3/blob/master/static/images/showcase_classic_novels_review.png)

## Credits

### Acknowledgements
- My mentor [Akshat Garg](https://github.com/akshatnitd) for his very much appreciated and needed advice and support.
- [Code Institute](https://codeinstitute.net/)'s Student Care and Slack community.

#### This project was made as part of Code Institute's Full Stack Software Development Programme. 
#### This is for educational purposes only.
#### Created by Dennis Chmielewski.
 
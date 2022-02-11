# Classic Novels Review
This website called Classic Novels Review is a website for book enthusiasts that provides a way for them to leave public reviews on book they have read and read reviews others have written. The name Classic Novels Review clearly states what the site is about. It is specifically geared towards classic novels that are know to many.
The purpose of this website is to create a platform for book lovers where they can both contribute to the wider community by leaving reviews and learn about potential books to read by reading reviews others have left.

## Showcase
You can view the Classic Novels Review website [here](https://classic-novels-review.herokuapp.com/).
![showcase_classic_novels_review.png](https://github.com/tetrapak-dev/milestone-project-3/blob/master/static/images/showcase_classic_novels_review.png)

## UX

### User Stories
My goal was to create a website with a vibe that is appealing to the reader and with an intuitive design that presents the book reviews, the sign up and log in forms, and the profile functionality in a clear manner.
My second goal was to create a website that is available wherever the user is and that works smoothly in all devices, so that they can read the reviews they and others have left wherever they want.

#### First Time User Goals
- As a first time user I want to be able to easily understand what services you provide.
- As a first time user I want to be able to easily be able to read reviews others have left.
- As a first time user I want to be able to easily understand what the membership is about.
- As a first time user I want to know the site easily accessible on computer and mobile devices, especially if I'm going to sign up.

#### Returning User Goals
- As an account holder I want to be able to leave reviews.
- As an account holder I want to be able to see the reviews I have left.
- As an account holder I want to be able to edit and/or delete reviews I have left.
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

During the development process the focus of the project shifted from the books themselves to focus more on the reviews. The main differences between the wireframes and the live site is that I left out the page to view a single book and that the site lists reviews rather than books. The main reason for this was that I had to lessen the scope of the project to meet the deadline.
The home page lists all reviews on the website while the account focuses on leaving reviews on the desired book.
The signup and login pages basically just contain simple forms for a clean design. 
Finally the profile page shows the reviews the user has left.

The wireframes were created using - [InVision](https://www.invisionapp.com/). 

You can view the wireframes [here](https://dennischmielewski323696.invisionapp.com/freehand/Classic-Novels-Review-EoIn0vC2r).
NOTE: The link to view the wireframes is not supported on the Firefox desktop browser but it works fine on mobile. It works fine on Chrome and Opera as well.

### Structure
The structure of the website is laid out in such a way that the reviews have the main focus. Only a navbar at the top for navigation through the website, a hero image along with welcome text and a footer is present otherwise.
The home page displays all reviews a stated above and if you create an account you get access to leaving reviews as well as editing and/or deleting reviews you have left. A non-member can only view the list of reviews without being able to interact with them. 

### Design
To create an appealing feel to the website, I chose a mellow theme with green and white colors with not much extra going on around the reviews themselves to keep the main focus on them rather anything else. The green theme with the brown in the hero image I think creates a cozy feeling which makes me want to read. This is what I myself would want in such a website. For this reason I also chose to just have the name 'Classic Novels Review' as the logo.
To make the website responsive I decided to go with Boostrap5 since it is an easy framework to work with that I have prior experience with. As a detail I added smooth scrolling behavior to the website to make the user experience more pleasant and seamless.

## Features
- Responsive Design across all device sizes, including a hamburger menu button on smaller screens.
- Functionality to read the reviews others have left.
- Functionality for users to create an account.
- Functionality to add, edit and delete reviews within the account.

#### Features Left to Implement
The following is a full list of features that will be implemented on a future release:

- Functionality for users to create their own book lists.
- A searchbox where the user can search for books.
- Emails sent to user for for resetting passwords.
- Function to delete account
- Showing one book in detail.
- Adding images to all books.

## Technologies
The technologies used to build this website are the following

#### Development
- [Gitpod Online IDE](https://www.gitpod.io/) for all code editing.
- [Firefox Devtools](https://developer.mozilla.org/en-US/docs/Tools) for all functional testing throughout the development process.

#### Testing
- [Lighthouse](https://developers.google.com/web/tools/lighthouse/) for performance testing of the website.
- [The W3C Markup Validator](https://validator.w3.org/) for testing of all HTML code.
- [The W3C CSS Validator](https://jigsaw.w3.org/css-validator/) for testing of all CSS code.

#### Images
- [Unsplash](https://unsplash.com/) for the image used on the website.
- [TinyPNG](https://tinypng.com/) for compressing project images.

#### Fonts & Icons
- [Google Fonts](https://fonts.google.com/share?selection.family=Noto%20Sans%20KR%7COpen%20Sans) for the fonstyles 'Noto Sans KR' and 'Open Sans' used on the website. 
- [Font Awesome](https://fontawesome.com/start) for all website icons.

### Languages 
- [HTML5](https://en.wikipedia.org/wiki/HTML5) was utilized for laying the foundation and structuring the basis of the website content. 
- [CSS3](https://en.wikipedia.org/wiki/CSS#CSS_3) was utilized for the placement and styling of all HTML5 content on the website. 
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) was utilized for creating animations on the website as well as creating interactivity with, and generating real-time information for the user.
- [Python3](https://www.python.org/downloads/) for handling user accounts and data with databases.

### Frameworks
- [Bootstrap v5.0](https://getbootstrap.com/docs/5.0/getting-started/introduction/) Bootstrap 5 was used to implement a responsive mobile-first design on the website.
- [Flask](https://palletsprojects.com/p/flask/) to create templates used for the website.

### Databases
- [MongoDB](https://www.mongodb.com/) for handling and storing user data when interacting with their account.

## Testing
Due to many difficulties along the way the site is not working properly as a whole.
The connection with the database works fine with both adding and deleting tasks.
The frontend is not working well at the moment. There is a problem with registration and the functionality that is supposed to be available only for registered users is available to non-registered users.

Testing was done for all user stories on the following devices and operating systems:

- Manually tested on Android on a Fairphone 3,  
- Manually tested on Linux Mint on an Dell XPS 15 Laptop.
- Manually tested on Windows 10 on an Dell XPS 15 Laptop.

- Tested on Iphone and several Android devices using Firefox Devtools.

- Test on an Ipad and Nexus Tablet using Firefox Devtools.


Results from Lighthouse performance test
![screenshot_lighthouse_report_viewer](static/images/screenshot_lighthouse_report_viewer.png)

The Lighthouse report came back around 75-85% on performance and accessibility. I them compressed the images but it only made a slight difference.

Results from W3C Markup Validator test
![w3c_html_validator_results](static/images/w3c_html_validator_results.png)

The Markup Validator came back with a few errors regarding the buttons. I tried to improve it but dit not manage to do it fully.

Results from W3C CSS Validator test
![w3c_css_validator_results](static/images/w3c_css_validator_results.png)

The CSS Validator came back with no issues at all.


#### Bugs Fixed
- Reversed the structure to make the reviews the main function, rather than the books which I had done from the beginning.
- Broken showcase link in README.md is now working properly. 

#### Bugs Left
- Buttons not showing when logged in.
- Book title and review title not showing in reviews.
- Bootstrap5 accordion not showing properly when logged in.
- Review info not loading into form when editing a review.
- Delete functionality available when logged out.
- Registration functionality does not work.

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
s
## Credits
- [The Grapes of Wrath](https://www.penguin.co.uk/books/26143/the-grapes-of-wrath/9780141185064.html)

- [The Adventures of Huckleberry Finn](https://www.penguin.co.uk/books/276485/the-adventures-of-huckleberry-finn/9780143107323.html)

- [1984](https://www.penguin.co.uk/books/1084996/nineteen-eighty-four/9781787302549.html)

- [Frankenstein](https://www.penguin.co.uk/books/183673/frankenstein/9780141198965.html)

- [Moby-Dick](https://www.penguin.co.uk/books/62240/moby-dick/9780142437247.html)

- [The Call of the Wild](https://www.penguin.co.uk/books/59518/the-call-of-the-wild/9780141321059.html)

- [Crime and Punishment](https://www.penguin.co.uk/books/35469/crime-and-punishment/9780140449136.html)

- [Brave New World](https://www.penguin.co.uk/books/34231/jane-eyre/9780141040387.html)

- [Pride and Prejudice](https://www.penguin.co.uk/books/1050871/pride-and-prejudice/9781857150018.html)

### Acknowledgements
- My mentor [Akshat Garg](https://github.com/akshatnitd) for his very much appreciated and needed advice and support.
- Code Institute's tutor Tim Nelson's video lessons on creating a backend project.
- [Code Institute](https://codeinstitute.net/)'s Student Care and Slack community.

#### This project was made as part of Code Institute's Full Stack Software Development Programme. 
#### This is for educational purposes only.
#### Created by Dennis Chmielewski.
 
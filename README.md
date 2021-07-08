# 1.0 Project Name: Human Resource Portal (HRP)
The aim of the project is to develop a custom application for Human Resource management of a company. The borrowed name of the company used in this case project is called MDB. 
The application consists of a home page for public users. The home page has a header bar, navigation bar, static image of employees in a meeting, a Self-service center for job seekers & employees, links to download future Android & ios mobile apps of the application, a brief note on the need for HRP and its success story, and finally a footer which also shows information about HRP and links to contact the developers.

The project is deployed to Heroku on https://human-resource-portal.herokuapp.com/


# 2.0 UX
The web Application is developed for Human Resource Managers of companies to effectively store and manage their employees' data, modify their employees' employment status, communicate internally with their employees, publish job advertisements to the public, receive job applications from prospective employees and send feedback to the applicants.

## 2.1 User stories
As Human Resource Manager (Admin/Super User), I want to:

1. create profile account for new employees which would contain their personal data.
2. enable the new employees' email addresses as their unique identifers which they can use to register on the HR Portal, so as to prevent unemployed/unauthorized persons from gaining access to Portal.
3. display individual employee's personal data and employment detail on their dashboard, accessible to them after they login
4. create new departments and modify existing departments in the company so as to group employees into appropriate departments based on their job roles and duties
5. view all employees list in a tabular form showing detail about their names, departments, date of employment, gender among others
6. send notice to all current employees accessible directly on their dashboard
7. receive comments, complains and feedback from all current employees
8. reply to employees' messages or delete the messages where necessary
9. modify and update indvidual employee's records or data existing in the company's database
10. delete employees' records and terminate their contract with the company
11. advertise new job vacancies to the public, receive applications online and send update to applicants
12. contact the developers' agent for technical support in case of any issue arising while using the application

As a current employee, I want to:
1. register on the HR Portal with my email successfully
2. login into the Portal with my email and password successfully
3. view my dashboard to see my personal data as it is in the company's record
4. read notifications sent to all employees by the HR manager
5. send my comments, complains and feedback to the HR office
6. receive response to my comments and complains from HR office
7. change my password at my own will
8. contact the developers' agent for Technical support such as in case I forget my password or for any other assistance
9. download mobile apps versions of the HR Portal if necessary

As a public user, I want to:
1. read brief information about the HR Portal
2. contact the developers in case I need to get the software for my own company's HR department
3. view exisitng career opportunities in the company, check current job vacancies, if any
4. apply for job online, in case there is vacancy, and get update from HR office in regard to my application
5. follow and connect to the company through their social media platforms 

## 2.2 Wireframes
In order to bring the idea of this project to life, wireframes were produced with the use of Figma. The folder named "wireframes" has been uploaded in this project's GitHub repository. The folder contains images of the wireframes designed to show Desktop, Tablet and Mobile views of various pages of the application


# 3.0 Features
## 3.1 Existing Features
1. This Web application basically consists of about twenty-three pages.

2. It consists of a top bar designed for Home page only. The top bar displays the project name and social media links by which users can connect to the company using the web application.

3. It also consists of a main navigation bar (navbar) that displays company's logo and menu items. This navigation bar is displayed across all pages of the application. Since there are three levels or categories of users, the menu items on this navbar are specifically selected to meet the needs of each user category. Public users can only view Home, Website, Register and Sign in menu links while registered employees who are logged in can view Home, Corporate and Profile menu links which has two submenu links named Dashboard and Logout. The highest level of user (Admin or HR manager) can view three additional menu links restricted to their official roles. The menu links are Internal Memo which comprises of Inbox & Notification submenu links, Operations which comprises of New Department & All Departments submenu links, and Employees which comprises of New Employees, Employee Directory & Manage Employees submenu links. 

4. It has a Home page particularly designed for public users and job seekers in mind. At the right side of the Home page is Self Service center where job seekers can expect to see existing vacancies as published by the Company's HR office. They can also apply for job through the Job Application link, check their job application status and get help from the Support team. If there are job vacancies, the HR office would update the Self Service section as needed. However, as at the time of developing this project, it was assumed that no vacancies existed yet due to the residual impact of COVID-19 pandemic. SO those links are working but no useful content in the pages since no vacancies existed. Job seekers could check again in future.

5. On the top left of the Home page is a static image of employees, happy on their jobs and holding a meeting. 

6. Also on the Home page, there are links to download ios & android mobile apps of this application in future. Although, there are no mobie apps available right now, but this is done in anticipation and as a way to improve use experience in future, such that employees can access their Portal anywhere and at anytime they wish, with the use of their mobile devices.  

6. Moreover, the Home page has three image links which allow current employees to login, contact Help Desk in case they forgot their passwords or username(email).

7. Coupled with the above, the Home page consists of a brief note about the application and its success story.

8. At the Home page footer section, there is brief information about the HR Portal and a link to read more about the application. The idea here was that those information can serve as advertisements for public users to consider using the software in managing their company's Human Resources. Public users could also contact to the developers and technical support team from the links provided at the footer section. 

7. The Home page footer section also consists of Quick links to navigate some important pages in the application.

8. It consists of a Register page which allows employees to register after the HR manager has created their profiles in the company's database records. The employees are required to use the same email address submitted to the HR office at their employment confirmation. No persons or individuals are allowed to register on the Portal without being duly documented as bonafide employees of the company

9. After successful registration, each employee can login to the HR Portal using their registered email and password created. For the purpose of granting access to Code Instistute's Project Assessment Team, the following login credentials are provided for them to login as Super/Admin user and have the HR manager's previledges. 

                   Email: admin@hrportal.com
                   Password: 1230master

10. The Login page consists of links to return to Home page and another link to navigate to Register page for new employees

11. Moreover, the Login page consists of link to go to Game page where employees can play a simple Shooting game, as they wish, in their lunch break time so as to relax and releive themselves from the regular stress of work. The game is a pure CSS game.

12. After successful login, employees get to their dashboard where they can view a welcome message, detail of their records with the company, their assigned duties and Attendance record. 

13. Also On the dashboard, there are links provided for employees to change their password, read industrial articles online and to contact Help Desk for support in case they encounter any issue while using the Portal.

14. Moreover, on the dashboard, there is a Complain form by which employees can send their complains, request or feedback to the HR Office directly. There is also a section on the dashboard where all employees can receive and read notifications sent from HR office. The latest notification is displayed in the space provided.

15. The Corporate page consists of general information to all employees about the company's Code of Conduct and Company Policy

16. Messages sent by employees to HR office are collected and viewable on Inbox page while the HR officer/manager can send general notice/message to all employees through the form provided on Notification page. Each message consists of two links for reply and delete. Reply can only be sent to the email of the sender. Both Inbox page and Notification page are accessible through Internal Memo menu link on the navbar. 

17. HR manager can create new departments through the form on New Department page while all existing departments in the company are accessible on All Departments page. On each department, there are two links for ediiting and deleting the department. Links to New Department and All Departments are accessible through Operations menu item on the navbar.

18. Furthermore, through Employees menu link, the HR manager can create profile for new employees through form available on New Employee page. Employees Directory page consists of a table that displays the list of all employess in the company. The list can be filtered by individual employee's name, department, email address or gender through a Live search bar on top of the table of employees. Manage Employees also consists of list of all employees grouped or categorized by their respective departments. An accordion is used for each department where each employee's record consists of two buttons; one for editing the employee's detail and the other button for deleting or terminating the employee from the company, an indication of firing or final dismisal.

19. A click on the Logout link, accessible through Profile menu link, would log out user and end their current session.

20. A click on the company's logo or the application's name on both top naigation bars would return all users to the Home page.


## 3.2 Features Left to Implement
1. To increase the capability of this application which would allow employees to be able to change their passwords without contacting Support team, in case they can't login to the portal as a result of forgotten password. They would be able change their password or create new password through a link that would be sent to their individual's email address.

2. Live counting of projects and customers with update on customer review to replace the static information on HR Portal Success story on Home page.

3. Links to download or revise Employees Code of conduct and the Company policy to be included on the Corporate page.

4. Each employee's attendance record available on their dashboard to be connected to the company's Clock in device that monitores employees' attendance

5. Record of each employee's payroll and account information to be included in thier respective profile


## 3.3 Languages and Technologies Used
HTML5: This project uses HTML5 for layout and main markup language

Material Design for Boostrap (MDB): It uses MD Bootstrap as Frontend Framework to design its layout and user interface

CSS3: The project uses CSS3 for for additional styling

Hover.CSS: It uses Hover.css for button hover

Font Awesome: It uses Font Awesome for Our services section, Team section and social links

JavaScript: It uses vanilla JavaScript for flash message close icon and cursor focus in Live search bar

Flask: It uses Flask microframework built on Python and which is based on Jinja Templating Method to write code that provides user authentication and othe functionalities

MongoDB: It uses NoSql database called MongoDB which stores user data that can be manipulated programmatically through CRUD operations

Heroku: It uses Heorku platform as a Service for deployment


4.0 Testing
All the internal and external links including menu items on navigation bar works well and the website looks good on Chrome, Mozilla and Edge browsers The website is responsive on mobile devices

4.1 Code Validation
HTML codes were tested with W3C MarkUp Validation Service. The codes returned with no error. HTML codes were tested with W3C CSS Validation Service. The codes returned with no error.

4.2 Testing Responsiveness
responsiveness-result

4.3 Testing Browser Compatibility
browser-compatibility-result

4.4 Testing User Story
As a user I want to:

read general information about the company including what they do: When a user logs on to the website, at the home page, he is able to view the specific areas of repair services and the category of devices that the company can handle for repair. In the about page, he is also provided a brief information about the company and their corporate goal

view the area of computer repair services offered by the company: A user is able to read about the technicians that work in the company with detail about their work experiences which can encourage the user to be confident in bringing repair jobs to the company

check if those areas of services meet my immediate needs: By reading through the information provided in the Service Section of home page, a user could be able to see id if the services provided by the company meet his needs

check the technicians that work in the repair center and be sure that they are qualified and certified to handle technical jobs in professional manner Our Team section on page was created to showcase the technicians that handle repair jobs for the company.

to contact the company and book an appointment by either filling a form, phone call or email A user could book an appointment by filling the form provided on the Booing page

to be able to connect with them on social media The social media icons on the Footer provide active links by which users or clients can connect to the company, post comments and follow the company

to be able to navigate well around the site The navigation bar provided at the top of the website allow users to navigate easily and conveniently to any desired parts of the website

4.5 Bugs
The bug I encountered was the navigation bar not displaying properly at mobile view because I used hamburger menu style. I fixed this bug by adding some media query for menu-item class by giving it a width 100% at max-width: 600px and making it important

At mobile view, menu items also displayed horizontally and scattered instead of vertically so I used clear both to separate them and make them display vertically in mobile view


5.0 Deployment
This project is hosted on GitHub as GitHub pages using this procedure:

Login into my GitHub account
On the navigation menu, click on Settings Tab on the right side
Scroll down to GitHub Pages Section
Click on the drop-down menu under Source and select Master Branch
I used Cayman theme for this project


6.0 Credits
6.1 Content
The code for Navigation bar was copied from here
The code for Goolge map was copied from here platform
The code for Carousel was copied from here
The code for Booking form and Contact form was copied from here

6.2 Media
The photos used in this site were obtained from Google images

6.3 Acknowledgement
The inspiration for this project was my personal idea


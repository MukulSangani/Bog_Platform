This Blog App is a scalable and reliable backend platform developed using Django Rest Framework (DRF) and PostgreSQL. It supports a wide range of users with different access levels and provides robust APIs for user authentication, blog management, and commenting features.

Features
User authentication (registration, login, social login)
Profile management (update user information)
Blog management (create, edit, delete, publish blogs)
Commenting system (add, upvote/downvote, delete comments)
Filtering and pagination for blog retrieval
Nested comments structure for replies
Secure user authentication and authorization

Python Version
Python 3.10

Project Structure
user/: Handles user management. Contains CRUD APIs to manage users.
blog/: Manages blog-related functionalities including creation, editing, and retrieval of blogs.
comments/: Manages comment functionalities including adding, upvoting/downvoting, and deleting comments.
api/: Contains all API views and serializers for the application.
config/: Configuration files for the Django project.

Running the Project Locally
Environment Setup

Ensure you have Python 3.10 installed on your machine.
Install PostgreSQL 15.10 and set up a database for the project.

Dependency Installation

Navigate to the project directory and run:
pip install -r requirements.txt

Application Startup Commands
Apply migrations: python manage.py migrate

Start the development server:
python manage.py runserver

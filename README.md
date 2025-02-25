# Discussion_platform
# Discussion_platform
# Discussion Platform

## Overview

This project is a discussion platform where users can sign up, log in, post discussions, comment on discussions, like posts and comments, follow other users, and search for posts based on hashtags or text content. It is built using Django and Django REST framework.

## Features

1. **User Management**
   - Sign up, log in, and log out
   - Create, update, and delete user profiles
   - Follow and unfollow users
   - Search users by name

2. **Discussions**
   - Create, update, and delete discussions
   - Add text and images to discussions
   - Like and unlike discussions
   - View count for each discussion
   - Search discussions by hashtags and text content

3. **Comments**
   - Add comments to discussions
   - Like and unlike comments
   - Edit and delete comments
   - Reply to comments

4. **Hashtags**
   - Manage hashtags for discussions
   - Search discussions by hashtags

## Installation

### Prerequisites

- Python 3.6+
- Django 3.2+
- Django REST framework
- Pillow
- django-filter
- drf-yasg

### Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/your-repository-name.git
   cd your-repository-name

2. Create a virtual environment and activate it:

python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

3. Install the dependencies:
pip install -r requirements.txt

4. Run migrations:
python manage.py makemigrations
python manage.py migrate

5. Create a superuser:
python manage.py createsuperuser

6. Run the development server:
python manage.py runserver

7. Access the application:

Open your web browser and navigate to http://127.0.0.1:8000


API Endpoints
Users
POST /users/ - Create a new user
PUT /users/{id}/ - Update user details
DELETE /users/{id}/ - Delete a user
GET /users/ - List all users
GET /users/?search={name} - Search users by name
Authentication
POST /auth/login/ - User login
POST /auth/signup/ - User signup
Discussions
POST /discussions/ - Create a new discussion
PUT /discussions/{id}/ - Update a discussion
DELETE /discussions/{id}/ - Delete a discussion
GET /discussions/ - List all discussions
GET /discussions/?tags={tag} - Get discussions by tag
GET /discussions/?text={text} - Get discussions by text
Comments
POST /comments/ - Create a new comment
PUT /comments/{id}/ - Update a comment
DELETE /comments/{id}/ - Delete a comment
GET /comments/ - List all comments
Hashtags
GET /hashtags/ - List all hashtags
Testing
A Postman collection is included in the project for testing the API endpoints. Import the postman-collection.json file into Postman to test the endpoints.

Contributing
Contributions are welcome! Please open an issue or submit a pull request for any changes.

License
This project is licensed under the MIT License.

Acknowledgments
Django
Django REST framework
drf-yasg for Swagger documentation

API Endpoints
Users
POST /users/ - Create a new user
PUT /users/{id}/ - Update user details
DELETE /users/{id}/ - Delete a user
GET /users/ - List all users
GET /users/?search={name} - Search users by name
Authentication
POST /auth/login/ - User login
POST /auth/signup/ - User signup
Discussions
POST /discussions/ - Create a new discussion
PUT /discussions/{id}/ - Update a discussion
DELETE /discussions/{id}/ - Delete a discussion
GET /discussions/ - List all discussions
GET /discussions/?tags={tag} - Get discussions by tag
GET /discussions/?text={text} - Get discussions by text
Comments
POST /comments/ - Create a new comment
PUT /comments/{id}/ - Update a comment
DELETE /comments/{id}/ - Delete a comment
GET /comments/ - List all comments
Hashtags
GET /hashtags/ - List all hashtags
Testing
A Postman collection is included in the project for testing the API endpoints. Import the postman-collection.json file into Postman to test the endpoints.

Contributing
Contributions are welcome! Please open an issue or submit a pull request for any changes.

License
This project is licensed under the MIT License.

Acknowledgments
Django
Django REST framework
drf-yasg for Swagger documentation
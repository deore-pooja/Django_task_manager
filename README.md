# Machine Test: Django REST API for User, Client, and Project Management

## Project Overview

This project involves building a set of RESTful APIs using Django for managing users, clients, and projects. The key functionalities of the project include:
- User registration and authentication.
- Client registration and management.
- Project creation and assignment.
- Assigning users to projects.
- Retrieving projects assigned to the logged-in user.

## Features

1. **User Management**:
   - User registration and login.
   - JWT authentication for secure access.

2. **Client Management**:
   - API for creating, updating, and deleting client information.
   - Listing all clients.

3. **Project Management**:
   - API to create and manage projects.
   - Assign users to specific projects.
   - Retrieve projects assigned to the logged-in user.

## Tech Stack

- **Backend**: Django, Django REST Framework (DRF)
- **Database**: SQLite (can be swapped with any other DB like PostgreSQL or MySQL)
- **Authentication**: JWT (JSON Web Token) for securing APIs
- **Tools**: Postman for API testing, Python 3.x

## Setup Instructions

### Prerequisites

- Python 3.x
- pip (Python package manager)
- Virtual environment (recommended)
- Django and Django REST Framework installed
- Postman (for testing APIs)

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/machine_test_project.git
   cd machine_test_project
Create a Virtual Environment (optional but recommended):

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Required Dependencies:

bash
Copy code
pip install -r requirements.txt
Run Migrations:

bash
Copy code
python manage.py makemigrations
python manage.py migrate
Run the Development Server:

bash
Copy code
python manage.py runserver
The application should now be running at http://127.0.0.1:8000/.

API Endpoints
Here is a list of key API endpoints:

## Demo

https://github.com/user-attachments/assets/2fc1e15f-531a-4a04-bdc1-d5f5077c6777

https://raw.githubusercontent.com/deore-pooja/Django_task_manager/master/Demo.mp4


Authentication
Register: POST /api/register/
Request: {"username": "your_username", "password": "your_password"}
Login: POST /api/login/
Request: {"username": "your_username", "password": "your_password"}
Client Management
Create Client: POST /api/clients/

Request: {"name": "Client Name", "email": "client_email@example.com"}
Get Clients: GET /api/clients/

Update Client: PUT /api/clients/<id>/

Request: {"name": "Updated Client Name", "email": "updated_client_email@example.com"}
Delete Client: DELETE /api/clients/<id>/

Project Management
Create Project: POST /api/projects/

Request: {"name": "Project Name", "client_id": <client_id>, "description": "Project description"}
Assign User to Project: POST /api/projects/<project_id>/assign/

Request: {"user_id": <user_id>}
Get Projects for Logged-in User: GET /api/my-projects/

Testing APIs
Using Postman:
Use Postman to test the endpoints.
Ensure to pass JWT tokens in the Authorization header (Bearer Token).
Running Tests
To run the tests, use the following command:

bash
Copy code
python manage.py test

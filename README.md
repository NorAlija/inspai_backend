
# Flask Web Application

It includes user authentication features such as registration, login, and logout. The application uses MySQL as the database to store user information.

## Overview

This project involes the development Flask-based web application designed for users to be able to login with the user that they registered. The application utilizes Flask, MySQL, Jinja templates and other related libraries.

## Technologies Used

- **Flask:** A lightwight web framework for Python
- **MySQL:** An open-source relational database managment system.
- **Jinja:** A fast, expressive, and extensible template engine for Python.
- **Python:** The programming language used for developing the application.
- **MySQL Server:** The programming language used for developing the application.

- Python 3.10.12
- Flask
- MySQL server


## Project Structure

- **init.py:** The main application file. It configures and creates the Flask app.

- **auth.py:** Manages user authentication, including registration, login, and logout.

- **db.py:** Handles database connections and provides functions to interact with the database.

- **templates:** Contains Jinja templates for the web pages.

- ## Application Components

### 1. `init.py`

The main application file responsible for configuring and creating the Flask app. Key configurations, such as MySQL parameters and secret key, are set here. The app's routes and blueprints are defined in this file.

### 2. `auth.py`

Manages user authentication features, including registration, login, and logout. Defines routes for user registration, login, and logout. Handles interactions with the database to check user credentials, hash passwords and manage user sessions.

### 3. `db.py`

Handles database connections and provides functions to interact with the MySQL database. Includes functions like `get_db` to obtain a database connection and `close_db` to close the connection. The `init_app` function initializes the app with the necessary teardown procedures.

### 4. Templates (`templates` directory)

Contains HTML templates for the web pages. Key templates include:
   - `base.html`: The base template for other pages, defining the structure and common elements.
   - `auth/register.html`: HTML template for the user registration page.
   - `auth/login.html`: HTML template for the user login page.

##Installation
## Installation

Follow these steps to set up and run the Flaskr web application:

### Prerequisites

- Python 3.10.12 
- MySQL server installed and running
- Flask installed

### 1. Clone the Repository

```bash
git clone <reposiotry_url>
cd your-repo
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate venv

```bash
. .venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install flask mysql-connector-python
```


## Conclusion

This Flask application serves as a simple yet robust authentication system with MySQL integration. The application structure follows the Flask best practices, employing an application factory pattern for creating the Flask instance and a blueprint for handling authentication-related routes. 

### Key Components:

- **`create_app` (init.py):** The application factory function initializes the Flask app, sets configuration parameters from environment variables, and registers blueprints.

- **`auth` Blueprint (auth.py):** Manages user registration, login, and logout functionalities. Passwords are securely hashed using Werkzeug's password hashing utility.

- **Database Connection (`get_db` in db.py):** Handles MySQL database connections, ensuring proper teardown and closure after each request.

- **Templates (base.html, register.html, login.html):** Implements a simple user interface with registration and login forms. Utilizes Jinja templating for dynamic content.

### Usage:

1. **Environment Variables:** Set the necessary environment variables for MySQL connection in your `.env` file.

2. **Database Initialization:** The application initializes the database connection using the provided configuration.

3. **User Registration:** Access the '/auth/register' route to register a new user, providing first name, last name, email, and password.

4. **User Login:** Use the '/auth/login' route for user login, requiring a valid email and password.

5. **User Logout:** Access the '/auth/logout' route to clear the session and log out the user.




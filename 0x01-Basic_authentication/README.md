# 0x01. Basic Authentication - Readme

## Project Overview

This project aims to help you understand and implement the **Basic Authentication** mechanism in a Flask-based API. You will learn how authentication works, how to encode strings in Base64, how the Authorization header functions, and how to implement Basic Authentication in an API using Flask.

### Background Context

In real-world applications, it is not advisable to implement your own authentication system. Frameworks like **Flask-HTTPAuth** provide secure implementations. However, for learning purposes, this project guides you through building a custom authentication system to understand the underlying principles.

## Learning Objectives

By the end of this project, you will be able to:

- Understand what authentication means.
- Explain Base64 encoding and how to implement it.
- Implement Basic Authentication for an API.
- Work with HTTP headers for sending Authorization data.

## Resources

To complete this project, the following resources will be helpful:

- **REST API Authentication Mechanisms**
- **Base64 in Python**
- **HTTP header Authorization**
- **Flask Documentation**
  
### Key Concepts:
- **Authentication**: The process of verifying the identity of a user or system.
- **Base64**: A method of encoding binary data into ASCII string format.
- **Basic Authentication**: A simple authentication scheme where the username and password are sent as a base64-encoded string in the HTTP Authorization header.
- **Flask**: A lightweight web framework for Python used for building APIs.

---

## Project Setup

### Requirements

- Python 3.7+
- Flask
- CORS (Cross-Origin Resource Sharing)

### Installation

1. Clone the repository and navigate to the project directory:

   ```bash
   git clone https://github.com/your-repo/alx-backend-user-data.git
   cd alx-backend-user-data/0x01-Basic_authentication
   ```

2. Install required dependencies:

   ```bash
   pip3 install -r requirements.txt
   ```

3. Set up the Flask server:

   ```bash
   API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
   ```

4. Access the API in a separate terminal using `curl`:

   ```bash
   curl "http://0.0.0.0:5000/api/v1/status" -vvv
   ```

---

## Project Tasks

### 1. Error Handler: Unauthorized

- Implement a 401 Unauthorized error handler that returns a JSON response `{"error": "Unauthorized"}`.
- Add a test route `/api/v1/unauthorized` to raise a 401 error using `abort(401)`.

### 2. Error Handler: Forbidden

- Implement a 403 Forbidden error handler that returns a JSON response `{"error": "Forbidden"}`.
- Add a test route `/api/v1/forbidden` to raise a 403 error using `abort(403)`.

### 3. Auth Class Implementation

- Create a class `Auth` in `api/v1/auth/auth.py` to manage the authentication system.
- Implement the following methods:
  - `require_auth(self, path, excluded_paths)`: Determines if a given path requires authentication.
  - `authorization_header(self, request)`: Retrieves the `Authorization` header from the request.
  - `current_user(self, request)`: Returns the current authenticated user.

### 4. Define Routes that Don't Need Authentication

- Update the `require_auth` method to exclude certain paths from authentication.
  - If `excluded_paths` contains the path, authentication is not required.
  - Ensure path is slash-tolerant (e.g., `/api/v1/status` and `/api/v1/status/` should be treated the same).

### 5. Request Validation

- Validate incoming requests:
  - Ensure the `Authorization` header is present.
  - Ensure the `current_user` method returns a valid user, or raise a 403 Forbidden error.

### 6. Basic Authentication

- Create a class `BasicAuth` that inherits from `Auth` and handles Basic Authentication.
- Update `api/v1/app.py` to switch between different authentication methods based on the `AUTH_TYPE` environment variable.

---

## File Structure

The project structure follows a modular Flask architecture:

```
├── api
│   └── v1
│       ├── app.py
│       ├── auth
│       │   ├── __init__.py
│       │   └── auth.py
│       ├── views
│       │   └── index.py
│       └── __init__.py
├── requirements.txt
└── README.md
```

### Key Files

- **api/v1/app.py**: Main Flask app file that contains routes, error handling, and the authentication mechanism.
- **api/v1/auth/auth.py**: Contains the `Auth` and `BasicAuth` classes to handle the authentication logic.
- **api/v1/views/index.py**: Contains API endpoints to test the functionality, including the unauthorized and forbidden routes.

---

## How to Test

### Running the Server

1. Start the Flask server:

   ```bash
   API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
   ```

2. Test the basic functionality:

   ```bash
   curl "http://0.0.0.0:5000/api/v1/status"
   ```

3. Test the error handling:

   - Unauthorized Error:
   
     ```bash
     curl "http://0.0.0.0:5000/api/v1/unauthorized"
     ```

   - Forbidden Error:
   
     ```bash
     curl "http://0.0.0.0:5000/api/v1/forbidden"
     ```

4. Test the authentication mechanism:

   - Without Authorization header:

     ```bash
     curl "http://0.0.0.0:5000/api/v1/users"
     ```

   - With invalid Authorization header:

     ```bash
     curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Test"
     ```

---

## Notes

- All API responses are in **JSON** format.
- The `AUTH_TYPE` environment variable determines which authentication method is used (either `basic_auth` or `auth`).
- Make sure to handle all error cases gracefully and ensure correct HTTP status codes are returned.

---

## Author

Abdelrhman Fikri

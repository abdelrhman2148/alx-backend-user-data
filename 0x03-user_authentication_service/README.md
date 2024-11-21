```markdown
# User Authentication Service

This project involves building a custom user authentication service using Python, Flask, SQLAlchemy, and bcrypt for educational purposes. While such systems are typically implemented using established frameworks, this project breaks down the core components to foster understanding.

## Learning Objectives

By the end of this project, you will learn:
- How to declare API routes in a Flask app.
- How to get and set cookies in Flask.
- How to retrieve form data from HTTP requests.
- How to handle HTTP status codes.
- The importance of password hashing and its implementation using bcrypt.
- The basics of session management and authentication mechanisms.

---

## Requirements

- **Languages and Tools**:
  - Python 3.7
  - Flask framework
  - SQLAlchemy 1.3.x
  - bcrypt library
- **Code Standards**:
  - Must adhere to PEP-8 (verified with `pycodestyle`).
  - Functions, modules, and classes must be well-documented.
  - All functions should be type-annotated.
- **Setup**:
  - Install bcrypt: `pip3 install bcrypt`.
- **System Compatibility**:
  - The project will be tested on Ubuntu 18.04 LTS.

---

## Project Tasks

### 0. **User Model**
Create a SQLAlchemy model `User` with the following attributes:
- `id`: Integer, Primary Key.
- `email`: Non-nullable string.
- `hashed_password`: Non-nullable string.
- `session_id`: Nullable string.
- `reset_token`: Nullable string.

**File**: `user.py`

---

### 1. **Create User**
Implement the `add_user` method in the `DB` class to:
- Accept `email` and `hashed_password` arguments.
- Save the user to the database.
- Return the created `User` object.

**File**: `db.py`

---

### 2. **Find User**
Create the `find_user_by` method in the `DB` class to:
- Search for a user using arbitrary filters.
- Raise `NoResultFound` or `InvalidRequestError` for errors.

**File**: `db.py`

---

### 3. **Update User**
Add the `update_user` method in the `DB` class to:
- Update user attributes passed as keyword arguments.
- Commit changes to the database.
- Raise `ValueError` for invalid attributes.

**File**: `db.py`

---

### 4. **Hash Password**
Define a `_hash_password` method that:
- Hashes a password using bcrypt.
- Returns the salted hash as bytes.

**File**: `auth.py`

---

### 5. **Register User**
Create the `Auth.register_user` method to:
- Register a new user with `email` and `password`.
- Hash the password before saving it.
- Raise `ValueError` if the email already exists.

**File**: `auth.py`

---

### 6. **Basic Flask App**
Set up a basic Flask application:
- Add a route `/` that returns a JSON message: `{"message": "Bienvenue"}`.

**File**: `app.py`

---

### 7. **Register User Endpoint**
Implement a POST `/users` route to:
- Register users with `email` and `password`.
- Respond with success or error messages in JSON format.

**File**: `app.py`

---

### 8. **Validate Credentials**
Define the `Auth.valid_login` method to:
- Validate email and password.
- Return `True` if valid, `False` otherwise.

**File**: `auth.py`

---

### 9. **Generate UUIDs**
Create a `_generate_uuid` method that:
- Returns a string representation of a new UUID.

**File**: `auth.py`

---

### 10. **Get Session ID**
Implement the `Auth.create_session` method to:
- Generate a session ID for a user based on their email.
- Store the session ID in the database.

**File**: `auth.py`

---

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/alx-backend-user-data.git
   cd alx-backend-user-data/0x03-user_authentication_service
   ```

2. Install dependencies:
   ```bash
   pip3 install -r requirements.txt
   ```

3. Run the Flask application:
   ```bash
   python3 app.py
   ```

4. Use `curl` or Postman to test endpoints.

---

## Testing
- Unit tests will be provided to validate each task.
- Run tests using:
  ```bash
  python3 -m unittest discover -s tests
  ```

---

## Resources
- [Flask Documentation](https://flask.palletsprojects.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [bcrypt Python Module](https://pypi.org/project/bcrypt/)
- [HTTP Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

---

## Author
**Abdelrhman Fikri**
```

# 0x00. Personal Data

## Project Overview
This project, part of ALX’s back-end development curriculum, focuses on handling sensitive user data responsibly. Specifically, it covers techniques for protecting Personally Identifiable Information (PII), securing database connections, and authenticating users by using encryption and filtering mechanisms.

**Project Scope:**
- Obfuscate PII in log files
- Use bcrypt for password encryption and validation
- Connect to a secure database using environment variables
- Handle logging and securely format sensitive data

## Learning Objectives
By the end of this project, you should be able to:
1. Identify various types of Personally Identifiable Information (PII).
2. Implement a logging filter to obfuscate sensitive fields.
3. Encrypt passwords securely and verify password validity.
4. Configure secure database access using environment variables.

## Requirements
- **Python Version**: All code will run on Python 3.7.
- **Style Guide**: Use `pycodestyle` (version 2.5) for code formatting.
- **Documentation**: Modules, classes, and functions must include docstrings.
- **Execution**: Files should be executable, with a new line at the end.
- **Type Annotations**: All functions must include type annotations.

## Files
### `filtered_logger.py`
Contains functions and classes for logging and obfuscating sensitive data.

### `encrypt_password.py`
Includes functions for password encryption and validation using the bcrypt library.

## Tasks

### Task 0: Regex-ing
Create a function `filter_datum` to obfuscate specific fields in a log message. 
- Fields will be obfuscated with a replacement string.
- The function should be concise and make use of `re.sub` for regex-based replacement.

### Task 1: Log Formatter
Implement the `RedactingFormatter` class to format log messages with filtered fields.
- The `format` method will filter out sensitive values in incoming log records using `filter_datum`.

### Task 2: Create Logger
Develop a `get_logger` function to return a configured `Logger` instance.
- This logger will filter PII and restrict logging levels to `INFO`.
- Define a tuple `PII_FIELDS` for all sensitive fields to mask.

### Task 3: Secure Database Connection
Implement `get_db` to securely connect to a MySQL database.
- Retrieve credentials using environment variables.
- This function returns a `mysql.connector.connection.MySQLConnection` object.

### Task 4: Read and Filter Data
Write a main function that:
- Connects to the database.
- Retrieves and logs user information in a filtered format to protect PII.

### Task 5: Encrypting Passwords
Define a `hash_password` function to hash passwords securely.
- Uses bcrypt to create a salted hash for storage.

### Task 6: Check Valid Password
Implement `is_valid` to check if an input password matches the hashed password.
- Uses bcrypt to validate password authenticity.

## Usage
### Logging Sensitive Data
```python
import logging

from filtered_logger import get_logger

logger = get_logger()
logger.info("name=Alice; email=alice@example.com; password=supersecret;")
```

### Password Encryption and Validation
```python
from encrypt_password import hash_password, is_valid

hashed = hash_password("MySecurePass123")
print(is_valid(hashed, "MySecurePass123"))  # Output: True
```

### Database Connection
Set environment variables to connect securely:
```bash
export PERSONAL_DATA_DB_USERNAME=root
export PERSONAL_DATA_DB_PASSWORD=yourpassword
export PERSONAL_DATA_DB_HOST=localhost
export PERSONAL_DATA_DB_NAME=yourdatabase
```

## Resources
- [What Is PII, Non-PII, and Personal Data?](https://example.com)
- [Python Logging Documentation](https://docs.python.org/3/library/logging.html)
- [bcrypt Documentation](https://pypi.org/project/bcrypt/)

## Author
Abdelrhman Fikri

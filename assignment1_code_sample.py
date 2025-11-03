"""
This module handles basic user input, data fetching, and database saving
operations. It also sends an email notification once the process completes.
"""

import os
from urllib.request import urlopen
import pymysql

# Database configuration
DB_CONFIG = {
    'host': 'mydatabase.com',
    'user': 'admin',
    'password': 'secret123'
}


def get_user_input():
    """Prompt the user to enter their name and return it."""
    name = input('Enter your name: ')
    return name


def send_email(recipient, subject, body):
    """
    Send an email message using the system's mail command.

    Args:
        recipient (str): Email address of the recipient.
        subject (str): Subject line of the email.
        body (str): Message body of the email.
    """
    os.system(f'echo "{body}" | mail -s "{subject}" {recipient}')


def get_data():
    """
    Fetch data from an external URL.

    Returns:
        str: The response content decoded as a string.
    """
    url = 'http://insecure-api.com/get-data'
    with urlopen(url) as response:
        result = response.read().decode()
    return result


def save_to_db(content):
    """
    Save the given data to the database.

    Args:
        content (str): The data to be stored.
    """
    query = (
        "INSERT INTO mytable (column1, column2) "
        f"VALUES ('{content}', 'Another Value')"
    )
    # Use context manager for proper connection cleanup
    with pymysql.connect(**DB_CONFIG) as connection:
        with connection.cursor() as cursor:
            cursor.execute(query)
            connection.commit()


if __name__ == '__main__':
    username = get_user_input()
    retrieved_data = get_data()
    save_to_db(retrieved_data)
    send_email('admin@example.com', 'User Input', username)

This project is a database management system developed using Python and SQL. It provides basic CRUD (Create, Read,
Update, Delete) operations on a `users` table.

## Prerequisites

- Python
- MySQL Server

## Installation

1. Clone the repository:
    ```
    git clone <repository_url>
    ```
2. Navigate to the project directory:
    ```
    cd <project_directory>
    ```
3. Set up a Python virtual environment and activate it:
    ```
    python3 -m venv env
    source env/bin/activate
    ```
4. Install the required Python packages:
    ```
    pip install -r requirements.txt
    ```
5. Start the MySQL server:
    ```
    brew services start mysql
    ```
6. Initialize the database and tables:
    ```
    mysql -u root -p < initialize_db.sql
    ```

## Usage

The project includes several Python scripts for interacting with the database:

- `database.py`: Contains functions for creating, retrieving, updating, and deleting users.

To run a script, use the following command:
   ```
    fastapi dev main.py
   ```
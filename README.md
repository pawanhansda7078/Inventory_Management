# Inventory Management System

An Inventory Management System built with Python and Tkinter, utilizing MySQL for database operations.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Database Schema](#database-schema)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Inventory Management System is a desktop application designed to help users manage inventory efficiently. It provides functionalities to sign up, log in, add items, update inventory, and manage user accounts.

## Features

- User Registration and Login
- Add new inventory items
- Update item details
- Display inventory items in a table format
- User-friendly GUI using Tkinter

## Installation

### Prerequisites

- Python 3.x
- MySQL Server
- `mysql-connector-python` package
- `tkinter` package (comes pre-installed with Python)

### Steps

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/inventory-management.git
    cd inventory-management
    ```

2. Install required Python packages:

    ```bash
    pip install mysql-connector-python
    ```

3. Set up the MySQL database:

    - Create a database named `project`.
    - Create a table named `users`:

      ```sql
      CREATE TABLE users (
          user_id INT PRIMARY KEY AUTO_INCREMENT,
          username VARCHAR(50) NOT NULL,
          password VARCHAR(50) NOT NULL
      );
      ```

    - Create a table named `added`:

      ```sql
      CREATE TABLE added (
          item_id INT PRIMARY KEY AUTO_INCREMENT,
          item_name VARCHAR(100),
          quantity INT,
          MRP DECIMAL(10,2)
      );
      ```

    - Create a table named `sold`:

      ```sql
      CREATE TABLE sold (
          item_id INT PRIMARY KEY AUTO_INCREMENT,
          item_name VARCHAR(100),
          quantity INT,
          MRP DECIMAL(10,2)
      );
      ```

4. Update database connection details in the Python scripts.

## Usage

1. Run the main script:

    ```bash
    python main.py
    ```

2. The main window will appear with options to sign up or log in.

3. After signing up or logging in, you can add, update, and view inventory items.

## Database Schema

### Users Table

| Field     | Type         | Description        |
|-----------|--------------|--------------------|
| user_id   | INT          | Primary Key        |
| username  | VARCHAR(50)  | Username of user   |
| password  | VARCHAR(50)  | Password of user   |

### Added Table

| Field     | Type          | Description           |
|-----------|---------------|-----------------------|
| item_id   | INT           | Primary Key           |
| item_name | VARCHAR(100)  | Name of the inventory item |
| quantity  | INT           | Quantity in stock     |
| MRP       | DECIMAL(10,2) | Maximum Retail Price  |

### Sold Table

| Field     | Type          | Description           |
|-----------|---------------|-----------------------|
| item_id   | INT           | Primary Key           |
| item_name | VARCHAR(100)  | Name of the inventory item |
| quantity  | INT           | Quantity sold         |
| MRP       | DECIMAL(10,2) | Selling Price         |

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License


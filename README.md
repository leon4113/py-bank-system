Certainly! Here's a potential README content based on the provided code:

---

# Banking System

This is a simple console-based banking system implemented in Python. It provides functionalities for creating and managing customer and admin accounts, logging in, changing passwords, withdrawing, depositing, checking balances, and generating account reports. The system offers three account types: superuser, admin, and customer.

## Features

- User authentication and account management.
- Superuser access for creating admin and customer accounts.
- Admin access for creating customer accounts, changing passwords, and generating reports.
- Customer access for account balance management and report generation.

## Installation

1. Make sure you have Python 3.x installed on your system.
2. Download or clone this repository to your local machine.
3. Open a terminal or command prompt and navigate to the repository directory.
4. Run the following command to execute the banking system:

```bash
python leonardo_banking_system.py
```

## Usage

1. Launch the banking system by following the installation instructions.
2. You will be presented with a login screen.
3. Enter your user ID and password.
4. Choose the appropriate menu option based on your account type: superuser, admin, or customer.
5. Follow the prompts to perform various banking operations.

## Account Types

- **Superuser**: Can create admin and customer accounts, display all existing accounts.
- **Admin**: Can create customer accounts, change passwords for themselves and customers, generate reports.
- **Customer**: Can manage their account balance, change passwords, generate account reports.

## Notes

- Passwords should be at least 6 characters long.
- Customer account types: 'C' for current, 'S' for saving.
- Initial balance requirements: 500 RM for current accounts, 100 RM for saving accounts.

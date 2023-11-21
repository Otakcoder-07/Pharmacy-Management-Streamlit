# Pharmacy Management System

The Pharmacy Management System is a web application built using [Streamlit](https://streamlit.io/) for managing pharmaceutical data, including company details, user information, drug inventory, sales history, and more. The system is designed to be user-friendly, providing both administrators and staff with the necessary tools to efficiently handle pharmacy-related tasks.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Admin Panel:**
  - Add and manage pharmaceutical companies.
  - Add and manage users with different roles (admin, staff).
  - Add drugs to the inventory, including details like name, type, barcode, dose, and more.

- **Staff Panel:**
  - View expiring drugs.
  - View total sales.

- **Shared Functionality:**
  - View sales history for a specific drug.
  - View information about drugs and their respective companies.
  - View total sales for each drug.

## Installation

To run the Pharmacy Management System locally, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/Pharmacy-Management-Streamlit.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Pharmacy-Management-Streamlit
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit application:

    ```bash
    streamlit run main.py
    ```

2. Open your web browser and navigate to the provided local URL.

3. Use the provided features based on your role (admin or staff).

## Contributing

If you'd like to contribute to this project, please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m "Add new feature"`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

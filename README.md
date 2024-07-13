# Restaurant Search System

Welcome to the Restaurant Search System, a Django-based application for searching through a database of restaurants.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project aims to create a robust search system using Django and SQLite, focusing on restaurants' names and details. It utilizes Django's powerful ORM and search capabilities to provide a seamless user experience.

## Features

- Search restaurants by name or location.
- Display detailed restaurant information.
- Responsive design for various devices.
- Integrated with SQLite for easy setup and deployment.

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/your-username/restaurant-search.git
   cd restaurant-search
   ```

2. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Apply migrations:

   ```
   python manage.py migrate
   ```

4. Load initial data (optional):

   ```
   python manage.py loaddata initial_data.json
   ```

5. Start the development server:

   ```
   python manage.py runserver
   ```

6. Access the application at `http://localhost:8000`.

## Usage

- Visit the homepage to search for restaurants using the search bar.
- Click on a restaurant to view detailed information.
- Navigate through the responsive interface for seamless user experience.

## Screenshots

![Screenshot 2024-07-13 140704](https://github.com/user-attachments/assets/912d877a-1f65-4b6d-81ed-743fe39c92ad)
![Screenshot 2024-07-13 140041](https://github.com/user-attachments/assets/f9e5009e-ed12-471b-9c8d-3cdd83b5927d)



## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements. For major changes, please open an issue first to discuss what you would like to change.

## License


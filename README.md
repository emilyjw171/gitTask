Shark Bait - Band Website

Welcome to Shark Bait, a Django-powered website for the fictional rock band "Shark Bait." This project includes user authentication, a band member showcase, and an album page where users can explore songs.

Features

User Registration & Login (Django’s built-in authentication system)

Album Page - View and explore band albums and songs

Band Members Page - Showcase the band’s lineup

Secure User Authentication

Built with:

Python (Django)

HTML, CSS

SQLite (default database)

Setup & Installation

Prerequisites

Ensure you have Python installed. You can check by running:

python --version

1️) Clone the Repository

git clone https://github.com/yourusername/sharkbait.git
cd sharkbait

2️) Set Up a Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3️) Install Dependencies

pip install -r requirements.txt

4️) Apply Migrations & Run the Server

python manage.py migrate
python manage.py runserver

Visit http://127.0.0.1:8000/ in your browser.

Project Structure

sharkbait/
│── band/              # Django app for band management
│   ├── migrations/
│   ├── templates/band/
│   │   ├── album.html
│   │   ├── home.html
│   │   ├── members.html
│   │   ├── register.html
│   │   ├── login.html
│   ├── views.py
│   ├── urls.py
│   ├── models.py
│   ├── admin.py
│── sharkbait/         # Main Django project settings
│── manage.py          # Django CLI commands
│── requirements.txt   # Project dependencies
│── README.md          # Project documentation

Setting Up Sphinx Documentation

1️) Install Sphinx

pip install sphinx

2️) Initialize Sphinx

sphinx-quickstart docs

Follow the prompts and choose:

Separate source and build directories? Yes

Project name: Shark Bait

Author name: Your Name

Project version: 1.0

Use autodoc? Yes

3️) Configure conf.py

Edit docs/source/conf.py and add:

import os
import sys
import django

sys.path.insert(0, os.path.abspath(".."))
os.environ["DJANGO_SETTINGS_MODULE"] = "sharkbait.settings"
django.setup()

4️) Generate API Documentation

sphinx-apidoc -o docs/source ../sharkbait

5️) Build Documentation

cd docs
make html

Open docs/build/html/index.html in a browser to view the documentation.

Running with Docker

1️) Build the Docker Image:

docker build -t sharkbait .

2️) Run the Container:

docker run -p 8000:8000 sharkbait

The app will be available at http://localhost:8000/.

Contributing

Fork the repository

Create a feature branch (git checkout -b feature-branch)

Commit your changes (git commit -m "Add new feature")

Push to GitHub (git push origin feature-branch)

Open a pull request

License

This project is licensed under the MIT License. 

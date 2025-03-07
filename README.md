# Shark Bait - Band Website 

Welcome to **Shark Bait**, a Django-powered website for the fictional rock band "Shark Bait." This project includes user authentication, a band member showcase, and an album page where users can explore songs.

## Features 
- **User Registration & Login** 
- **Album Page**
- **Band Members Page** 🎤
- **Secure User Authentication** (Django's built-in login/logout system)

 
- Python
- HTML, CSS
- SQLite

## Setup & Installation 

### Prerequisites
Ensure you have Python installed. You can check by running:
```sh
python --version
```

### Clone the Repository
```sh
git clone https://github.com/yourusername/sharkbait.git
cd sharkbait
```

### Install Dependencies
```sh
pip install -r requirements.txt
```

### Apply Migrations & Run the Server
```sh
python manage.py migrate
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

## Project Structure 
```
sharkbait/
│── band/
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
│── sharkbait/
│── manage.py
│── requirements.txt
│── README.md
```

## Contributing 
1. **Fork the Repository**
2. **Create a Feature Branch**
3. **Commit Changes**
4. **Push to GitHub**
5. **Open a Pull Request** 

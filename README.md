# Web Chat Application

This is a web chat application built using Python, Flask, and SQLite3. The application supports user account creation/registration, login, and real-time chat functionality using WebSockets.

## Project Structure

```
/c:/Users/tguen/Desktop/LocalProjects/WebChat_python/
│
├── app.py
├── database.py
├── requirements.txt
├── static/
│   └── css/
│       └── styles.css
└── templates/
    ├── chat.html
    ├── login.html
    └── register.html
```

## Setup Instructions

1. Clone the repository or download the source code.

2. Navigate to the project directory:

   ```sh
   cd /c:/Users/tguen/Desktop/LocalProjects/WebChat_python/
   ```

3. Create a virtual environment:

   ```sh
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```sh
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```sh
     source venv/bin/activate
     ```

5. Install the required dependencies:

   ```sh
   pip install -r requirements.txt
   ```

6. Run the application:

   ```sh
   python app.py
   ```

7. Open your web browser and navigate to `http://127.0.0.1:5000/` to access the application.

## Usage

- **Register**: Create a new user account by navigating to the registration page.
- **Login**: Log in with your registered username and password.
- **Chat**: Once logged in, you can send and receive messages in real-time with other users.

## Dependencies

- Flask==2.0.1
- Flask-SocketIO==5.1.1
- bcrypt==3.2.0

## License

This project is licensed under the MIT License.

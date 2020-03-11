from flask import Flask
from flask_bcrypt import Bcrypt
import sqlite3


def connectSQL():
    conn = sqlite3.connect('app/site.db')
    return conn, conn.cursor()


# Creates a Flask application
app = Flask(__name__)

# Creates a bcrypt oobject from the flask application
bcrypt = Bcrypt(app)

if __name__ == "__main__":
    # Creates the connection to the data base
    conn, cur = connectSQL()

    # Receive input data from the user in the console
    name = input("Enter first and last name: ")
    while not name.replace(" ", "").isalpha():
        print("Error: enter a valid name")
        name = input("Enter first and last name: ")
    while True:
        email = input("Enter an email: ")
        if email.replace("@", "").replace(".", "").isalnum() and "@" in email:
            break
        else:
            print("Error: enter a valid email")
    while True:
        password = input("Enter a password: ")
        while not password.isalnum():
            print("Error: enter a valid password")
            password = input("Enter a password: ")
        password2 = input("Enter the password againg: ")
        if password == password2:
            break
        else:
            print("The passwords didn't macth, please try again...")

    # Encrypt the password using bcrypt object before saving it in the database
    pw_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    try:
        # Query and values to execute
        query = """INSERT INTO users 
                    (name, email, password)
                    VALUES (?, ?, ?)"""
        values = (name, email, pw_hash)
        cur.execute(query, values)

        # Save changes in the data base
        conn.commit()

        # Closes the connection to the data base
        cur.close()
        conn.close()
    except Exception as e:
        print(str(e))
    else:
        print("Success!!")

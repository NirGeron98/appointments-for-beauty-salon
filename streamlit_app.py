import streamlit as st
import sqlite3
from sqlite3 import Error
from datetime import datetime
import pandas as pd

# Create a connection to the SQLite database
conn = sqlite3.connect('salon.db')
c = conn.cursor()

# Create a table for appointments if it doesn't exist
c.execute('''
    CREATE TABLE IF NOT EXISTS appointments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        phone_number TEXT,
        service TEXT,
        appointment_time TEXT
    )
''')
conn.commit()

def make_reservation(name, phone_number, service, appointment_datetime):
    # Insert the reservation into the database
    c.execute('''
        INSERT INTO appointments (name, phone_number, service, appointment_time)
        VALUES (?, ?, ?, ?)
    ''', (name, phone_number, service, appointment_datetime))
    conn.commit()

def admin_login():
    st.subheader("Admin Login")

    username = st.text_input("Username", key="username")
    password = st.text_input("Password", type="password", key="password")
    login_button = st.button("Login")

    if login_button:
        # Perform admin login verification here (you can replace the condition with your own logic)
        if username == "admin" and password == "maya":
            st.success("Login successful!")
            # Set the session state variable to True after successful login
            session_state.logged_in = True

def show_all_reservations():
    st.title("All Reservations")
    # Retrieve all appointments from the database
    c.execute('SELECT * FROM appointments')
    appointments = c.fetchall()

    if len(appointments) > 0:
        columns = [col[0] for col in c.description]
        df = pd.DataFrame(appointments, columns=columns)
        st.dataframe(df)
    else:
        st.write("No reservations found.")

# Define the SessionState class to manage session state variables
class SessionState:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

# Initialize the session state variable
session_state = SessionState(logged_in=False)

# Streamlit app code
def main():
    st.title("My Place - Maya Sela")

    # Initialize the page variable with a default value
    page = "Make a Reservation"

    # Login section in the sidebar
    st.sidebar.subheader("Admin Login")
    username = st.sidebar.text_input("Username", key="username")
    password = st.sidebar.text_input("Password", type="password", key="password")
    login_button = st.sidebar.button("Login")

    if login_button:
        # Perform admin login verification here (you can replace the condition with your own logic)
        if username == "admin" and password == "maya":
            st.sidebar.success("Login successful!")
            # Set the session state variable to True after successful login
            session_state.logged_in = True
            # Set the page to "All Reservations" after successful login
            page = "All Reservations"

    # Check if the admin is logged in before displaying the pages in the sidebar
    if session_state.logged_in:
        if st.sidebar.button("Logout"):
            session_state.logged_in = False
            page = "Admin Login"

        # Select the active page using the sidebar
        page = st.sidebar.selectbox("Select Page", ["All Reservations"], key="page_select")
        show_all_reservations()

    if page == "Make a Reservation":
        # Existing code for customer reservation
        st.header("Make a Reservation")
        name = st.text_input("Name", key="customer_name")
        phone_number = st.text_input("Phone Number", key="phone_number")
        service = st.selectbox("Service", ["Manicure", "Pedicure", "Facial Treatments"], key="service_select")
        appointment_date = st.date_input("Appointment Date", key="appointment_date")
        appointment_time = st.time_input("Appointment Time", key="appointment_time")

        if st.button("Make Reservation"):
            if name and phone_number and service and appointment_date and appointment_time:
                try:
                    # Combine the selected date and time into a single datetime object
                    appointment_datetime = datetime.combine(appointment_date, appointment_time)
                    current_datetime = datetime.now()
                    if appointment_datetime < current_datetime:
                        st.error("Invalid appointment time. Please choose a future date and time.")
                    else:
                        # Make the reservation and send the email
                        make_reservation(name, phone_number, service, appointment_datetime)
                        st.success("Reservation made successfully!")
                except ValueError:
                    st.error("Invalid appointment time format. Please select a valid date and time.")
            else:
                st.error("Please fill in all the fields.")

    elif page == "Admin Login":
        admin_login()

        # Show "All Reservations" only when the admin is logged in
        if session_state.logged_in:
            show_all_reservations()

if __name__ == '__main__':
    main()


# My Beauty Salon Reservation System

This is a Streamlit-based web application for managing a beauty salon's reservations. The application allows customers to book appointments for services and provides an admin interface for viewing all reservations.

## Features

- **Customer Reservation**: Customers can easily make a reservation by providing their name, phone number, and selecting a service along with the appointment date and time.
- **Admin Login**: Admins can log in to view all reservations made by customers.
- **Reservation Management**: All reservations are stored in an SQLite database, and admins can view all bookings in a tabular format.

## Installation

### Prerequisites

- Python 3.7 or higher
- Streamlit
- SQLite

### Step-by-Step Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/salon-reservation-system.git
   cd salon-reservation-system
   ```

2. **Install required dependencies:**

   Create a virtual environment and activate it (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts ctivate`
   ```

   Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**

   ```bash
   streamlit run salon_reservation.py
   ```

4. **Access the application:**

   Open your web browser and navigate to `http://localhost:8501`.

## Usage

### Customer Interface

- **Make a Reservation**: 
  - Enter your name and phone number.
  - Select the desired service (e.g., Manicure, Pedicure, Facial Treatments).
  - Choose the appointment date and time.
  - Click "Make Reservation" to confirm your booking.

### Admin Interface

- **Login**: 
  - Enter the admin credentials (`username: admin`, `password: admin_password`).
  - After successful login, you can view all reservations.
  
- **View All Reservations**: 
  - Admins can see a table with all reservations made by customers.

## Database

- The application uses SQLite to store reservation data.
- The database (`salon.db`) is created automatically upon running the application if it doesn't already exist.

## Future Enhancements

- Add more services and allow customers to select multiple services.
- Implement features for updating and canceling reservations.
- Improve security features for admin login.
- Enhance the UI/UX for a better user experience.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

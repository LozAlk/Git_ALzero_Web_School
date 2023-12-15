# --------------------------------------------------
# -- Databases => SQLite => Training On Everything --
# --------------------------------------------------

import sqlite3

def get_all_data():
    try:
        # Connect to the database
        db = sqlite3.connect('app.db')

        # Print success message
        print("Connected to the database successfully")

        # Setting up the cursor
        cr = db.cursor()

        # Fetch data from the "users" table
        cr.execute("SELECT * FROM users")
        results = cr.fetchall()

        # Print the number of rows in the table
        print(f"Database has {len(results)} rows.")

        # Loop through the results
        for row in results:
            print(f"UserID => {row[0]},", end=" ")
            print(f"Username => {row[1]}")

    except sqlite3.Error as err:
        print(f"Error reading: {err}")

    finally:
        if db:
            # Close the database connection
            db.close()
            print("Connection to the database is closed")

# Call the function to get and display all data
get_all_data()

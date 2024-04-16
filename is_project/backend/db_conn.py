import psycopg2


# Function to authenticate user credentials
def authenticate(username, password):
    # Establish a connection to the PostgreSQL database
    conn = psycopg2.connect(
        dbname='your_database_name',
        user='your_username',
        password='your_password',
        host='localhost'  # Change this to your PostgreSQL host if needed
    )

    # Create a cursor object
    cursor = conn.cursor()

    # Query to check if the username and password match
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    
    # Execute the query
    cursor.execute(query)

    # Fetch the result
    result = cursor.fetchone()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    # Check if the result is not None (i.e., user exists)
    if result:
        return True
    else:
        return False
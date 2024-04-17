import streamlit as st
import is_project.backend.db_conn as conn



# Streamlit UI
def main():
    st.title("Login Page")

    # Input fields for username and password
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Login button
    if st.button("Login"):
        if conn.authenticate(username, password):
            st.success("Logged in successfully!")
            # You can redirect the user to another page here
        else:
            st.error("Invalid username or password")

if __name__ == "__main__":
    main()

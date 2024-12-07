import streamlit as st

# Dictionary to store user credentials
users = {"admin": "password"}

# Function to check login credentials
def check_login(username, password):
    if username in users and users[username] == password:
        return True
    else:
        return False

# Function to create a new user
def create_user(username, password):
    if username in users:
        return False
    else:
        users[username] = password
        return True

# Streamlit app
st.title("Login Page")

# Tabs for login and sign up
tab1, tab2 = st.tabs(["Login", "Sign Up"])

with tab1:
    st.header("Login")
    username = st.text_input("Username", key="login_username")
    password = st.text_input("Password", type="password", key="login_password")
    if st.button("Login"):
        if check_login(username, password):
            st.success("Login successful!")
            st.write("Welcome, ", username)
        else:
            st.error("Invalid username or password")

with tab2:
    st.header("Sign Up")
    new_username = st.text_input("New Username", key="signup_username")
    new_password = st.text_input("New Password", type="password", key="signup_password")
    if st.button("Sign Up"):
        if create_user(new_username, new_password):
            st.success("User created successfully!")
        else:
            st.error("Username already exists")



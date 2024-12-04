import streamlit as st
st.set_page_config(page_title="Disaster Management App",page_icon=":house:",layout="wide")
st.markdown(
    """
    <style>
    .stApp {
        background-image:linear-gradient(130deg,rgba(228,4,0,0.9),rgb(236,244,11));
        background-position-x:initial;
        background-position-y:initial;
        background-attachment:initial;
        background-origin:initial;
        background-clip:initial;
        background-color:initial;
        background-size:cover;
        background-repeat:no-repeat;
        font-family:Arial,Helvetica,sans-serif;
        display:flex;
        justify-content:center;
        align-items:center;
        height:100vh;
        color:#fff;
        text-align:center;
    
      }
    </style>
    """,
    unsafe_allow_html=True
          
)

def home_page():
    st.title("Disaster Management App")
    st.write("Welcome to our app!")
def shelter_location_page():
    st.title("Shelter Location")
    st.map()
def food_supply_page():
    st.title("Food and Supply Management")
    st.write("Manage food and supplies here")
def donor_management_page():
    st.title("Donor Management")
    st.write("Manage donors here")
def recipient_registration_page():
    st.title("Recipient Registration")
    st.write("Register recipients here")
def volunteer_management_page():
    st.title("Volunteer Management")
    st.write("Manage volunteers here")
def about_us_page():
    st.title("About Us")
    st.write("Learn more about our team here")
pages = {
    "Home": home_page,
    "Shelter Location": shelter_location_page,
    "Food and Supply Management": food_supply_page,
    "Donor Management": donor_management_page,
    "Recipient Registration": recipient_registration_page,
    "Volunteer Management": volunteer_management_page,
    "About Us": about_us_page
}
page = st.selectbox("CHOOSE : ", list(pages.keys()))
pages[page]()
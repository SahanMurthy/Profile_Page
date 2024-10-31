import streamlit as st
from streamlit_option_menu import option_menu
import importlib.util
import os
from PIL import Image

st.set_page_config(
    page_title="Sahan N Murthy - Profile",
    page_icon="👨‍🎓",
    layout="wide"
)

# Custom CSS to improve the appearance
st.markdown("""
<style>
    .reportview-container {
        background: #1E1E1E;
    }
    .sidebar .sidebar-content {
        background: #262626;
    }
    .Widget>label {
        color: #FFFFFF;
    }
    .stRadio>div{
        color: #FFFFFF;
    }
    .stSelectbox>div>div>div {
        background: #262626;
        color: #FFFFFF;
    }
    .stTextInput>div>div>input {
        background: #262626;
        color: #FFFFFF;
    }
    .profile-content {
        display: flex;
        align-items: flex-start;
        gap: 2rem;
    }
    .profile-image {
        width: 200px;
        height: 200px;
        border-radius: 50%;
        overflow: hidden;
    }
    .profile-text {
        flex: 1;
    }
</style>
""", unsafe_allow_html=True)

def load_page_content(page_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, f"{page_name}.py")
    module_name = f"profile_page.{page_name}"

    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    if hasattr(module, 'main'):
        module.main()
    else:
        st.error(f"The {page_name} module does not have a 'main' function.")

# Navigation
with st.sidebar:
    st.title("Navigation")
    selected = option_menu(
        menu_title=None,
        options=["Home", "About Me", "Projects & Publications", "Experience", "Academic Details", "Skills & Languages"],
        icons=["house", "person", "book", "briefcase", "mortarboard", "tools"],
        menu_icon="cast",
        default_index=0,
    )

# Content
if selected == "Home":
    col1, col2 = st.columns([1, 2])
    
    with col1:
        try:
            image = Image.open("sahan.png")
            st.image(image, width=200, use_column_width=True)
        except FileNotFoundError:
            st.error("Profile image not found. Please ensure 'sahan_photo.png' is in the same directory as this script.")
    
    with col2:
        st.title("Welcome to My Profile")
        st.write("Please use the sidebar to navigate through different sections of my profile.")
        st.write("""
        Hello! I'm Sahan N Murthy, an Electronics and Communication Engineering student passionate about technology and innovation.
        Explore my profile to learn more about my projects, skills, experience, and academic journey.
        """)

elif selected == "About Me":
    st.title("About Me")
    load_page_content("1_About_Me")

elif selected == "Projects & Publications":
    st.title("Projects and Publications")
    load_page_content("2_Projects_and_Publications")

elif selected == "Experience":
    st.title("Experience")
    load_page_content("3_Experience")

elif selected == "Academic Details":
    st.title("Academic Details")
    load_page_content("4_Academic_Details")

elif selected == "Skills & Languages":
    st.title("Skills and Languages")
    load_page_content("5_Skills_and_Languages")


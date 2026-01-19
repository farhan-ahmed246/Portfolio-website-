import os
import streamlit as st
import requests
from PIL import Image
from streamlit_lottie import st_lottie
import webbrowser

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="My Webpage",
    page_icon="🎉",
    layout="wide"
)

# ---------------- Lottie Loader ----------------
def load_lottieurl(url):
    try:
        r = requests.get(url, timeout=10)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

# ---------------- Sidebar Theme ----------------
st.sidebar.title("Theme Settings")
theme = st.sidebar.radio("Select Theme", ["Light White", "Full White", "Black"])

if theme == "Light White":
    bg = "#f4f6f8"
    text = "#1f2937"
elif theme == "Full White":
    bg = "#ffffff"
    text = "#000000"
else:
    bg = "#0e1117"
    text = "#ffffff"

st.markdown(f"""
<style>
.stApp {{
    background-color: {bg};
    color: {text};
}}
</style>
""", unsafe_allow_html=True)

# ---------------- Header ----------------
st.subheader("My Personal Portfolio 👋")
st.title("Welcome to My Personal Portfolio")
st.write("This is a place where I share my projects and work.")
st.write("[LinkedIn Profile](https://www.linkedin.com/in/farhan-ahmed-05140b299)")

# ---------------- Lottie Animation ----------------
lottie_animation = load_lottieurl(
    "https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json"
)

left_col, right_col = st.columns(2)
with left_col:
    st.header("What I Do")
    st.markdown("""
    - Project Development  
    - Web / App Design  
    - Automation Tools  
    - Creative Solutions  
    """)
with right_col:
    if lottie_animation:
        st_lottie(lottie_animation, height=300)



# ---------------- Contact Info Buttons ----------------
st.subheader("Contact Me 📞✉️")
col1, col2 = st.columns(2)
with col1:
    if st.button("📞 WhatsApp / Call +92 336 3016943"):
        webbrowser.open_new_tab("https://wa.me/923363016943")
with col2:
    if st.button("📧 Email: ucristao37@gmail.com"):
        webbrowser.open_new_tab("mailto:ucristao37@gmail.com")

import os
import streamlit as st
from PIL import Image
import webbrowser
import requests
from streamlit_lottie import st_lottie

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="My Portfolio", page_icon="🎉", layout="wide")

# ---------------- Lottie Loader ----------------
def load_lottieurl(url):
    try:
        r = requests.get(url, timeout=10)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

# ---------------- THEME ----------------
st.sidebar.title("Theme Settings")
theme = st.sidebar.radio("Select Theme", ["Light White", "Full White", "Black"])

if theme == "Light White":
    bg = "#f4f6f8"
    text = "#1f2937"
elif theme == "Full White":
    bg = "#ffffff"
    text = "#000000"
else:
    bg = "#0e1117"
    text = "#ffffff"

st.markdown(f"""
<style>
.stApp {{
    background-color: {bg};
    color: {text};
}}
</style>
""", unsafe_allow_html=True)

# ---------------- TOP NAV BUTTONS ----------------
nav_cols = st.columns(3)
with nav_cols[0]:
    if st.button("📁 Projects"):
        st.session_state['section'] = "projects"
with nav_cols[1]:
    if st.button("📞 Contact Me"):
        st.session_state['section'] = "contact"
with nav_cols[2]:
    if st.button("📄 Download Resume"):
        st.session_state['section'] = "resume"

st.markdown("---")

# ---------------- DEFAULT SECTION ----------------
if 'section' not in st.session_state:
    st.session_state['section'] = "projects"

# ---------------- PROJECTS ----------------
projects = [
    {
        "title": "PDF GENERATOR",
        "description": "Automation tool using Python to generate PDFs easily.",
        "image": "proj2.png",
        "url": "https://www.linkedin.com/posts/farhan-ahmed-05140b299_pythondeveloper-automationtools-pdfgenerator-activity-7412236161559191552-jQlG"
    },
    {
        "title": "Airplane Flight",
        "description": "Streamlit app to manage airplane ticket registrations.",
        "image": "proj1.png",
        "url": "https://www.linkedin.com/posts/farhan-ahmed-05140b299_streamlit-pythonprojects-codingjourney-activity-7400967741312004097-J1_j"
    }
]

if st.session_state['section'] == "projects":
    st.subheader("📁 My Projects")
    for project in projects:
        cols = st.columns([3, 1])
        with cols[0]:
            st.write(f"### {project['title']}")
            st.write(project["description"])
            if os.path.exists(project["image"]):
                img = Image.open(project["image"])
                st.image(img, use_column_width=True)
            else:
                st.warning(f"Image nahi mila: {project['image']}")
        with cols[1]:
            st.markdown(
                f'<a href="{project["url"]}" target="_blank" '
                'style="display:block; background-color:#ff4b4b; color:white; padding:10px; '
                'text-align:center; border-radius:5px; text-decoration:none;">▶ Watch Now</a>',
                unsafe_allow_html=True
            )

# ---------------- CONTACT ----------------
elif st.session_state['section'] == "contact":
    st.subheader("📞 Contact Me")
    st.write("Reach me via WhatsApp, Email, or send a message directly:")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            '<a href="https://wa.me/923363016943" target="_blank" '
            'style="display:block; background-color:#25D366; color:white; padding:10px; '
            'text-align:center; border-radius:5px; text-decoration:none;">WhatsApp</a>',
            unsafe_allow_html=True
        )
    with col2:
        st.markdown(
            '<a href="mailto:fmukhtar420@gmail.com" target="_blank" '
            'style="display:block; background-color:#0072C6; color:white; padding:10px; '
            'text-align:center; border-radius:5px; text-decoration:none;">Email</a>',
            unsafe_allow_html=True
        )

    st.write("---")

    # ---------------- MESSAGE FORM ----------------
    with st.form("contact_form", clear_on_submit=True):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submit_button = st.form_submit_button("Send Message")
        if submit_button:
            if name and email and message:
                url = f"https://formsubmit.co/fmukhtar420@gmail.com?name={name}&email={email}&message={message}"
                webbrowser.open_new_tab(url)
                st.success("Message sent successfully!")
            else:
                st.error("Please fill all the fields before submitting.")

# ---------------- RESUME ----------------
elif st.session_state['section'] == "resume":
    st.markdown(
        '<a href="/mnt/data/53bf4c03-001e-499c-ba26-53bde8ca1b4e.docx" download '
        'style="display:inline-block; background-color:#555555; color:white; padding:10px 20px; '
        'text-align:center; border-radius:5px; text-decoration:none;">Download Resume</a>',
        unsafe_allow_html=True
    )

    st.write("---")

# ---------------- Skills ----------------
st.subheader("Skills 🛠️")
skills = ["HTML", "TypeScript", "JavaScript", "Python", "Agentic AI Engineer", "Next.js"]
st.write(", ".join(skills))

# ---------------- Social Buttons ----------------
st.write("Connect with me:")
col1, col2 = st.columns(2)
with col1:
    if st.button("🔗 LinkedIn"):
        webbrowser.open_new_tab("https://www.linkedin.com/in/farhan-ahmed-05140b299")
with col2:
    if st.button("🐙 GitHub"):
        webbrowser.open_new_tab("https://github.com/farhan-ahmed246")

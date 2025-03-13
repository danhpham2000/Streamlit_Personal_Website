import streamlit as st
from PIL import Image

# Page Configuration
st.set_page_config(page_title="Work Experience", page_icon="⚙️")

# Header Section
st.markdown(
    """
    <div style="background-color:#4CAF50; padding:10px; border-radius:10px;">
        <h1 style="color:white; text-align:center;">Work Experience ⚙️</h1>
    </div>
    """, unsafe_allow_html=True
)
st.markdown("---")

# Internship Overview
st.write(
    """
    <p style="font-size:18px; line-height:1.6;">
    💼 During my academic journey, I have immersed myself in internships as a <strong>Software Engineer</strong> 
    at multiple companies, gaining hands-on experience in backend development, team collaboration, 
    and product delivery.
    </p>
    """, unsafe_allow_html=True
)


# Motate Sheridan Experience
st.markdown("## 1. 🏢 Motate ")
st.markdown("<h4>📍 Location: Sheridan, Wyoming (Remote) </h4>", unsafe_allow_html=True)
st.markdown("<h4 style='color:#FF5722;'>👨‍💻 Software Engineering Intern</h4>", unsafe_allow_html=True)
st.markdown("<p style='color:#2196F3;'>🗓️ February 2025 - Present</p>", unsafe_allow_html=True)

st.write(
    """
    <ul>
        <li>👥 <strong>Team Management Feature:</strong> Led the creation and implementation of a comprehensive team management feature for platform growth.</li>
        <li>📧 <strong>Email Verification System:</strong> Developed a secure email verification process to enhance account integrity.</li>
        <li>🔑 <strong>Password Reset System:</strong> Spearheaded the development of a secure password reset feature for better user security.</li>
        <li>⚙️ <strong>Settings & Preferences:</strong> Architected a user-friendly settings management system to improve user satisfaction.</li>
    </ul>
    """, unsafe_allow_html=True
)

st.markdown("### 🛠️ Technologies Used")
st.write("⚛️ React, 🎨 ShadCN, 💅 Tailwind CSS, 🐍 Python, ⚡ FastAPI, ☁️ AWS")

# Footer
st.markdown(
    """
    <div style="background-color:#2196F3; padding:10px; border-radius:10px; margin-top:20px;">
        <p style="color:white; text-align:center; font-size:16px;">
        🚀 My experience in backend development, security, and user experience has been enriched through diverse projects in fast-paced environments.
        </p>
    </div>
    """, unsafe_allow_html=True
)

st.markdown("<br></br>", unsafe_allow_html=True)


# Life Stages Experience
st.markdown("## 2. 🌱 Life Stages")
st.markdown("<h4>📍 Location: San Francisco, CA (Remote) </h4>", unsafe_allow_html=True)

logo_ls = Image.open("file/logo.jpg")
st.image(logo_ls, width=300, caption="Life Stages")

st.markdown("<h4 style='color:#FF5722;'>👨‍💻 Software Engineering Intern</h4>", unsafe_allow_html=True)
st.markdown("<p style='color:#2196F3;'>🗓️ September 2023 - May 2024</p>", unsafe_allow_html=True)

st.write(
    """
    <ul>
        <li>🔒 <strong>Secure Backend Development:</strong> Built a scalable backend infrastructure with user registration and validation using Firebase Authentication.</li>
        <li>🔧 <strong>User Preference Management:</strong> Developed a dynamic preference selection feature integrated with Firestore.</li>
        <li>✅ <strong>Quality Assurance:</strong> Applied systematic testing, reducing post-launch errors by <strong>30%</strong>.</li>
    </ul>
    """, unsafe_allow_html=True
)


st.markdown("### 🛠️ Technologies Used")
st.write("⚛️ React Native, 📊 Node.js, 🚀 Express.js, 🔥 Firebase")



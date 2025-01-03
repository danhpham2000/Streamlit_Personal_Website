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
    During my academic journey, I completed a 1-year internship as a <strong>Software Engineer</strong> 
    at a healthcare startup, gaining hands-on experience in backend development, team collaboration, 
    and product delivery.
    </p>
    """, unsafe_allow_html=True
)

# Company Information with Logo
st.markdown(
    """
    <div style="display:flex; align-items:center;">
        <h5 style="margin-right:10px;">Life Stages</h5>
    </div>
    """, unsafe_allow_html=True
)
logo = Image.open("file/logo.jpg")
st.image(logo, width=300, caption="Life Stages")

# Role and Duration
st.markdown("<h4 style='color:#FF5722;'>Software Engineering Intern</h4>", unsafe_allow_html=True)
st.markdown("<p style='color:#2196F3;'>September 2023 - May 2024</p>", unsafe_allow_html=True)

# Internship Details
st.write(
    """
    <p style="font-size:16px; line-height:1.6;">
    I began my internship at Life Stages on <strong>September 22nd, 2023</strong>. 
    After the onboarding meeting, I joined the backend team, collaborating closely with a 
    small yet dedicated group comprising 8 interns, 1 development lead, a product manager, and the CEO.
    </p>
    """, unsafe_allow_html=True
)

# Achievements Section
st.markdown(
    """
    <h3 style="color:#4CAF50;">Achievements & Key Responsibilities</h3>
    <ul style="font-size:16px; line-height:1.8;">
        <li>🎯 <strong>Secure Backend Development:</strong> Built a scalable backend infrastructure with user registration and validation, utilizing Firebase Authentication to safeguard data integrity and confidentiality.</li>
        <li>⚙️ <strong>User Preference Management:</strong> Engineered a dynamic user preference selection feature, seamlessly integrated with REST API endpoints for Firestore operations.</li>
        <li>🔍 <strong>Quality Assurance:</strong> Applied systematic testing methodologies, reducing post-launch error reports by <strong>30%</strong> and significantly enhancing user satisfaction.</li>
    </ul>
    """, unsafe_allow_html=True
)

# Technologies Used Section
st.markdown(
    """
    <h3 style="color:#FF5722;">Technologies Used</h3>
    <div style="font-size:16px; line-height:1.8;">
        <ul>
            <li>🌐 <strong>Frontend:</strong> React Native</li>
            <li>🖥️ <strong>Backend:</strong> Node.js, Express.js</li>
            <li>☁️ <strong>Cloud Services:</strong> Google Firebase (Authentication, Firestore)</li>
        </ul>
    </div>
    """, unsafe_allow_html=True
)

# Footer Section with Highlight
st.markdown(
    """
    <div style="background-color:#2196F3; padding:10px; border-radius:10px; margin-top:20px;">
        <p style="color:white; text-align:center; font-size:16px;">
        This experience honed my skills in backend development, testing, and cross-functional collaboration within a fast-paced startup environment.
        </p>
    </div>
    """, unsafe_allow_html=True
)

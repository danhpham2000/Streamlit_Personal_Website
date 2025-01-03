import streamlit as st

# Page Configuration
st.set_page_config(page_title="Education", page_icon="🎓")

# Header Section
st.markdown(
    """
    <div style="background-color:#673AB7; padding:10px; border-radius:10px;">
        <h1 style="color:white; text-align:center;">Education 🎓</h1>
    </div>
    """, unsafe_allow_html=True
)
st.markdown("---")

# Education 1: San Francisco State University
st.markdown(
    """
    <h2 style="color:#FF5722;">San Francisco State University</h2>
    <p><strong>Location:</strong> San Francisco, CA</p>
    <p><strong>Degree:</strong> Bachelor of Science in Computer Science</p>
    <p><strong>Duration:</strong> August 2022 - December 2024</p>
    <p><strong>Status:</strong> <span style="color:#4CAF50;">Graduated</span></p> 
    <h6 style="font-weight: bold; color: #FF5722;">Relevant Coursework:</h6>
    <ul style="font-size:16px; line-height:1.8;">
        <li>📚 Data Structures and Algorithms</li>
        <li>📐 Linear Algebra</li>
        <li>🌐 Web Development</li>
        <li>💻 Computer Architecture</li>
        <li>🖥️ Operating Systems</li>
        <li>📊 Probability and Statistics</li>
        <li>🤖 Machine Learning</li>
        <li>🧠 Deep Learning</li>
        <li>🔬 Data Science of Personalized Medicine</li>
        <li>🛠️ Software Development and Engineering</li>
        <li>💾 Database Systems</li>
    </ul>
    """, unsafe_allow_html=True
)
st.markdown("---")

# Education 2: San Jose City College
st.markdown(
    """
    <h2 style="color:#FF9800;">San Jose City College</h2>
    <p><strong>Location:</strong> San Jose, CA</p>
    <p><strong>Degree:</strong> Associate in Science in Mathematics</p>
    <p><strong>Duration:</strong> January 2019 – May 2022</p>
    <p><strong>Status:</strong> <span style="color:#4CAF50;">Graduated</span></p> 
    """, unsafe_allow_html=True
)

st.markdown("---")

# Footer Section
st.markdown(
    """
    <div style="background-color:#2196F3; padding:10px; border-radius:10px; margin-top:20px;">
        <p style="color:white; text-align:center; font-size:16px;">
        Education is the foundation for my continuous learning journey and drives my passion for building impactful technologies.
        </p>
    </div>
    """, unsafe_allow_html=True
)

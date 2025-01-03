import streamlit as st

# Page Configuration
st.set_page_config(page_title="Projects", page_icon="💻")

# Header Section
st.markdown(
    """
    <div style="background-color:#673AB7; padding:10px; border-radius:10px;">
        <h1 style="color:white; text-align:center;">Projects 💻</h1>
    </div>
    """, unsafe_allow_html=True
)
st.markdown("---")

# Project 1: Mind Learning
st.markdown(
    """
    <h2 style="color:#FF5722;">Mind Learning (HackTX 2024)</h2>
    <p><strong>Duration:</strong> November 2024 – Present</p>
    <ul style="font-size:16px; line-height:1.8;">
        <li>🚀 <strong>AI-Powered E-Learning Platform:</strong> Developed a platform that personalizes educational pathways using real-time assessments for tailored learning experiences.</li>
        <li>⚡ <strong>Gemini API Optimization:</strong> Reduced response time from 7 seconds to 2 seconds through schema definition, enhancing interaction speed and platform efficiency.</li>
        <li>🔐 <strong>Secure Authentication:</strong> Integrated JWT and OAuth2 protocols within React and NestJS, enabling seamless user registration, login, and personalized session management.</li>
        <li>📂 <strong>Data Handling:</strong> Configured PostgreSQL for efficient data handling and indexing, supporting rapid storage and retrieval of user profiles, assessments, and adaptive learning paths.</li>
    </ul>
    <a href="https://devpost.com/software/mind-learning" style="color:#3F51B5; font-size:16px;" target="_blank">🔗 View Project</a>
    """, unsafe_allow_html=True
)
st.markdown(
    """
    <h3 style="color:#FF5722;">Technologies Used for Mind Learning (HackTX 2024)</h3>
    <div style="font-size:16px; line-height:1.8;">
        <ul>
            <li>🌐 <strong>Frontend:</strong> React</li>
            <li>🖥️ <strong>Backend:</strong> NestJS, FastAPI</li>
            <li>📊 <strong>Database:</strong> PostgreSQL</li>
            <li>🤖 <strong>AI/ML:</strong> Python</li>
            <li>🔗 <strong>APIs:</strong> Gemini API</li>
        </ul>
    </div>
    """, unsafe_allow_html=True
)

st.markdown("---")

# Project 2: Music Buddy
st.markdown(
    """
    <h2 style="color:#FF9800;">Music Buddy (HackUTA 6)</h2>
    <p><strong>Duration:</strong> October 2024 – Present</p>
    <ul style="font-size:16px; line-height:1.8;">
        <li>🎵 <strong>Music Platform Development:</strong> Architected a music platform with Angular frontend, Hono microservices on Bun runtime, and AWS for scalable cloud infrastructure.</li>
        <li>🔐 <strong>Authentication:</strong> Built secure authentication flows using AWS Cognito and custom microservices, ensuring seamless user experiences.</li>
        <li>🎶 <strong>Machine Learning for Music Analysis:</strong> Designed a Python-based service using AudioFlux for mood detection and personalized recommendations based on user behavior.</li>
    </ul>
    <a href="https://devpost.com/software/musical-analysis-generative-ai-playlists" style="color:#3F51B5; font-size:16px;" target="_blank">🔗 View Project</a>
    """, unsafe_allow_html=True
)
st.markdown(
    """
    <h3 style="color:#FF9800;">Technologies Used for Music Buddy (HackUTA 6)</h3>
    <div style="font-size:16px; line-height:1.8;">
        <ul>
            <li>🌐 <strong>Frontend:</strong> Angular</li>
            <li>🖥️ <strong>Backend:</strong> Bun, Hono</li>
            <li>📊 <strong>Database:</strong> PostgreSQL (TypeORM)</li>
            <li>☁️ <strong>Cloud Services:</strong> AWS (Amplify, S3, EC2, Cognito)</li>
            <li>🤖 <strong>AI/ML:</strong> Python (AudioFlux)</li>
        </ul>
    </div>
    """, unsafe_allow_html=True
)

st.markdown("---")

# Project 3: Credit Score Classification
st.markdown(
    """
    <h2 style="color:#4CAF50;">Credit Score Classification</h2>
    <p><strong>Duration:</strong> December 2023</p>
    <ul style="font-size:16px; line-height:1.8;">
        <li>📊 <strong>Machine Learning Model:</strong> Developed a neural network model to classify credit scores, achieving 79% accuracy on a dataset of 100,000 records.</li>
        <li>🤝 <strong>Collaboration:</strong> Worked with 2 team members to clean and standardize a dataset for scalability across 27 features.</li>
        <li>📜 <strong>Documentation:</strong> Documented model configurations and performance for knowledge transfer to a team of 30 people in under a week.</li>
    </ul>
    """, unsafe_allow_html=True
)
st.markdown(
    """
    <h3 style="color:#4CAF50;">Technologies Used for Credit Score Classification</h3>
    <div style="font-size:16px; line-height:1.8;">
        <ul>
            <li>🤖 <strong>Machine Learning:</strong> Python, TensorFlow, Keras</li>
            <li>☁️ <strong>Cloud:</strong> Google Colabs</li>
            <li>📊 <strong>Dataset:</strong> 100,000 credit records</li>
        </ul>
    </div>
    """, unsafe_allow_html=True
)


# Footer Section
st.markdown(
    """
    <div style="background-color:#2196F3; padding:10px; border-radius:10px; margin-top:20px;">
        <p style="color:white; text-align:center; font-size:16px;">
        These projects demonstrate my ability to build scalable applications, optimize AI integrations, and deliver impactful solutions across diverse domains.
        </p>
    </div>
    """, unsafe_allow_html=True
)

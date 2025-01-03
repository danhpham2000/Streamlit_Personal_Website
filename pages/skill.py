import streamlit as st

# Create a dictionary for each category of skills
skills = {
    "Languages": ["Python", "JavaScript", "SQL", "Java", "C#", "C/C++", "PHP", "TypeScript"],
    "Frameworks and Libraries": [
        "React", "React Native", "Next.js", "Angular", "Bootstrap", "Sass", "Tailwind CSS",
        "Streamlit", "FastAPI", "Node.js", "Express.js", "Bun", "Hono", "NestJS", "ASP.NET",
        "Spring Boot", "Hibernate", "Sequelize", "Mongoose", "Prisma", "TensorFlow", "Keras",
        "PyTorch", "Pandas", "NumPy", "Matplotlib", "Seaborn"
    ],
    "Databases": ["MySQL", "PostgreSQL", "SQLite", "Microsoft SQL Server", "MongoDB", "Firebase", "Redis"],
    "Tools": ["AWS", "Google Cloud Platform", "Git", "GitHub", "Docker", "JUnit", "GraphQL", "Tableau", "Postman", "Visual Studio Code", "Jupyter Notebook", "Google Colabs", "IntelliJ"]
}

# Set up the page
st.set_page_config(page_title="Technical Skills", page_icon="🛠️")

# Header Section
st.markdown(
    """
    <div style="background-color:#673AB7; padding:10px; border-radius:10px;">
        <h1 style="color:white; text-align:center;">Technical Skills 🛠️</h1>
    </div>
    """, unsafe_allow_html=True
)

# Create grid layout for each category
category_colors = {
    "Languages": "#FF5722",  # Red
    "Frameworks and Libraries": "#2196F3",  # Blue
    "Databases": "#4CAF50",  # Green
    "Tools": "#FF9800"  # Orange
}

for category, items in skills.items():
    # Get the color for the category title
    category_color = category_colors.get(category, "#000000")  # Default to black if no color is defined

    # Apply color to category title
    st.markdown(f"<h2 style='color:{category_color};'>{category}</h2>", unsafe_allow_html=True)
    
    # Create a grid of skills
    columns = st.columns(4)  # Create 4 columns for the grid
    for i, item in enumerate(items):
        col = columns[i % 4]  # Cycle through the columns
        col.button(item)  # Display each skill as a button

# Create a plain text for download
download_content = ""
for category, items in skills.items():
    download_content += f"{category}\n"
    for item in items:
        download_content += f"- {item}\n"
    download_content += "\n"


# Footer Section
st.markdown(
    """
    <div style="background-color:#2196F3; padding:10px; border-radius:10px; margin-top:20px;">
        <p style="color:white; text-align:center; font-size:16px;">
        These technical skills represent my strong foundation in software development, cloud computing, machine learning, and data analysis.
        </p>
    </div>
    """, unsafe_allow_html=True
)

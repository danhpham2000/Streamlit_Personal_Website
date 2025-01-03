import streamlit as st


experience = st.Page("pages/experience.py", title="Experience", icon=":material/work_history:")
project = st.Page("pages/project.py", title="Project", icon=":material/assignment:")
education = st.Page("pages/education.py", title="Education", icon=":material/school:")
skill = st.Page("pages/skill.py", title="Skills", icon=":material/psychology:")
main = st.Page("pages/main.py", title="Home", icon=":material/person:")


pg = st.navigation([main, experience, project, education, skill ])

pg.run()




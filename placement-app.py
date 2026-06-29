import pickle
import pandas as pd
import streamlit as st


#load model
placement_model = pickle.load(open("student_placement_model.pkl", "rb"))


# Page Configuration
st.set_page_config(
    page_title="Student Placement Prediction",
    page_icon="🎓",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>

.stApp{
    background: linear-gradient(to right,#667eea,#764ba2);
}

.main-title{
    text-align:center;
    color:white;
    font-size:42px;
    font-weight:bold;
}

.sub-title{
    text-align:center;
    color:#f1f1f1;
    font-size:18px;
}

[data-testid="stVerticalBlock"]{
    border-radius:15px;
}

div[data-testid="stButton"]>button{
    background:#00c853;
    color:white;
    font-size:20px;
    font-weight:bold;
    border-radius:10px;
    width:100%;
    height:55px;
}

div[data-testid="stButton"]>button:hover{
    background:#009624;
    color:white;
}

input{
    border-radius:8px !important;
}

</style>
""", unsafe_allow_html=True)



#app interface
# Title
st.markdown("<h1 class='main-title'>🎓 Student Placement Prediction</h1>", unsafe_allow_html=True)

st.markdown("<p class='sub-title'>Enter the student's details to predict placement status.</p>", unsafe_allow_html=True)

st.write("")

# Two-column layout
col1, col2 = st.columns(2)

with col1:
    cgpa = st.number_input("CGPA", 0.0, 10.0)
    internships = st.number_input("Internships", 0, 20)
    projects = st.number_input("Projects", 0, 50)
    workshops_certifications = st.number_input("Workshops/Certifications", 0, 50)
    aptitude_test_score = st.number_input("Aptitude Test Score", 0, 100)

with col2:
    soft_skills_rating = st.number_input("Soft Skills Rating", 0.0, 5.0)
    extracurricular_activities = st.number_input("Extracurricular Activities", 0,1)
    placement_training = st.selectbox("Placement Training", [0, 1])
    ssc_marks = st.number_input("SSC Marks", 0, 100)
    hsc_marks = st.number_input("HSC Marks", 0, 100)


input_df = pd.DataFrame({
    "CGPA": [cgpa],
    "Internships": [internships],
    "Projects": [projects],
    "Workshops/Certifications": [workshops_certifications],
    "AptitudeTestScore": [aptitude_test_score],
    "SoftSkillsRating": [soft_skills_rating],
    "ExtracurricularActivities": [extracurricular_activities],
    "PlacementTraining": [placement_training],
    "SSC_Marks": [ssc_marks],
    "HSC_Marks": [hsc_marks]
})


#predicting placement
placement_analysis = ''
if st.button("Predict the Placement Results"):
    placement_prediction = placement_model.predict(
        [[cgpa, internships, projects, workshops_certifications, aptitude_test_score, extracurricular_activities, placement_training, soft_skills_rating, hsc_marks, ssc_marks]]
        )

    if (placement_prediction[0] == 1):
        placement_analysis = '🎉 Congratulations! Student is likely to be PLACED.'
        st.balloons()
    else:
        placement_analysis = '❌ Student is likely to be NOT PLACED.'
            
st.success(placement_analysis)
#!/usr/bin/env python3
"""
Ta'allim Teacher Dashboard
AI-powered English teaching platform for Algerian teachers

Usage:
    cd C:\Users\Admin\Projects\active\teacher-dashboard
    streamlit run app.py
"""

import streamlit as st
import json
import os
import random
from datetime import datetime

# Page config
st.set_page_config(
    page_title="Ta'allim Teacher Dashboard",
    page_icon="📚",
    layout="wide",
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1e293b;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #64748b;
        margin-bottom: 2rem;
    }
    .stat-card {
        background: linear-gradient(135deg, #2563eb 0%, #10b981 100%);
        padding: 1.5rem;
        border-radius: 12px;
        color: white;
        text-align: center;
    }
    .stat-number {
        font-size: 2.5rem;
        font-weight: 700;
    }
    .stat-label {
        font-size: 0.9rem;
        opacity: 0.9;
    }
    .section-header {
        font-size: 1.5rem;
        font-weight: 600;
        color: #1e293b;
        margin: 2rem 0 1rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #e2e8f0;
    }
</style>
""", unsafe_allow_html=True)

# Load topics data
@st.cache_data
def load_topics():
    topics_path = os.path.join(os.path.dirname(__file__), "..", "..", "My Drive", "LifeWorkspace", "10_Education_Project", "Exercise_Generator", "data", "topics")
    topics = {}
    for level in ["A1", "A2", "B1", "B2"]:
        file_path = os.path.join(topics_path, f"{level}.json")
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                topics[level] = data.get("topics", [])
    return topics

# Session state
if "generated_exercises" not in st.session_state:
    st.session_state.generated_exercises = []
if "lesson_plans" not in st.session_state:
    st.session_state.lesson_plans = []

# Header
st.markdown('<p class="main-header">📚 Ta\'allim Teacher Dashboard</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">AI-powered English teaching for Algerian schools</p>', unsafe_allow_html=True)

# Sidebar navigation
page = st.sidebar.selectbox(
    "Navigate to",
    ["Dashboard", "Lesson Planner", "Exercise Generator", "Assessment Creator", "Class Analytics"]
)

# Dashboard page
if page == "Dashboard":
    st.markdown('<p class="section-header">📊 Dashboard Overview</p>', unsafe_allow_html=True)
    
    # Stats
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-number">34</div>
            <div class="stat-label">Grammar Topics</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-number">4</div>
            <div class="stat-label">Levels (A1-B2)</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-number">6</div>
            <div class="stat-label">Exercise Types</div>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-number">275+</div>
            <div class="stat-label">Exercises Ready</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Recent activity
    st.markdown('<p class="section-header">📝 Recent Activity</p>', unsafe_allow_html=True)
    
    if st.session_state.generated_exercises:
        for exercise in st.session_state.generated_exercises[-5:]:
            st.info(f"Generated {exercise['type']} exercise for {exercise['topic']} ({exercise['level']})")
    else:
        st.info("No recent activity. Start generating exercises!")
    
    # Quick actions
    st.markdown('<p class="section-header">⚡ Quick Actions</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("📝 Generate Exercise", use_container_width=True):
            st.session_state.page = "Exercise Generator"
            st.rerun()
    with col2:
        if st.button("📋 Create Lesson Plan", use_container_width=True):
            st.session_state.page = "Lesson Planner"
            st.rerun()
    with col3:
        if st.button("📊 View Analytics", use_container_width=True):
            st.session_state.page = "Class Analytics"
            st.rerun()

# Lesson Planner page
elif page == "Lesson Planner":
    st.markdown('<p class="section-header">📋 Lesson Planner</p>', unsafe_allow_html=True)
    
    # Input form
    with st.form("lesson_plan_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            level = st.selectbox("Level", ["A1", "A2", "B1", "B2"])
            topics = load_topics().get(level, [])
            topic_names = [t["name"] for t in topics]
            topic = st.selectbox("Topic", topic_names)
        
        with col2:
            duration = st.selectbox("Duration (minutes)", [30, 45, 60, 90])
            class_size = st.number_input("Class Size", min_value=10, max_value=50, value=30)
        
        submitted = st.form_submit_button("Generate Lesson Plan")
    
    if submitted:
        # Find topic details
        topic_data = next((t for t in topics if t["name"] == topic), None)
        
        if topic_data:
            # Generate lesson plan
            lesson_plan = {
                "level": level,
                "topic": topic,
                "duration": duration,
                "class_size": class_size,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "stages": [
                    {
                        "name": "Warm-up",
                        "duration": f"{duration // 6} min",
                        "activities": [
                            "Greeting and attendance",
                            "Review of previous lesson",
                            f"Introduction to {topic}"
                        ]
                    },
                    {
                        "name": "Presentation",
                        "duration": f"{duration // 3} min",
                        "activities": [
                            f"Present {topic} through examples",
                            "Drill pronunciation",
                            "Check understanding"
                        ]
                    },
                    {
                        "name": "Practice",
                        "duration": f"{duration // 3} min",
                        "activities": [
                            "Controlled practice exercises",
                            "Pair work activities",
                            "Individual practice"
                        ]
                    },
                    {
                        "name": "Production",
                        "duration": f"{duration // 6} min",
                        "activities": [
                            "Free practice activity",
                            "Role play or discussion",
                            "Creative application"
                        ]
                    },
                    {
                        "name": "Wrap-up",
                        "duration": f"{duration // 10} min",
                        "activities": [
                            "Review key points",
                            "Assign homework",
                            "Preview next lesson"
                        ]
                    }
                ]
            }
            
            st.session_state.lesson_plans.append(lesson_plan)
            
            # Display lesson plan
            st.success("✅ Lesson plan generated!")
            
            st.markdown(f"### {level} - {topic}")
            st.markdown(f"**Duration:** {duration} minutes | **Class Size:** {class_size} students")
            
            for stage in lesson_plan["stages"]:
                with st.expander(f"📌 {stage['name']} ({stage['duration']})"):
                    for activity in stage["activities"]:
                        st.markdown(f"- {activity}")
    
    # Display saved lesson plans
    if st.session_state.lesson_plans:
        st.markdown('<p class="section-header">📋 Saved Lesson Plans</p>', unsafe_allow_html=True)
        
        for i, plan in enumerate(st.session_state.lesson_plans):
            with st.expander(f"📝 {plan['level']} - {plan['topic']} ({plan['timestamp']})"):
                st.markdown(f"**Duration:** {plan['duration']} minutes | **Class Size:** {plan['class_size']} students")
                for stage in plan["stages"]:
                    st.markdown(f"**{stage['name']}** ({stage['duration']})")
                    for activity in stage["activities"]:
                        st.markdown(f"  - {activity}")

# Exercise Generator page
elif page == "Exercise Generator":
    st.markdown('<p class="section-header">🎯 Exercise Generator</p>', unsafe_allow_html=True)
    
    # Input form
    with st.form("exercise_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            level = st.selectbox("Level", ["A1", "A2", "B1", "B2"])
            topics = load_topics().get(level, [])
            topic_names = [t["name"] for t in topics]
            topic = st.selectbox("Topic", topic_names)
        
        with col2:
            exercise_type = st.selectbox("Exercise Type", [
                "Fill in the Blank",
                "Multiple Choice",
                "Sentence Building",
                "Error Correction",
                "Matching",
                "Translation"
            ])
            num_questions = st.slider("Number of Questions", 5, 20, 10)
        
        submitted = st.form_submit_button("Generate Exercise")
    
    if submitted:
        # Find topic details
        topic_data = next((t for t in topics if t["name"] == topic), None)
        
        if topic_data:
            # Generate exercise
            exercise = {
                "level": level,
                "topic": topic,
                "type": exercise_type,
                "num_questions": num_questions,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "questions": []
            }
            
            # Generate sample questions based on type
            if exercise_type == "Fill in the Blank":
                for i in range(num_questions):
                    exercise["questions"].append({
                        "question": f"Question {i+1}: ________ is the correct answer.",
                        "answer": "sample answer"
                    })
            elif exercise_type == "Multiple Choice":
                for i in range(num_questions):
                    exercise["questions"].append({
                        "question": f"Question {i+1}: Choose the correct option.",
                        "options": ["Option A", "Option B", "Option C", "Option D"],
                        "correct": "Option A"
                    })
            elif exercise_type == "Sentence Building":
                for i in range(num_questions):
                    exercise["questions"].append({
                        "question": f"Arrange the words: word1, word2, word3",
                        "answer": "word1 word2 word3"
                    })
            elif exercise_type == "Error Correction":
                for i in range(num_questions):
                    exercise["questions"].append({
                        "question": f"Find the error: This sentence have a mistake.",
                        "answer": "This sentence has a mistake."
                    })
            elif exercise_type == "Matching":
                for i in range(num_questions):
                    exercise["questions"].append({
                        "question": f"Match: A{i+1} - B{i+1}",
                        "answer": f"A{i+1} = B{i+1}"
                    })
            elif exercise_type == "Translation":
                for i in range(num_questions):
                    exercise["questions"].append({
                        "question": f"Translate to English: (Arabic text {i+1})",
                        "answer": f"English translation {i+1}"
                    })
            
            st.session_state.generated_exercises.append(exercise)
            
            # Display exercise
            st.success("✅ Exercise generated!")
            
            st.markdown(f"### {level} - {topic} ({exercise_type})")
            st.markdown(f"**Questions:** {num_questions}")
            
            for i, q in enumerate(exercise["questions"], 1):
                st.markdown(f"**{i}.** {q['question']}")
                if "options" in q:
                    for option in q["options"]:
                        st.markdown(f"  - {option}")
                if "answer" in q:
                    st.markdown(f"  *Answer: {q['answer']}*")
    
    # Display generated exercises
    if st.session_state.generated_exercises:
        st.markdown('<p class="section-header">📝 Generated Exercises</p>', unsafe_allow_html=True)
        
        for i, exercise in enumerate(st.session_state.generated_exercises):
            with st.expander(f"📝 {exercise['level']} - {exercise['topic']} ({exercise['type']})"):
                st.markdown(f"**Questions:** {exercise['num_questions']}")
                for j, q in enumerate(exercise["questions"], 1):
                    st.markdown(f"{j}. {q['question']}")
                    if "options" in q:
                        for option in q["options"]:
                            st.markdown(f"  - {option}")
                    if "answer" in q:
                        st.markdown(f"  *Answer: {q['answer']}*")

# Assessment Creator page
elif page == "Assessment Creator":
    st.markdown('<p class="section-header">📝 Assessment Creator</p>', unsafe_allow_html=True)
    
    # BEM format info
    st.info("""
    **BEM Exam Format (4AM - Level B2)**
    - Section A: Reading Comprehension (10 MCQ = 10 marks)
    - Section B: Grammar & Vocabulary (10 MCQ = 10 marks)
    - Section C: Writing (1 essay = 10 marks)
    - **Total: 30 marks, 60 minutes**
    """)
    
    # Input form
    with st.form("assessment_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            assessment_type = st.selectbox("Assessment Type", [
                "BEM Format (4AM)",
                "A1 Assessment",
                "A2 Assessment",
                "B1 Assessment",
                "B2 Assessment"
            ])
        
        with col2:
            num_students = st.number_input("Number of Students", min_value=10, max_value=50, value=30)
        
        submitted = st.form_submit_button("Generate Assessment")
    
    if submitted:
        # Generate assessment based on type
        assessment = {
            "type": assessment_type,
            "num_students": num_students,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "sections": []
        }
        
        if assessment_type == "BEM Format (4AM)":
            assessment["sections"] = [
                {"name": "Reading Comprehension", "questions": 10, "marks": 10, "type": "MCQ"},
                {"name": "Grammar & Vocabulary", "questions": 10, "marks": 10, "type": "MCQ"},
                {"name": "Writing", "questions": 1, "marks": 10, "type": "Essay"}
            ]
            assessment["total_marks"] = 30
            assessment["duration"] = 60
        elif assessment_type == "A1 Assessment":
            assessment["sections"] = [
                {"name": "Multiple Choice", "questions": 20, "marks": 20, "type": "MCQ"},
                {"name": "Fill in the Blank", "questions": 10, "marks": 10, "type": "Fill-blank"},
                {"name": "Matching", "questions": 5, "marks": 5, "type": "Matching"}
            ]
            assessment["total_marks"] = 35
            assessment["duration"] = 45
        elif assessment_type == "A2 Assessment":
            assessment["sections"] = [
                {"name": "Multiple Choice", "questions": 15, "marks": 15, "type": "MCQ"},
                {"name": "Fill in the Blank", "questions": 10, "marks": 10, "type": "Fill-blank"},
                {"name": "Sentence Building", "questions": 5, "marks": 5, "type": "Sentence building"}
            ]
            assessment["total_marks"] = 30
            assessment["duration"] = 60
        elif assessment_type == "B1 Assessment":
            assessment["sections"] = [
                {"name": "Multiple Choice", "questions": 15, "marks": 15, "type": "MCQ"},
                {"name": "Fill in the Blank", "questions": 10, "marks": 10, "type": "Fill-blank"},
                {"name": "Error Correction", "questions": 5, "marks": 5, "type": "Error correction"},
                {"name": "Short Essay", "questions": 1, "marks": 5, "type": "Essay"}
            ]
            assessment["total_marks"] = 35
            assessment["duration"] = 90
        elif assessment_type == "B2 Assessment":
            assessment["sections"] = [
                {"name": "Multiple Choice", "questions": 15, "marks": 15, "type": "MCQ"},
                {"name": "Fill in the Blank", "questions": 10, "marks": 10, "type": "Fill-blank"},
                {"name": "Error Correction", "questions": 5, "marks": 5, "type": "Error correction"},
                {"name": "Essay (200-250 words)", "questions": 1, "marks": 10, "type": "Essay"}
            ]
            assessment["total_marks"] = 40
            assessment["duration"] = 120
        
        # Display assessment
        st.success("✅ Assessment generated!")
        
        st.markdown(f"### {assessment_type}")
        st.markdown(f"**Total Marks:** {assessment['total_marks']} | **Duration:** {assessment['duration']} minutes")
        
        for section in assessment["sections"]:
            with st.expander(f"📋 {section['name']} ({section['marks']} marks)"):
                st.markdown(f"**Questions:** {section['questions']} | **Type:** {section['type']}")
                st.markdown(f"**Instructions:** Answer all questions in this section.")

# Class Analytics page
elif page == "Class Analytics":
    st.markdown('<p class="section-header">📊 Class Analytics</p>', unsafe_allow_html=True)
    
    # Sample data
    st.markdown("### 📈 Performance Overview")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Average Score", "72%", "+5%")
    with col2:
        st.metric("Completion Rate", "85%", "+10%")
    with col3:
        st.metric("Active Students", "28", "+3")
    
    # Performance chart
    st.markdown("### 📊 Score Distribution")
    
    # Sample data for chart
    scores = [random.randint(50, 100) for _ in range(30)]
    
    import pandas as pd
    df = pd.DataFrame({"Student": range(1, 31), "Score": scores})
    st.bar_chart(df.set_index("Student"))
    
    # Recommendations
    st.markdown("### 💡 Recommendations")
    
    recommendations = [
        "Focus on Present Simple for struggling students",
        "Review Past Simple irregular verbs with the class",
        "Assign extra practice for Comparatives",
        "Celebrate progress in Present Perfect!"
    ]
    
    for rec in recommendations:
        st.info(f"💡 {rec}")

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("**Ta'allim** - AI-powered English teaching")
st.sidebar.markdown("Built for Algerian teachers")

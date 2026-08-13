#!/usr/bin/env python3
"""
English Exercise Generator — Streamlit Web Interface
For Algerian public school teachers.

Usage:
    cd C:\Users\Admin\My Drive\LifeWorkspace\10_Education_Project\Exercise_Generator
    streamlit run app.py
"""

import sys
import os
import json
import datetime

# Add parent dir to path so imports work
sys.path.insert(0, os.path.dirname(__file__))

import streamlit as st
from exercise_generator import ExerciseGenerator, EXERCISE_TYPES, to_html, to_markdown
from topics import get_topics_by_level, get_topic_by_id, find_topic_by_name, LEVELS

st.set_page_config(
    page_title="English Exercise Generator",
    page_icon="📚",
    layout="wide",
)

st.title("📚 English Exercise Generator")
st.caption("AI-powered grammar exercises for Algerian students")

# --- Sidebar: Configuration ---
with st.sidebar:
    st.header("Configuration")

    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    api_key_input = st.text_input(
        "Claude API Key (optional)",
        value=api_key,
        type="password",
        help="Leave empty to use offline mode",
    )
    if api_key_input:
        os.environ["ANTHROPIC_API_KEY"] = api_key_input

    st.divider()
    st.markdown("**Mode:** " + ("🟢 API" if api_key_input else "🔴 Offline (no API key)"))
    st.markdown("Offline mode uses pre-built exercise templates.")

# --- Main Area: Exercise Generation ---
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Exercise Settings")

    level = st.selectbox("CEFR Level", LEVELS, index=0)

    topics = get_topics_by_level(level)
    topic_names = [t["name"] for t in topics]
    topic_map = {t["name"]: t for t in topics}

    selected_topic = st.selectbox("Topic", topic_names, index=0)

    # Get exercise types for selected topic
    if selected_topic:
        topic_info = topic_map[selected_topic]
        valid_types = topic_info.get("exercise_types", EXERCISE_TYPES)
        # Filter to only types that exist in EXERCISE_TYPES
        valid_types = [t for t in valid_types if t in EXERCISE_TYPES]
    else:
        valid_types = EXERCISE_TYPES

    exercise_type = st.selectbox(
        "Exercise Type",
        valid_types,
        format_func=lambda x: x.replace("_", " ").title(),
    )

    count = st.slider("Number of Exercises", min_value=1, max_value=20, value=5)

    generate_btn = st.button("Generate Exercises", type="primary", use_container_width=True)

# --- Results Area ---
with col2:
    st.subheader("Generated Exercises")

    if generate_btn and selected_topic:
        topic_info = topic_map[selected_topic]

        with st.spinner("Generating exercises..."):
            gen = ExerciseGenerator(api_key=api_key_input or None)
            result = gen.generate(topic_info["id"], exercise_type, count)

        if "error" in result:
            st.error(result["error"])
        else:
            st.success(f"Generated {result['count']} exercises ({result['source']} mode)")

            # Store in session state for export
            st.session_state["last_result"] = result

            # Render exercises
            for i, ex in enumerate(result["exercises"], 1):
                with st.expander(f"Exercise {i}", expanded=(i <= 3)):
                    if exercise_type == "fill_in_blank":
                        st.write(f"**{ex['sentence']}**")
                        st.write(f"Answer: `{ex['answer']}`")
                        if ex.get("hint"):
                            st.caption(f"Hint: {ex['hint']}")

                    elif exercise_type == "multiple_choice":
                        st.write(f"**{ex['question']}**")
                        for j, opt in enumerate(ex.get("options", [])):
                            letter = chr(65 + j)
                            marker = " ✓" if letter == ex.get("answer") else ""
                            st.write(f"  {letter}) {opt}{marker}")
                        if ex.get("explanation"):
                            st.caption(f"Explanation: {ex['explanation']}")

                    elif exercise_type == "sentence_building":
                        st.write(f"**Arrange:** {ex['words']}")
                        st.write(f"Answer: `{ex['correct_sentence']}`")

                    elif exercise_type == "transformation":
                        st.write(f"**Original:** {ex['original']}")
                        st.write(f"**Task:** {ex['instruction']}")
                        st.write(f"Answer: `{ex['transformed']}`")
                        if ex.get("explanation"):
                            st.caption(f"Rule: {ex['explanation']}")

                    elif exercise_type == "error_correction":
                        st.write(f"**Find the error:** {ex['incorrect_sentence']}")
                        st.write(f"Answer: `{ex['correct_sentence']}`")
                        if ex.get("explanation"):
                            st.caption(f"Explanation: {ex['explanation']}")

                    elif exercise_type == "matching":
                        st.write(f"**Match:** {ex['left']} ↔ {ex['right']}")

    elif generate_btn:
        st.warning("Please select a topic first.")

# --- Export Section ---
if "last_result" in st.session_state:
    st.divider()
    st.subheader("Export")

    result = st.session_state["last_result"]
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename_base = f"exercises_{result['topic'].lower().replace(' ', '_')}_{result['level']}_{ts}"

    col_a, col_b, col_c = st.columns(3)

    with col_a:
        html_content = to_html([result])
        st.download_button(
            label="Download HTML",
            data=html_content,
            file_name=f"{filename_base}.html",
            mime="text/html",
            use_container_width=True,
        )

    with col_b:
        md_content = to_markdown([result])
        st.download_button(
            label="Download Markdown",
            data=md_content,
            file_name=f"{filename_base}.md",
            mime="text/markdown",
            use_container_width=True,
        )

    with col_c:
        json_content = json.dumps(result, indent=2, ensure_ascii=False)
        st.download_button(
            label="Download JSON",
            data=json_content,
            file_name=f"{filename_base}.json",
            mime="application/json",
            use_container_width=True,
        )

# --- Footer ---
st.divider()
st.caption("English Exercise Generator v1.0 | Built for Algerian public schools")

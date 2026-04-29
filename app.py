import streamlit as st
from agents import planner, analyzer, generator, reviewer

st.set_page_config(page_title="AI Study Planner", layout="centered")

# 🔥 HEADER
st.title("🚀 Autonomous AI Study Planner")
st.caption("Multi-Agent System with Decision Intelligence")

# 📥 INPUTS
subjects = st.text_input("Enter subjects (comma separated)")
hours = st.number_input("Study hours per day", min_value=1, max_value=12)

goal = st.text_input("Enter your goal (e.g., exam in 30 days)")

difficulty = st.selectbox(
    "Select difficulty level",
    ["Easy", "Medium", "Hard"]
)

# 🚀 GENERATE
if st.button("Generate Plan"):

    if subjects and goal:

        subject_list = [s.strip() for s in subjects.split(",")]

        user_input = f"""
        Subjects: {subject_list}
        Study Hours: {hours} hours/day
        Goal: {goal}
        Difficulty Level: {difficulty}
        """

        # 🧠 PLANNER
        st.subheader("🧠 Planning Phase")
        step1 = planner(user_input)
        st.info(step1)

        # 📊 ANALYZER
        st.subheader("📊 Analysis Phase")
        step2 = analyzer(user_input + "\n" + step1)
        st.success(step2)

        # 📅 GENERATOR
        st.subheader("📅 Study Plan")
        step3 = generator(user_input + "\n" + step2)
        st.write(step3)

        # ✅ REVIEWER
        st.subheader("✅ Optimized Plan")
        final_output = reviewer(user_input + "\n" + step3)

        st.markdown("### 📌 Final Output")
        st.success(final_output)

    else:
        st.warning("Please enter all details")
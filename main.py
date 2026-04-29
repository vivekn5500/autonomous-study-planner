from agents import planner, analyzer, generator, reviewer

# 🧾 USER INPUT
user_input = """
Class: 10th
Subjects: Math, Science
Study Hours: 5 hours/day
Goal: Exam in 30 days
"""

# 🔄 WORKFLOW
step1 = planner(user_input)
step2 = analyzer(step1)
step3 = generator(step2)
final_output = reviewer(step3)

# 📤 OUTPUT
print("\n===== FINAL STUDY PLAN =====\n")
print(final_output)
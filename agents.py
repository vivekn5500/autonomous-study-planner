import requests

# 🔥 LLM CONNECTION
def call_llm(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]


# 🧠 Planner Agent (SHORT + CLEAN)
def planner(input_data):
    prompt = f"""
    You are a planning agent.

    Briefly summarize what needs to be done based on the student goal.

    Keep it short (3-4 lines max).

    Input:
    {input_data}
    """
    return call_llm(prompt)


# 📊 Analyzer Agent (REAL DECISION MAKING 🔥)
def analyzer(input_data):
    prompt = f"""
    You are an analyzer agent.

    Based on the input:
    - Assign priority (High/Medium/Low)
    - Give focus score (1-10)
    - Estimate effort level (Low/Moderate/High)

    DO NOT ask questions.
    GIVE FINAL DECISION.

    Format:
    Subject → Priority → Focus Score → Effort

    Input:
    {input_data}
    """
    return call_llm(prompt)


# 📅 Generator Agent (STRUCTURED OUTPUT 🔥)
def generator(input_data):
    prompt = f"""
    You are a study planner agent.

    STRICT RULES:
    - Use only given input
    - Do NOT add random subjects

    Create:
    1. Day-wise study plan (clean format)
    2. Time allocation per subject

    Format:

    Day 1:
    - Subject: X hours

    Day 2:
    ...

    Keep it short, structured, and practical.

    Input:
    {input_data}
    """
    return call_llm(prompt)


# ✅ Reviewer Agent (OPTIMIZATION + EXPLANATION 🔥)
def reviewer(input_data):
    prompt = f"""
    You are a reviewer agent.

    Improve the plan:
    - Make it realistic
    - Avoid overload

    ALSO ADD:
    "Why this plan works" (3 bullet points)

    Keep output clean.

    Input:
    {input_data}
    """
    return call_llm(prompt)
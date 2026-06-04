import streamlit as st
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("get_openai_key"))

st.set_page_config(page_title="AI Decision Auditor")

st.title("🧠 AI Decision Auditor")
st.write("This tool audits reasoning behind career or academic decisions.")
st.markdown("⚠️ *This system provides reasoning analysis only, not life advice.*")

decision = st.text_area(
    "Describe your decision:",
    placeholder="Example: I want to skip my project because exams are coming."
)

if st.button("Audit Decision"):
    if decision.strip() == "":
        st.warning("Please enter a decision.")
    else:
        with st.spinner("Analyzing reasoning..."):
            prompt = f"""
You are an AI Decision Auditor.

Rules:
- Do NOT make decisions.
- Do NOT give direct advice.
- Analyze reasoning, biases, emotions.
- Provide alternative perspectives.
- State limitations clearly.

Output Format:
Decision Summary:
Detected Biases:
Emotional Influence Level:
Key Factors Considered:
Missing / Overlooked Factors:
Alternative Perspectives:
Confidence Score (0–1):
Limitations of This Analysis:

Decision:
{decision}
"""

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )

            st.text(response.choices[0].message.content)


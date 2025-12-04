import streamlit as st

# ------- PAGE CONFIG -------
st.set_page_config(
    page_title="MBTI Quick Test",
    layout="centered",
)

# ------- STYLING -------
st.markdown("""
    <style>
        .question-card {
            background-color: #11111110;
            padding: 16px;
            border-radius: 10px;
            margin-bottom: 15px;
            border: 1px solid #5552;
        }
        .result-box {
            background-color: #4a6fa5;
            padding: 16px;
            border-radius: 10px;
            color: #fff;
            font-size: 20px;
            text-align: center;
            font-weight: bold;
        }
        .option-label {
            font-weight: 600;
        }
    </style>
""", unsafe_allow_html=True)

# ------- TITLE -------
st.title("🧠 MBTI Quick Test")
st.write("A lightweight personality test — just **12 questions**!")
st.caption("Pick the option that feels most natural, not the one you *think* you should choose.")

st.markdown("### 👇 Start answering:")

# ------- QUESTIONS -------
questions = {
    1: ("When you're recharging:", "A) Prefer alone / one close friend", "B) Energized by people"),
    2: ("In conversations:", "A) Speak when needed", "B) Think out loud"),
    3: ("Problem-solving style:", "A) Logic first", "B) Feelings & harmony"),
    4: ("Decision-making:", "A) Proven facts", "B) Ideas & possibilities"),
    5: ("Your space:", "A) Organized & neat", "B) Creative chaos"),
    6: ("Time management:", "A) Planned & structured", "B) Spontaneous"),
    7: ("Work style:", "A) One task at a time", "B) Multiple ideas at once"),
    8: ("Social preference:", "A) Deep friendships", "B) Wide circle"),
    9: ("Arguments:", "A) Honest even if harsh", "B) Kind even if softened"),
    10: ("Interests:", "A) Concepts, systems", "B) People, emotions"),
    11: ("Learning style:", "A) Detail first", "B) Big picture first"),
    12: ("Focus:", "A) Present reality", "B) Future possibilities"),
}

answers = {}

# ------- FORM -------
with st.form("mbti_form"):
    for i in range(1, 13):
        q, a, b = questions[i]
        st.markdown(f"<div class='question-card'><b>Q{i}. {q}</b>", unsafe_allow_html=True)
        choice = st.radio(
            "Select:",
            options=[a, b],
            index=None,
            key=f"q{i}",
            label_visibility="collapsed",
        )
        st.markdown("</div>", unsafe_allow_html=True)
        if choice:
            answers[i] = "A" if choice.startswith("A)") else "B"

    submitted = st.form_submit_button("Show My MBTI Type 🎯")

# ------- RESULTS -------
if submitted:
    if len(answers) < 12:
        st.error("⚠️ Please answer all questions.")
    else:
        # Traits calculation using map lists
        traits = {
            "I-E": ([1, 2, 8], "I", "E"),
            "S-N": ([4, 11, 12], "S", "N"),
            "T-F": ([3, 9, 10], "T", "F"),
            "J-P": ([5, 6, 7], "J", "P"),
        }

        result = []
        for group, A_type, B_type in traits.values():
            scoreA = sum(answers[q] == "A" for q in group)
            result.append(A_type if scoreA >= 2 else B_type)

        mbti_type = "".join(result)

        descriptions = {
            "ISTP": "Logical, hands-on, independent, good problem-solver.",
            "INTP": "Analytical, idea-focused, loves theory & exploration.",
            "ISTJ": "Organized, responsible, values order & reliability.",
            "INTJ": "Strategic, planner, independent thinker.",
            "ESTP": "Action-oriented, energetic, real-world problem solver.",
            "ENTP": "Curious, creative thinker, debates ideas easily.",
            "ESTJ": "Leader personality with strong practicality.",
            "ENTJ": "Bold, strategic, natural commander.",
            "ISFP": "Artistic, gentle, values personal freedom.",
            "INFP": "Idealistic, values meaning & deep beliefs.",
            "ISFJ": "Kind, responsible, supportive protector.",
            "INFJ": "Insightful, guides others with deep empathy.",
            "ESFP": "Fun-loving, spontaneous performer energy.",
            "ENFP": "Inspirational, imaginative, loves possibilities.",
            "ESFJ": "Caring, social, community-focused.",
            "ENFJ": "Charismatic, natural mentor & motivator.",
        }

        st.markdown(f"<div class='result-box'>Your MBTI Type: {mbti_type}</div>",
                    unsafe_allow_html=True)

        st.info(descriptions.get(mbti_type, "A unique personality type!"))

        st.caption("📌 Note: This is a simplified estimation, not official MBTI.")


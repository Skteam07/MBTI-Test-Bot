import streamlit as st

st.set_page_config(page_title="MBTI Quick Test", layout="centered")

st.title("MBTI Quick Test (12 Questions)")
st.write(
    "Answer each question with what feels most natural. "
    "At the end, you'll get an approximate MBTI type."
)

st.markdown("---")

questions = {
    1: (
        "When you're recharging:",
        "A) I prefer being alone or with one close person",
        "B) I feel energized around groups of people",
    ),
    2: (
        "In conversations:",
        "A) I speak only when I have something meaningful to say",
        "B) I enjoy talking and thinking out loud",
    ),
    3: (
        "When solving problems:",
        "A) I focus on what’s logical and makes sense objectively",
        "B) I focus on people’s feelings and harmony",
    ),
    4: (
        "In decision-making:",
        "A) I prefer sticking to clear facts and proven methods",
        "B) I trust ideas, possibilities, and patterns",
    ),
    5: (
        "Your desk or room is usually:",
        "A) Organized and neat",
        "B) Creative chaos — I know where everything is (mostly)",
    ),
    6: (
        "Planning vs improvising:",
        "A) I like schedules, planning ahead, structure",
        "B) I like keeping options open and being spontaneous",
    ),
    7: (
        "When working on something:",
        "A) I want to finish one thing before starting another",
        "B) I often jump between multiple ideas",
    ),
    8: (
        "Social preference:",
        "A) A few deep friendships",
        "B) A wide circle of acquaintances",
    ),
    9: (
        "In arguments:",
        "A) I prefer being honest even if it may hurt",
        "B) I soften truth to protect feelings",
    ),
    10: (
        "Interest preference:",
        "A) Science, systems, abstract concepts",
        "B) Real-life stories, emotions, human behavior",
    ),
    11: (
        "When learning something:",
        "A) I like details step-by-step",
        "B) I understand big-picture first",
        ),
    12: (
        "Your focus:",
        "A) How things are now",
        "B) How things could be",
    ),
}

answers = {}

with st.form("mbti_form"):
    for i in range(1, 13):
        q, a_text, b_text = questions[i]
        st.subheader(f"Q{i}. {q}")
        choice = st.radio(
            "Choose one:",
            options=[a_text, b_text],
            index=None,
            key=f"q{i}",
        )
        if choice is not None:
            answers[i] = "A" if choice.startswith("A)") else "B"
        st.markdown("---")

    submitted = st.form_submit_button("Get my MBTI type")

if submitted:
    if len(answers) < 12:
        st.error("Please answer all questions before submitting.")
    else:
        # ----- SCORING -----
        # I vs E: Q1, Q2, Q8
        I_score = (answers[1] == "A") + (answers[2] == "A") + (answers[8] == "A")
        E_score = 3 - I_score
        I_or_E = "I" if I_score >= E_score else "E"

        # S vs N: Q4, Q11, Q12
        S_score = (answers[4] == "A") + (answers[11] == "A") + (answers[12] == "A")
        N_score = 3 - S_score
        S_or_N = "S" if S_score >= N_score else "N"

        # T vs F: Q3, Q9, Q10
        T_score = (answers[3] == "A") + (answers[9] == "A") + (answers[10] == "A")
        F_score = 3 - T_score
        T_or_F = "T" if T_score >= F_score else "F"

        # J vs P: Q5, Q6, Q7
        J_score = (answers[5] == "A") + (answers[6] == "A") + (answers[7] == "A")
        P_score = 3 - J_score
        J_or_P = "J" if J_score >= P_score else "P"

        mbti_type = I_or_E + S_or_N + T_or_F + J_or_P

        descriptions = {
            "ISTP": "ISTP – The Virtuoso: logical, hands-on, independent, good at troubleshooting.",
            "INTP": "INTP – The Logician: analytical, idea-focused, loves theories and concepts.",
            "ISTJ": "ISTJ – The Inspector: responsible, detail-oriented, likes structure and order.",
            "INTJ": "INTJ – The Architect: strategic, long-term planner, independent thinker.",
            "ESTP": "ESTP – The Dynamo: energetic, action-oriented, loves real-world challenges.",
            "ENTP": "ENTP – The Debater: curious, playful with ideas, likes exploring possibilities.",
            "ESTJ": "ESTJ – The Supervisor: organized, practical leader, likes clear rules.",
            "ENTJ": "ENTJ – The Commander: bold, strategic, natural leader.",
            "ISFP": "ISFP – The Adventurer: gentle, artistic, values personal freedom.",
            "INFP": "INFP – The Mediator: idealistic, driven by values and meaning.",
            "ISFJ": "ISFJ – The Defender: caring, responsible, supportive of others.",
            "INFJ": "INFJ – The Advocate: deep, insightful, focused on helping people grow.",
            "ESFP": "ESFP – The Performer: fun-loving, spontaneous, people-oriented.",
            "ENFP": "ENFP – The Campaigner: enthusiastic, creative, loves possibilities.",
            "ESFJ": "ESFJ – The Provider: social, caring, community-focused.",
            "ENFJ": "ENFJ – The Protagonist: charismatic, empathetic, natural mentor.",
        }

        st.success(f"Your approximate MBTI type is: **{mbti_type}**")
        if mbti_type in descriptions:
            st.info(descriptions[mbti_type])

        st.caption("Note: This is a simplified test, not an official MBTI assessment.")

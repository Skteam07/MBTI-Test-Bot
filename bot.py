import streamlit as st

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="MBTI Quick Test · Cattipucchi",
    layout="centered",
)

# ---------- THEME / CSS ----------
st.markdown(
    """
    <style>
        body {
            background: radial-gradient(circle at top, #ffe6f7 0, #fdfdfd 45%, #e6f0ff 100%);
        }
        .main {
            background: transparent;
        }
        .catti-title {
            text-align: center;
            font-weight: 800;
            font-size: 2.1rem;
            padding-top: 0.5rem;
        }
        .catti-subtitle {
            text-align: center;
            font-size: 0.95rem;
            color: #555;
            margin-bottom: 1.5rem;
        }
        .catti-card {
            background: linear-gradient(145deg, #ffffffee, #ffeefd);
            border-radius: 22px;
            padding: 24px 22px;
            box-shadow: 0 14px 30px rgba(0,0,0,0.06);
            border: 1px solid #ffc7f3aa;
        }
        .catti-pill {
            display: inline-block;
            padding: 4px 10px;
            border-radius: 999px;
            background: #ffdff5;
            font-size: 0.75rem;
            font-weight: 600;
            color: #944b8f;
            margin-bottom: 6px;
        }
        .catti-qtext {
            font-size: 1.05rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
            color: #3b264b;
        }
        .stRadio > label {
            font-weight: 600;
        }
        .stRadio [role="radiogroup"] > label {
            padding: 0.35rem 0.6rem;
            border-radius: 999px;
        }
        .result-card {
            margin-top: 1.5rem;
            padding: 18px;
            border-radius: 20px;
            background: linear-gradient(135deg, #ffd6f0, #d6e5ff);
            text-align: center;
            box-shadow: 0 10px 25px rgba(0,0,0,0.08);
        }
        .result-type {
            font-size: 1.8rem;
            font-weight: 800;
            color: #442255;
        }
        .result-label {
            font-size: 0.9rem;
            font-weight: 600;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            color: #6b4d7a;
        }
        .small-hint {
            font-size: 0.8rem;
            color: #777;
            text-align: center;
            margin-top: 0.5rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- STATE SETUP ----------
if "current_q" not in st.session_state:
    st.session_state.current_q = 1

if "answers" not in st.session_state:
    st.session_state.answers = {}

if "show_result" not in st.session_state:
    st.session_state.show_result = False

# ---------- DATA ----------
questions = {
    1: ("When you're recharging:", "A) I prefer being alone or with one close person",
        "B) I feel energized around groups of people"),
    2: ("In conversations:", "A) I speak only when I have something meaningful to say",
        "B) I enjoy talking and thinking out loud"),
    3: ("When solving problems:", "A) I focus on what’s logical and makes sense objectively",
        "B) I focus on people’s feelings and harmony"),
    4: ("In decision-making:", "A) I prefer sticking to clear facts and proven methods",
        "B) I trust ideas, possibilities, and patterns"),
    5: ("Your desk or room is usually:", "A) Organized and neat",
        "B) Creative chaos — I know where everything is (mostly)"),
    6: ("Planning vs improvising:", "A) I like schedules, planning ahead, structure",
        "B) I like keeping options open and being spontaneous"),
    7: ("When working on something:", "A) I want to finish one thing before starting another",
        "B) I often jump between multiple ideas"),
    8: ("Social preference:", "A) A few deep friendships",
        "B) A wide circle of acquaintances"),
    9: ("In arguments:", "A) I prefer being honest even if it may hurt",
        "B) I soften truth to protect feelings"),
    10: ("Interest preference:", "A) Science, systems, abstract concepts",
         "B) Real-life stories, emotions, human behavior"),
    11: ("When learning something:", "A) I like details step-by-step",
         "B) I understand big-picture first"),
    12: ("Your focus:", "A) How things are now",
         "B) How things could be"),
}
TOTAL_Q = len(questions)


# ---------- CALLBACKS ----------
def on_choice_change():
    """Store answer + auto-move to next question or show result on last."""
    q = st.session_state.current_q
    choice = st.session_state.get(f"q{q}_choice")

    if not choice:
        return

    st.session_state.answers[q] = "A" if choice.startswith("A)") else "B"

    # Auto-advance or show result
    if q < TOTAL_Q:
        st.session_state.current_q = q + 1
    else:
        st.session_state.show_result = True


# ---------- HEADER ----------
st.markdown(
    "<div class='catti-title'>🐾 Cattipucchi MBTI Quick Test</div>",
    unsafe_allow_html=True,
)
st.markdown(
    "<div class='catti-subtitle'>12 cozy questions to guess your MBTI vibe. "
    "Answer what feels natural, not what feels ideal. 💭</div>",
    unsafe_allow_html=True,
)

# ---------- QUESTION CARD ----------
q_num = st.session_state.current_q
q_text, a_text, b_text = questions[q_num]

st.markdown("<div class='catti-card'>", unsafe_allow_html=True)

st.markdown(
    f"<span class='catti-pill'>Question {q_num} / {TOTAL_Q}</span>",
    unsafe_allow_html=True,
)
st.markdown(
    f"<div class='catti-qtext'>{q_text}</div>",
    unsafe_allow_html=True,
)

# Pre-select previously chosen option (if any)
prev_answer = st.session_state.answers.get(q_num)
if prev_answer == "A":
    default_index = 0
elif prev_answer == "B":
    default_index = 1
else:
    default_index = None

choice = st.radio(
    "Choose one:",
    options=[a_text, b_text],
    index=default_index,
    key=f"q{q_num}_choice",
    label_visibility="collapsed",
    on_change=on_choice_change,
)

st.markdown("</div>", unsafe_allow_html=True)

# ---------- NAVIGATION BUTTONS ----------
nav_cols = st.columns([1, 1, 2])

with nav_cols[0]:
    if st.button("⬅️ Back", use_container_width=True, disabled=(q_num == 1)):
        if st.session_state.current_q > 1:
            st.session_state.current_q -= 1
            st.session_state.show_result = False  # if they go back, keep editing

with nav_cols[1]:
    # Optional explicit "Show Result" when all answered
    if len(st.session_state.answers) == TOTAL_Q:
        if st.button("🎯 Show Result", use_container_width=True):
            st.session_state.show_result = True

st.markdown(
    "<div class='small-hint'>Tip: selecting an option jumps to the next question automatically. "
    "You can always go back and change answers.</div>",
    unsafe_allow_html=True,
)

# ---------- RESULT ----------
if st.session_state.show_result and len(st.session_state.answers) == TOTAL_Q:
    answers = st.session_state.answers

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

    st.markdown("<div class='result-card'>", unsafe_allow_html=True)
    st.markdown("<div class='result-label'>Your Cattipucchi MBTI vibe</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='result-type'>{mbti_type}</div>", unsafe_allow_html=True)
    st.write(descriptions.get(mbti_type, "A pretty rare & special combination. 🐾"))
    st.markdown("</div>", unsafe_allow_html=True)

    st.caption("Note: This is a simplified test, not an official MBTI assessment. 💌")

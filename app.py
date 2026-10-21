
import re
import streamlit as st

st.set_page_config(
    page_title="Password Lab",
    page_icon="🔐",
    layout="centered"
)

# Modern dark UI
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0b1020, #131b35, #111827);
    color: #f1f5f9;
}
[data-testid="stHeader"] {
    background: transparent;
}
.block-container {
    max-width: 800px;
    padding-top: 2.5rem;
}
h1, h2, h3, p, label {
    color: #f1f5f9;
}
div[data-testid="stTextInput"] input {
    background: #111827;
    color: white;
    border: 1px solid #475569;
    border-radius: 12px;
    padding: 12px;
}
.stButton > button,
[data-testid="stFormSubmitButton"] button {
    background: linear-gradient(90deg, #06b6d4, #6366f1);
    color: white;
    border: none;
    border-radius: 12px;
    font-weight: 700;
    min-height: 45px;
}
.result-card {
    background: rgba(30, 41, 59, 0.75);
    border: 1px solid #334155;
    border-radius: 20px;
    padding: 24px;
    text-align: center;
    margin: 12px 0;
}
.score {
    font-size: 42px;
    font-weight: 800;
}
.strength {
    font-size: 23px;
    font-weight: 700;
}
</style>
""", unsafe_allow_html=True)

st.title("🔐 Password Lab")
st.write("Check your password strength in seconds.")
st.caption("A simple, privacy-conscious password checker demo.")

def check_password(password):
    common_passwords = {
        "password", "12345678", "qwerty123",
        "admin123", "letmein", "welcome1",
        "iloveyou"
    }

    lower = password.lower()

    # Detect common patterns and repeated characters
    patterns = (
        "1234", "abcd", "qwerty",
        "password", "asdf", "1111", "0000"
    )

    common = lower in common_passwords
    repeated = bool(re.search(r"(.)\1{3,}", password))
    obvious_pattern = (
        any(pattern in lower for pattern in patterns)
        or repeated
    )

    # Count character categories
    groups = sum([
        bool(re.search(r"[a-z]", password)),
        bool(re.search(r"[A-Z]", password)),
        bool(re.search(r"\d", password)),
        bool(re.search(r"[^a-zA-Z0-9]", password))
    ])

    # Educational heuristic, not a security guarantee
    if len(password) >= 16:
        score = 40
    elif len(password) >= 12:
        score = 30
    elif len(password) >= 8:
        score = 18
    else:
        score = 5

    score += {0: 0, 1: 4, 2: 10, 3: 18, 4: 25}[groups]

    if not common:
        score += 20

    if not obvious_pattern:
        score += 15

    if common or obvious_pattern:
        score = min(score, 30)

    score = min(score, 100)

    if score < 35:
        strength, color = "Weak", "#fb7185"
    elif score < 60:
        strength, color = "Fair", "#fbbf24"
    elif score < 80:
        strength, color = "Strong", "#34d399"
    else:
        strength, color = "Very Strong", "#22d3ee"

    return score, strength, color, common, obvious_pattern, groups


with st.form("password_form"):
    password = st.text_input(
        "Enter a test password",
        type="password",
        placeholder="Type a sample password..."
    )
    submitted = st.form_submit_button(
        "🔎 Check Strength",
        use_container_width=True
    )

if submitted:
    if not password:
        st.warning("Pehle ek test password enter kar.")
    else:
        score, strength, color, common, pattern, groups = (
            check_password(password)
        )

        st.markdown(
            f"""
            <div class="result-card">
                <div class="score" style="color:{color}">
                    {score}/100
                </div>
                <div class="strength" style="color:{color}">
                    {strength}
                </div>
                <p>Your password strength estimate</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.progress(score)

        st.subheader("✅ Security checklist")

        checks = [
            ("At least 12 characters", len(password) >= 12),
            ("16+ characters", len(password) >= 16),
            ("Uppercase and lowercase", 
             bool(re.search(r"[A-Z]", password))
             and bool(re.search(r"[a-z]", password))),
            ("Contains a number", bool(re.search(r"\d", password))),
            ("Contains a symbol", 
             bool(re.search(r"[^a-zA-Z0-9]", password))),
            ("No obvious patterns", not pattern and not common)
        ]

        left, right = st.columns(2)

        for index, (label, passed) in enumerate(checks):
            with (left if index % 2 == 0 else right):
                st.write(
                    f"{'✅' if passed else '⬜'} {label}"
                )

        st.subheader("💡 Improve your password")

        tips = []

        if len(password) < 12:
            tips.append(
                "Use a longer password. Try aiming for 16 or more characters."
            )

        if common:
            tips.append(
                "Avoid common passwords that people can easily guess."
            )

        if pattern:
            tips.append(
                "Avoid predictable sequences and repeated characters."
            )

        if groups < 3:
            tips.append(
                "Consider a long passphrase made from unrelated words."
            )

        if not tips:
            tips.append(
                "Use a unique password for every account."
            )

        for tip in tips:
            st.write(f"💡 {tip}")

        st.caption(
            "Demo only: this score is a rough estimate, "
            "not a guarantee of security or a breach-database check."
        )

st.divider()
st.caption("🔒 Password Lab | Python Mini Project")

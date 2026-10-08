import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Password Security Awareness",
    page_icon="🔐",
    layout="centered"
)

# Title
st.title("🔐 Password Strength & Security Awareness")

st.write(
    "Check the basic strength of a test password and learn "
    "important cybersecurity practices."
)

st.info(
    "🔒 Privacy Notice: This application checks the password "
    "directly in your browser session. Do not enter real, "
    "banking, or sensitive passwords."
)

# Password input
password = st.text_input(
    "Enter a test password:",
    type="password",
    placeholder="Enter a test password"
)

# Check button
if st.button("🔍 Check Password Strength", use_container_width=True):

    if password == "":
        st.warning("⚠️ Please enter a test password.")

    else:

        score = 0
        requirements = []

        # Length
        if len(password) >= 8:
            score += 1
            requirements.append("✅ At least 8 characters")
        else:
            requirements.append("❌ At least 8 characters")

        # Uppercase
        if any(char.isupper() for char in password):
            score += 1
            requirements.append("✅ Uppercase letter")
        else:
            requirements.append("❌ Uppercase letter")

        # Lowercase
        if any(char.islower() for char in password):
            score += 1
            requirements.append("✅ Lowercase letter")
        else:
            requirements.append("❌ Lowercase letter")

        # Number
        if any(char.isdigit() for char in password):
            score += 1
            requirements.append("✅ Number")
        else:
            requirements.append("❌ Number")

        # Special character
        if any(not char.isalnum() for char in password):
            score += 1
            requirements.append("✅ Special character")
        else:
            requirements.append("❌ Special character")

        # Result
        st.subheader("Password Strength Result")

        if score <= 2:
            st.error("🔴 WEAK PASSWORD")
            st.write(
                "Your password needs improvement. "
                "Follow the recommendations below."
            )

        elif score <= 4:
            st.warning("🟡 MEDIUM PASSWORD")
            st.write(
                "Your password is acceptable, "
                "but it can be made stronger."
            )

        else:
            st.success("🟢 STRONG PASSWORD")
            st.write(
                "Good! Your password meets all "
                "basic strength checks."
            )

        st.metric("Security Score", f"{score}/5")

        # Requirements
        st.subheader("Password Requirements")

        for requirement in requirements:
            st.write(requirement)


# Security tips
st.divider()

st.header("🛡️ Password Security Tips")

tips = [
    "Use a long password or passphrase.",
    "Use uppercase and lowercase letters.",
    "Include numbers and special characters.",
    "Do not use your name or date of birth.",
    "Avoid common passwords such as 123456 or password.",
    "Never share your password with other people.",
    "Use different passwords for important accounts.",
    "Enable two-factor authentication (2FA) when available."
]

for tip in tips:
    st.write(f"• {tip}")


# About project
st.divider()

st.header("📚 About This Project")

st.write(
    "This project demonstrates basic password security concepts. "
    "It checks common password characteristics and provides "
    "security awareness recommendations."
)

st.write("**Student:** Dhanush Devendra")
st.write("**Course:** TY BSc Information Technology")
st.write("**College:** SIWS College")
st.write("**Project:** Password Strength & Security Awareness")


# Footer
st.divider()

st.caption("Cybersecurity Awareness Mini Project")
st.caption("Created by Dhanush Devendra")

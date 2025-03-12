import re
import random
import string
import streamlit as st

def check_password_strength(password):
    score = 0
    feedback = []
    
    # Criteria checks
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Make your password at least 8 characters long.")
    
    if any(char.islower() for char in password) and any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Include both uppercase and lowercase letters.")
    
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Add at least one digit (0-9).")
    
    if re.search(r"[!@#$%^&*]", password):
        score += 2
    else:
        feedback.append("Use at least one special character (!@#$%^&*).")
    
    common_passwords = {"password123", "123456", "qwerty", "admin", "letmein"}
    if password.lower() in common_passwords:
        score = 1
        feedback = ["Avoid using common passwords."]
    
    return score, feedback

def generate_strong_password():
    characters = (
        random.choice(string.ascii_uppercase) +
        random.choice(string.ascii_lowercase) +
        random.choice(string.digits) +
        random.choice("!@#$%^&*")
    )
    remaining_chars = random.choices(string.ascii_letters + string.digits + "!@#$%^&*", k=8)
    password = list(characters + "".join(remaining_chars))
    random.shuffle(password)
    return "".join(password)

def main():
    st.title("🔐 Password Strength Meter")
    password = st.text_input("Enter a password:", type="password")
    
    if st.button("Check Strength"):
        score, feedback = check_password_strength(password)
        
        if score == 5:
            st.success("✅ Strong Password!")
        elif score >= 3:
            st.warning("⚠️ Moderate Password. Consider improving it.")
        else:
            st.error("❌ Weak Password! Suggestions:")
            for tip in feedback:
                st.write(f"- {tip}")
            st.info(f"🔹 Suggested Strong Password: {generate_strong_password()}")

main()

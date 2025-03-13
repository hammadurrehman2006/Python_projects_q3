import streamlit as st
import re
import random
import string
import streamlit.components.v1 as components

# Custom CSS for better styling
st.markdown("""
    <style>
    .title {text-align: center; color: rgb(230, 107, 31); font-family: 'Arial', sans-serif; margin-bottom: 20px;}
    .strength-bar {height: 15px; border-radius: 8px; margin: 15px 0; transition: width 0.3s ease-in-out;}
    .weak {background-color: #ff4d4d; width: 25%; border: 1px solid #cc0000;}
    .moderate {background-color: #ff9900; width: 50%; border: 1px solid #cc7a00;}
    .good {background-color: #ffff00; width: 75%; border: 1px solid #cccc00;}
    .strong {background-color: #00cc00; width: 100%; border: 1px solid #009900;}
    .footer {text-align: center; color: #666; margin-top: 70px; font-size: 14px;}
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 class='title'>Password Strength Checker</h1>", unsafe_allow_html=True)
def check_password_strength(password):
    if not password:
        return 0, []
    
    score = 0
    feedback = []
    
    # Length checks
    length = len(password)
    if length >= 12:
        score += 2
    elif length >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters (12+ for best security).")
    
    # Character variety checks
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter (A-Z).")
        
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter (a-z).")
        
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Include at least one number (0-9).")
        
    if re.search(r"[@#$%&]", password):
        score += 1
    else:
        feedback.append("Add at least one special character (@#$%& etc.).")
    
    # Additional security checks
    if re.search(r"(.)\1{2,}", password):
        feedback.append("Avoid repeating the same character more than twice in a row.")
        score -= 1
    
    return min(max(score, 0), 4), feedback

def generate_strong_password(length=16):
    characters = (string.ascii_lowercase + string.ascii_uppercase + 
                 string.digits + "@#$%&")
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice("@#$&")
    ]
    password += random.choices(characters, k=length-4)
    random.shuffle(password)
    return ''.join(password)

# Main Interface
st.subheader("Secure Your Personal Accounts")
st.write("Create a strong password to protect your accounts.")

# Password Input Section
col1, col2 = st.columns(2)
with col1:
    password = st.text_input("Enter your password:", type="password", 
                           help="Keep it unique and memorable!")
with col2:
    confirm_password = st.text_input("Confirm your password:", type="password")

# Evaluate Password
if password:
    score, feedback = check_password_strength(password)
    
    # Password Match Check
    if password != confirm_password and confirm_password:
        st.error("❌ Passwords don\'t match!")
    else:
        # Strength Display
        strength_levels = {
            4: ("strong", "✅ Excellent Password! Your data is well-protected."),
            3: ("good", "👍 Good Password - Almost perfect security."),
            2: ("moderate", "⚠️ Moderate Password - Could be stronger."),
            1: ("weak", "❌ Weak Password - Needs improvement."),
            0: ("weak", "❌ Very Weak Password - Needs significant improvement.")
        }
        
        strength_class, message = strength_levels[score]
        st.markdown(f"<div class='strength-bar {strength_class}'></div>", unsafe_allow_html=True)
        st.write(message)
        
        # Display Feedback
        if feedback:
            st.write("Improvement Tips:")
            for tip in feedback:
                st.write(f"- {tip}")
else:
    st.info("🔑 Enter a password to check its strength.")

# Password Suggestion 
st.markdown("### Need a Strong Password?")
if st.button("Generate Secure Password"):
    suggested_password = generate_strong_password()
    st.markdown("<div class='suggestion-box'>", unsafe_allow_html=True)
    st.write(f"Suggested Password: `{suggested_password}`")
    st.write("This password includes uppercase, lowercase, numbers, and special characters.")
    components.html(
    f"""
    <style>
    .copy-button {{
        background-color: #4CAF50;
        color: white;
        padding: 5px 10px;
        border-radius: 5px;
        cursor: pointer;
        border: none;
        font-size: 16px;
    }}
    .copy-button:hover {{
        background-color: #45a049;
    }}
    </style>
    <button class='copy-button' onclick='copyToClipboard()'>Copy</button>
    <script>
    function copyToClipboard() {{
        var tempInput = document.createElement("input");
        tempInput.value = "{suggested_password}";
        document.body.appendChild(tempInput);
        tempInput.select();
        document.execCommand("copy");
        document.body.removeChild(tempInput);
        alert("Password copied to clipboard!");
    }}
    </script>
    """,
    height=60
)
st.markdown("</div>", unsafe_allow_html=True)
st.markdown("<div class='footer'>Made with 🤍 by Muhammad Hammad ur Rehman</div>", unsafe_allow_html=True)
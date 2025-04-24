# Develop a Secure Data Storage System!

import streamlit as st
import hashlib
import json
import os
import time
from cryptography.fernet import Fernet
from base64 import urlsafe_b64encode
from hashlib import pbkdf2_hmac

# User Information

DATA_FILE = "secure_data.json"
SALT = b"secure_salt_value"
LOGOUT_DURATION = 60

# Login Details

if "authenticated_user" not in st.session_state:
    st.session_state.authenticated_user = None

if "failed_attempts" not in st.session_state:
        st.session_state.failed_attempts = 0

if "logout_time" not in st.session_state:
      st.session_state.logout_time = 0

# if data is load

def load_data():
      if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                  return json.load(f)
      return {}
def save_data(data):
      with open(DATA_FILE, "w") as f:
            json.dump(data, f)
    
def generate_key(passkey):
      key = pbkdf2_hmac('sha256', passkey.encode(), SALT, 100000)
      return urlsafe_b64encode(key)

def hash_password(password):
      return hashlib.pbkdf2_hmac('sha256', password.encode(), SALT, 100000).hex()

# cryptography.fernet used

def encrypt_text(text, key):
      cipher = Fernet(generate_key(key))
      return cipher.encrypt(text.encode()).decode()

def decrypt_text(encrypt_text, key):
      try:
            cipher = Fernet(generate_key(key))
            return cipher.decrypt(encrypt_text.encode()).decode()
      except:
            return None
      
stored_data = load_data()

# Navigation Bar

st.title(" 🔐 Secure Data Encryption App")
menu = ["Home", "Register", "Login", "Store Data", "Retieve Data"]
choice = st.sidebar.selectbox("Navigation", menu)

if choice == "Home":
      st.subheader(" Welcome to my 🔐 Secure Data Encryption System ! ")
      st.markdown("🙂 Develop a Streamlit-base secure data storage and retrival system..")
      st.markdown("✅ Encrypt & store sensitive text..")
      st.markdown("🔐 Protected by secure hashing (PBKDF2).")

# User Rigistration 

elif choice == "Register":
    st.subheader("Register New User")
    username = st.text_input("choose Your User_Name")
    password = st.text_input("Choose Password", type="password")

    if st.button("Register"):
        if username and password:
            if username in stored_data:
                st.warning("User already exisits..")
            else:
                stored_data[username] = {
                      "password": hash_password(password),
                      "data" : []
                      }
                save_data(stored_data)
                st.success("✅User Register Successfully")
        else:
            st.error("Both fields are required..")

elif choice == "Login":
        st.subheader("User Login")

        if time.time() < st.session_state.logout_time:
            remaining = int(st.session_state.logout_time - time.time())
            st.error(f"Too many failed attempts. please wait {remaining} seconds..")
            st.stop()

        username = st.text_input("Username")
        password = st.text_input("password", type="password")

        if st.button("Login"):
            if username in stored_data and stored_data[username]["password"] == hash_password(password):
                        st.session_state.authenticated_user = username
                        st.session_state.failed_attempts = 0
                        st.success(f"✅ Welcome {username}!")
            else:
                        st.session_state.failed_attempts += 1
                        remaining = 3 - st.session_state.failed_attempts
                        st.error(f"❌ Invaliede Credentials! Attempts left: {remaining}")

                        if st.session_state.failed_attempts >= 3:
                              st.session_state.logout_time = time.time() + LOGOUT_DURATION
                              st.error("To many failed attempts. Locked for 60 seconds")
                              st.stop()

# data storage section

elif choice == "Store Data":
      if not st.session_state.authenticated_user:
            st.warning("🔒Please login first.")
      else:
            st.subheader("Store Encrypted Data")
            data = st.text_area("Enter data to encrypt")
            passkey = st.text_input("Encrypt key (passphrase)", type="password")

            if st.button("Encrypt and Save"):
                  if data and passkey:
                        encrypted = encrypt_text(data, passkey)
                        stored_data[st.session_state.authenticated_user]["data"].append(encrypted)
                        save_data(stored_data)
                        st.success("✅Data encrypted and save sucessfully")

                  else:
                        st.error("All fields are required to fill..")

# data retrive data section

elif choice == "Retieve Data":
      if not st.session_state.authenticated_user:
            st.warning("🔒Please login first!")
      else:
            st.subheader("Retieve Data")
            user_data = stored_data.get(st.session_state.authenticated_user, {}).get("data", [])

            if not user_data:
                  st.info("No Data Found!")
            else:
                  st.write("Encrypted Data Enteries:")
                  for i, item in enumerate(user_data):
                        st.code(item,language="text")

                  encrypt_input = st.text_area("Enter Encrypted Text")
                  passkey = st.text_input("Enter Passkey T Decrypt", type="password")

                  if st.button("Decrypt"):
                        result = decrypt_text(encrypt_input, passkey)
                        if result:
                              st.success(f"✅Decrypted: {result}")
                        else:
                              st.error("Incorrect passkey or corrupted data!")

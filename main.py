import streamlit as st
import random
import string                                          # string ka module hame specific letters provide krta hai aur letters kese bhi form me ho skate yani uppercase, lowercase or etc.
import re                                              # check krta hai ke password strong hai ya weak 

def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters                  #ascii characters hame uppercase or lowercase letters provide krta hai
    if use_digits:
        characters += string.digits                     # agar user digits istemal krna cha raha hai to string ka digits ka  module digits bhi provide krta hai . += ka matalab hai ke iss variable ke andar app assign karo 
    if use_special:
        characters += string.punctuation                 # agar user special characters istemal krna cha raha hai to string ka punctuation method ye bhi  provide krta hai 
    return ''.join(random.choice(characters) for _ in range(length))            # random.choice() method random character select krta hai aur join() method un characters ko join kr deta hai. range() method hame length provide krta hai ke kitne characters chahiye


def check_password_strength(password):
    strength = 0                              # start with zero strength
    criteria = [
        (r"[a-z]", "Lowercase Letter"),
        (r"[A-Z]", "Uppercase Letter"),
        (r"\d", "Number"),
        (r"[@$!%*?&]", "Special Character (@$!%*?&)"),
        (r".{8,}", "At least 8 characters")
    ]
    
    passed_criteria = [check for pattern, check in criteria if re.search(pattern, password)]            # the goal  of this line is to check how strong a password is by matching it with criteria 
    strength = len(passed_criteria)
    
    return strength, passed_criteria

st.title('Password Generator & Strength Meter')

length = st.slider('Length of password:', min_value=8, max_value=32, value=12)
use_digits = st.checkbox('Use digits')
use_special = st.checkbox('Use special characters')

if st.button('Generate Password'):
    password = generate_password(length, use_digits, use_special)
    st.write(f"Generated Password : {password}")
    
    strength, passed_criteria = check_password_strength(password)
    
    if strength == 5:
        st.success("Strong Password! ✅")
    elif strength >= 3:
        st.warning("Moderate Password! ⚠️ Try adding more complexity.")
    else:
        st.error("Weak Password! ❌ Use a mix of letters, numbers, and symbols.")
    
    st.write("### Criteria Matched:")
    for criterion in passed_criteria:
        st.write(f"✅ {criterion}")
    
    st.write("-----------------------------------------------")
    st.write("Made By Muhammad Usaid Khan")

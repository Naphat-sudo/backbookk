import streamlit as st
import requests

st.title("BACKBOOK")

fname = st.text_input("First Name")
lname = st.text_input("Last Name")
age = st.text_input("Age")
gender = st.text_input("Gender")
nation = st.text_input("Nation")
school = st.text_input("School Name")
student_id = st.text_input("Student ID")
grade = st.text_input("Grade")
address = st.text_input("Address")
tel = st.text_input("Tel")

if st.button("Submit"):

    data = {
        "fname": fname,
        "lname": lname,
        "age": age,
        "gender": gender,
        "nation": nation,
        "school": school,
        "student_id": student_id,
        "grade": grade,
        "address": address,
        "tel": tel
    }

    url = "https://script.google.com/macros/s/AKfycbxsPiT9l-Iz-nEiqKftaHyqGG_MW-XjZ2vp2C_Mw2UKr7gfbJgnEpu48zhV4PKemJNZKw/exec"

    response = requests.post(url, json=data)

    if response.text == "Success":
        st.success("ส่งข้อมูลสำเร็จ!")
    else:
        st.error("เกิดข้อผิดพลาด")
import streamlit as st 


st.title("Calculator")
st.divider()

# name = st.text_input("What is your name ?")

# age = st.number_input("How old are you ?", min_value=1, max_value=100)

# occupaiton = st.selectbox("What is your occupation ?", ["Employee", "Businessman", "Freelancer"])

# submit = st.button("Submit")

# if submit:
#     if(name == "" or age == 0 or occupaiton == ""):
#         st.warning("Please enter your details")
#     else : 
#         st.success(f"Hello {name}, you are {age} years old and you are a {occupaiton}")

# two_number = st.text_input("Enter two numbers", value="1,2")

# operator = st.selectbox("Select an operator", ["+", "-", "*", "/"])

# press = st.button("Show Result")

# if press :
#     try : 
#         num1 , num2 = map(int,two_number.split(","))
#         if operator == "+":
#             st.success(f"{num1} + {num2} = {num1 + num2}")
#         elif operator == "-":
#              st.success(f"{num1} - {num2} = {num1 - num2}")
#         elif operator == "*":
#           st.success(f"{num1} * {num2} = {num1 * num2}")
#         elif operator == "/":
#             st.success(f"{num1} / {num2} = {num1 / num2}")

#     except Exception as e :
#         st.error(f"Error : {e}")
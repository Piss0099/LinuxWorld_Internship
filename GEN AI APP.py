import streamlit as st
import google.generativeai as genai

# ---------------------------------------------------
# Title (App ka naam)
# ---------------------------------------------------
st.title("Simple AI Chat App")
st.write("Ask anything and AI will reply.")

# ---------------------------------------------------
# API key input (user yaha apni API key dalega)
# ---------------------------------------------------
api_key = st.text_input("Enter your Gemini API Key:", type="password")

# Agar user ne API key di hai tab hi AI chalega
if api_key:

    # AI configure karna
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.5-flash")

    st.subheader("Ask your question")

    # User question input
    user_msg = st.text_input("Type something...")

    # Jab user message likhe tab AI reply karega
    if user_msg:

        # Exit command
        if user_msg.lower() == "exit":
            st.warning("Goodbye!")
        else:
            # AI se jawaab lana
            response = model.generate_content(user_msg)

            # Bot ka reply show karna
            st.write("###AI Reply:")
            st.success(response.text)

else:
    st.info("Please enter API key to start the AI.")

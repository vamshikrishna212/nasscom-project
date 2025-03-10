import streamlit as st
from post_generator2 import generate_post, get_modified_response, get_prompt

# Options for length and language
length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish", "Telugu", "Hindi", "Tenglish", "Malayalam"]

# Main app layout
def main():
    st.subheader("Email Generator: NassCom Project")

    # Create three columns for dropdowns
    col1, col2, col3 = st.columns(3)

    tags = ["Formal", "Casual", "Friendly", "Professional", "Persuasive", "Apologetic", "Appreciative", "Introduction",
            "Follow-up", "Thank You", "Apology", "Complaint", "Invitation", "Job Application", "Networking", "Reminder",
            "Announcement", "Feedback Request", "Sales Pitch", "Very Formal", "Semi-Formal", "Informal", "Colleague",
            "Boss", "Client", "Customer", "Friend", "Professor", "Recruiter", "Vendor", "Bullet Points",
            "Paragraph-Based", "Hybrid", "Low", "Moderate", "High", "Personalized", "Generic", "Template-Based",
            "No Response Needed", "Response Expected", "Follow-Up Required"]

    with col1:
        selected_tag = st.selectbox("Type", options=tags)
    with col2:
        selected_length = st.selectbox("Length", options=length_options)
    with col3:
        selected_language = st.selectbox("Language", options=language_options)

    scenario = st.text_input('Enter the Scenario:', 'Eg: Ask permission to manager for a leave')
    sender = st.text_input("Sender's Name:")
    receiver = st.text_input("Receiver's Name:")

    # Initialize session state
    if "generated_email" not in st.session_state:
        st.session_state.generated_email = ""
    if "modification_history" not in st.session_state:
        st.session_state.modification_history = ""
    if "idx" not in st.session_state:
        st.session_state.idx = 1

    # Generate Button
    if st.button("Generate"):
        st.session_state.prompt = get_prompt(selected_length, selected_language, selected_tag, scenario, sender, receiver)
        st.session_state.generated_email = generate_post(st.session_state.prompt)
        st.session_state.modification_history = st.session_state.prompt  # Store base prompt for modifications

    # Layout for email and chatbot-style modifications
    col_email, col_modifications = st.columns([3, 2])

    with col_email:
        # Display the generated email
        if st.session_state.generated_email:
            st.markdown("Generated Email")
            st.markdown(f"""
            <div style="
                background-color: #f8f9fa; 
                color : #000;
                padding: 15px; 
                border-radius: 8px; 
                font-family: Arial, sans-serif;
                border: 1px solid #ddd;">
                {st.session_state.generated_email}
            </div>
            """, unsafe_allow_html=True)

    with col_modifications:
        # Chatbot-style modification requests
        st.markdown("### 🤖 Chatbot - Modify Email")

        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []

        # Display past modifications
        for chat in st.session_state.chat_history:
            with st.chat_message("user"):
                st.write(chat)

        # Modification request input
        modification_request = st.text_area("Enter Modification Request:", "Eg: Make it more formal, Add a thank you note, etc.")

        if st.button("♻️ Regenerate"):
            st.session_state.modification_history += f" *** Modification Request {st.session_state.idx}*** {modification_request}"
            st.session_state.idx += 1  # Increment modification count
            st.session_state.generated_email = get_modified_response(st.session_state.modification_history)

            # Add modification request to chat history
            st.session_state.chat_history.append(modification_request)
            if len(st.session_state.chat_history) > 4:
                st.session_state.chat_history.pop(0)  # Remove the oldest message

            st.rerun()

# Run the app
if __name__ == "__main__":
    main()
















# import streamlit as st
# from post_generator2 import generate_post, get_modified_response, get_prompt

# # Options for length and language
# length_options = ["Short", "Medium", "Long"]
# language_options = ["English", "Hinglish", "Telugu", "Hindi", "Tenglish", "Malayalam"]

# # Main app layout
# def main():
#     st.subheader("Email Generator: NassCom Project")

#     # Create three columns for the dropdowns
#     col1, col2, col3 = st.columns(3)

#     tags = ["Formal", "Casual", "Friendly", "Professional", "Persuasive", "Apologetic", "Appreciative", "Introduction",
#             "Follow-up", "Thank You", "Apology", "Complaint", "Invitation", "Job Application", "Networking", "Reminder",
#             "Announcement", "Feedback Request", "Sales Pitch", "Very Formal", "Semi-Formal", "Informal", "Colleague",
#             "Boss", "Client", "Customer", "Friend", "Professor", "Recruiter", "Vendor", "Bullet Points",
#             "Paragraph-Based", "Hybrid", "Low", "Moderate", "High", "Personalized", "Generic", "Template-Based",
#             "No Response Needed", "Response Expected", "Follow-Up Required"]

#     with col1:
#         selected_tag = st.selectbox("Type", options=tags)
#     with col2:
#         selected_length = st.selectbox("Length", options=length_options)
#     with col3:
#         selected_language = st.selectbox("Language", options=language_options)

#     scenario = st.text_input('Enter the Scenario: ', 'Eg: Ask permission to manager for a leave')
#     sender = st.text_input("Sender's Name : ")
#     receiver = st.text_input("Receiver's Name : ")

#     # Initialize session state variables
#     if "generated_email" not in st.session_state:
#         st.session_state.generated_email = ""
#     if "modification_history" not in st.session_state:
#         st.session_state.modification_history = ""
#     if "idx" not in st.session_state:
#         st.session_state.idx = 1

#     # Generate Button
#     if st.button("Generate"):
#         st.session_state.prompt = get_prompt(selected_length, selected_language, selected_tag, scenario, sender, receiver)
#         st.session_state.generated_email = generate_post(st.session_state.prompt)
#         st.session_state.modification_history = st.session_state.prompt  # Store base prompt for modifications

#     # Display the generated email
#     if st.session_state.generated_email:
#         cssString = '''
#             @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
#             .email-template {
#                 background-color: white;
#                 color: black;
#                 border: 1px solid #ddd;
#                 font-family: sans-serif;
#                 font-size: 14px;
#             }
#             .email-para p::before {
#                 content: "      ";
#                 display: block;
#             }
#         '''
#         st.markdown(f"<style>{cssString}</style>", unsafe_allow_html=True)
#         st.markdown(st.session_state.generated_email, unsafe_allow_html=True)

#         # Textbox for modification request
#         modification_request = st.text_area("Modification Request (Optional):", 
#                                             "Eg: Make it more formal, Add a thank you note, etc.")

#         # Regenerate Button - Calls API Again
#         if st.button("Regenerate"):
#             # Append the modification request to history
#             st.session_state.modification_history += f" *** Modification Request {st.session_state.idx}*** {modification_request}"
#             st.session_state.idx += 1  # Increment modification count
#             # Get the modified response
#             st.session_state.generated_email = get_modified_response(st.session_state.modification_history)
#             st.rerun()

# # Run the app
# if __name__ == "__main__":
#     main()

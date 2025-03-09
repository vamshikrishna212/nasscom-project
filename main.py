import streamlit as st
from post_generator import generate_post


# Options for length and language
length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish","Telugu","Hindi","Tenglish","Malayalam"]


# Main app layout
def main():
    st.subheader("Email Generator: NassCom Project")

    # Create three columns for the dropdowns
    col1, col2, col3 = st.columns(3)

    tags = ["Formal", "Casual", "Friendly", "Professional", "Persuasive", "Apologetic", "Appreciative", "Introduction", "Follow-up", "Thank You", "Apology", "Complaint", "Invitation", "Job Application", "Networking", "Reminder", "Announcement", "Feedback Request", "Sales Pitch", "Very Formal", "Semi-Formal", "Informal", "Colleague", "Boss", "Client", "Customer", "Friend", "Professor", "Recruiter", "Vendor", "Bullet Points", "Paragraph-Based", "Hybrid", "Low", "Moderate", "High", "Personalized", "Generic", "Template-Based", "No Response Needed", "Response Expected", "Follow-Up Required"]
    with col1:
        # Dropdown for Topic (Tags)
        selected_tag = st.selectbox("Type", options=tags)

    with col2:
        # Dropdown for Length
        selected_length = st.selectbox("Length", options=length_options)

    with col3:
        # Dropdown for Language
        selected_language = st.selectbox("Language", options=language_options)

    scenario = st.text_input('Enter the Scenario: ', 'Eg: Ask permission to manager for a leave')
    sender = st.text_input("Sender's Name : ")
    receiver = st.text_input("Receiver's Name : ")

    # Generate Button
    if st.button("Generate"):
        post = generate_post(selected_length, selected_language, selected_tag,scenario,sender,receiver)
        cssString = '''
            @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
            .email-template {
            background-color: white;
            color: black;
            border: 1px solid #ddd;
            font-family: sans-serif;
            font-size: 14px;
           
            }
            
            .email-para p::before{
                content: "      ";
                display: block;
            }
        '''
        st.markdown(f"<style>{cssString}</style>", unsafe_allow_html=True)
        st.markdown(post, unsafe_allow_html=True)
        #st.write(post)


# Run the app
if __name__ == "__main__":
    main()

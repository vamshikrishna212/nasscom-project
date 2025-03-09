import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post


# Options for length and language
length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish","Telugu","Hindi","Tenglish","Malayalam"]


# Main app layout
def main():
    st.subheader("Email Generator: NassCom Project")

    # Create three columns for the dropdowns
    col1, col2, col3 = st.columns(3)

    fs = FewShotPosts()
    #tags = fs.get_tags()
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

    # Generate Button
    if st.button("Generate"):
        post = generate_post(selected_length, selected_language, selected_tag,scenario)
#         post = '''
#         Dear Manager,\n\n\tI am writing to inform you that, unfortunately, I will be unable to come to work for the next few days.\n\n\tI am currently not feeling well and my health is not in the best condition.\n\n\tI have been diagnosed with an illness that requires me to take some time off to recover.\n\n\tI apologize for any inconvenience this may cause and will make sure to catch up on any missed work as soon as possible.\n\n\tI will keep you updated on my status and provide a doctor\'s note if needed.\n\n\tThe expected dates of my leave are from [start date] to [end date].\n\n\tI will be available by email if anything urgent comes up while I am away.\n\n\tPlease let me know if there are any pressing matters that need my attention before my leave.\n\n\tI appreciate your understanding and support during this time.\n\n\tIf there is anything I can do to mitigate the impact of my absence, please let me know.\n\n\tI am committed to my responsibilities and will ensure a smooth transition of tasks.\n\n\tI will respond to all emails and messages as soon as I am feeling better.\n\n\tThank you for your consideration and I look forward to returning to work as soon as possible.\n\n\tPlease do not hesitate to contact me if you have any questions or concerns.\n\nSincerely,\n\n[Your Name]\n\nBest regards, \n\n[Your Name]
# Dear Manager,\n\n\tI am writing to inform you that, unfortunately, I will be unable to come to work for the next few days.\n\n\tI am currently not feeling well and my health is not in the best condition.\n\n\tI have been diagnosed with an illness that requires me to take some time off to recover.\n\n\tI apologize for any inconvenience this may cause and will make sure to catch up on any missed work as soon as possible.\n\n\tI will keep you updated on my status and provide a doctor\'s note if needed.\n\n\tThe expected dates of my leave are from [start date] to [end date].\n\n\tI will be available by email if anything urgent comes up while I am away.\n\n\tPlease let me know if there are any pressing matters that need my attention before my leave.\n\n\tI appreciate your understanding and support during this time.\n\n\tIf there is anything I can do to mitigate the impact of my absence, please let me know.\n\n\tI am committed to my responsibilities and will ensure a smooth transition of tasks.\n\n\tI will respond to all emails and messages as soon as I am feeling better.\n\n\tThank you for your consideration and I look forward to returning to work as soon as possible.\n\n\tPlease do not hesitate to contact me if you have any questions or concerns.\n\nSincerely,\n\n[Your Name]\n\nBest regards, \n\n[Your Name]
# '''
        cssString = '''
            @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
            .email-template {
            background-color: white;
            color: black;
            border: 1px solid #ddd;
            font-family: sans-serif;
            font-size: 14px;
           
        }
        '''
        st.markdown(f"<style>{cssString}</style>", unsafe_allow_html=True)
        st.markdown(post, unsafe_allow_html=True)
        #st.write(post)


# Run the app
if __name__ == "__main__":
    main()

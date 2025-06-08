import os 
import streamlit as st 
from chatbot.agent import generate_response
from utils.info_extract import extract_user_info
from prompts.base_prompts import exit_keywords, exit_message, info_collection_prompt, tech_stack_prompt, dynamic_generation_prompt 

def render_chat_interface(greeting_prompt):
    st.set_page_config(page_title = "TalentScout Hiring Assistant", layout = "centered")

    # A clean UI for the chat interface from the .html file 
    with open(os.path.join("ui", "chat.html"), "r") as f:
        st.markdown(f.read(), unsafe_allow_html = True)

    st.markdown("<h2 style='text-align: center;'>TalentScout Hiring Assistant</h2>", unsafe_allow_html = True)

    # Initilize a list to store the conversation history and end flag to indicate if the conversation has ended or
    if "conversation" not in st.session_state:
        st.session_state.conversation = [] 
    if "ended" not in st.session_state:
        st.session_state.ended = False 

    # Collect the user information an store the user/candidate name for the chat
    if "user_info_collected" not in st.session_state:
        st.session_state.user_info_collected = False
    if "candidate_name" not in st.session_state:
        st.session_state.candidate_name = "You"

    # Show the collect info panel only once
    if "info" not in st.session_state:
        st.session_state.info = False 

    # Show the tech stack panel only once
    if "techstack" not in st.session_state:
        st.session_state.techstack = False 

    # Show the greeting message only at the beginning of the conversation
    if "started" not in st.session_state:
        st.session_state.started = False

    # Start the session with Greeting message
    if not st.session_state.started:
        st.markdown(f"<div class='chat-bubble bot'><strong>TalentScout Hiring Assistant:</strong><br>{greeting_prompt}</div>", unsafe_allow_html = True)
        if st.button("Get Started"):
            st.session_state.started = True
            st.rerun()
        return  
    
    # The information panel needs to be visible only once
    if not st.session_state.conversation and not st.session_state.info:
        st.session_state.conversation.append(("bot", info_collection_prompt))
        st.session_state.info = True

    # The tech stack panel needs to be visible only once
    if not st.session_state.conversation and not st.session_state.techstack:
        st.session_state.conversation.append(("bot", tech_stack_prompt))
        st.session_state.techstack = True 

    # Display the bot and user messages/chat
    for role, message in st.session_state.conversation:
        role_class = "bot" if role == "bot" else "user"
        label = "TalentScout Hiring Assistant" if role == "bot" else st.session_state.candidate_name
        st.markdown(f"<div class='chat-bubble {role_class}'><strong>{label}:</strong><br>{message}</div>", unsafe_allow_html = True)

    # Taking user details after the grreting message with separate input fields for each
    if not st.session_state.user_info_collected:

        st.header("Please enter your details")

        full_name = st.text_input("Full Name", key="full_name")
        email = st.text_input("Email Address", key="email")
        phone = st.text_input("Phone Number", key="phone")
        years_exp = st.text_input("Years of Experience", key="years_exp")
        desired_pos = st.text_input("Desired Position", key="desired_pos")

        if st.button("Submit Info"):
            # Store user details in a dictionary
            user_info_dict = {
                "Full Name": full_name,
                "Email Address": email,
                "Phone Number": phone,
                "Years of Experience": years_exp,
                "Desired Position": desired_pos
            }
            
            print(user_info_dict) 
            st.session_state.user_profile = user_info_dict

            # Use the user/candidate name for the chat 
            candidate_name = user_info_dict.get("Full Name", "Candidate")
            st.session_state.candidate_name = candidate_name
            st.session_state.user_info_collected = True

            # Remove the info panel from conversation 
            st.session_state.conversation = [
                msg for msg in st.session_state.conversation if msg[1] != info_collection_prompt
            ]
            print(st.session_state.conversation)

            st.rerun()

    # After info collected, we will ask for tech stack
    elif st.session_state.user_info_collected and "tech_stack_collected" not in st.session_state:
        tech_stack = st.text_input("Tech Stack (e.g., Python, ML, Docker)", key="tech_stack")

        if st.button("Submit Tech Stack"):
            st.session_state.user_profile["Tech Stack"] = tech_stack
            st.session_state.tech_stack_collected = True

            # Remove the tech stack panel from conversation 
            st.session_state.conversation = [
                msg for msg in st.session_state.conversation if msg[1] != tech_stack_prompt
            ]

            # Add bot message confirming tech stack collection
            bot_reply = (
                f"Thank you, {st.session_state.candidate_name}. I’ve recorded your tech stack: "
                "Let's proceed with some questions based on it."
            )
            st.session_state.conversation.append(("bot", bot_reply))

            # # Generate the questions for the user based on the tech stacks
            hidden_prompt = dynamic_generation_prompt(tech_stack) 
            llm_context = st.session_state.conversation + [("system", hidden_prompt)]
            generate_question = generate_response(llm_context)
            st.session_state.conversation.append(("bot", generate_question)) 

            st.rerun()

    # Taking input from the user 
    elif not st.session_state.ended:
        with st.form("user_input_form", clear_on_submit = True):
            user_input = st.text_input("Your response", placeholder = "Type here...", key = "input")
            submitted = st.form_submit_button("Send")

            if submitted and user_input.strip():
                st.session_state.conversation.append(("user", user_input.strip()))

                # Handling exit if user types any of the exit keyword in the chat
                if any(exit_word in user_input.lower() for exit_word in exit_keywords):
                    st.session_state.conversation.append(("bot", exit_message))
                    st.session_state.ended = True
                else:
                    # Generate AI reply
                    bot_reply = generate_response(st.session_state.conversation)
                    st.session_state.conversation.append(("bot", bot_reply))

                st.rerun()

    else:
        st.success("This session has ended. Refresh the page to start over.")

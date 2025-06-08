
# Initial greeting to the user/candidate
greeting_prompt = """
<div style='
    background-color: #ffffff;
    padding: 20px;
    border-radius: 15px;
    margin: 20px auto;
    max-width: 600px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.3);
    font-size: 16px;
    line-height: 1.6;
'>
    <strong>Hello!</strong> I'm TalentScout's virtual hiring assistant.<br>
    I'm here to guide you through the initial screening process.<br>
    Click <strong>Get Started</strong> below to start!
</div>
"""

# Prompt to gather the user information 
info_collection_prompt = """
<div style='
    background-color: #fef9e7;
    padding: 20px;
    border-radius: 15px;
    margin: 20px auto;
    max-width: 600px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.08);
    font-size: 16px;
    line-height: 1.6;
'>
    <strong style='font-size: 17px;'>Please provide the following details:</strong><br><br>
    <ul style='padding-left: 20px;'>
        <li><strong>Full Name:</strong></li>
        <li><strong>Email Address:</strong></li>
        <li><strong>Phone Number:</strong></li>
        <li><strong>Years of Experience:</strong></li>
        <li><strong>Desired Position:</strong></li>
    </ul>
</div>
"""

# Prompt for tech stack details
tech_stack_prompt = """
<div style='
    background-color: #e8f8f5;
    padding: 20px;
    border-radius: 15px;
    margin: 20px auto;
    max-width: 600px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.08);
    font-size: 16px;
    line-height: 1.6;
'>
    <strong style='font-size: 17px;'>Great! Now tell me about your technical skills:</strong><br><br>
    You can include:
    <ul style='padding-left: 20px; margin-top: 5px;'>
        <li>Programming Languages</li>
        <li>Frameworks & Libraries</li>
        <li>Databases</li>
        <li>Cloud Platforms</li>
        <li>Other Tools & Technologies</li>
    </ul>
</div>
"""

# Generate dynamic prompt for technical questions
def dynamic_generation_prompt(tech: str, level: str = "intermediate"): 
    return (
        f"Generate 3 technical interview questions at {level} level"
        f"to evaluate a candidate skills in {tech}"
        f"Make the questions concise but effective"
    )

# Exit messages to terminate the conversation
exit_message = (
    "Thank you for your time!"
    "Our recuritment team will get in touch with you shortly."
)

exit_keywords = ["exit", "quit", "end", "stop", "thank you"]
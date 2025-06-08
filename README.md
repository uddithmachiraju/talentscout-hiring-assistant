# TalentScout: Intelligent Hiring Assistant 
In this project I built a AI-Powered Hiring Assistance chatbot the helps in the initial screening process for the candidates in tech roles. This project is built with `streamlit` and the AI agent used is `google.generativeai` this agent gathers the candidate information and dynamically generates messages based on the candidate tech stack and chat history. 

## Key Features
- Clean and minimal UI 
- Collects essential details of the candidate
    - Full Name
    - Email Address
    - Phone Number
    - Years of Experience
    - Desired Position
    - Current Location
- Gathers the candidate tech stack.
- Dynamically generated technical questions using `google.generativeai` agent. 
- Maintains context/history throught the converstation. 
- Fallback response and exit handling.

### Access it from the streamlit cloud(free tier) 
Link: 

## Installation Instructions:
Follow the steps to set up the project locally:

### 1. Clone the repository
```bash
git clone https://github.com/uddithmachiraju/talentscout-hiring-assistant.git 
cd talentscout-hiring-assistant
```

### 2. Install required dependencies
```bash
pip install -r requirements.txt
```

### 3. Generate a google access key for the LLM agent. 
**Steps** 
1. Go to [Google AI Studio](https://makersuite.google.com/app)
2. Click "Get API Key" (don't worry it's free)
3. Click Create API Key and copy the generated key.

### 4. Create a `.env` file
- In the root directory of the project create a `.env` file
    ```bash
    touch .env
    ```
- Add the copied access key:  
    ```bash 
    AGENT_API_KEY = your_access_key
    ``` 
- Save the file.

### 5. Run the application
```bash
streamlit run app.py
```
If everything goes well. You can see it in your default browser. 

## Usage Guide
- After running the above command. The first thing you see is the **welcome screen** with a **Get Started** button. Click it to begin your journey. 
- After the welcome screen you will see the **information panel** with all the necessary details you enter the details and click submit form. 
- After the welcome screen you will see the **tech stack** panel. Enter the **programming languages, frameworks, databases, and tools they are proficient in**.
- Based on the tech stack information the **agent** will automatically generates some technical questions for you.
- You can **end** the session anytime by typing any of the exit keywords mentioned below:
    ```bash
    "exit", "quit", "end", "stop", "thank you"
    ```
- To restart the conversation, simply refresh the page. (Note: if you refresh the page you need start from the beginning again(no data saved)) 

## Technical Details

### Libraries and Frameworks used
- `python 3.10+` 
- `Streamlit` - Used for uilding UI
- `Google Generative AI` - Gemini LLM to handle conversations and generate tech questions. 
- `dotenv` - For managing API Keys. 

### Model Details
- Used **Google Gemini 1.5 Flash** 

### Architectural Decisions
- **Modular Project Structure** - used different folders for `chatbot`, `prompts`, `utils`, `ui`. 
- Context is maintained locally via Steamlit `session_state` and passed the full conversation to LLM to follow-up questions and ensure a coherent flow.
- **UI Design** - Maintained with simple and minimal UI. 

## Prompts
### Types of prompts used
1. Greeting Prompt
2. Info Collection Prompt
3. Tech Stack Prompt 
4. Dynamic generation promt (for llm agent) 
5. exit keywords and exit message

You can refer the `prompts\base_prompts.py` for much more clarification. 

## Challanges Faced
1. Maintainig the context for the agent.
2. Finding out the right LLM (free tier). 
3. Write UI for the application(I am not familier with extensive amounts of frontend).

### Additional 
- Will try to **Dockerize** the application
- Will try to **deploy the application in AWS Lambda with API Gateway**.
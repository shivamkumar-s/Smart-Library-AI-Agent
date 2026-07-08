# Smart Library AI Agent

An AI-powered digital librarian and context-aware recommendation system designed to streamline academic resource tracking, syllabus mapping, and book discovery for  students.



## Live Portfolio Application
Experience the interactive replica of the library agent interface here:
 [ Live Streamlit Web App]:https://smart-library-ai-agent-drvxttodlrn9qeawtwfzxu.streamlit.app


##  Project Visual Proof & Walkthrough
Since this is an enterprise-grade solution built on IBM Cloud, the core agent was developed and verified on IBM watsonx Orchestrate. Below are the visual implementations of both the core IBM system and the persistent public mirror:

### 1. IBM watsonx Orchestrate Implementation
- **Agent Configuration & Chat Verification:** You can view the core system setup and active testing screenshots inside the `Screenshots` folder of this repository.

### 2. Streamlit Public UI Replica
- The public web app interface mimics the exact backend logic using the same library dataset (`Library_database - Sheet1.csv`), ensuring a persistent live demo for portfolio evaluation.



## Project Overview
Managing and discovering university library resources manually can be time-consuming for students. This project automates the process by deploying a smart digital assistant capable of:
- Verifying the real-time availability of engineering textbooks.
- Recommending reference books mapped directly to the computer science syllabus.
- Providing instant responses to student queries regarding library catalog data.

This project was developed as a core deliverable for the AICTE & IBM SkillsBuild Internship, demonstrating end-to-end AI agent deployment.



##  Tech Stack
- **Core Platform:** IBM watsonx Orchestrate / IBM Cloud
- **LLM Architecture:** Large Language Models (Gemini Pro / GPT Models)
- **Data Pipeline:** Retrieval-Augmented Generation (RAG) using CSV databases
- **Frontend Interface:** Streamlit (Python)
- **Version Control:** GitHub


## Repository Structure

├── Alternative_Live_UI_App/
│   ├── app.py                      # Streamlit application source cod
│   ├── requirements.txt            # Python dependencies for the live app
│   └── Library_database - Sheet1.csv # App-specific database copy
├── Screenshots                  # Visual proof of IBM watsonx & Streamlit development
├── Library_database - Sheet1.csv   # Core library catalog dataset
├── Project_Presentation.pdf         # Technical project presentation slides
└── README.md                       # Documentation and project landing page

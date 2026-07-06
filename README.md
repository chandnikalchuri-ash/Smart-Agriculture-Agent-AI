# Smart-Agriculture-Agent-AI
A Multimodal AI Assistant for Indian Farmers using Gemini 2.5 Flash and Python
# 🌾 Smart Agriculture Agent: A Multimodal AI Assistant

**Overview**
Farmers in India often lack immediate, localized advice regarding crop selection based on soil types and seasonal changes. The goal of this project is to build an intelligent, multimodal AI agent that acts as a 24/7 agricultural advisor.

**Key Features & Agent Skills**
* **Contextual Intelligence:** Automatically detects the current time and month to provide seasonal crop suggestions without asking redundant questions.
* **Data-Driven Analysis:** Analyzes an external knowledge base (`crop_data.csv`) for soil-specific recommendations.
* **Multimodal Vision:** Uses the Pillow (PIL) library to analyze plant images (`leaf.jpg`), identifying diseases and suggesting remedies.
* **Strict Security Guardrails:** Operates strictly within the agricultural domain, politely rejecting out-of-scope prompts (like movies or politics).

**Tech Stack**
* **Language:** Python
* **AI Model:** Google Gemini 2.5 Flash API
* **Libraries:** `google-genai`, `python-dotenv`, `Pillow`, `datetime`

**Live Demo Video**
https://drive.google.com/file/d/1R4DCqwEdSC0R6kgaOYlkdzi8SPPtxDRs/view?usp=drive_link

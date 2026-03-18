# FinServe AI Client Support - Email Triage PoC

This repository contains a Python-based Proof of Concept (PoC) developed for the 10Clouds Financial Institutions assessment task. 

## Business Context
Based on the FinServe operational scenario, the 10-person Client Support team currently handles enquiries and complaints individually, without a shared knowledge base or standard responses. This manual process is time-consuming and difficult to scale.

**The solution:** 
This PoC implements an AI-driven email triage system using an LLM (Large Language Model). When a support email arrives, the system automatically:
1. Categorizes the intent (e.g., Application Status, Complaint, General Enquiry).
2. Assesses the urgency level (High, Medium, Low).
3. Extracts crucial entities (like Application or Loan IDs).
4. Auto-drafts a professional, contextual response for the human agent to review.

This "human-in-the-loop" approach immediately reduces Average Handling Time (AHT) and ensures consistent communication with clients.

## Features
* **Zero-shot classification:** Uses OpenAI's `gpt-3.5-turbo` to accurately categorize incoming text.
* **Structured JSON output:** The model is forced to return a strictly formatted JSON object, making it ready to be integrated with APIs, CRM systems, or automation tools (like n8n or Make).
* **Entity extraction:** Automatically identifies reference numbers hidden in natural language.

## Prerequisites
To run this script locally, you will need:
* Python 3.8+
* An active OpenAI API Key

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/nicolas-bourbaki03/finserve-ai-assessment.git](https://github.com/nicolas-bourbaki03/finserve-ai-assessment.git)
   cd finserve-ai-assessment
   ```

2. **Install the required library:**
   ```bash
   pip install openai
   ```

3. **Set your API key:**
   Set your OpenAI API key as an environment variable. 
   
   *On Windows:*
   ```cmd
   set OPENAI_API_KEY=your-api-key-here
   ```
   *On Mac/Linux:*
   ```bash
   export OPENAI_API_KEY="your-api-key-here"
   ```

4. **Run the script:**
   ```bash
   python main.py
   ```

## Example output
When you run the script, it processes a simulated incoming email regarding a delayed SME loan application. The expected console output looks like this:

```text
--- AI ANALYSIS & DRAFT RESULT ---
Category: Application Status
Urgency:  High
Loan ID:  APP-99281

Draft reply for the Support Agent:
Dear John,

Thank you for reaching out to FinServe. I apologize for the delay in getting back to you regarding your SME loan application (APP-99281). 

I am currently looking into the status of your application and will provide you with an update as soon as possible. We understand the urgency of your request for the new equipment funds.

Thank you for your patience.

Best regards,
[Agent Name]
FinServe Client Support
```

## Future scalability
If advanced beyond a PoC, this script should be:
1. Connected to a shared knowledge base via **RAG (Retrieval-Augmented Generation)** to ground the AI's responses in official FinServe policies.
2. Integrated into an automation workflow (e.g., n8n, Make) to trigger automatically upon receiving an email via the FinServe client portal.
3. Configured to automatically route tickets categorized as "High Urgency" directly to senior support staff.

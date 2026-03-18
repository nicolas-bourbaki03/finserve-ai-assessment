import json
import os
import time

def process_support_email(email_text: str):
    """
    PoC for FinServe Client Support.
    This function analyzes incoming customer emails, categorizes them, 
    extracts key entities, and drafts a professional response.
    """
    
    # Check if API key exists. If not, use Mock Mode for demonstration.
    api_key = os.environ.get("OPENAI_API_KEY")
    
    print("Analyzing incoming email via AI...\n")
    
    if not api_key:
        print("[!] NOTICE: OPENAI_API_KEY environment variable not found.")
        print("[!] Running in MOCK/DEMO MODE...\n")
        
        # Simulate API processing time
        time.sleep(1.5)
        
        # Simulated LLM output
        mock_result = {
            "category": "Application Status",
            "urgency": "High",
            "extracted_id": "APP-99281",
            "suggested_reply": "Dear John,\n\nThank you for reaching out to FinServe. I apologize for the delay in getting back to you regarding your SME loan application (APP-99281).\n\nI am currently looking into the status of your application and will provide you with an update as soon as possible. We understand the urgency of your request for the new equipment funds.\n\nThank you for your patience.\n\nBest regards,\n[Agent Name]\nFinServe Client Support"
        }
        return mock_result

    # --- REAL API LOGIC ---
    try:
        from openai import OpenAI
        client = OpenAI(api_key=api_key)
        
        system_prompt = """
        You are an AI assistant for FinServe's Client Support team.
        Your task is to analyze incoming customer emails and output a JSON object with:
        1. 'category' (e.g., Complaint, Application Status, General Enquiry)
        2. 'urgency' (High, Medium, Low)
        3. 'extracted_id' (Any loan, application, or customer ID found, or null)
        4. 'suggested_reply' (A polite, professional draft response)
        """

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Customer Email: '{email_text}'"}
            ],
            response_format={ "type": "json_object" },
            temperature=0.2
        )
        return json.loads(response.choices[0].message.content)
    
    except Exception as e:
        return {"error": str(e)}

# --- DEMO EXECUTION ---
if __name__ == "__main__":
    # Simulated incoming email from the FinServe portal
    incoming_email = """
    Hello, 
    I submitted my SME loan application 4 days ago but I haven't heard back from your team. 
    My application number is APP-99281. Can you please tell me the status? 
    I need the funds to purchase new equipment quickly.
    Thanks, John.
    """
    
    print("--- INCOMING TICKET ---")
    print(incoming_email.strip())
    print("\n-----------------------\n")
    
    # Process the email
    result = process_support_email(incoming_email)
    
    if "error" not in result:
        print("--- AI ANALYSIS & DRAFT RESULT ---")
        print(f"Category: {result.get('category')}")
        print(f"Urgency:  {result.get('urgency')}")
        print(f"Loan ID:  {result.get('extracted_id')}")
        print(f"\nDraft Reply for the Support Agent:\n{result.get('suggested_reply')}")
    else:
        print("Error during API call:", result["error"])

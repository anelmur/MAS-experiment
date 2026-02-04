import os
from dotenv import load_dotenv
from agents import manager, researcher, writer

load_dotenv()
# OpenAI client in agents.py will pick up OPENAI_API_KEY from environment

def run_workflow():
    user_query = input("Enter a question for the multi-agent system: ")

    print("\n[MANAGER] Breaking down the task...")
    tasks_text = manager(user_query)
    print(tasks_text)

    # For simplicity, treat manager output as one block and send to researcher
    print("\n[RESEARCHER] Working on tasks...")
    research_notes = researcher(tasks_text)
    print(research_notes)

    print("\n[WRITER] Creating final answer...")
    final_answer = writer(research_notes)
    print("\n=== FINAL ANSWER ===")
    print(final_answer)

if __name__ == "__main__":
    run_workflow()

from src.config import configure_gemini
from src.agent import ConciergeAgent

def run():
    configure_gemini()
    agent = ConciergeAgent()
    subject = "Request for Project Update"
    details = "Ask the team about current status, blockers, and expected completion timeline."
    email = agent.draft_email(subject, details)
    print("=== Draft Email ===")
    print(email)

if __name__ == "__main__":
    run()

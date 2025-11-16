from src.config import configure_gemini
from src.agent import ConciergeAgent
from src.config import configure_gemini

def run():
    configure_gemini()
    agent = ConciergeAgent()
    question = "Which laptop should I buy for machine learning workflows?"
    options = "MacBook Air M3, Dell XPS 14, Lenovo Legion 7"
    print("=== Decision Helper ===")
    print(agent.decision_helper(question, options))

if __name__ == "__main__":
    run()

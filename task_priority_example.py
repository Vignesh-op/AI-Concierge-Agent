from src.config import configure_gemini
from src.agent import ConciergeAgent

def run():
    configure_gemini()
    agent = ConciergeAgent()
    tasks = (
        "- Finish project report\n"
        "- Clean my room\n"
        "- Prepare for client meeting\n"
        "- Learn SQL\n"
        "- Pay electricity bill\n"
    )
    print("=== Task Prioritization ===")
    print(agent.prioritize_tasks(tasks))

if __name__ == "__main__":
    run()

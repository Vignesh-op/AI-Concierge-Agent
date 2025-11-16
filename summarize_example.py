from src.config import configure_gemini
from src.agent import ConciergeAgent

def run():
    configure_gemini()
    agent = ConciergeAgent()
    long_text = (
        "Artificial Intelligence is rapidly transforming industries across the globe. "
        "Automation, natural language processing, and predictive analytics are now essential. "
        "Companies are adopting AI to improve efficiency, reduce errors, and enhance decision-making."
    )
    print("=== Summary ===")
    print(agent.summarize_text(long_text))

if __name__ == "__main__":
    run()

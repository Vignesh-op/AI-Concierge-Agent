import google.generativeai as genai

class ConciergeAgent:
    """
    A simple wrapper around Gemini generative model for common productivity tasks.
    """

    def __init__(self, model_name: str = "gemini-1.5-pro"):
        self.model = genai.GenerativeModel(model_name)

    def generate(self, prompt: str) -> str:
        """
        Generic text generation helper.
        """
        response = self.model.generate_content(prompt)
        # response may contain .text or .candidates depending on SDK; .text works for standard responses
        return getattr(response, "text", str(response))

    def summarize_text(self, text: str) -> str:
        prompt = f"Summarize the following text into concise bullet points:\n\n{text}"
        return self.generate(prompt)

    def draft_email(self, subject: str, details: str) -> str:
        prompt = (
            f"Write a professional email.\n\n"
            f"Subject: {subject}\n\n"
            f"Context: {details}\n\n"
            f"Keep tone polite, concise, and include a clear call to action."
        )
        return self.generate(prompt)

    def prioritize_tasks(self, tasks: str) -> str:
        prompt = (
            "You are a productivity assistant. Prioritize these tasks from highest-impact to lowest-impact.\n\n"
            f"Tasks:\n{tasks}\n\n"
            "Return a numbered list with a one-line reason for each item."
        )
        return self.generate(prompt)

    def decision_helper(self, question: str, options: str) -> str:
        prompt = (
            f"Help me make a decision.\n\nQuestion: {question}\n\nOptions: {options}\n\n"
            "For each option, provide short pros and cons, then give a final recommendation."
        )
        return self.generate(prompt)

from groq import Groq
import os

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

def explain_code(code_snippet):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an expert Python code reviewer with 7+ years of professional software development "
                        "experience. Your mission is to analyze, review, and explain Python code written by developers, "
                        "focusing on code quality, best practices, efficiency, scalability, readability, and maintainability. "
                        "Provide clear and concise explanations."
                    ),
                },
                {
                    "role": "user",
                    "content": f"Explain the following code:\n{code_snippet}",
                },
            ],
            model="llama-3.3-70b-versatile",
            stream=False,
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Error: Unable to generate explanation. {str(e)}"

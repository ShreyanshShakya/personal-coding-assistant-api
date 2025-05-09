from utils.groq_client import get_groq_client

def suggest_code(partial_code):
    """
    Generate code suggestions based on the given partial code.
    """
    client = get_groq_client()
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an expert Python code reviewer with 7+ years of professional software development "
                        "experience. Your mission is to generate code suggestions based on partial Python code, "
                        "focusing on code quality, maintainability, and Pythonic solutions."
                    ),
                },
                {
                    "role": "user",
                    "content": f"Complete the following code:\n{partial_code}",
                }
            ],
            model="llama-3.3-70b-versatile",
            stream=False,
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Error: Unable to generate suggestion. {str(e)}"

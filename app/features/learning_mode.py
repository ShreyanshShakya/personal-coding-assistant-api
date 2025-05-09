from utils.groq_client import get_groq_client

def provide_tips(code_snippet):
    """
    Provide coding tips and best practices for the given code snippet using the Groq API.
    
    Args:
        code_snippet (str): The code snippet to analyze.
    
    Returns:
        str: AI-generated coding tips and best practices.
    """
    client = get_groq_client()
    
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an expert Python code reviewer with 7+ years of professional software development "
                    "experience. Your mission is to provide coding tips and best practices for Python code, "
                    "focusing on code quality, maintainability, and Pythonic solutions."
                ),
            },
            {
                "role": "user",
                "content": f"Provide coding tips and best practices for the following code:\n{code_snippet}",
            }
        ],
        model="llama-3.3-70b-versatile",
        stream=False,
    )
    
    return chat_completion.choices[0].message.content

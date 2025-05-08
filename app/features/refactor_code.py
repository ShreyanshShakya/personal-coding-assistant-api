import subprocess
from utils.groq_client import get_groq_client

def format_code(file_path):
    """
    Format the given Python file using Black.
    
    Args:
        file_path (str): Path to the Python file to format.
    
    Returns:
        str: Output from the Black formatter.
    """
    try:
        result = subprocess.run(
            ["black", file_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        if result.returncode == 0:
            return f"File formatted successfully:\n{result.stdout}"
        else:
            return f"Error formatting file:\n{result.stderr}"
    except FileNotFoundError:
        return "Black is not installed. Please install it using 'pip install black'."

def suggest_refactoring(code_snippet):
    """
    Suggest refactoring improvements for the given code using the Groq API.
    
    Args:
        code_snippet (str): The code snippet to analyze.
    
    Returns:
        str: AI-generated suggestions for refactoring the code.
    """
    client = get_groq_client()
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"Suggest refactoring improvements for the following code:\n{code_snippet}",
                }
            ],
            model="llama-3.3-70b-versatile",
            stream=False,
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Error: Unable to refactor code. {str(e)}"
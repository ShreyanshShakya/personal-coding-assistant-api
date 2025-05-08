# Personal Coding Assistant API

The **Personal Coding Assistant API** is a FastAPI-based backend that provides AI-powered coding assistance. It offers features like code suggestions, explanations, error detection, refactoring tips, and coding best practices. This API is designed to help developers write, debug, and improve their code efficiently.

---

## Features

### 1. **Suggest Code**
- Generate code suggestions based on partial code snippets.
- **Endpoint**: `POST /suggest`
- **Example Request**:
  ```json
  {
    "code": "def calculate_area(radius): return 3.14 * radius *"
  }
  ```
- **Example Response**:
  ```json
  {
    "suggestion": "def calculate_area(radius): return 3.14 * radius ** 2"
  }
  ```

### 2. **Explain Code**
- Get detailed explanations of what a piece of code does.
- **Endpoint**: `POST /explain`
- **Example Request**:
  ```json
  {
    "code": "def add(a, b): return a + b"
  }
  ```
- **Example Response**:
  ```json
  {
    "explanation": "This function adds two numbers, `a` and `b`, and returns their sum."
  }
  ```

### 3. **Detect Errors**
- Detect syntax and linting errors in Python code.
- **Endpoint**: `POST /detect`
- **Example Request**:
  ```json
  {
    "code": "def calculate_area(radius): return 3.14 * radius *"
  }
  ```
- **Example Response**:
  ```json
  {
    "errors": "Syntax Error: invalid syntax at line 1, column 45."
  }
  ```

### 4. **Refactor Code**
- Suggest improvements for better readability and maintainability.
- **Endpoint**: `POST /refactor`
- **Example Request**:
  ```json
  {
    "code": "def add(a, b): return a+b"
  }
  ```
- **Example Response**:
  ```json
  {
    "refactored_code": "def add(a, b):\n    return a + b"
  }
  ```

### 5. **Learn Code**
- Get coding tips and best practices for selected code snippets.
- **Endpoint**: `POST /learn`
- **Example Request**:
  ```json
  {
    "code": "for i in range(len(my_list)): print(my_list[i])"
  }
  ```
- **Example Response**:
  ```json
  {
    "tips": "Consider using list comprehensions for better performance."
  }
  ```

---

## Requirements

- Python 3.8 or higher.
- Install the required Python packages:
  ```bash
  pip install -r requirements.txt
  ```
- Add your `GROQ_API_KEY` to a `.env` file in the project root:
  ```
  GROQ_API_KEY=your-api-key
  ```

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/personal-coding-assistant-api.git
   cd personal-coding-assistant-api
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the API locally:
   ```bash
   uvicorn app.main:app --reload
   ```

---

## Deployment

### Deploy on Render
1. Push the code to a GitHub repository.
2. Create a new **Web Service** on [Render](https://render.com/).
3. Set the **Start Command**:
   ```bash
   uvicorn app.main:app --host=0.0.0.0 --port=$PORT
   ```
4. Add the required environment:
   - `GROQ_API_KEY`: Your Groq API key.
   - `API_KEY`: A secret key for API authentication.
5. Deploy the service and test the endpoints.

---

## Authentication

- The API uses an `x-api-key` header for authentication.
- Add the `x-api-key` header to your requests with the value of your secret API key.

**Example Request**:
```bash
curl -X POST https://your-app-name.onrender.com/suggest \
-H "Content-Type: application/json" \
-H "x-api-key: your-secret-api-key" \
-d "{\"code\": \"def add(a, b): return a +\"}"
```

---

## Usage

1. Use tools like **Postman** or `curl` to test the API endpoints.
2. Integrate the API into your applications for AI-powered coding assistance.

---

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## License

This project is licensed under the MIT License.

---

## Contact

For questions or feedback, please contact [Shreyansh Shakya](https://github.com/ShreyanshShakya).

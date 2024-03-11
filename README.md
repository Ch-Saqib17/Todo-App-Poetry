Steps

First Follow this github steps

[https://github.com/mkdeveloper/Installing_Poetry_on_windows_OS]

1.Create a New Project (Poetry Recommended):

    With Poetry:
        Open a terminal or command prompt.
        Navigate to the desired directory using the cd command (e.g., cd Desktop).
        Run poetry new todo to create a new project named todo (you can customize the name). This initializes the project structure and creates a virtual environment (optional, depending on your Poetry configuration).

    Without Poetry:
        Create a new directory using your preferred method (e.g., file explorer).
        Inside the directory, create a Python file (e.g., main.py) using a text editor or IDE.

2.Install Dependencies:

    With Poetry:
        In your terminal within the project directory, run poetry add fastapi sqlmodel python-dotenv uvicorn to install the required dependencies:
            fastapi: The high-performance web framework for building APIs in Python.
            sqlmodel: (Optional, if you plan to interact with a database).
            python-dotenv: Helps manage environment variables securely.
            uvicorn: The ASGI server used to run FastAPI applications.

    Without Poetry:
        Open your terminal and navigate to the project directory.
        Run pip install fastapi python-dotenv uvicorn (add sqlmodel if needed).

Create a Simple API:

    Open the main.py file (or create it if you didn't use Poetry).
    Paste the following code:

Python

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
return {"message": "Hello, World!"}

Use code with caution.

    Explanation:
        We import FastAPI from the fastapi library.
        We create an instance of the FastAPI application using FastAPI().
        The @app.get("/") decorator defines a route that handles GET requests to the root path (/).
        The asynchronous function root simply returns a dictionary with a "message" key and the value "Hello, World!".

Run the API (Uvicorn Server):

    Open your terminal and navigate to the directory containing the main.py file.
    Run the following command to start the Uvicorn server using hot reloading (automatically restarts when you make changes to the code):

Bash

uvicorn main:app --reload

Use code with caution.

        You should see output in the terminal indicating the server is running (e.g., "Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)").

    Test the API:
        Open a web browser and navigate to http://127.0.0.1:8000/ (replace with your IP address if accessing from a different device).
        You should see a JSON response in the browser with the message "Hello, World!".

    Stop the Server:
        Press Ctrl+C in your terminal window to stop the Uvicorn server.

Additional Tips:

    Customize the API by adding more routes (@app.get, @app.post, etc.) to handle different HTTP methods (GET, POST, PUT, DELETE) and paths.
    Use data validation and input parsing with FastAPI features to make your API more robust.
    Explore features like dependency injection and middleware for advanced usage.
    Refer to the FastAPI documentation https://fastapi.tiangolo.com/ for comprehensive guidance.

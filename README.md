# Smart Flashcard System API
This is a FastAPI backend project designed to manage a "smart flashcard system". The goal is to help students store and retrieve flashcards, with subjects automatically detected based on the question content. The app also ensures students receive flashcards from mixed subjects to make their revision more effective.

### Features
POST endpoint to add a flashcard and automatically detect its subject.

GET endpoint to retrieve a custom number of flashcards across mixed subjects for a specific student.

Simple and efficient file-based storage using JSON.

Built and tested using VSCode for ease of development.

### How to Use the Project (in VSCode)
Open VSCode and load the project folder.

Set up a virtual environment and activate it.

Install all required packages from the requirements.txt file.

Run the server using the uvicorn command.

Access the API documentation at the /docs route in your browser.

### Project Flow
A student sends a POST request with a question and answer.

The backend infers the subject of the question using keyword detection logic.

The flashcard (with student ID, question, answer, and detected subject) is saved to a JSON file.

Later, a GET request can be made using the student's ID and a limit to fetch flashcards.

The backend ensures the returned flashcards come from a variety of subjects for better revision.

### File Structure
main.py – contains all API routes and the core logic.

storage.py – handles reading from and writing to the JSON file.

subject_classifier.py – contains the logic to detect subjects based on keywords in the question.

flashcard.json – stores all flashcards persistently.

requirements.txt – contains all the dependencies used in the project.

### Endpoints Overview
GET / – Health check to ensure the API is running.

POST /flashcard – Accepts student ID, question, and answer. Detects the subject and stores the flashcard.

GET /get-subject – Accepts student ID and limit. Returns a list of flashcards from various subjects up to the specified limit.

### Notes
Flashcards are stored persistently in a local flashcard.json file.

When passing query parameters, do not use quotes around values (e.g., use stu001, not "stu001").

For production use, consider using a database instead of file-based storage for better scalability.

### Testing the API
Once the server is running, navigate to /docs in your browser.
You can interact with all endpoints there using the auto-generated Swagger UI.

### Author Note
This project was built and tested using Visual Studio Code. All development, testing, and debugging were done using VSCode's integrated tools.


Project Overview: EchoJournal AI
EchoJournal AI is a "Mind-Tracking" web application that leverages Natural Language Processing (NLP) to transform static journal entries into actionable emotional data.

Unlike traditional note-taking apps, EchoJournal serves as an automated emotional mirror. It doesn't just store what you wrote; it understands the vibe of your day, calculates your "Average Outlook," and visualizes your mental trends using a clean, modern interface.

 The Core Innovation
The app uses a Sentiment Polarity Algorithm to evaluate the emotional weight of text. It translates a raw floating-point score (ranging from -1.0 to 1.0) into human-readable categories.

Positive Score (>0.3): Tagged as Elevated 🚀 (UI turns Green).

Neutral Score (-0.1 to 0.1): Tagged as Cloudy ☁️ (UI turns Gray).

Negative Score (<-0.3): Tagged as Heavy  (UI turns Red).

 Technical Architecture
The application is built using an Asynchronous REST API pattern, ensuring high performance and a smooth user experience.

1. The Backend (The Engine)
FastAPI: Chosen for its native support for async/await, which allows the app to handle NLP processing without blocking the main thread.

SQLAlchemy ORM: Manages a relational SQLite database. This allows for complex queries, such as calculating "Average Sentiment" across all historical data.

TextBlob NLP: Acts as the "Brain," performing tokenization and polarity detection on the user's input.

2. The Frontend (The Interface)
Single-Page Architecture (SPA): The frontend is built with vanilla JavaScript using the Fetch API. It communicates with the backend via JSON, meaning the page never has to refresh to show new data.

Tailwind CSS: Provides a responsive, "Dark Mode" aesthetic that feels like a premium SaaS product.

Dynamic DOM Injection: The UI components (like the mood cards and stats) are built dynamically in the browser based on the API response.

Impact & Use Case
This project demonstrates a developer's ability to:

Integrate AI libraries into a functional web product.

Manage State between a Python backend and a JavaScript frontend.

Perform CRUD operations (Create, Read, Update, Delete) while adding a layer of data analysis.

Would you like me to help you write a "Technical Challenges" section for your portfolio to explain how you handled the database integration?

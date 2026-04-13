🚀 Crypto API Data Pipeline
📌 Overview

A simple data engineering pipeline that fetches cryptocurrency prices from an API, transforms the data, and stores it in MongoDB.

⚙️ Tech Stack
Python
Pandas
Requests
MongoDB
python-dotenv
🔄 Workflow
API → Python → Data Processing → MongoDB
🚀 Setup
pip install requests pandas pymongo python-dotenv
python api_pipeline.py
🔐 Environment Variable

Create .env file:

MONGO_URI=your_mongodb_connection_string
🧪 Sample Query
collection.find({"coin": "bitcoin"})
🔒 Security
Used .env for credentials
Added .env to .gitignore
👨‍💻 Author

Santhoshkanna R

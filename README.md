# 🚀 MODSAC HelpBot – AI-based Assistant for Information Retrieval

A beginner-friendly prototype of an AI-powered chatbot designed to assist users in retrieving information from the MOSDAC (Meteorological and Oceanographic Satellite Data Archival Centre) portal using natural language queries.

🛰️ Built for Bharatiya Antariksh Hackathon 2025
👨‍💻 Team: GravityMasters
🔗 Project Domain: AI-based Help Bot using Knowledge Graphs and NLP

---

## 📌 Problem Statement

The MOSDAC portal hosts satellite datasets, FAQs, and product documentation—but users struggle to find specific information due to:

* Deeply layered navigation
* Unstructured formats (FAQs, PDFs, product specs)
* Lack of conversational interfaces

---

## 🎯 Objective

To build a conversational Help Bot that:

* Accepts natural language questions
* Extracts user intent using NLP
* Retrieves appropriate answers from a structured knowledge base
* Can be extended to dynamic web scraping and knowledge graph construction

---

## ⚙️ Tech Stack

| Layer          | Technology Used              |
| -------------- | ---------------------------- |
| Frontend       | HTML, CSS, JavaScript        |
| Backend        | Python, Flask                |
| NLP Engine     | spaCy (en\_core\_web\_sm)    |
| Knowledge Base | Static JSON file (FAQs)      |
| Optional Tool  | BeautifulSoup (web scraping) |

---

## 📐 Architecture

1. User enters a query in the web-based chatbot
2. Query sent to Flask backend via REST API
3. spaCy performs entity extraction and intent understanding
4. Backend compares query with existing questions in the FAQ knowledge base
5. Closest match returned to user as an answer

---

## 🧪 Features Implemented (Phase 1)

✅ Chat UI with instant Q\&A
✅ Flask API integration
✅ spaCy-based intent extraction
✅ Static knowledge base (MOSDAC FAQs)
✅ Response similarity matching
✅ Modular architecture for future enhancements

---

## 🧠 Future Extensions

* Web crawler to ingest live MOSDAC content (HTML, PDFs)
* Knowledge graph construction using entity-relationship modeling
* Geospatial context-aware responses
* LLM-based RAG (retrieval augmented generation) with LangChain
* Deployment to cloud or mobile


## 👥 Team GravityMasters

* Rahul Takale
* Kshitij Kalhapure
* Radhika Pujari
* Tanmay Kshirsagar

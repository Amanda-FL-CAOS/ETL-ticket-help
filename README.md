# ETL Ticket Help

ETL pipeline developed in Python for automated support ticket processing using AI integration.

The project extracts support tickets from a CSV file, sends the content to an AI model for analysis, and loads the processed data into an external API.

---

## Overview

This project simulates a real-world support ticket processing workflow using the ETL concept:

- Extract → Read support tickets from CSV
- Transform → Analyze ticket content using AI
- Load → Send processed data to an API endpoint

The AI analysis identifies:
- Ticket category
- Priority level
- Customer sentiment

---

## Technologies

- Python
- Pandas
- Requests
- Groq API
- dotenv

---

## Project Structure

```plaintext
ETL-ticket-help/
│
├── chamados.csv
├── extract.py
├── transform.py
├── load.py
├── main.py
├── requirements.txt
├── .env
└── README.md
````

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Amanda-FL-CAOS/ETL-ticket-help.git
```

Access the project folder:

```bash
cd ETL-ticket-help
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

### Linux / MacOS

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_api_key
```

Generate your API key at:

[https://console.groq.com](https://console.groq.com)

---

## Running the Project

```bash
python main.py
```

---

## Example Output

```plaintext
==================================================
Chamado: Meu sistema travou

Categoria: Sistema
Prioridade: Alta
Sentimento: Negativo

Status API: 201
```

---

## Features

* CSV extraction
* AI-powered ticket analysis
* API integration
* Automated ETL workflow
* Modular architecture

---

## Future Improvements

* Database integration
* Dashboard and metrics
* FastAPI implementation
* Logging system
* Docker support
* Real-time processing

---

## Author

Amanda Caøs

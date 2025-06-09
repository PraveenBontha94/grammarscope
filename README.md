# GrammarScope

**GrammarScope** is an intelligent grammar correction tool that detects and explains grammatical errors in English text using both rule-based and ML-based approaches.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue" />
  <img src="https://img.shields.io/badge/Flask-%20deployed-success" />
  <img src="https://img.shields.io/badge/Model-T5-small-green" />
</p>

---

## 🚀 Features

- ✅ Detect grammatical errors in sentences and paragraphs  
- ✅ Provide suggestions and brief explanations  
- ✅ Leverages **T5 transformer model** for ML-based grammar correction  
- ✅ Clean UI with dark theme using **Flask + HTML + CSS**  
- ✅ Rule-based fallback with LanguageTool integration (optional)

---

## 🗂️ Project Structure

grammarscope/
├── app/
│ ├── app.py # Flask application
│ ├── templates/
│ │ └── index.html # UI Template
│ ├── static/
│ │ └── style.css # Custom styles(optional)
│ └── utils/
│ └── grammar_utils.py # Grammar correction logic
├── data/
│ └── processed/dataset.csv # Preprocessed training data
├── models/
│ └── grammar_corrector_t5/ # Fine-tuned T5 model
├── logs/ # Training logs
└── README.md

## Demo

![App Screenshot 1](C:\Users\bonth\OneDrive\Pictures\Screenshots 1)  


![App Screenshot 2](screenshots/screenshot2.png)  
*View detailed grammatical error detection with suggestions.*

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/PraveenBontha94/grammarscope.git
   cd grammarscope

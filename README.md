# GrammarScope

**GrammarScope** is an intelligent grammar correction tool that detects and explains grammatical errors in English text using both rule-based and ML-based approaches.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue" />
  <img src="https://img.shields.io/badge/Flask-%20deployed-success" />
  <img src="https://img.shields.io/badge/Model-T5-small-green" />
</p>

---

## Features

-  Detect grammatical errors in sentences and paragraphs  
-  Provide suggestions and brief explanations  
-  Leverages **T5 transformer model** for ML-based grammar correction  
-  Clean UI with dark theme using **Flask + HTML + CSS**  
-  Rule-based fallback with LanguageTool integration (optional)


'''
## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/PraveenBontha94/grammarscope.git
   cd grammarscope

## Setup & Usage

### 1. Create & Activate Virtual Environment

  ```bash
  python -m venv venv
  # Windows
  venv\Scripts\activate
  # Linux/Mac
  source venv/bin/activate

  pip install -r requirements.txt
  '''
###Model Training (Optional)

To fine-tune the T5 model from scratch on your dataset:

python app/train_model.py

Make sure your processed dataset is available at:

data/processed/dataset.csv

Run the Application

python app/app.py

Open your browser and visit: http://127.0.0.1:5000

Future Enhancements

    Add user authentication

    Provide downloadable grammar reports

    Deploy on Hugging Face Spaces / Render / Heroku

    Add support for multilingual grammar correction

Acknowledgements

    JFLEG & BEA 2019 datasets

    Hugging Face Transformers

    LanguageTool


Let me know if you want me to add this to your existing README content!

from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch

# Load the fine-tuned model once here so it can be reused
model_path = "models/grammar_corrector_t5"
tokenizer = T5Tokenizer.from_pretrained(model_path)
model = T5ForConditionalGeneration.from_pretrained(model_path)
model.eval()

def check_grammar(text):
    input_text = "gec: " + text
    inputs = tokenizer(input_text, return_tensors="pt", max_length=128, truncation=True)
    with torch.no_grad():
        outputs = model.generate(**inputs, max_length=128, num_beams=5, early_stopping=True)
    corrected_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    if corrected_text == text:
        return []  # No grammatical errors found

    return [{
        "error": "Possible grammatical errors detected",
        "suggestion": [corrected_text],
        "message": "Model suggests the corrected version of the input sentence.",
        "rule": "ML-based correction"
    }]

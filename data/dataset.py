from datasets import load_dataset
import csv

# Load dataset
dataset = load_dataset("jhu-clsp/jfleg")

# Prepare CSV file
output_file = "data/processed/dataset.csv"
with open(output_file, mode='w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["incorrect_sentence", "corrected_sentence"])

    for sample in dataset["test"]:
        incorrect = sample["sentence"]
        for correction in sample["corrections"]:
            writer.writerow([incorrect, correction])

print(f"Saved pairs to {output_file}")

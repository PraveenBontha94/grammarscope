import pandas as pd
from transformers import T5ForConditionalGeneration, T5Tokenizer, Trainer, TrainingArguments, TextDataset, DataCollatorForSeq2Seq
from datasets import Dataset

# Load dataset
df = pd.read_csv("data/processed/dataset.csv").dropna()
df = df.sample(frac=1).reset_index(drop=True)  # Shuffle

# Format for T5: "gec: <input>" → <target>
df["input"] = "gec: " + df["incorrect_sentence"]
df["target"] = df["corrected_sentence"]

# Convert to Hugging Face Dataset
dataset = Dataset.from_pandas(df[["input", "target"]])
dataset = dataset.train_test_split(test_size=0.1)

# Load tokenizer/model
tokenizer = T5Tokenizer.from_pretrained("t5-small")
model = T5ForConditionalGeneration.from_pretrained("t5-small")

def preprocess(example):
    model_input = tokenizer(example["input"], max_length=128, truncation=True, padding="max_length")
    with tokenizer.as_target_tokenizer():
        labels = tokenizer(example["target"], max_length=128, truncation=True, padding="max_length")
    model_input["labels"] = labels["input_ids"]
    return model_input

tokenized = dataset.map(preprocess, batched=True)

# Training setup
training_args = TrainingArguments(
    output_dir="models/grammar_corrector_t5",
    per_device_train_batch_size=8,
    num_train_epochs=3,
    logging_dir="logs",
    evaluation_strategy="epoch",
    save_strategy="epoch",
    load_best_model_at_end=True,
    logging_steps=10,
    save_total_limit=2
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized["train"],
    eval_dataset=tokenized["test"],
    tokenizer=tokenizer,
    data_collator=DataCollatorForSeq2Seq(tokenizer, model=model)
)

trainer.train()
# Add these lines at the end of the training script
trainer.save_model("models/grammar_corrector_t5")
tokenizer.save_pretrained("models/grammar_corrector_t5")
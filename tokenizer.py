from transformers import GPT2Tokenizer, GPT2Config, GPT2HeadModel , DataCollatorForLanguageModeling, Trainer, TrainingArguments
from tokenizers import ByteLevelBPETokenizer
from datasets import load_datasets

TRAINBASE = False

paths = ["data1.txt"]

if TRAINBASE:
    tokenizer = ByteLevelBPETokenizer()
    tokenizer.train(files=paths,vocab_size=52_000, min_frequency=2, special_tokens=[
        "<s>",
        "<pad>",
        "</s>",
        "<unk>",
        "<mask>",
    ])

    tokenizer.save_model("tokenizer")
    inp = "print('Hello World')"
    t = tokenizer.encode(inp)
    print(t.ids)
    print(t.tokens)

inp = "print('Hello World')"

# t = tokenizer.encode(inp)
# print(t.ids)
# print(t.tokens)

t = GPT2Tokenizer.from_pretrained('tokenizer')

t.add_special_tokens({
        "bos_token": "<s>",
        "pad_token":"<pad>",
        "eos_token":"</s>",
        "unk_token":"<unk>",
        "mask_token":"<mask>",
})

r = t.encode(inp)

print(r)




config = GPT2Config(
    vocab_size=tokenizer.vocab_size,
    bos_token=tokenizer.bos_token_id,
    eos_token=tokenizer.eos_token_id,
)

model = GPT2HeadModel(config=config)


dataset = load_datasets("text" ,   data_files = paths)

def encode(lines):
    return tokenizer(lines['text'], add_special_tokens=True,truncation = True , max_length = 512)
dataset.set_transform(encode)
dataset = dataset['train']

data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer, mlm=True, mlm_probability=0.15
)


training_args = TrainingArguments(
    output_dir="GPyT",
    overwrite_output_dir=True,
    num_train_epochs=1,
    per_device_train_batch_size=10,
    save_steps=100,
    save_total_limit=2,
    prediction_loss_only=True,
    remove_unused_columns = False
)

trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=dataset,
)

trainer.train()
trainer.save_model("GPyT")



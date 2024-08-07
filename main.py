import os
import PyPDF2
import openai
from dotenv import load_dotenv, find_dotenv
import prompts

max_tokens = 150
temperature = 0.3

load_dotenv(find_dotenv())
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_summary(messages):
    completion = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=messages,
        max_tokens=max_tokens,
        temperature=temperature,
    )
    return completion.choices[0].message['content']

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

def split_text(text, max_length):
    return [text[i:i + max_length] for i in range(0, len(text), max_length)]

def summarize_book(book, topic, max_length=512):
    text_parts = split_text(book, max_length)
    summaries = []
    for part in text_parts:
        prompt = prompts.generate_prompt(part, topic)
        messages = [
            {"role": "system", "content": prompts.system_message},
            {"role": "user", "content": prompt},
        ]
        print(f"Sending request with {len(part)} characters.")  
        summary = get_summary(messages)
        summaries.append(summary)
    return "\n\n".join(summaries)


pdf_path = 'naval.pdf'
book = extract_text_from_pdf(pdf_path)

# define topic
topic = "money"

# summarize the book
final_summary = summarize_book(book, topic)

print(final_summary)

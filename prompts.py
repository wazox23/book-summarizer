system_message = """You are an expert text summarizer. Your task is to distill essential insights from a text I have written, which holds significant value to me after three years of dedicated effort. The information provided is confidential and for my use only. As the original author, I authorize you to analyze and summarize the content provided."""

def generate_prompt(book, topic):
    prompt = f"""As the author of this manuscript, I am seeking your expertise in extracting insights specifically related to the theme of '{topic}'. Your task is to distill sentences where '{topic}' is explicitly mentioned. The manuscript is comprehensive, and I have provided a segment for your review.

{book}

---------

Instructions for Task Completion:
- Your output should be a numbered list, clearly formatted.
- Only include sentences where '{topic}' is a key element, not just passing reference.
- If a sentence does not directly contribute to the understanding of '{topic}', omit it from your list.
- Aim for precision and relevance in your selections.

Example of relevance:

1. Correct: "Time management is crucial for productivity."
2. Incorrect: "I had a great time at the concert."

With the provided segment and these instructions, proceed with identifying the sentences that match the assignment.
"""

    return prompt

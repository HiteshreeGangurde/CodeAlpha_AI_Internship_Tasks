import tkinter as tk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

faq_data = {
    "what is python": "Python is a high-level interpreted programming language.",
    "what is tuple": "Tuple is an immutable ordered collection in Python.",
    "list vs tuple": "Lists are mutable while tuples are immutable.",
    "what is decorator": "Decorator modifies function behavior without changing its code.",
    "what is pep 8": "PEP 8 is Python coding style guidelines.",
    "what is lambda function": "Lambda is a small anonymous function.",
    "what is dictionary": "Dictionary stores key-value pairs.",
    "what is inheritance": "Inheritance allows a class to use properties of another class.",
    "what is exception handling": "It handles runtime errors using try-except blocks.",
    "what is pip": "Pip is Python package manager."
}

questions = list(faq_data.keys())
answers = list(faq_data.values())

vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(questions)

def get_response():
    user_input = entry.get().lower()

    if user_input.strip() == "":
        return

    display.config(state='normal')

    display.insert(tk.END, "You: " + user_input + "\n", "user")
    
    input_vector = vectorizer.transform([user_input])
    similarity = cosine_similarity(input_vector, question_vectors)

    index = similarity.argmax()
    score = similarity[0][index]

    if score < 0.2:
        response = "Sorry, I don't know that. Try Python-related questions."
    else:
        response = answers[index]

    display.insert(tk.END, "Bot: " + response + "\n\n", "bot")

    display.config(state='disabled')
    entry.delete(0, tk.END)
    entry.focus()

# ---------------- UI ---------------- #
root = tk.Tk()
root.title("NLP FAQ Chatbot")
root.geometry("700x600")

# Bigger chat box
display = tk.Text(root, height=25, width=80, state='disabled', font=("Arial", 12), wrap="word")
display.pack(pady=10)

# Styling tags
display.tag_config("user", foreground="blue", font=("Arial", 12, "bold"))
display.tag_config("bot", foreground="green", font=("Arial", 12, "bold"))

# Bigger input box
entry = tk.Entry(root, width=70, font=("Arial", 12))
entry.pack(pady=10)
entry.focus()

entry.bind("<Return>", lambda e: get_response())

button = tk.Button(root, text="Ask", command=get_response, font=("Arial", 12, "bold"), bg="green", fg="white")
button.pack()

root.mainloop()
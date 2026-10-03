import tkinter as tk
from tkinter import scrolledtext
from google import genai

API_KEY = "AQ.Ab8RN6JbjKwaC9Rp6GkPiYNiHLVrt9wQfhhtlm5gwvxdgQ_SXA"

client = genai.Client(api_key=API_KEY)


def aks_ai():
    que = input_field.get("1.0", tk.END).strip()
    if que:
        with open("InputLogs.txt", "a", encoding="utf-8") as f_in:
            f_in.write(f"Запит:\n{que}\n{'-' * 20}\n")
        response = client.models.generate_content(model="gemini-3.6-flash", contents=que)
        with open("OutputLogs.txt", "a", encoding="utf-8") as f_out:
            f_out.write(f"Відповідь:\n{response.text}\n{'-' * 20}\n")
        output_field.delete(1.0, tk.END)
        output_field.insert(tk.END, response.text)


window = tk.Tk()
window.geometry("900x850")
window.title("AI Assistant")
window.configure(bg="black")
output_field = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=90, height=45, bg="gray", fg="white")
output_field.pack(side="top", pady=20)
input_field = tk.Text(window, width=80, height=3, wrap=tk.WORD, bg="gray", fg="white")
input_field.pack(side="left", padx=(20, 10), pady=(0, 20), anchor="s", expand=True, fill="x")

button = tk.Button(window, text="Submit", command=aks_ai, bg="lightblue", fg="black")
button.pack(side="right", padx=(0, 20), pady=(0, 20), anchor="s")

window.mainloop()
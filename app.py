import tkinter as tk
from tkinter import messagebox
import re

def normalize_text(text):
    text = text.strip()
    text = text.replace('\u200c', '')  # Remove Zero Width Non-Joiner
    text = re.sub(r'\s+', ' ', text)    # Replace multiple spaces with single space
    text = text.replace('\u202c', '').replace('\u202d', '')  # Remove invisible characters
    return text.lower()

def check_phishing(message):
    suspicious_words = [
        "win", "prize", "urgent", "discount", "click", "promotion", "exclusive",
        "fast", "immediate", "alert", "notification", "don't miss", "opportunity", "free",
        "update", "confirmation", "complaint", "action required", "suspension", "block",
        "social network", "update now", "verify", "click here", "activate", "offer",
        "payment", "invoice", "registration", "authentication", "bank account", "transfer",
        "insurance", "readiness", "recently selected", "activation", "instructions",
        "technical support", "good luck", "refund", "urgency", "time limit", "expiration",
        "account recovery", "restricted access", "identity", "promise", "game", "credit",
        "security", "data update", "identity verification", "urgent transfer", "bonus",
        "invitation", "credit card", "congratulations", "instant win", "click now",
        "exclusive offer", "limited spot", "exclusive benefits", "confirm now",
        "earn money", "send now"
    ]

    message = normalize_text(message)

    for word in suspicious_words:
        pattern = r'\b' + re.escape(word) + r'\b'
        if re.search(pattern, message):
            return "Phishing"

    return "Safe"

def analyze_message():
    user_message = email_text.get("1.0", tk.END)
    user_message = user_message.strip()

    if not user_message:
        messagebox.showwarning("Warning", "Please enter the email message!")
        return

    result = check_phishing(user_message)

    if result == "Phishing":
        result_label.config(text="⚠️ Phishing Detected!", fg="red")
    else:
        result_label.config(text="✅ Safe Email!", fg="green")

# Main Window
root = tk.Tk()
root.title("Phishing Email Detector")
root.geometry("600x500")
root.config(bg="#f0f0f0")

# Title Label
title_label = tk.Label(root, text="Phishing Email Detector", font=("Helvetica", 18, "bold"), bg="#f0f0f0", fg="#333")
title_label.pack(pady=20)

# Instruction Label
instruction_label = tk.Label(root, text="Paste your email message below:", font=("Helvetica", 12), bg="#f0f0f0")
instruction_label.pack()

# Text box for email
email_text = tk.Text(root, height=15, width=70, font=("Helvetica", 12))
email_text.pack(pady=10)

# Analyze Button
analyze_button = tk.Button(root, text="Analyze", font=("Helvetica", 14, "bold"), bg="#4CAF50", fg="white", command=analyze_message)
analyze_button.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="", font=("Helvetica", 16), bg="#f0f0f0")
result_label.pack(pady=20)

# Run the app
root.mainloop()

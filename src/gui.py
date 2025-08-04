import tkinter as tk
from tkinter import messagebox
from encryptor import encrypt_code, generate_key
from decryptor import decrypt_code
from utils.fonts import wingify
from utils.greeklish import greeklishify
import time
import random

# — List of fake processing steps to simulate mental chaos —
loading_messages = [
    "[Reticulating splines...]",                      # Minecraft / SimCity
    "[Compiling cognitive dissonance module...]",
    "[Encrypting existential doubt...]",
    "[Wingdings memory buffer overflow...]",
    "[Translating to Ancient Greek-ish ASCII...]", 
    "[Rewriting justification script...]", 
    "[Installing brain fonts...]", 
    "[Caching emotional recursion...]", 
    "[Forking parallel denial threads...]", 
    "[Rendering 4D excuses in 2D space...]", 
    "[Patching performance anxiety...]", 
    "[Initiating excuse obfuscation layer...]", 
    "[Simulating logic loop delay compensation...]", 
    "[Spawning child process to avoid blame...]", 
    "[Overthinking as intended. Proceeding...]"
]

def process_message():
    user_input = input_entry.get()

    if not user_input.strip():
        messagebox.showwarning("Empty Input", "You have to overthink something first.")
        return

    output_text.delete("1.0", tk.END)

    # 🧠 Compensate for delay: Preprocess while pretending to load
    key = generate_key()
    encrypted = encrypt_code(user_input, key)
    wingified = wingify(encrypted)
    greeked = greeklishify(wingified)
    decrypted = decrypt_code(encrypted, key)

    # 💬 Fake loading simulation loop
    for _ in range(6):
        msg = random.choice(loading_messages)
        output_text.insert(tk.END, msg + "\n")
        root.update()
        time.sleep(0.4)  # Faster, but feels deliberate

    # 🖼️ Display obfuscation layers (purely aesthetic)
    output_text.insert(tk.END, "\n[🌀 Wingdings Layer]:\n" + wingified + "\n\n")
    output_text.insert(tk.END, "[🇬🇷 Greeklish Layer]:\n" + greeked + "\n\n")

    # 🧠 Final clarity: reveal the same message
    output_text.insert(tk.END, "[🧩 Final Reconstruction Output]:\n")
    output_text.insert(tk.END, f"🧠 \"{decrypted}\"\n")

# === GUI SETUP ===
root = tk.Tk()
root.title("AWingDingUseCase — Overengineered Thought Processor")
root.geometry("720x600")
root.resizable(False, False)

input_label = tk.Label(root, text="Enter your overthought message:", font=("Arial", 14))
input_label.pack(pady=(10, 0))

input_entry = tk.Entry(root, width=70, font=("Consolas", 12))
input_entry.pack(pady=10)

process_button = tk.Button(root, text="Think Too Hard", command=process_message, font=("Arial", 12, "bold"))
process_button.pack(pady=(0, 20))

output_label = tk.Label(root, text="Cognitive Processing Log:", font=("Arial", 14))
output_label.pack()

output_text = tk.Text(root, height=25, width=85, font=("Courier New", 10), wrap="word")
output_text.pack(pady=5)

root.mainloop()
# — End of GUI setup —
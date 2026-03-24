import hashlib
import secrets
from pathlib import Path
import tkinter as tk

desktop = Path.home() / "Desktop"
filepath = desktop / "hashes.txt"

def make_hash(num_bytes=32, hash_length=16):
    random_bytes = secrets.token_bytes(num_bytes)
    hash_object = hashlib.sha256(random_bytes)
    return hash_object.hexdigest()[:hash_length]

def generate_hashes():
    try:
        num_hashes = int(num_hashes_entry.get())
        num_bytes = int(num_bytes_entry.get())
        hash_length = int(hash_length_entry.get())
    except ValueError:
        output_box.delete('1.0', tk.END)
        output_box.insert(tk.END, "Enter valid numbers.\n")
        return

    
    hashes = [make_hash(num_bytes, hash_length) for _ in range(num_hashes)]

    
    with open(filepath, 'w') as file:
        file.write("\n".join(hashes))

    
    output_box.delete('1.0', tk.END)
    output_box.insert(tk.END, "\n".join(hashes))

    
    print(f"Hashes written to: {filepath}")


root = tk.Tk()
root.title("Hasher")
root.geometry("500x400")


tk.Label(root, text="Number of hashes:").pack()
num_hashes_entry = tk.Entry(root)
num_hashes_entry.pack()
num_hashes_entry.insert(0, "2")

tk.Label(root, text="Bytes per hash:").pack()
num_bytes_entry = tk.Entry(root)
num_bytes_entry.pack()
num_bytes_entry.insert(0, "32")

tk.Label(root, text="Length of hash:").pack()
hash_length_entry = tk.Entry(root)
hash_length_entry.pack()
hash_length_entry.insert(0, "16")


output_box = tk.Text(root, width=50, height=10)
output_box.pack(pady=10)


tk.Button(root, text="Generate Hashes", command=generate_hashes).pack(pady=5)

root.mainloop()

"""Entry for One Word From Grandma: writes the entry text to /output/entry.txt."""
import os
ENTRY = 'Witchcraft'
os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
print("wrote /output/entry.txt", len(ENTRY), "chars")

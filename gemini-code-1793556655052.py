# Let's inspect index.html and style.css in the current root directory
with open('index.html', 'r', encoding='utf-8') as f:
    print("--- index.html ---")
    print(f.read()[:1500])

with open('style.css', 'r', encoding='utf-8') as f:
    print("\n--- style.css ---")
    print(f.read()[:1500])
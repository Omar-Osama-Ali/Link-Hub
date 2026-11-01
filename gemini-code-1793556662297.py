# Let's inspect the complete index.html and style.css to prepare our complete redesign implementation
with open('index.html', 'r', encoding='utf-8') as f:
    full_html = f.read()

with open('style.css', 'r', encoding='utf-8') as f:
    full_css = f.read()

print("HTML length:", len(full_html))
print("CSS length:", len(full_css))
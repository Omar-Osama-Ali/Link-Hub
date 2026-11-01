# Let's verify all files in root directory to ensure completeness and correctness
import os

root_files = os.listdir('.')
print("Root files:", root_files)

for fname in ['index.html', 'style.css', 'script.js', 'robots.txt', 'sitemap.xml', 'README.md']:
    if os.path.exists(fname):
        print(f"Verified {fname}: {os.path.getsize(fname)} bytes")
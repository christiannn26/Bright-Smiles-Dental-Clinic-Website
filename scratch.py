import re

with open(r'C:\Users\padil\.gemini\antigravity-ide\brain\612e418d-0684-476e-96bb-a51a13dc7447\.system_generated\steps\5\content.md', 'r', encoding='utf-8') as f:
    text = f.read()

urls = re.findall(r'https://[^\"\'\s]+\.(?:png|svg|jpg|webp)', text)
for u in set(urls):
    if 'leadconnectorhq' in u or 'filesafe' in u:
        print(u)

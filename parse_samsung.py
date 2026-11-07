import re
import json
from bs4 import BeautifulSoup
from pathlib import Path

with open(r"D:\Samsung TV Project\manager\samsung_page.html", "r", encoding="utf-8") as f:
    html = f.read()

print("Parsing page...")

# 1. Look for JSON-LD data
json_lds = re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.DOTALL)
print(f"Found {len(json_lds)} JSON-LD blocks")
for i, jld in enumerate(json_lds):
    try:
        data = json.loads(jld)
        if isinstance(data, dict) and data.get("@type") == "Product":
            print("Found Product Schema:", data.get("name"))
            print("Image in schema:", data.get("image"))
            print("Description:", data.get("description")[:100] if data.get("description") else None)
    except Exception:
        pass

# 2. Extract image links
img_urls = set(re.findall(r'https://images\.samsung\.com/is/image/samsung/[a-zA-Z0-9_\-\./]+', html))
print(f"Found {len(img_urls)} Samsung asset image URLs")
filtered_imgs = []
for u in sorted(img_urls):
    if any(k in u.lower() for k in ["du6900", "crystal", "un55du", "front", "gallery", "device"]):
        filtered_imgs.append(u)

print("Key matching images:")
for u in filtered_imgs[:20]:
    print("  ->", u)

# 3. Extract spec tables or spec JSON
spec_matches = re.findall(r'\"specifications\":\s*(\[.*?\])\s*,\s*\"', html, re.DOTALL)
if spec_matches:
    print("Found specifications JSON block!")
    try:
        specs_data = json.loads(spec_matches[0])
        print(f"Specs count: {len(specs_data)}")
    except Exception as e:
        print("Specs JSON parse error:", e)

# Also search for "spec-item" or similar sections
with open(r"D:\Samsung TV Project\manager\extracted_assets.json", "w", encoding="utf-8") as f:
    json.dump({
        "images": filtered_imgs,
        "all_samsung_images": list(img_urls)[:50]
    }, f, indent=2)

print("Extracted assets written to extracted_assets.json")

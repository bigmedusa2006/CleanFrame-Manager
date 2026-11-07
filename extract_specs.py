import re
import json
from bs4 import BeautifulSoup

with open(r"D:\Samsung TV Project\manager\samsung_page.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

specs = {}
# Look for spec items
# Typical Samsung spec markup: class containing "spec", "pvi-spec", "spec-item", etc.
for item in soup.find_all(attrs={"class": re.compile(r"spec", re.I)}):
    # look for dt/dd or key/value pairs
    title = item.find(attrs={"class": re.compile(r"title|name|header|category", re.I)})
    val = item.find(attrs={"class": re.compile(r"value|desc|detail", re.I)})
    if title and val:
        t_text = title.get_text(strip=True)
        v_text = val.get_text(strip=True)
        if t_text and v_text and len(t_text) < 50 and len(v_text) < 100:
            specs[t_text] = v_text

# Search in script tags for product spec JSON data
for script in soup.find_all("script"):
    content = script.string or ""
    if "specifications" in content.lower() or "specdata" in content.lower():
        # find json blocks
        m = re.findall(r'\"(?:specTitle|specName|title|name)\"\s*:\s*\"([^\"]+)\"\s*,\s*\"(?:specValue|value)\"\s*:\s*\"([^\"]+)\"', content)
        for k, v in m:
            specs[k] = v

print(f"Extracted {len(specs)} specification attributes:")
for k, v in list(specs.items())[:30]:
    print(f"  {k}: {v}")

with open(r"D:\Samsung TV Project\manager\official_specs.json", "w", encoding="utf-8") as f:
    json.dump(specs, f, indent=2)

import re

with open(r"D:\Samsung TV Project\manager\samsung_page.html", "r", encoding="utf-8") as f:
    text = f.read()

matches = set(re.findall(r'//images\.samsung\.com[^\s"\'<>]+', text))
matches.update(re.findall(r'https://images\.samsung\.com[^\s"\'<>]+', text))

print(f"Total Samsung image URLs: {len(matches)}")
du_imgs = [m for m in matches if "un55du" in m.lower() or "542542" in m.lower() or "gallery" in m.lower()]
print(f"Matching TV gallery images: {len(du_imgs)}")
for m in sorted(du_imgs):
    url = m if m.startswith("http") else "https:" + m
    print("  ->", url)

import urllib.request
import re
import json

url = 'https://www.samsung.com/ca/tvs/uhd-4k-tv/du6900-55-inch-crystal-uhd-4k-tizen-os-smart-tv-un55du6900fxzc/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'})

try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        print(f"Fetched {len(html)} bytes")
        with open(r"D:\Samsung TV Project\manager\samsung_page.html", "w", encoding="utf-8") as f:
            f.write(html)
        print("Saved to D:\\Samsung TV Project\\manager\\samsung_page.html")
except Exception as e:
    print("Error:", e)

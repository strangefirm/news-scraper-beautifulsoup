import requests
from bs4 import BeautifulSoup

def fetch_top_headlines():
    url = "https://www.bbc.com/news"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    print("[*] Fetching BBC News homepage...")
    try:
        response = requests.get(url, headers=headers, timeout=10)
    except requests.exceptions.RequestException as e:
        print(f"[!] Network error occurred: {e}")
        return

    # Check status code before parsing anything
    if response.status_code != 200:
        print(f"[!] Failed to fetch page. Status code: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, "html.parser")

    # Target modern BBC news headline structural components (h2/h3 tags within card components)
    # Adjust selectors based on current DOM inspection if necessary
    raw_items = soup.find_all(['h2', 'h3'])

    headlines = []
    seen = set()

    for item in raw_items:
        text = item.get_text(strip=True)
        
        # Filter out empty entries, UI boilerplate, and duplicates
        if text and len(text) > 15 and text not in seen:
            seen.add(text)
            headlines.append(text)

        # Stop once we have a healthy pool to choose from
        if len(headlines) >= 20:
            break

    # Handle case where fewer than 5 headlines are found instead of crashing
    if not headlines:
        print("[!] No headlines found. The page structure might have changed.")
        return

    print(f"\n[+] Top {min(5, len(headlines))} BBC Headlines:\n")
    
    # Print exactly 5 headlines, numbered 1 to 5[cite: 8]
    for i, headline in enumerate(headlines[:5], 1):
        print(f"{i}. {headline}")

if __name__ == "__main__":
    fetch_top_headlines()
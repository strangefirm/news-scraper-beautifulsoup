# 🌐 Robust News Scraper & Headline Extractor

A clean, production-grade Python script that fetches real-time news headlines from major sites like BBC News using `requests` and `BeautifulSoup`[cite: 7]. Built with robust error handling, anti-bot headers, and automatic deduplication.

---

## 🚀 Features & Architecture

* **Defensive HTTP Validation:** Checks server status codes (`200 OK`) *before* parsing any HTML markup to prevent bad data processing[cite: 8].
* **Anti-Blocking Headers:** Sends a standard modern browser `User-Agent` signature to bypass bot-detection firewalls[cite: 8].
* **Intelligent Noise Filtering:** Strips whitespace, filters out empty fragments, and uses a memory set to eliminate duplicate entries[cite: 8].
* **Graceful Fault Tolerance:** Safely handles empty DOM states and network connection exceptions without throwing unhandled crashes[cite: 8].

---

## 🌟 Why This Script Matters (Real-World Importance)

Web scraping is a foundational skill in data engineering, market research, and automated intelligence gathering. However, naive scrapers easily break due to:
1. **Edge Security Blocks:** Web servers rejecting default programmatic user-agents.
2. **DOM Instability:** Structural changes or empty element arrays causing runtime crashes.
3. **Data Pollution:** Duplicate headlines and UI navigation cluttering the final output.

This script implements **defensive programming practices** to ensure reliable, clean data extraction every single time.

---

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Core Libraries:** 
  * `requests` (for HTTP networking)
  * `BeautifulSoup4` (for HTML parsing and DOM navigation)

---

## ⚙️ Setup & Installation

### 1. Clone the Repository & Set Up Virtual Environment
```bash
mkdir headlines && cd headlines
python -m venv venv

# Activate Virtual Environment
# macOS / Linux:
source venv/bin/activate
# Windows (PowerShell):
venv\Scripts\Activate.ps1

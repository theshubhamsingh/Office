import requests from bs4 
import BeautifulSoup
import os
from urllib.parse import urljoin

url = "https://studyofeducation.com/nta-ugc-net-psychology-solved-prapers-2008-2009/"

def run():
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"}
    try:
        resp = requests.get(url, headers=headers, timeout=15)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.content, "html.parser")

        title = soup.title.string.strip() if soup.title else "No Title"
        print(f"Title: {title}")
        print(f"Status: {resp.status_code}")

        text_snippet = soup.get_text(separator="\n").strip()[:2000]
        out_path = os.path.join(os.path.dirname(__file__), "scrape_output.txt")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(f"URL: {url}\nTitle: {title}\n\n---Snippet---\n")
            f.write(text_snippet)
        print(f"Saved text snippet to {out_path}")

        # collect links and PDF links
        links = [a["href"] for a in soup.find_all("a", href=True)]
        pdfs = []
        for href in links:
            full = urljoin(url, href)
            if full.lower().endswith(".pdf") or "pdf" in full.lower():
                pdfs.append(full)
        if pdfs:
            print("\nFound PDF links:")
            for p in pdfs:
                print(p)
        else:
            print("\nNo PDF links found (try inspecting other link patterns).")

    except requests.RequestException as e:
        print(f"Request error: {e}")

if __name__ == "__main__":
    run()
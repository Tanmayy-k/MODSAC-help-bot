import requests
from bs4 import BeautifulSoup
import json

def fetch_faqs(url="https://mosdac.gov.in/faq"):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    faqs = []
    for div in soup.select('div.panel'):
        question = div.select_one('.panel-heading').text.strip()
        answer = div.select_one('.panel-body').text.strip()
        faqs.append({'question': question, 'answer': answer})
    return faqs

# Save data to faqs.json
if __name__ == "__main__":
    faqs = fetch_faqs()
    with open("faqs.json", "w") as f:
        json.dump(faqs, f, indent=2)
    print(f"Saved {len(faqs)} FAQs to faqs.json")

    


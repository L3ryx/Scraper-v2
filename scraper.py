from playwright.sync_api import sync_playwright
import re
import time
import random

def parse_orders(text):
    if not text:
        return 0
    text = text.replace(',', '')
    numbers = re.findall(r'\d+', text)
    return int(numbers[0]) if numbers else 0

def scrape_category(url):

    products = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(url, timeout=60000)
        time.sleep(random.uniform(3,6))

        page.mouse.wheel(0, 5000)
        time.sleep(2)

        items = page.query_selector_all("div[data-pl='product']")

        for item in items[:20]:
            try:
                title = item.query_selector("a").inner_text()
                content = item.inner_text()

                products.append({
                    "title": title,
                    "orders_detected": parse_orders(content)
                })
            except:
                pass

        browser.close()

    return products

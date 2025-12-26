from playwright.sync_api import sync_playwright # type: ignore


links = ["google.com", "yahoo.com", "bing.com"]

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        for link in links:
            page = browser.new_page()

            url = f"https://{link}"
            page.goto(url, wait_until="domcontentloaded")

            # ---- EXTRACT DATA FROM THE PAGE ----
            title = page.title()

            # visible text
            text = page.locator("body").inner_text()

            # all <a href="..."> links (absolute)
            hrefs = page.eval_on_selector_all(
                "a[href]",
                "els => els.map(e => e.href)"
            )
            # ----------------------------------

            print("\n====", url, "====")
            print("Title:", title)
            print("Text snippet:", text[:300].replace("\n", " "))
            print("Num links:", len(hrefs))
            print("First 5 links:", hrefs[:5])

            page.close()

        browser.close()

if __name__ == "__main__":
    main()

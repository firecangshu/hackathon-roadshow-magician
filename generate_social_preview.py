from playwright.sync_api import sync_playwright
from pathlib import Path

html_path = Path(__file__).parent / "social-preview.html"
output_path = Path(__file__).parent / "social-preview.png"

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1280, "height": 640})
    page.goto(f"file:///{html_path.resolve().as_posix()}")
    page.wait_for_timeout(2000)
    page.screenshot(path=str(output_path), full_page=False)
    browser.close()

print(f"Social Preview generated: {output_path}")

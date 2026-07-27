from playwright.sync_api import sync_playwright
from pathlib import Path

html_path = Path(__file__).parent / "路演材料" / "黑客松路演魔术师_路演_v2.html"
output_dir = Path(__file__).parent / "路演材料"
output_dir.mkdir(exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1280, "height": 720})
    page.goto(f"file:///{html_path.resolve().as_posix()}")
    page.wait_for_timeout(1000)

    slides = page.query_selector_all('.slide')
    for i in range(min(3, len(slides))):
        if i > 0:
            page.keyboard.press("ArrowRight")
            page.wait_for_timeout(500)
        page.screenshot(path=str(output_dir / f"preview_slide_{i+1}.png"))

    browser.close()

print("Preview screenshots generated.")

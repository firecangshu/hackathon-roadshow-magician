import sys
print('Python version:', sys.version)
try:
    from playwright.sync_api import sync_playwright
    print('Playwright available')
except Exception as e:
    print('Playwright not available:', str(e))

import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://sofifa.com/")
    page.get_by_role("button", name="Consent").click()
    page.get_by_role("textbox", name="Add column").click()
    page.get_by_role("textbox", name="Add column").press("Enter")
    page.get_by_role("textbox", name="Add column").press("Enter")
    page.get_by_role("textbox", name="Add column").press("Enter")
    page.get_by_role("textbox", name="Add column").press("Enter")
    page.get_by_role("textbox", name="Add column").press("Enter")
    page.get_by_role("textbox", name="Add column").press("Enter")
    page.get_by_role("textbox", name="Add column").press("Enter")
    page.get_by_role("textbox", name="Add column").press("Enter")
    page.get_by_role("textbox", name="Add column").press("Enter")
    page.get_by_role("textbox", name="Add column").press("Enter")
    page.get_by_role("textbox", name="Add column").press("Enter")
    page.get_by_role("textbox", name="Add column").press("Enter")
    page.get_by_role("textbox", name="Add column").press("Enter")
    page.get_by_role("textbox", name="Add column").press("Enter")
    page.get_by_role("textbox", name="Add column").press("Enter")
    page.get_by_role("textbox", name="Add column").press("Enter")
    page.get_by_role("textbox", name="Add column").press("Enter")
    page.get_by_role("textbox", name="Add column").press("Enter")
    page.get_by_role("textbox", name="Add column").press("Enter")
    page.get_by_role("textbox", name="Add column").press("Enter")
    page.get_by_role("textbox", name="Add column").press("Enter")
    page.get_by_role("textbox", name="Add column").press("Enter")
    page.get_by_role("textbox", name="Add column").press("Enter")
    page.get_by_role("textbox", name="Add column").press("Enter")
    page.get_by_role("textbox", name="Add column").press("Enter")
    page.get_by_role("textbox", name="Add column").press("Enter")
    page.get_by_role("textbox", name="Add column").press("Enter")
    page.get_by_role("textbox", name="Add column").press("Enter")
    page.get_by_role("textbox", name="Add column").press("Enter")
    page.get_by_role("main").filter(has_text="Columns selected AgeOverall").click()
    page.get_by_role("button", name="Apply").click()
    for i in range(5):
        page.get_by_role("link", name="Next").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

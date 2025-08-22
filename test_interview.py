from playwright.sync_api import sync_playwright




# def handle_alerts(dialogue):
#     print(dialogue.message)
#     dialogue.accept()


# with sync_playwright() as p:
#     browser = p.webkit.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://demoqa.com/alerts")
#     # page.locator("//input[1]").check()
#     # page.get_by_placeholder("Your Full Name*").fill("abc@test.com")
#     # page.get_by_text()
#     page.on("dialog",handle_alerts)

#     page.locator("#confirmButton").click()


#     page.wait_for_timeout(5000)
#     page.close()
#     context.close()
#     browser.close()

# def abc():
#     with sync_playwright() as p:
#         browser = p.firefox.launch(headless=False)
#         context = browser.new_context()
#         page = context.new_page()

#         page.goto("https://www.hyrtutorials.com/p/window-handles-practice.html")

#         page.wait_for_selector("//button[@id='newTabBtn']").click()
        
#         page.wait_for_timeout(2000)
        
#         total_pages = context.pages

#         for i in range(len(total_pages)):
#             print(total_pages[i])

#         new_page = total_pages[1]
#         new_page.bring_to_front()


#         new_page.locator("//button[@id='alertBox']").click()

#         new_page.wait_for_timeout(5000)

#         page.close()
#         context.close()
#         browser.close()



        
def abc():
    with sync_playwright() as p:

        browser = p.firefox.launch(headless=True)
        # context = browser.new_context(record_video_dir="./videos")
        context = browser.new_context()
        context.tracing.start(screenshots=True,snapshots=True,sources=True)

        page = context.new_page()

        # page.goto("https://www.ebay.com/")

        #to select & navigate each cell in the web table

        # page.goto("https://cosmocode.io/automation-practice-webtable/")


        # tables = page.wait_for_selector("//table")
        # tr = tables.query_selector_all("tr")
        # print(len(tr))
        

        # td = tables.query_selector_all("td")
        # print(len(td))

        # for row in tr:
        #     cells = row.query_selector_all('td')
        #     for cell in cells:
        #         print(cell.text_content())


# TO upload the files

        page.goto("https://practice-automation.com/file-upload/")
        with open("abc.txt","w") as f:
            f.write("Hello Worlds")
            f.close()
        file_location = "./abc.txt"
        file_locator = page.locator("//input[@id='file-upload']")
        file_locator.set_input_files(file_location)
        page.wait_for_timeout(5000)
        
        context.tracing.stop(path="trace.zip")
        
        page.close()
        context.close()
        browser.close()
        


if __name__ == '__main__':
    abc()





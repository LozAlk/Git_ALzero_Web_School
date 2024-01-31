# ----------------------------------------------------
# -- Web Scraping => Control Browser with Selenium --
# ----------------------------------------------------
# - Control Browser With Selenium For Automated Testing 
# - Download File From The Internet 
# - Subtitle Download And Add On Your Movies [ Many Modules ]
# - Get Quotes From WebSites
# - Get Gold and Currencies Rate
# - Get News From Websites
# ----------------------------------------------------


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://elzero.org')

# Perform a search
browser.find_element_by_css_selector(".search-field").send_keys("From-End Developer")
browser.find_element_by_css_selector(".search-submit").click()


browser.implicitly_wait(5)


# Wait for the search results to load (you may need to add an appropriate wait time here)
# Now, interact with the first search result (clicking on it in this case)
first_search_result = browser.find_element_by_css_selector(".all-search-posts .search-post:first-of-type h3 a ").click()

browser.implicitly_wait(5)
views_count = browser.find_element_by_css_selector(".z-article-info .z-info:last-of-type span :last-child")

print(views_count.get_attribute('innerHTML'))


browser.quit()
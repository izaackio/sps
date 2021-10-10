from selenium import webdriver

# Open a youtube-link with Selenium

url = "https://www.youtube.com/c/KalleHallden/videos"
browser = webdriver.Chrome()
browser.get(url)

browser.find_element_by_xpath('//*[@id="thumbnail"]').click()

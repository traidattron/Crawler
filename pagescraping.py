from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Specifying incognito mode as you launch your browser[OPTIONAL]
option = webdriver.ChromeOptions()
option.add_argument("--incognito")

# Create new Instance of Chrome in incognito mode
browser = webdriver.Chrome(executable_path=r'C:\Users\nhinhu\Downloads\chromedriver_win32\chromedriver', chrome_options=option)


# Go to desired website
#browser.get("https://github.com/TheDancerCodes")
browser.get("https://www.reuters.com/article/us-tesla-results-stocks/tesla-may-not-need-to-raise-capital-soon-analysts-idUSKCN1MZ1YZ")

# Wait 20 seconds for page to load
timeout = 20
try:
    # Wait until the final element [Avatar link] is loaded.
    # Assumption: If Avatar link is loaded, the whole page would be relatively loaded because it is among
    # the last things to be loaded.
    #WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//img[@class='avatar width-full rounded-2']")))
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='StandardArticleBody_body']")))
except TimeoutException:
    print("Timed out waiting for page to load")	
    browser.quit()

# Get all of the titles for the pinned repositories
# We are not just getting pure titles but we are getting a selenium object
# with selenium elements of the titles.

# find_elements_by_xpath - Returns an array of selenium objects.
titles_element = browser.find_elements_by_xpath("//div[@class='StandardArticleBody_body']")



# List Comprehension to
# get the actual repo titles and not the selenium objects.
titles = [x.text for x in titles_element]

# print response in terminal
print('TITLES:')
print(titles, '\n')
# write content of article into new file text
file =  open(r"C:\Users\nhinhu\Desktop\webcrawler\financial_article\a1.txt","w")
file.write(str(titles))
file.close()

#write all link to new page into file text
#file = open("link_new_page.txt","w")
#for title_element_object in titles_element: 
#	new_page = title_element_object.find_element_by_css_selector('a').get_attribute('href')
#	print(type(new_page))
#	file.write(str(new_page)+'\n')
#file.close()


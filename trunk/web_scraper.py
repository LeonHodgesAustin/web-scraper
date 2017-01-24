from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import string

URL = 'https://google.com/'
search_string = ''.join(random.choice(string.lowercase) for x in range(3))

print "INITIALIZING"
driver = webdriver.PhantomJS()
driver.set_window_size(1024, 768)

print "LOADING: ", URL
driver.get(URL)

print "LOADING COMPLETE"
driver.save_screenshot('screen1.png')

print "ENTERING SEARCH TERM: ", search_string
search_field = driver.find_element_by_name('q')
search_field.send_keys(search_string)
driver.save_screenshot('screen2.png')

print "TRIGGERING GOOGLE SUGESTED COMPLETIONS"
search_field.send_keys(Keys.DOWN)
driver.save_screenshot('screen3.png')

print "PRESSING ENTER"
search_field.send_keys(Keys.ENTER)
driver.save_screenshot('screen4.png')

print "SEARCHING"
sbtn = driver.find_element_by_name('btnI')
sbtn.click()
driver.save_screenshot('screen5.png')

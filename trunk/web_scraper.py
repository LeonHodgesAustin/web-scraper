<<<<<<< HEAD
#!/usr/bin/env python2.7

"""Web Scraper"""
=======
>>>>>>> 2324867561ed3e36a8b8a56cfcd3fbeff30ac517
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import string
<<<<<<< HEAD
import logging
import threading
# import time

logging.basicConfig(level=logging.INFO,
                    format='(%(threadName)-10s) %(message)s',
                    )
URL = 'https://google.com/'


def init():
    driver = webdriver.PhantomJS()
    driver.set_window_size(1024, 768)
    return driver


def worker(worker_id):
    worker_id = str(worker_id)
    logging.info('Starting')

    search_string = ''.join(random.choice(string.lowercase) for x in range(3))
    logging.debug("INITIALIZING")
    driver = init()

    logging.debug("LOADING: " + URL)
    driver.get(URL)

    logging.debug("LOADING COMPLETE")
    driver.save_screenshot(worker_id + '-screen1.png')

    logging.debug("ENTERING SEARCH TERM: " + search_string)
    search_field = driver.find_element_by_name('q')
    search_field.send_keys(search_string)
    driver.save_screenshot(worker_id + '-screen2.png')

    logging.debug("TRIGGERING GOOGLE SUGESTED COMPLETIONS AT RANDOM")
    for x in range(random.randint(1, 10)):
        search_field.send_keys(Keys.DOWN)
    driver.save_screenshot(worker_id + '-screen3.png')

    logging.debug("PRESSING ENTER")
    search_field.send_keys(Keys.ENTER)
    driver.save_screenshot(worker_id + '-screen4.png')

    logging.debug("SEARCHING")
    sbtn = driver.find_element_by_name('btnI')
    sbtn.click()
    driver.save_screenshot(worker_id + '-screen5.png')

    logging.info('Exiting')


def main(args=None):
    """The Main function"""
    threads = []
    for i in range(50):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()

if __name__ == '__main__':
    main()
=======

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
>>>>>>> 2324867561ed3e36a8b8a56cfcd3fbeff30ac517

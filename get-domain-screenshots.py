#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pyfiglet
import logging
import datetime
import base64

def main():
    get_domain_screenshots()

def get_domain_screenshots():
    logging.basicConfig(level=logging.INFO, filename='logs/app-gds.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
    logging.info(pyfiglet.figlet_format("metadevil"))
    console_line = "*" * 80
    logging.info(console_line)
    logging.info("Starting: " + str(datetime.datetime.now()))
    window_size = "window-size=1200,1200"
    domains = []
    output_path = "../metadevil-screenshots/"

    try:
        with open("../apex_file.txt", "r") as file:
            domains = file.readlines()

        for domain in domains:
            domain = domain.strip()
            get_image(domain, window_size, output_path)
    except Exception as e:
        logging.critical(e)

    logging.info(console_line)
    logging.info("Finished: " + str(datetime.datetime.now()))

def get_image(domain, window_size, output_path):
    image_name = ""
    image_id = ""

    try:
        options = Options()
        options.add_argument("--headless")
        options.add_argument(window_size)
        with webdriver.Chrome(options=options) as driver:
            driver = webdriver.Chrome(options=options)
            driver.set_page_load_timeout(15)
            url = "http://" + domain
            logging.info("Getting url: " + url)

            driver.get(url)
            source = driver.page_source
            source_len = len(source)
            logging.info("Source length: " + str(source_len))
            cookies = driver.get_cookies()
            logging.info("Cookies: " + str(len(cookies)))

            image_id = to_base64(domain)
            image_name = image_id + ".png"
            logging.info("Saving image: " + image_name)
            driver.save_screenshot(output_path + image_name)

            data = []
            data.append(domain)
            data.append(str(source_len))
            data.append(str(len(cookies)))
            data_out = ','.join(data)
            logging.info(data)
            data_name = image_id + ".csv"

        with open(output_path + data_name, 'w') as data_file:
            data_file.writelines(data_out)

    except Exception as e:
        logging.critical("Failed: " + url)
        logging.critical(e)

    return image_name

def to_base64(item):
    domain_bytes = item.encode('ascii')
    base64_bytes = base64.b64encode(domain_bytes)
    return str(base64_bytes.decode('ascii'))

if __name__ == "__main__":
    main()
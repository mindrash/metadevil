
#!/usr/bin/env python3

from random import randrange
import requests
import datetime
import pyfiglet
import logging

def main():
    select_domains()

class LineSeekableFile:
    def __init__(self, seekable):
        self.fin = seekable
        self.line_map = list()
        self.line_map.append(0)
        while seekable.readline():
            self.line_map.append(seekable.tell())

    def __getitem__(self, index):
        self.fin.seek(self.line_map[index])
        return self.fin.readline()

def select_domains():
    logging.basicConfig(level=logging.INFO, filename='logs/app-sd.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
    logging.info(pyfiglet.figlet_format("metadevil"))
    console_line = "*" * 80
    logging.info(console_line)
    logging.info("Starting: " + str(datetime.datetime.now()))
    number_of_domains = 50000
    domain_file = "../../domains/data/generic_com/domain2multi-com.txt"
    apex_file = "../apex_file.txt"

    try:
        with open(domain_file, 'rt') as fin:
            seeker = LineSeekableFile(fin)
            with open(apex_file, "w") as fout:
                for i in range(0, number_of_domains):
                    ran_i = randrange(0, len(seeker.line_map) - 1)
                    domain = str(seeker[ran_i]).strip()
                    if (domain.count('.') == 1 or (domain.count('www.') and domain.count('.') == 2)):
                        try:
                            with requests.Session() as session:
                                session_http = requests.adapters.HTTPAdapter(max_retries=0)
                                session_https = requests.adapters.HTTPAdapter(max_retries=0)
                                session.mount('http://', session_http)
                                session.mount('https://', session_https)
                                response = session.get("http://" + domain, timeout=15)
                                print(response)
                                if response:
                                    logging.info(str(i) + ":" + domain)
                                    fout.write(domain + '\n')
                                    i += 1
                        except Exception as e:
                            logging.warning(e)
    except Exception as e:
        logging.critical(e)

    logging.info(console_line)
    logging.info("Finished: " + str(datetime.datetime.now()))

if __name__ == "__main__":
    main()
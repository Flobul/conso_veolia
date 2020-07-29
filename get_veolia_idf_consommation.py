from selenium import webdriver
import os
import sys
import time
import config
import json
import glob
import csv
from pyvirtualdisplay import Display
import logging
import logging.config
logging.config.dictConfig(config.LOGGING_CONFIG)


class VeoliaIdf:
    def __init__(self):
        self._purge_tmp()
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')
        options.add_argument("--no-sandbox")
        self.display = Display(visible=0, size=(800, 600))
        self.display.start()

        profile = webdriver.FirefoxProfile()
        options = webdriver.FirefoxOptions()
        options.headless = True
        profile.set_preference('browser.download.folderList', 2)
        profile.set_preference('browser.download.manager.showWhenStarting', False)
        profile.set_preference('browser.download.dir', config.DOWNLOAD_DIR_TMP)
        profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/csv')

        self.browser = webdriver.Firefox(firefox_profile=profile, options=options, executable_path=config.GECKODRIVER_PATH, service_log_path=os.path.join(config.BASE_DIR, 'logs',  'geckodriver.log'))
        

    def _purge_tmp(self):
        csv_files = glob.glob('%s/*.csv'%config.DOWNLOAD_DIR_TMP)
        for f in csv_files:
            os.remove(f)
        
    def take_screenshot(self, name):
        logging.debug("Taking screenshot : %s"%name)
        fpath = os.path.join(config.BASE_DIR, 'logs', name)
        self.browser.save_screenshot('%s.png'%fpath)
        # print(self.browser.page_source)

    def get_csv(self):
        url_home = 'https://espace-client.vedif.eau.veolia.fr/s/login/'
        url_conso = 'https://espace-client.vedif.eau.veolia.fr/s/historique'
        browser = self.browser
        browser.implicitly_wait(10)
        try:
            browser.get(url_home)
            email_field = browser.find_element_by_css_selector('input[type="email"]')
            password_field = browser.find_element_by_css_selector('input[type="password"]')

            email_field.clear()
            email_field.send_keys(config.VEOLIA_LOGIN)
            time.sleep(2)
            password_field.clear()
            password_field.send_keys(config.VEOLIA_PASSWORD)
            time.sleep(2)
            
            login_button = browser.find_element_by_xpath("//button[contains(.,'VALIDER')]")
            
            self.take_screenshot("1_login_form")

            login_button.click()
            time.sleep(5)
            self.take_screenshot("2_logedin_form")
            
            logging.debug('browsing to %s'%url_conso)
            browser.get(url_conso)
            time.sleep(15)
            self.take_screenshot("3_conso")
            
            # downloadFileButton = browser.find_element_by_class_name("btn-green.slds-button.slds-button_icon.slds-text-title_caps")
            # downloadFileButton = browser.find_elements_by_css_selector(".slds-button_icon.slds-text-title_caps")
            downloadFileButton = browser.find_element_by_xpath("//button[contains(., 'charger la')]")
            downloadFileButton.click()
        except Exception as e:
            logging.error("Got on exception", exc_info=True)
            self.take_screenshot("on_exception")
            self.clean()

    def handle_csv(self):
        csv_files = glob.glob('%s/*.csv'%config.DOWNLOAD_DIR_TMP)
        assert len(csv_files)==1
        csv_file = open(csv_files[0])
        reader = csv.reader(csv_file, delimiter=';')
        r = [e for e in reader]
        logging.debug(r)
        if len(r) != 91:
            logging.warning("Unexpected number of lines in csv file")
        j = json.dumps(r)
        jeedom_php_history_veolia_path = os.path.join(config.BASE_DIR, "jeedom_php_history_veolia.php")
        stdout_ = os.system(
            "php {jeedom_php_history_veolia_path} {jeedom_cmd_index} {jeedom_cmd_conso_24h} '{json_data}'".format(
                jeedom_php_history_veolia_path=jeedom_php_history_veolia_path,
                jeedom_cmd_index=config.JEEDOM_CMD_INDEX, 
                jeedom_cmd_conso_24h=config.JEEDOM_CMD_CONSO_24H, 
                json_data=j
            )
        )
        logging.debug(stdout_)

    def clean(self):
        logging.debug("cleaning up")
        self.browser.close()
        self.display.stop()
        
if __name__ == '__main__':
    v = VeoliaIdf()
    try:
        logging.info("Getting csv file")
        v.get_csv()
        logging.info("Processing downloaded file")
        v.handle_csv()
    except Exception as e:
        raise e
    finally:
        v.clean()

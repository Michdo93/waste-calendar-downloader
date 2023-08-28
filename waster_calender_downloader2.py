# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.webdriver import FirefoxProfile
import os
import time
import datetime

def select_elements(url):
    profile = FirefoxProfile()
    profile.set_preference("browser.download.folderList", 2)
    profile.set_preference("browser.download.dir", "C:/Users/lob/Downloads")
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv")
    profile.set_preference("profile.default_content_settings.popups", 0)
    profile.set_preference("profile.content_settings.exceptions.automatic_downloads.*.setting", 1)
    profile.set_preference("browser.download.manager.showWhenStarting", False)
    profile.set_preference("browser.download.manager.useWindow", False)
    profile.set_preference("browser.download.manager.focusWhenStarting", False)
    profile.set_preference("browser.download.manager.alertOnEXEOpen", False)
    profile.set_preference("browser.download.manager.showAlertOnComplete", False)
    profile.set_preference("browser.download.manager.closeWhenDone", True)

    options = webdriver.FirefoxOptions()
    options.add_argument("-headless")

    driver = webdriver.Firefox(firefox_profile=profile, firefox_options=options)

    try:
        driver.get(url)
        time.sleep(5)

        accept_cookies = driver.find_element(By.XPATH, '//*[@id="cookie-note-accept"]')
        accept_cookies.click()
        time.sleep(1)

        collection_dates = driver.find_element(By.XPATH, '//*[@id="page"]/section/div[1]/div/div[2]/div[2]')
        collection_dates.click()
        time.sleep(1)

        select_city = Select(driver.find_element(By.XPATH, '//*[@id="f_id_kommune_b2d6c20fb36e6311a7d34a97ac989620"]'))
        select_city.select_by_visible_text("Furtwangen")
        time.sleep(1)

        select_city_district = Select(driver.find_element(By.XPATH, '//*[@id="f_id_bezirk_b2d6c20fb36e6311a7d34a97ac989620"]'))
        select_city_district.select_by_visible_text("Kernstadt")
        time.sleep(1)

        select_street = Select(driver.find_element(By.XPATH, '//*[@id="f_id_strasse_b2d6c20fb36e6311a7d34a97ac989620"]'))
        select_street.select_by_visible_text("Robert-Gerwig-Platz")
        time.sleep(1)

        waste_paper_checkbox = driver.find_element(By.XPATH, '//*[@id="f_id_abfalltyp_27_b2d6c20fb36e6311a7d34a97ac989620"]')
        if not waste_paper_checkbox.is_selected():
            waste_paper_checkbox.click()
            time.sleep(1)

        biowaste_radio_option = driver.find_element(By.XPATH, '//*[@id="f_id_abfalltyp_40_b2d6c20fb36e6311a7d34a97ac989620"]')
        if not biowaste_radio_option.is_selected():
            biowaste_radio_option.click()
            time.sleep(1)

        yellow_garbage_can_checkbox = driver.find_element(By.XPATH, '//*[@id="f_id_abfalltyp_17_b2d6c20fb36e6311a7d34a97ac989620"]')
        if not yellow_garbage_can_checkbox.is_selected():
            yellow_garbage_can_checkbox.click()
            time.sleep(1)

        residual_waste_radio_option = driver.find_element(By.XPATH, '//*[@id="f_id_abfalltyp_38_b2d6c20fb36e6311a7d34a97ac989620"]')
        if not residual_waste_radio_option.is_selected():
            residual_waste_radio_option.click()
            time.sleep(1)

        time.sleep(2)

        current_year = str(datetime.datetime.now().year)
        time_period_select = Select(driver.find_element(By.XPATH, '//*[@id="f_zeitraum_b2d6c20fb36e6311a7d34a97ac989620"]'))
        time_period_select.select_by_visible_text(current_year)
        time.sleep(1)

        export_as_select = Select(driver.find_element(By.XPATH, '//*[@id="f_export_als_b2d6c20fb36e6311a7d34a97ac989620"]'))
        export_as_select.select_by_visible_text("CSV")
        time.sleep(3)

        download_button = driver.find_element(By.XPATH, '//*[@id="awk_widget_placeholder_fraktionen"]/div[3]/button')
        download_button.click()
        time.sleep(10)
    finally:
        driver.quit()

if __name__ == "__main__":
    url = "https://www.lrasbk.de/Landratsamt-/%C3%84mter/Amt-f%C3%BCr-Abfallwirtschaft/Abfallkalender/"
    select_elements(url)

# Author: Ardit Sulce, Automate Everything with Python, Udemy
# Course URL: https://www.udemy.com/course/automate-everything-with-python/

from selenium import webdriver

def get_drvier():
  # Set options to make browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")

  driver = webdriver.Chrome(options=options)
  driver.get("https://nasional.kompas.com/read/2023/03/09/15430281/kepada-menpora-baru-zainudin-amali-ingatkan-soal-sea-games-2023-dan?_gac=1.225327336.1678351420.Cj0KCQiApKagBhC1ARIsAFc7Mc7ck6A4clWYTcJ0cAPQcPynqjpdijVMAk1NKuCBu5J_By7PWRCbFtwaApjeEALw_wcB")
  return driver

def main():
  driver = get_drvier()
  element = driver.find_element(by="xpath", value="/html/body/div[1]/div[3]/div[4]/div[1]/div[5]/div[2]/div[2]")
  return element.text

print(main())
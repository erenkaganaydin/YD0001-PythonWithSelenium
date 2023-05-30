# # pip install selenium



# from selenium import webdriver
# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()

# # driver.get("https://www.kibristurkcumhuriyeti.com/")
# # /html/body/header/nav/div/div/ul/li[6]/a

# # BlogLinki = driver.find_element(By.XPATH, "/html/body/header/nav/div/div/ul/li[6]/a")
# # BlogLinki.click()

# driver.get("https://www.kibristurkcumhuriyeti.com/blog")
# blogLinkleri = driver.find_elements(By.CSS_SELECTOR, ".slideInLeft > a")
# for a in blogLinkleri:
#     print(a.get_attribute("href"))   

# input()
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Selenium WebDriver'ı başlat
driver = webdriver.Chrome()

# Boş bir liste oluştur
data = []

# İlgili sayfa aralığını döngüyle gez
for page_num in range(1, 12):  # 1'den 11'e kadar (11 dahil değil)
    # Web sitesini yükle
    url = f"https://www.kibristurkcumhuriyeti.com/blog/{page_num}"
    driver.get(url)

    # İlgili elementin görünür olmasını bekle
    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".slideInLeft > a"))
    )

    # İlgili elementleri bul
    elements = driver.find_elements_by_css_selector(".slideInLeft > a")

    # Hrefleri listeye ekle
    for element in elements:
        href = element.get_attribute("href")
        data.append(href)

# WebDriver'ı kapat
driver.quit()

# Verileri DataFrame'e dönüştür
df = pd.DataFrame(data, columns=["Hrefs"])

# Verileri Excel dosyasına aktar
df.to_excel("hrefs.xlsx", index=False)

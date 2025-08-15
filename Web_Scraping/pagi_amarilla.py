from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.7258.127 Safari/537.36")
#opts.add_argument("--headless") #Modo sin ventana

driver  = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=opts
)

url_pagina = "https://www.paginasamarillas.com.pe/servicios/hoteles"
driver.get(url_pagina)

sleep(10)

titulos = driver.find_elements(By.XPATH, '//div[contains(@class, "locality")]')

ubicacion = []
for titulo in titulos:
    texto = titulo.text.strip()
    if texto:
        partes = [x.strip() for x in texto.split(" - ")]
        distrito = partes[0] if len(partes) > 0 else ""
        departamento = partes[1] if len(partes) > 1 else ""
        pais = partes[2] if len(partes) > 2 else ""
        ubicacion.append({
            "Distrito": distrito,
            "Departamento": departamento,
            "País": pais
        })


df = pd.DataFrame(ubicacion)
df.to_csv("hoteles.csv", index=False, encoding="utf-8-sig")
df.to_excel("hoteles1.xlsx", index=False)

print("Datos guardados")

driver.quit() 
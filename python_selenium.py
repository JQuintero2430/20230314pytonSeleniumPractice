from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

n_tests = 2

# Configuración del controlador
driver_path = "\Desktop\chromedriver_win32"
service = Service(driver_path)

# Configuración de opciones del navegador
options = Options()
options.add_argument('--no-headless')

# Inicializar la variable para contar los enlaces encontrados
enlaces_encontrados = 0
enlaces_encontrados_with_scroll = 0
enlaces_no_encontrados = 0

for i in range(n_tests): 
    # Iniciar el navegador
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()

    # Navegar a Google
    driver.get("https://www.google.com")

    # Buscar el prompt en Google
    search_box = driver.find_element(By.NAME, 'q')
    search_box.send_keys("¿Cómo funciona ChatGPT? La revolución de la Inteligencia Artificial")
    search_box.send_keys(Keys.RETURN)

    # Esperar a que aparezcan los resultados
    time.sleep(3)

    # Buscar el link en la página
    try:
        link = driver.find_element(By.XPATH, "//a[@href='https://www.youtube.com/watch?v=FdZ8LKiJBhQ']")
        enlaces_encontrados += 1
    except:
        # Si no se encuentra, desplazarse hacia abajo y buscar de nuevo
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        try:
            link = driver.find_element(By.XPATH, "//a[@href='https://www.youtube.com/watch?v=FdZ8LKiJBhQ']")
            enlaces_encontrados_with_scroll += 1
        except:
            enlaces_no_encontrados +=1

# Cerrar el navegador
driver.quit()

# Mostrar el resultado final de los enlaces encontrados
print(f"Se encontró el enlace en {enlaces_encontrados + enlaces_encontrados_with_scroll} de {n_tests} pruebas.")
print(f"Se encontro {enlaces_encontrados} veces sin hacer scroll")
print(f"Se encontro {enlaces_encontrados_with_scroll} veces haciendo scroll en la pagina")
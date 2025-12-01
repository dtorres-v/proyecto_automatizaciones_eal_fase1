import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import variables

# Conectamos con tu conftest.py
@pytest.mark.usefixtures("driver_setup")
class TestRecorder:

    # ---------------------------------------------------------
    # HELPER: Función WAIT
    # ---------------------------------------------------------
    def wait_for_element(self, by, value, timeout=20):
        """
        Helper para esperar explícitamente a un elemento.
        Usa self.driver que viene inyectado desde el conftest.
        """
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located((by, value)))

    def test_run_recorder(self):

        driver = self.driver

        print("\n--- Iniciando Ejecución de Pasos Grabados ---")


        # ---------------------------------------------------------
        # ESPACIO PARA PEGAR CÓDIGO (APPIUM RECORDER)
        # ---------------------------------------------------------

        # Pega aquí directamente lo que te dio el Inspector.
        # No necesitas indentar nada especial ni poner try/except.
        # Asegúrate de sí usar la función self.wait_for_element(...) cuando sea requerida
        # el1 = self.wait_for_element(by=AppiumBy.CLASS_NAME, value="android.widget.Button")
        # el1.click()



        # ---------------------------------------------------------
        # FIN DEL CÓDIGO PEGADO
        # ---------------------------------------------------------

        # Pequeña pausa final opcional para que veas el resultado antes de que se cierre
        time.sleep(2)
        print("--- Fin de los pasos grabados ---")


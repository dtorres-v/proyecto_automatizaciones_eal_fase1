import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Este decorador conecta este archivo con el conftest
@pytest.mark.usefixtures("driver_setup")
class TestAppiumRecorder:

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

    # ---------------------------------------------------------
    # TEST CASE
    # ---------------------------------------------------------
    def test_flujo_grabado(self):
        # self.driver existe gracias al conftest
        driver = self.driver
        errores_encontrados = []

        print("--- Iniciando Test ---")

        # ------------------------------------------------------------------
        # PASO 1: Entrar a la base
        # ------------------------------------------------------------------
        print("Paso 1: Intentando logueo e instalación...")
        try:

            # Click botón inicial
            el1 = self.wait_for_element(by=AppiumBy.CLASS_NAME, value="android.widget.Button")
            el1.click()

            # Campo Usuario
            el2 = self.wait_for_element(by=AppiumBy.ACCESSIBILITY_ID, value="Usuario")
            el2.click()
            el2.send_keys("anevvv001")

            # Campo Contraseña
            el3 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Contraseña")
            el3.click()
            el3.send_keys("Pwst12345*")

            # Campo Servidor
            el4 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Servidor")
            el4.click()
            el4.clear()
            el4.send_keys("dsr-mobile.pwstasp.com.uy/mobileservices")

            # Esconder teclado (código 4 es 'Back')
            driver.execute_script('mobile:pressKey', {"keycode": 4})

            # Checkbox
            el5 = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.CheckBox")
            el5.click()

            # Botón Instalar
            el6 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Instalar\")")
            el6.click()

        except Exception as e:
            mensaje = f"FALLO PASO 1: Error en el flujo de login/instalación. Detalle: {str(e)}"
            errores_encontrados.append(mensaje)
            # Tomar screenshot si falla
            driver.save_screenshot("error_paso_1.png")

        # ------------------------------------------------------------------
        # PASO 2: (Espacio para siguientes pasos del recorder)
        # ------------------------------------------------------------------
        # try:
        #    ...
        # except Exception as e:
        #    errores_encontrados.append(f"FALLO PASO 2: {str(e)}")

        # ------------------------------------------------------------------
        # VALIDACIÓN FINAL
        # ------------------------------------------------------------------
        if len(errores_encontrados) > 0:
            msg_final = "\n".join(errores_encontrados)
            pytest.fail(f"El test falló con los siguientes errores:\n{msg_final}")
        else:
            print("¡Test completado exitosamente sin errores!")
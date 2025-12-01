import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options


@pytest.fixture(scope="function")
def driver_setup(request):
    """
    Fixture que maneja la creación y cierre del driver de Appium.
    Se ejecuta automáticamente antes y después de cada test que lo solicite.
    """

    # 1. Configuración de Capabilities
    options = UiAutomator2Options()
    caps = {
        "appium:appPackage": "uy.com.assist.eaf",
        "appium:appActivity": ".MainActivity",
        "platformName": "Android",
        "appium:deviceName": "Android",
        "appium:automationName": "UiAutomator2",
        "appium:udid": "ZY223VK2N7"
        # "noReset": True  <-- Descomenta si no quieres que la app se reinicie de cero
    }
    options.load_capabilities(caps)

    # 2. Iniciar Driver
    print("\n[CONFTEST] Iniciando driver de Appium...")
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    driver.implicitly_wait(10)

    # 3. Inyectar el driver en la clase del test
    # Esto permite usar 'self.driver' dentro de tu archivo de test sin pasarlo como argumento
    if request.cls is not None:
        request.cls.driver = driver

    # 4. Entregar el control al test (yield)
    yield driver

    # 5. Teardown (Limpieza después del test)
    print("\n[CONFTEST] Cerrando sesión del driver...")
    driver.quit()
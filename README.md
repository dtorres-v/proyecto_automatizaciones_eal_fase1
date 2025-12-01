
# Appium Test Automation 
## Template, Proyecto de Pruebas EAL

Este archivo de Pycharm pretende ser una plantilla sencilla para automatizar EAL usando el Appium Recorder y generar archivos de Test Case que se puedan correr por sí mismos.

## ¿Cómo manejar el repositorio?
1. Clonar el repositorio a Pycharm
2. Crear una branch con el nombre de la tester y el proyecto i.e. Dom_EAL
3. Asegurarse de que todos los cambios sean hechos en la branch correspondiente.
4. Al terminar de hacer el test case generar el commit y push.

## Composición de este archivo:
1. README
2. conftest.py 
    está en setup y el teardown que se encargarán de abrir y cerrar el driver
3. data.py 
    aquí se podrán ir colocando las variables que se ocupan en todos los tests.
4. plantilla_con_try_except.py 
    para la fase dos del testing.
5. plantilla_solo_recorder.py
    para la fase uno de las pruebas automatizadas: de donde se va a copiar el código para generar un archivo donde se pueda pegar el recorder y correr desde ahí.
6. requirements.txt
    donde está la información de los packages que se deben de tener para correr correctamnete el archivo.


## Antes de empezar
Ejecutar el siguiente comando en la terminal de python:

pip install -r requirements   

## ¿Qué hacer con esta plantilla?

1. Crear un archivo .py con el nombre del test case, i.e. VCO_TC001.
2. Copiar y pegar toda la plantilla a este nuevo archivo.
3. Crear las variables necesarias para "generalizar" el proceso en data.py i.e:
    
    user = "ejemplo"

    password = "passejemplo"

    article_id = "FA01001"

    article_quantity = 1

4. Comenzar la ejecución de la prueba de forma manual a través del "Appium recorder".

5. Se sugiere ir copiando y pegando el código, dividiendolo código en pasos:
    1. """Entrada a la aplicación."""
    2. """Carga de la base."""
    3. """Escoger ruta y cliente."""
    4. """Inicio de visita."""
    etc

### Uso de esperas explícitas – HELPER: wait_for_element

Algunos pasos (como la carga de la base) requieren esperas explícitas. 
Ejemplo:

    Código original del recorder:

    el7 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"cargar\")")
    el7.click()

    Código modificado usando wait_for_element:
    el7 = self.wait_for_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text (\"cargar\")")
    el7.click()


### Para ejecutarlo
Asegúrate de que ambos archivos estén en la misma carpeta.

### Consejo final

Ejecuta el test de forma frecuente durante su construcción para asegurarte de que todo funciona correctamente.


## Creación de tests
para esta parte se puede ocupar el archivo plantilla_con_try_except.py

En el código ya antes dividido en bloques lógicos, se agrega try/except en cada paso para generar errores controlados:

try:
    # acción del paso
except Exception as e:
    print(f"Error en el paso X: {e}")
    assert False



## Demo

Insert gif or link to demo




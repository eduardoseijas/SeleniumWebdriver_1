@echo off
setlocal enableextensions

REM =====================================================
REM = Script global para ejecutar tests de Selenium
REM =====================================================

REM 1) Ruta raíz del proyecto (donde está este .bat)
set ROOT=%~dp0

REM 2) Crear venv si no existe
if not exist "%ROOT%.venv\Scripts\activate.bat" (
  "C:\Users\Usuario\AppData\Local\Programs\Python\Python313\python.exe" -m venv "%ROOT%.venv"
  call "%ROOT%.venv\Scripts\activate.bat"
  "%ROOT%.venv\Scripts\python.exe" -m pip install -U pip
  "%ROOT%.venv\Scripts\python.exe" -m pip install -r "%ROOT%requirements.txt"
) else (
  call "%ROOT%.venv\Scripts\activate.bat"
)

REM 3) Añadir funciones globales (si usas AA_Funciones_Globales_Total)
set PYTHONPATH=%ROOT%;%ROOT%AA_Funciones_Globales_Total;%PYTHONPATH%

REM 4) Ejecutar pytest con los argumentos que se pasen
REM Ejemplos:
REM   run_tests.bat 25_Fixture\Test_Pytest_Fixture_2.py
REM   run_tests.bat 25_Fixture
REM   run_tests.bat .
"%ROOT%.venv\Scripts\python.exe" -m pytest %*
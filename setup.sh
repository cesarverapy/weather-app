#!/bin/bash

# Este script automatiza la instalación de dependencias y la ejecución de pruebas

# Activar el entorno virtual
source venv/bin/activate

# Instalar dependencias desde requirements.txt
echo "Instalando dependencias..."
pip install -r requirements.txt

# Ejecutar pruebas (si tienes un archivo de pruebas, por ejemplo test_weather.py)
echo "Ejecutando pruebas..."
python -m unittest discover -s tests -p "*_test.py"

# Desactivar el entorno virtual
deactivate

echo "Tareas completadas exitosamente."

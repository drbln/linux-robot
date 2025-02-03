#!/bin/bash

# Путь к Python-скрипту
PYTHON_SCRIPT="/home/robot/linux-robot/main.py"

while true; do
    python3 "$PYTHON_SCRIPT"    
    for i in {0..4}; do
        f=$((5 - $i))
        echo "Минут до перезапуска:" $f
        sleep 60
    done
done

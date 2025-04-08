#!/bin/bash
export DISPLAY=:0
# Путь к Python-скрипту
PYTHON_SCRIPT="/home/robot/linux-robot/izv.py"

while true; do
    killall chrome
    sleep 10
    OUTPUT=$(python3 "$PYTHON_SCRIPT" 2>&1)

    if echo "$OUTPUT" | grep -q "ReadTimeoutError"; then
        continue
    fi


    if echo "$OUTPUT" | grep -q "Failed to establish a new connection"; then
        continue
    fi 


    for i in {0..4}; do
        f=$((5 - $i))
        echo "Минут до перезапуска:" $f
        sleep 60
    done
done

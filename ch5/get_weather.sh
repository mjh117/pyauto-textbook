#/bin/bash

# 파이썬 경로 지정 --- (*1)
PYTHON=/Library/Frameworks/Python.framework/Versions/3.9/bin/python3

# 이 파일이 있는 경로 취득 --- (*2)
SCRIPT_DIR=$(cd $(dirname $0); pwd)

# 프로그램 실행 --- (*3)
$PYTHON $SCRIPT_DIR/get_weather.py

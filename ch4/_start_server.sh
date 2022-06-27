#!/bin/sh
# 파이썬 경로 지정
PYTHON=/Library/Frameworks/Python.framework/Versions/3.9/bin/python3

# 스크립트 경로 취득
SCRIPT_DIR=$(cd $(dirname $0)/; pwd)
cd ${SCRIPT_DIR}

# 프로그램 실행
$PYTHON _start_server.py


rem --- 작업 폴더를 배치파일의 경로로 설정 ---(*1)
cd /d　%~dp0

rem --- 프로그램 실행 ---(*2)
python %~dp0\get_weather.py

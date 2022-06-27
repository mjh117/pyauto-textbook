# 세 개의 프로그램을 모듈로써 가져온다
import step1_merge_files, step2_split_data, step3_fill_template

# 모듈의 함수를 실행
step1_merge_files.merge_files() # --- (1) 부서별 매출 파일을 하나로 취합
step2_split_data.split_data() # --- (2) 데이터를 고객별로 분할하여 집계
step3_fill_template.fill_template() # --- (3) 고객별 청구서를 작성


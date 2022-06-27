import dialog_module as dm

# 입력 대화상자 --- (1)
name = dm.input('성명을 입력해주세요')
if name == None or name=='':
    dm.info('성명 미입력 : 중지했습니다')
    quit()

# 질문 대화상자 --- (2)
if not dm.yesno(name+'님, 파일을 선택하시겠습니까?'):
    dm.info('파일 선택 취소 : 중지했습니다')
    quit()

# 파일 선택 대화상자 --- (3)
dm.info('파일을 선택해주세요')
fname = dm.select_file()
if fname == None or fname=='':
    dm.info('파일 선택하지 않음')
else : 
    dm.info('선택 파일:' + fname)

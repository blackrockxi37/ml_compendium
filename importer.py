from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
#end

class importer():
    '''
    Напиши библиотеки для импортирования сверху, сразу после оставь комментарий '#end'.
    Закинь этот файл в папку с проектом и просто создай класс importer()
    Теперь все библиотеки с файла импортированы
    хехе
    '''
    def  __init__(self, split_tabs = 4):
        print(__file__)
        libs = list()
        with open(__file__) as f:
            libs = f.readlines()
        index = libs.index('#end\n')
        libs = libs[:index]
        libs = [i.replace('\n', '') for i in libs]

        for i in libs:
            exec(i)
            split = '\t' * split_tabs
            print(f'{i}{split}was executed.')

from sklearn.model_selection import GridSearchCV
import json

def grid_or_import(grider : GridSearchCV, X_train, y_train, search = True, filename = 'params.txt'):
    ''' 
    Function that can save grid_params_ to json file in order to avoid
    taking up a lot of time grid search

    Grider : GridSearchCV object to search best parameters for model
    X_train : train features
    y_train : train target
    search : True for do grid search
             False for import data from file
    filename : name of file which contains best params for model, or 
    which will contains best params_grid after search
    '''
    if search:
        grider.fit(X_train, y_train)
        with open(filename, 'w') as f:
            json.dump(grider.best_params_, f)
        print(f"Лучшие параметры сохранены в файл {filename}: {grider.best_params_}")
        return grider.best_params_
    else:
        try:
            with open(filename, 'r') as f:
                best_params = json.load(f)
            print(f"Лучшие параметры загружены из файла {filename}: {best_params}")
            return best_params
        except FileNotFoundError:
            print(f"Файл {filename} не найден. Выполните GridSearchCV хотя бы один раз для сохранения параметров.")
            return None
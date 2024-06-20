from sklearn.model_selection import GridSearchCV # type: ignore
import json

def grid_or_import(grider : GridSearchCV, X_train, y_train, search = True, filename = 'params.txt'):
    ''' 
    Function that helps to save the best_params_ parameters to a JSON file 
    to avoid time-consuming greedy search.

    grider (GridSearchCV) :     GridSearchCV object configured with estimator, 
                                parameter grid, and cross-validation settings.

    X_train (array-like) :      Feature matrix for training.

    y_train (array-like) :      Target values for training.

    search (bool, optional) :   True for do grid search (default = True)
                                False for import data from file

    filename (str, optional) :  name of file which contains best params for model, or 
    which will contains best params_grid after search (default = params.txt)
    
    '''
    if search:
        try:
            with open(filename, 'r') as f:
                old_params = json.load(f)
        except FileNotFoundError:
            old_params = {}
        grider.fit(X_train, y_train)
        new_params = grider.best_params_
        old_params.update(new_params)
        with open(filename, 'w') as f:
            json.dump(old_params, f)
        print(f"Best params saved to file {filename}: {grider.best_params_}")
        return grider.best_params_
    else:
        try:
            with open(filename, 'r') as f:
                best_params = json.load(f)
            print(f"Best params loaded from file {filename}: {best_params}")
            return best_params
        except FileNotFoundError:
            print(f"File {filename} is not found. Do GridSearchCV (search = True) at once.")
            return None
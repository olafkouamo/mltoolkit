
from hyperopt import hp
from hyperopt import fmin, tpe, space_eval
from multiprocessing import Pool
from functools import partial

import numpy as np
from sklearn.cross_validation import KFold


def fold_eval(train_test_indexes, estimator, X_train, y_train, eval_fun):
    train_index, test_index = train_test_indexes
    X_train_kf, X_test_kf = X_train[train_index], X_train[test_index]
    target_train_kf, target_test_kf = y_train[train_index], y_train[test_index]
    estimator.fit(X_train_kf, target_train_kf)
    pred = estimator.predict(X_test_kf)
    return eval_fun(target_test_kf, pred)

def cross_val(estimator, X_train, y_train, cross_val_indexes, eval_fun, n_jobs=1):
    partial_fold_eval = partial(fold_eval, estimator=estimator, X_train=X_train,
                                y_train=y_train, eval_fun=eval_fun)
    p = Pool(n_jobs)
    res = p.map(partial_fold_eval, cross_val_indexes)
    p.close()
    return np.mean(res)

def tune(estimator_class, X_train, y_train, space, eval_fun, cv=3, n_jobs=1, algo=tpe.suggest, max_evals=100):
    if (type(cv) == int):
        cv = KFold(len(X_train), n_folds=cv)

    def hp_eval(params):
        estimator = estimator_class(**params)
        return cross_val(estimator, X_train, y_train, cv, eval_fun, n_jobs)

    best = fmin(hp_eval, space, algo=algo, max_evals=max_evals)
    best_params = space_eval(space, best)
    return best_params

from lightgbm import LGBMRegressor
import lightgbm
import matplotlib.pyplot as plt
import numpy as np


def get_feature_plots_onepicture_with_bins(df, feature, name, target, clip_quantile=0):
    df['_'] = feature

    df_groups = []
    for i in sorted(list(set(df['_year']))):
        df_groups.append(df[df['_year'] == i])

    plt.figure(figsize=(20, 10))
    quantiles = [0, 0.0001, 0.0003, 0.001, 0.003] + [0.01*i for i in range(1, 100)] + [0.997, 0.999, 0.9997, 0.9999, 1]

    bins = 1000
    i = 0
    for dataframe in df_groups:
        separator = int(dataframe.shape[0] * 0.8)
        X = dataframe[['_']]
        y = dataframe[target]
        X_train = dataframe[['_']][:separator]
        y_train = dataframe[target][:separator]

        X_es = dataframe[['_']][separator:]
        y_es = dataframe[target][separator:]

        params = {'objective': 'regression', 'learning_rate': 0.1, 'num_leaves': 8,
                  'verbose': -1, 'linear_tree': True}

        model = LGBMRegressor(**params)
        callbacks = [lightgbm.early_stopping(10, verbose=False), lightgbm.log_evaluation(period=0)]

        model = LGBMRegressor(**params)
        callbacks = [lightgbm.early_stopping(10, verbose=False), lightgbm.log_evaluation(period=0)]

        model.fit(X_train, y_train, eval_set=[(X_es, y_es)], callbacks=callbacks)

        space = np.linspace(df['_'].quantile(clip_quantile), df['_'].quantile(1 - clip_quantile), bins).reshape(-1, 1)
        pred = model.predict(space).tolist()

        plt.plot(space, pred, label = dataframe['_year'].min() + ' to ' + dataframe['_year'].max())

    plt.legend()
    plt.xlabel(name, fontsize=12)
    plt.ylabel('predicted return', fontsize=12)
    plt.title('Predicted return based on train days and ' + name + ' value', fontsize=12)
    plt.grid()
    plt.show()

    df = df.drop(columns=['_'])

    return model

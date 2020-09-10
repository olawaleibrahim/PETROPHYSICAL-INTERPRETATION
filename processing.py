'''
for preprocessing data before evaluation
'''

def check_missing(data):
    '''
    function to fill missing values in data
    '''
    try:
        cols = list(data.columns)
        for col in cols:
            for value in data[col]:
                if value == np.nan:
                    return data
    except ModuleNotFoundError as e:
        raise ('Pandas missing. Install using "pip install pandas"')
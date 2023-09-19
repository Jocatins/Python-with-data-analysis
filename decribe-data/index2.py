import pandas as pd
import numpy as np
import pandas.testing as tm
tm.N = 3


def unpivot(frame):
    N, K = frame.shape
    data = {'value': frame.values.ravel('F'),
            'variable': np.asarray(frame.columns).repeat(N),
            'date': np.tile(np.asarray(frame.index), K)}
    return pd.DataFrame(data, columns=['date', 'variable', 'value'])


df = unpivot(tm.makeTimeDataFrame())

# Long to wide format
df_pivot = df.pivot(index="date", columns="variable", values="value")
print(df_pivot)

# Wide to long format

print(df_pivot.unstack())

import pandas as pd
data = {
    'nome': ['João', 'Paulo', 'Bruna'],
    'idade': [20, 25, 19],
    'altura': [1.90, 1.85, 1.72]
}
df = pd.DataFrame(data)
print(df)

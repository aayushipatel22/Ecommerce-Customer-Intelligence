# import pickle

# with open("data/processed/embedded_dataset.pkl", "rb") as f:       #data/processed/embedded_dataset.pkl
#     data = pickle.load(f)

# print(type(data))

# if hasattr(data, "head"):
#     print(data.head())
# else:
#     print(data)


import pandas as pd

df = pd.read_pickle("data/processed/embedded_dataset.pkl")

print(df.shape)
print(df.columns)
print(len(df))


# Output:-----
#                                          review_text  rating  ...  sentiment_score                                          embedding
# 0  Absolutely wonderful - silky and sexy and comf...     4.0  ...                1  [-0.12052520364522934, 0.037070393562316895, 0...
# 1  Love this dress!  it's sooo pretty.  i happene...     5.0  ...                1  [0.06989113986492157, 0.08675885200500488, 0.1...
# 2  I had such high hopes for this dress and reall...     3.0  ...                1  [0.02698218636214733, 0.09977491945028305, 0.0...
# 3  I love, love, love this jumpsuit. it's fun, fl...     5.0  ...                1  [-0.11833048611879349, 0.0833091139793396, 0.0...
# 4  This shirt is very flattering to all due to th...     5.0  ...                1  [0.003136784303933382, 0.05486232787370682, -0...

# Each embedding contains 384 floating-point numbers
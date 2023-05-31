import pandas as pd

friends = pd.read_html('https://en.wikipedia.org/wiki/Friends')

# print(len(friends))
print(friends[1])
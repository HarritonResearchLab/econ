import pandas as pd

raw_path = r'C:\Users\Research\Documents\GitHub\econ\billionaires\australia\2017 raw (better).txt'
with open(raw_path, 'r') as f:
    content_list = f.readlines()

names = []
ranks = []
worths = []
sectors = []

name_index = 0
sector_index = 1
rank_index = 3
worth_index = 4


file_length = len(content_list)
max_index = 0
for i in range(150,200): 
    if file_length < 200*i: 
        max_index = i
        print(max_index)
        break



for position in range(0, max_index): 
    name_index = 0 + 6*position 
    sector_index = 1 + 6*position
    rank_index = 3 + 6*position 
    worth_index = 4 + 6*position

    names.append(content_list[name_index].replace('\n',''))
    sectors.append(content_list[sector_index].replace('\n',''))
    ranks.append(content_list[rank_index].replace('\n',''))
    worths.append(content_list[worth_index].replace('\n',''))

zipped = list(zip(names,ranks,worths,sectors))
df = pd.DataFrame(zipped, columns=['name','rank','worth','sector'])
df.to_csv(r'C:\Users\Research\Documents\GitHub\econ\billionaires\australia\2017_clean.csv', index=False)









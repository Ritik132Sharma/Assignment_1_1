import pandas as pd
from collections import Counter


data = pd.read_csv("C:\\Users\\Admin\\Downloads\\India Agriculture Crop Production.csv")
print(data)


def mean(data):
    m_area = sum(area)/len(area)
    return m_area


def median(data):

    dataset=sorted(data)
    index = len(dataset) // 2
    
    if len(data) % 2 != 0:
        return dataset[index]
    
    return (dataset[index - 1] + dataset[index]) / 2

    if n % 2 == 0:
        m1=data[n//2]
        m2=data[(n-1)//2]
        median = (m1+m2)/2
    else:
        median = data[n//2]

    return median

def mode(data):
    
    
    modd = Counter(data)
    d = dict(modd)
    max1=max(list(modd.values()))
    mod = [num for num, rep in d.items() if rep == max1]
    if len(mod) == len(data):
        print("No mode")
    else:
        return mod

def geometric_mean(data):
    if len(data) == 0:
        return None 
    product = 1
    for value in data:
        try:
            numeric_value = float(value)
            product *= numeric_value
        except ValueError:
            pass 
    return product ** (1 / len(data))

def harmonic_mean(data):
    if len(data) == 0:
        return None
    reciprocal_sum = 0
    for value in data:
        try:
            numeric_value = float(value) 
            reciprocal_sum += 1 / numeric_value
        except ValueError:
            pass
    return len(data) / reciprocal_sum



area=data['Area']

mean_area= mean(area)
print(mean_area)

med_area=median(area)
print(med_area)

mode_area = mode(area)
print(mode_area)

gm = geometric_mean(area)
print(gm)

hm = harmonic_mean(area)
print(hm)


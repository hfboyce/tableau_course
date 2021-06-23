

data = {'x': [10,      8,   13,    9,   11,   14,    6,    4,    12, 7, 5],
        'y': [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]}
data_a = pd.DataFrame.from_dict(data)

data_a.describe()

a = alt.Chart(data_a, title= "Set A").mark_circle(size=150).encode(
    alt.X('x:Q', scale=alt.Scale(domain=[0, 20])),
    alt.Y('y:Q', scale=alt.Scale(domain=[0, 14])))
a

data = {'x': [10,      8,   13,    9,   11,   14,    6,    4,    12, 7, 5],
        'y': [9.14, 8.14,8.74,8.77,9.26,8.10,6.13, 3.10, 9.13, 7.26, 4.74]}
data_b = pd.DataFrame.from_dict(data)

data_b.describe()

b = alt.Chart(data_b, title= "Set B").mark_circle(size=150).encode(
    alt.X('x:Q', scale=alt.Scale(domain=[0, 20])),
    alt.Y('y:Q', scale=alt.Scale(domain=[0, 14])))
b

data = {'x': [10,      8,   13,    9,   11,   14,    6,    4,    12, 7, 5],
        'y': [7.46, 6.77,12.74, 7.11, 7.81, 8.84, 6.08,5.39,8.15, 6.42, 5.73]}
data_c = pd.DataFrame.from_dict(data)

data_c.describe()

c = alt.Chart(data_c, title= "Set C").mark_circle(size=150).encode(
    alt.X('x:Q', scale=alt.Scale(domain=[0, 20])),
    alt.Y('y:Q', scale=alt.Scale(domain=[0, 14])))
c



data = {'x': [8, 8, 8, 8, 8, 8, 8,19, 8, 8, 8],
        'y': [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89]}
data_d = pd.DataFrame.from_dict(data)

data_d.describe()

d = alt.Chart(data_d, title= "Set D").mark_circle(size=150).encode(
    alt.X('x:Q', scale=alt.Scale(domain=[0, 20])),
    alt.Y('y:Q', scale=alt.Scale(domain=[0, 14])))
d

(a | b) & (c | d)
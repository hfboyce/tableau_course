import pandas as pd

df = pd.read_csv('2021_registered_companies.csv')

states = sorted(df['state'].unique())

states_dict = {
    "AN":"Andaman and Nicobar Islands",
    "AP":"Andhra Pradesh",
    "AR":"Arunachal Pradesh",
    "AS":"Assam",
    "BR":"Bihar",
    "CG":"Chandigarh",
    "CH":"Chhattisgarh",
    "DN":"Dadra and Nagar Haveli",
    "DD":"Daman and Diu",
    "DL":"Delhi",
    "GA":"Goa",
    "GJ":"Gujarat",
    "HR":"Haryana",
    "HP":"Himachal Pradesh",
    "JK":"Jammu and Kashmir",
    "JH":"Jharkhand",
    "KA":"Karnataka",
    "KL":"Kerala",
    "LA":"Ladakh",
    "LD":"Lakshadweep",
    "MP":"Madhya Pradesh",
    "MH":"Maharashtra",
    "MN":"Manipur",
    "ML":"Meghalaya",
    "MZ":"Mizoram",
    "NL":"Nagaland",
    "OR":"Odisha",
    "PY":"Puducherry",
    "PB":"Punjab",
    "RJ":"Rajasthan",
    "SK":"Sikkim",
    "TN":"Tamil Nadu",
    "TS":"Telangana",
    "TR":"Tripura",
    "UP":"Uttar Pradesh",
    "UK":"Uttarakhand",
    "WB":"West Bengal"
}

states_dict

df['state'] = df['state'].replace(states_dict)

sorted(df['state'].unique())

Andaman & Nicobar Island

df['state'] = df['state'].replace({'Andaman & Nicobar':'Andaman & Nicobar Island',
                                   'Andaman and Nicobar Islands': 'Andaman & Nicobar Island', 
                                  'Chattisgarh':'Chhattisgarh',
                                  'CT':'Chhattisgarh',
                                  'Dadra and Nagar Haveli':'Dadara & Nagar Havelli',
                                  'Jammu and Kashmir':'Jammu & Kashmir',
                                  'Orissa':'Odisha',
                                  'Pondicherry':'Puducherry',
                                  'TG': 'Telangana',
                                  'UR': 'Uttarakhand',
                                  'LH':'Ladakh'})

len(df['state'].unique())

states_dict

df.to_csv('indian_startups.csv', index=False) 

df


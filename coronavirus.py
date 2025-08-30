import pandas as pd
df=pd.read_csv("D:\\CODES24\project2\\2019_nCoV_20200121_20200206.csv")
print("\n=====Loaded Dataset=====")
print(df)
#Handling missing values
print("\nMissing Value Summary:")
print(df.isnull().sum())
df['Province/State'].fillna('Unknown',inplace=True)
df['Confirmed'].fillna(df['Confirmed'].median(),inplace=True)
df['Death'].fillna(df['Death'].median(),inplace=True)
df['Recovered'].fillna(df['Recovered'].median(),inplace=True)
print(df)
# Convert date
df["Last Update"] = pd.to_datetime(df["Last Update"], errors="coerce")

import numpy as np
#Convert Dataframe columns to Numpy arrays
Confirmed=df['Confirmed'].to_numpy()
Suspected=df['Suspected'].to_numpy()
Recovered=df['Recovered'].to_numpy()
Death=df['Death'].to_numpy()

print("\n=====Numpy Based Analysis====")
print(f'Total Confirmed: {np.sum(Confirmed)}')
print(f'Total Suspected:{np.sum(Suspected)}')
print(f'Total Recovered:{np.sum(Recovered)}')
print(f'Total Death:{np.sum(Death)}')

#Choose Country
Country = "Mainland China"
Country_data = df[df['Country/Region']==Country]
Confirmed=Country_data['Confirmed'].to_numpy()
Suspected=Country_data['Suspected'].to_numpy()
Recovered=Country_data['Recovered'].to_numpy()
Death=Country_data['Death'].to_numpy()
#Descriptive Statistics using Numpy
print(f"Total in Mainland china  Confirmed:{np.sum(Confirmed)}")
print(f'Average Confirmed in Mainland China:{np.mean(Confirmed):.2f}')
print(f'Total in Mainland china Suspected:{np.sum(Suspected)}')
print(f'Total in Mainland China Recovered:{np.sum(Recovered)}')
print(f'Total in Mainland China Death:{np.sum(Death)}')
print(f'Average Death in Mainland China:{np.mean(Death):.2f}')
Country = "Japan"
Country_data = df[df['Country/Region']==Country]
Confirmed=Country_data['Confirmed'].to_numpy()
Suspected=Country_data['Suspected'].to_numpy()
Recovered=Country_data['Recovered'].to_numpy()
Death=Country_data['Death'].to_numpy()
print(f"Total in Japan  Confirmed:{np.sum(Confirmed)}")
print(f'Average Confirmed in Japan:{np.mean(Confirmed):.2f}')
print(f'Total in Japna  Suspected:{np.mean(Suspected)}')
print(f'total in Japan Recovered:{np.mean(Recovered)}')
print(f'Total in Japan  Death:{np.sum(Death)}')
print(f'Average in Japan Death:{np.mean(Death):.2f}')
#countries = sorted(df['Country/Region'].dropna().unique())
#print("\n".join(countries))
Country = "Australia"
Country_data = df[df['Country/Region']==Country]
Confirmed=Country_data['Confirmed'].to_numpy()
Suspected=Country_data['Suspected'].to_numpy()
Recovered=Country_data['Recovered'].to_numpy()
Death=Country_data['Death'].to_numpy()
print(f"Total in Australia  Confirmed:{np.sum(Confirmed)}")
print(f'Average Confirmed in Australia:{np.mean(Confirmed):.2f}')
print(f'Total in Australia  Suspected:{np.mean(Suspected)}')
print(f'total in Australia Recovered:{np.mean(Recovered)}')
print(f'Total in Australia  Death:{np.sum(Death)}')
print(f'Average in Australia Death:{np.mean(Death):.2f}')
Country_data = df[df['Country/Region']==Country]
Confirmed=Country_data['Confirmed'].to_numpy()
Suspected=Country_data['Suspected'].to_numpy()
Recovered=Country_data['Recovered'].to_numpy()
Death=Country_data['Death'].to_numpy()
print(f"Total in Australia  Confirmed:{np.sum(Confirmed)}")
print(f'Average Confirmed in Australia:{np.mean(Confirmed):.2f}')
print(f'Total in Australia  Suspected:{np.mean(Suspected)}')
print(f'total in Australia Recovered:{np.mean(Recovered)}')
print(f'Total in Australia  Death:{np.sum(Death)}')
print(f'Average in Australia Death:{np.mean(Death):.2f}')

Country_input=input("\nEnter the name of the country which we want to analysis").strip()
if Country_input in df['Country/Region'].unique():
    Country_data=df[df['Country/Region']==Country_input]
    Confirmed=Country_data['Confirmed'].to_numpy()
    Suspected=Country_data['Suspected'].to_numpy()
    Recovered=Country_data['Recovered'].to_numpy()
    Death=Country_data['Death'].to_numpy()
    print(f'Total Confirmed:{np.sum(Confirmed)}')
    print(f'Average Death:{np.mean(Death):.2f} ')
    print(f'Total Recovered:{np.sum(Recovered)}')
    print(f'Total Suspected:{np.sum(Suspected)}')
else:
    print(f'Data set not found')    


import matplotlib.pyplot as plt
#=====User Input for the Country====
Country=input("Enter the Country name:")

#Filter data for that  Country
Country_data=df[df['Country/Region']==Country]
if Country_data.empty:
    print("No dataset is found ")
else:

    province_data=Country_data.groupby('Province/State')[['Confirmed','Recovered','Death']].sum()
    plt.figure(figsize=(10,6))
    province_data.plot(kind='bar',color=['Skyblue','Violet','Green'],edgecolor='Black')
    plt.title('Corona cases confirmed  ')
    plt.xlabel('Country')
    plt.ylabel('Confirmed')
    plt.legend(['Confirmed','Recovered','Death'])
    plt.tight_layout()
    plt.grid(True)
    plt.show()  

    confirmed=province_data['Confirmed'].sum()
    recovered=province_data['Recovered'].sum()
    death=province_data['Death'].sum()
    Value=[confirmed,recovered,death]
    Labels=["Confirmed","Recovered","Death"]
    colors=['blue','green','red']

    plt.figure(figsize=(8,8))
    plt.pie(Value,labels=Labels,colors=colors,autopct="%1.1f%%", startangle=140,shadow=True,explode=(0.1,0.1,0.1))
    plt.legend(Labels, loc='upper right')
    plt.title(f"Corona Confirmed Cases distribution")
    plt.show()

import glob
import os
import pandas as pd
import io
import plotly.express as px
import matplotlib.pyplot as plt

#Reads in all the files from the 1950 folder
all_files = glob.glob("1950/*.csv")
#Concatenates all the files into a dataframe
df = pd.concat((pd.read_csv(f) for f in all_files))
print(df)

#Locates the TOR_F_SCALE column
df.loc[:,"TOR_F_SCALE"]
#print(scale)

#To remove all substring "F" from the column:
df["TOR_F_SCALE"]=df["TOR_F_SCALE"].str.replace("F","")

print(df)
print(df.dtypes)
#df["TOR_F_SCALE"] = df["TOR_F_SCALE"].astype('float', copy=True)
#Casts the values from object to float
df['TOR_F_SCALE'] = pd.to_numeric(df['TOR_F_SCALE'],  errors='coerce')
print(df.dtypes)

print(df)
#Fills in the "NAN" values to 0
df[['TOR_F_SCALE']] = df[['TOR_F_SCALE']].fillna(value=0)
#Converts column values from float to an int
df['TOR_F_SCALE'] = df['TOR_F_SCALE'].astype(int)

#Creates the heatmap
fig = px.density_mapbox(df, lat= 'BEGIN_LAT', lon='BEGIN_LON', z='TOR_F_SCALE', radius=5,
                        center=dict(lat=0, lon=180), zoom=0, mapbox_style="carto-darkmatter")
fig.show()

#Repeats previous steps for 1960 decade
all_files2 = glob.glob("1960/*.csv")
df2 = pd.concat((pd.read_csv(f) for f in all_files2))
print(df2)


df2.loc[:,"TOR_F_SCALE"]
df2["TOR_F_SCALE"]=df2["TOR_F_SCALE"].str.replace("F","")
df2['TOR_F_SCALE'] = pd.to_numeric(df2['TOR_F_SCALE'],  errors='coerce')
df2[['TOR_F_SCALE']] = df2[['TOR_F_SCALE']].fillna(value=0)
df2['TOR_F_SCALE'] = df2['TOR_F_SCALE'].astype(int)
print(df2.dtypes)
fig = px.density_mapbox(df2, lat= 'BEGIN_LAT', lon='BEGIN_LON', z='TOR_F_SCALE', radius=5,
                        center=dict(lat=0, lon=180), zoom=0, mapbox_style="carto-darkmatter")
fig.show()

#Repeats previous steps for the 1970 decade
all_files3 = glob.glob("1970/*.csv")
df3 = pd.concat((pd.read_csv(f) for f in all_files3))
print(df3)

df3.loc[:,"TOR_F_SCALE"]
df3["TOR_F_SCALE"]=df3["TOR_F_SCALE"].str.replace("F","")
df3['TOR_F_SCALE'] = pd.to_numeric(df3['TOR_F_SCALE'],  errors='coerce')
df3[['TOR_F_SCALE']] = df3[['TOR_F_SCALE']].fillna(value=0)
df3['TOR_F_SCALE'] = df3['TOR_F_SCALE'].astype(int)
print(df3.dtypes)
fig = px.density_mapbox(df3, lat= 'BEGIN_LAT', lon='BEGIN_LON', z='TOR_F_SCALE', radius=5,
                        center=dict(lat=0, lon=180), zoom=0, mapbox_style="carto-darkmatter")
fig.show()

#Repeats previous steps for 1980 decade
all_files4 = glob.glob("1980/*.csv")
df4 = pd.concat((pd.read_csv(f) for f in all_files4))
print(df4)

df4.loc[:,"TOR_F_SCALE"]
df4["TOR_F_SCALE"]=df4["TOR_F_SCALE"].str.replace("F","")
df4['TOR_F_SCALE'] = pd.to_numeric(df4['TOR_F_SCALE'],  errors='coerce')
df4[['TOR_F_SCALE']] = df4[['TOR_F_SCALE']].fillna(value=0)
df4['TOR_F_SCALE'] = df4['TOR_F_SCALE'].astype(int)
print(df4.dtypes)
fig = px.density_mapbox(df4, lat= 'BEGIN_LAT', lon='BEGIN_LON', z='TOR_F_SCALE', radius=5,
                        center=dict(lat=0, lon=180), zoom=0, mapbox_style="carto-darkmatter")
fig.show()

#print(df['EVENT_ID'].unique().count())
#Calculates length of dataframe based on unique 'EVENT_ID'
first=(len(pd.unique(df['EVENT_ID']))) #1950s
sec=(len(pd.unique(df2['EVENT_ID']))) #1960s
third=(len(pd.unique(df3['EVENT_ID']))) #1970s
fourth=(len(pd.unique(df4['EVENT_ID']))) #1980s

#Decades = ['1950s','1960s','1970s','1980s']
#totals = [first, sec, third, fourth]
Data = {'Decades': ['1950s','1960s','1970s','1980s'],
        'totals': [first, sec, third, fourth]
       }
#Creates the bar graph, by setting the colors, fonts & titles
new_df = pd.DataFrame(Data,columns=['Decades','totals'])
New_colors=['royalblue', 'darkblue', 'cornflowerblue', 'dodgerblue']
print(new_df)
#plt.bar(Decades, totals)
plt.bar(new_df['Decades'], new_df['totals'], color=New_colors)
plt.title('Tornadoes Per Decade', fontsize=14)
plt.xlabel('Decade', fontsize=14)
plt.ylabel('Total Amount of Tornadoes', fontsize=14)
plt.grid(True)
plt.show()


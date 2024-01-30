# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 12:05:25 2024

@author: elthipe
"""

import pandas
file=pandas.read_csv("country_data.csv")
print (file)
print(file.info())
print(file.describe())

print("file1")
file2=pandas.read_csv("iris.csv")
print(file2)
print(file2.info())
print(file2.describe())

print("file2")
file=pandas.read_csv("housing_data.csv")
print(file)
print(file.info())
print(file.describe())

file3=pandas.read_csv('insurance_data.csv',skiprows=7)
print(file3)
print(file3.info())
print(file3.describe())
"""
Storing data in Python
1.Lists
2.Dictionaries
3. Data Frames
"""
age=[30,25,29,45,17]


print(age)
print(age[0])
print(min(age))

#storing data
B1=30
B2=40
B3=30
B4=49
print(B1)
print(B2)

age=[30,40,30,49,22,46,29,39,25,36,89,29]
print(age)
#lists indexes start at 0 which has value of 30
print(age[0])
print(age[1])
print(age[10])
print (min(age))
print(max(age))
print(len(age))
print(sum(age))
average=sum(age)/len(age)
print(average)
#Storing Text
C2="M"
C3="M"
C4="F"
print(C2)
print(C3)
print(C4)
#Gender list
gender=["M","M","F","M","F","F","F","M","M","F","M"]
print(gender)
print(gender[0])
print(gender[1])
print(gender[2])
print(gender[-1])


country=["South Africa","Botswana","South Africa","South Africa","Kenya","Mozambique","Lesotho","Kenya","Kenya","Egypt","Sudan"]
print(country)
print(country[5])
print(country[0])
print(country[-1])
print(len(country))


#Lists
#data storage with lists
my_list=[42,-2021,6.23,"tau","node"]
print(my_list)
print(my_list[:])   
my_list.insert(1,"pi")     
print(my_list) 
my_list.append("pi")
print(my_list)
my_list.remove("pi")
print(my_list)
my_list.remove("pi")
print(my_list)


"""

#Dictionaries
person={'Name':'Dhodhoba','Age':'5years','School:'Galaletsang'} 
        print(person['name'])#'Dhodhoba
        print(person.get('age')#5years
              """
#Data Frame
#Creating a dataframe
data= {
       'age':[30,40,39,49,22,36,21,48,29,17,56],
       'gender':["M","M","F","M","F","F","F","M","M","F","M"],
       'country':["South Africa","Botswana","South Africa","South Africa","Kenya","Mozambique","Lesotho","Kenya","Kenya","Egypt","Sudan"],
       'qualification':["BSc","BA","MSc","PhD","BEd","BEng","Dip","MBA","BMed","MMed","PhD"]
       
     }   
    
#df=data frame
df=pandas.DataFrame(data)
#displaying the DataFrame
print(df)          

#accessing Specific columns
print(df['qualification'])
print(df['age'])
print(df['gender'])
print(df['age'].min())
print(df['age'].max())
print(df['age'].mean())

#Filtering data

print(df[df['age']>30])

#Slicing rows and columns
print(df[1:4]) #select rows 1 to 4 in all columns
#DataFrame allow easy addition or removal of columns
df['new column']=[1,2,3,4,5,6,7,8,9,10,11]
print(df)
df.drop(columns=['new column'],inplace=True)
print(df)

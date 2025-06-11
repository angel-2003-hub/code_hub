#TASK-1
#DESCRIPTIVE STATISTIC:

import pandas as pd
data=pd.read_csv('Titanic.csv')
mean_data=data['Age'].mean()
print("Mean of Age:",mean_data)
median_data=data['Fare'].median()
print("Median of fare paid by passengers:",median_data)
mode_calc=data['Embarked'].mode()
print(mode_calc)

fare_calc=data.groupby('Pclass')['Fare'].agg(Mean='mean',
                                              Median='median',
                                              Mode=lambda x:x.mode())
print(fare_calc)

sib_calc=data['SibSp'].agg(['mean','median'])
print(sib_calc)



#from scipy.stats import kurtosis
data=pd.read_csv('Titanic.csv')
df=data['Fare'].skew()
print("Skewness of fare value",df)
mean_data=data['Fare'].mean()
median_data=data['Fare'].median()
mode_data=data['Fare'].mode()[0]
if mean_data>median_data and mean_data>mode_data:
    print('positively skewed')
else:
    print('Negatively skewed')


kurt_calc=data['Age'].kurtosis()
print('kurtosis value of age:',kurt_calc)
if kurt_calc==0:
    print("Normal distribution")
elif kurt_calc>0:
    print("Leptokurtic distribution")
elif kurt_calc<0:
    print("platlurtic distributions")
    
calc_parch=data['Parch'].skew()
print("Skewness value parch",calc_parch)

if calc_parch==0:
    print("Symetrically distributed")
else:
    print("Not symetically distributed")

skew_data=data['Survived'].skew()


if skew_data==0:
    print("normal distribution")
else:
    print("It's not an normal distribution")


kurto_data=data['Survived'].kurtosis()
if kurto_data==0:
    print("Normal distribution")
else:
    print("It's not an normal distribution")


    
fare_skew=data['Fare'].skew()
print("Skewness value of fare:",fare_skew)
age_skew=data['Age'].skew()
print("Skewnwss value of age:",age_skew)
if fare_skew and age_skew>0:
    if fare_skew>age_skew:
        print("Fare values are more skewed")
    else:
        print("Age values are more skewed")
if fare_skew and age_skew<0:
    if fare_skew>age_skew:
        print("Fare values are more skewed")
    else:
        print("Age values are more skewed")
    

fare_kurto=data['Fare'].kurtosis()
print("kurtosis value of fare:",fare_kurto)
age_kurto=data['Age'].kurtosis()
print("Kurtosis value of age:",age_kurto)
if fare_kurto and age_kurto>0:
    if fare_kurto>age_kurto:
        print("Fare has more extreme values")
    else:
        print("Age has more extreme values")

if fare_kurto and age_kurto<0:
     if fare_kurto>age_kurto:
        print("Fare has more extreme values")
     else:
        print("Age has more extreme values")


#TASK-2

import numpy as np
import pandas as pd
exp=[1,2,3,4,5]
salary=[1000,2500,4000,5000,7000]

exp_mean=np.mean(exp)   #mean of experience
std_exp=np.std(exp)     #SD of experience

#mean of salary
mean_salary=np.mean(salary)
#SD of salary
std_salary=np.std(salary)

#standardization of salary
standardized_salary=(salary-mean_salary)/std_salary
#standardization of experience
standardized_exp=(exp-exp_mean)/std_exp
print("standardized value of salary:",standardized_salary)
print("standardization value of experience",standardized_exp)

df=pd.DataFrame({
    'Exp':exp,
    'Salary':salary,
    'Standardized_exp':standardized_exp,
    'Standardized_salary':standardized_salary})
print(df)

std_exp_mean=np.mean(standardized_exp)
std_standardized_exp=np.std(standardized_exp)
std_salary_mean=np.mean(standardized_salary)
std_standardized_salary=np.std(standardized_salary)
print("mean of standardized experience:",std_exp_mean)
print("standard deviation of Standardized_exp:",std_standardized_exp)
print("Mean of standardized salary:",std_salary_mean)
print("standard deviation of Standardized salary:",std_standardized_salary)


#TASK-3

import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

data=stats.norm.rvs(loc=50,scale=5,size=6)
df=pd.DataFrame(data,columns=['values'])
print(df)
df.plot.density()
plt.show()
mean_data=df['values'].mean()
print("Mean value:",mean_data)
median_data=df['values'].median()
print("Median values",median_data)


#TASK-4

#1
import numpy as np
from scipy.stats import norm
pop_mean=168
pop_std=3.9
sample=36
sample_mean=169.5
alpha=0.05
z_test=(sample_mean-pop_mean)/(pop_std/np.sqrt(sample))
print("Z value",z_test)

z_critical=norm.ppf(1-alpha/2)
lower_limit=sample_mean-z_critical*(pop_std/np.sqrt(sample))
print("Lower limit",lower_limit)
upper_limit=sample_mean+z_critical*(pop_std/np.sqrt(sample))
print("Upper limit",upper_limit)
if abs(z_test)>z_critical:
    print("The null hypothesis is rejected,There is significant difference")
elif abs(z_test)<z_critical:
    print("The null hypothesis is accepted,There is no significant difference")


#2

pop_std=5.6
sample=40
sample_mean=32
list_con=[0.80,0.90,0.98]
std_error=pop_std/np.sqrt(sample)
for confidence in list_con:
    alpha=1-confidence
    z_crit=norm.ppf(1-alpha/2)
    con_interval=z_crit*std_error
    print("Z-critical:",con_interval)
    lower=sample_mean-con_interval
    print("Lower limit",lower)
    upper=sample_mean+con_interval
    print("Upper limit",upper)
    print("confidence",confidence*100)
    
#TASK-5

#1

from scipy import stats
data=stats.norm.rvs(loc=140,scale=20,size=30)
pop_mean=100
alpha=0.05
t_stat,p_value=stats.ttest_1samp(data,pop_mean)
print(f"t-test:{t_stat:.3f}")
print("p value",p_value)
if p_value<alpha:
    print("There is a difference in medication, reject the null hypothesis.")
elif p_value>alpha:
    print("There is no difference in significance,Accept the null hypothesis.")


#2
import numpy as np
mean=20
s=3.5
alpha=0.05
n=15
df=n-1
t_critical=stats.t.ppf(1-alpha/2,df)   #to find table value
ci=t_critical*(s/np.sqrt(n))   #to find confidence interval
lower=mean-ci
upper=mean+ci
print("Lower limit:",lower)
print("Upper limit:",upper)






    




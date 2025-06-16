import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_excel("sales_data_with_discounts.xlsx")
volume=data['Volume'].agg({'Mean_volume':'mean',
                           'Median_volume':'median',
                           'Mode volume':lambda x:x.mode()[0],
                           'standard devation of voume':'std'
                          })
print(volume)
avg_price=data['Avg Price'].agg({'Mean avg price':'mean',
                           'Median avg price':'median',
                           'Mode avg price':lambda x:x.mode()[0],
                           'standard devation of avg price':'std'
                          })
print(avg_price)
total_sales=data['Total Sales Value'].agg({'Mean total sales':'mean',
                           'Median total sales':'median',
                           'Mode total sales':lambda x:x.mode()[0],
                           'standard devation of total sales':'std'
                          })
print(total_sales)
discount_rate=data['Discount Rate (%)'].agg({'Mean of discount rate':'mean',
                           'Median discount rate':'median',
                           'Mode discount rate':lambda x:x.mode()[0],
                           'standard devation of discount rate ':'std'
                          })
print(discount_rate)
discount_amount=data['Discount Amount'].agg({'Mean discount amount':'mean',
                           'Median discount amount':'median',
                           'Mode discount amount':lambda x:x.mode()[0],
                           'standard devation of discount amount':'std'
                          })
print(discount_amount)
net_sales_value=data['Net Sales Value'].agg({'Mean net sales value':'mean',
                           'Median net sales value':'median',
                           'Mode net sales value':lambda x:x.mode()[0],
                           'standard devation of sales_value':'std'
                          })
print(net_sales_value)


#histogram

numerical_column=data.select_dtypes(include=['number']).columns
for column in numerical_column:
    col_data=data[column].dropna()
    plt.hist(col_data)
    plt.title(f"Histogram of {column}")
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()
    



#Box plot

num_var=data.select_dtypes(include=['number']).columns
for columns in num_var:
    col_data=data[columns]
    plt.figure(figsize=(6,3))
    plt.boxplot(col_data,vert=False,patch_artist=True,
                boxprops=dict(facecolor='lightblue',color='blue'),
                capprops=dict(color='red'),
                flierprops=dict(markerfacecolor='red',marker='o'))
    plt.xlabel('columns') 
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()
          
    #calculate outliers
    q1=data[columns].quantile(0.25)      #25%
    q3=data[columns].quantile(0.75)      #75%
    
    iqr=q3-q1
    lower_bound=q1-3*iqr      #for extreme skew we use 3
    higher_bound=q3+3*iqr
    outliers=data[(data[columns]<lower_bound) | (data[columns]>higher_bound)]
    print("number of values:",len(col_data))
    print("number of outliers:\n",outliers)


#BAR CHART
cate_data=data.select_dtypes(include=['object','category']).columns
for category in cate_data:
    cat_coln=data[category].value_counts()  #count the frequent value
    
    #values-count the frequent value
    #index-count the index in the column

    plt.figure(figsize=(8,4))
    plt.bar(cat_coln.index,cat_coln.values,color='yellow',edgecolor='black')
    plt.xlabel(category)
    plt.ylabel('y')
    plt.xticks(rotation=45)
    plt.show()

    
#standardization

numerical_column=data.select_dtypes(include=['number']).columns
for column in numerical_column:
    col_data=data[column]
    z_score=(col_data-col_data.mean())/col_data.std()
    print(z_score)
print(" Before Standardization:\n", data.describe())
print("\n After Standardization:\n", z_score.describe())


#Transforming categorical variable
import numpy as np
categorical_column=data.select_dtypes(include=[object,'category']).columns
for category_coln in categorical_column:
    datas=data[category_coln]
    dummy=pd.get_dummies(datas)
    
    for coln in dummy:
        if dummy.dtypes[coln]==np.bool_:
            convert=dummy[coln].astype(int)
            print(convert)


#TASK-2
import numpy as np
import pandas as pd
import scipy.stats as stats
sample=[5.1, 4.9, 5.3, 5.0, 4.7, 5.2, 4.8, 5.1, 5.0, 4.9, 5.2, 4.6]
sample_mean=np.mean(sample)
print(sample_mean)
sample_size=12
pop_mean=5.5
sample_std=np.std(sample,ddof=1)
#t_stat,p_value=stats.ttest_1samp(sample,pop_mean)
#print(t_stat)
t_test=(sample_mean-pop_mean)/(sample_std/np.sqrt(sample_size))
print("t-test",t_test)
alpha=0.05
df=sample_size-1
t_critical=stats.t.ppf(alpha,df)
print("t_critical value",t_critical)
if t_test<=t_critical:
    print("The average battery life is less than 5.5 hours,The null hypothesis is rejected.")
else:
    print("The average battery life is 5.5 hours or more,The null hypothesis is accepted.")
    print("\nYes,we can support the quality control analyst")



















    



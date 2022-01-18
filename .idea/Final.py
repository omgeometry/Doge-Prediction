import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython import get_ipython
import plotly.graph_objects as go
#get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
plt.style.use("fivethirtyeight")


# In[29]:


#get_ipython().system('pip install plotly')


# In[2]:


df = pd.read_csv("Dogecoin.csv")


# In[3]:


df.head()


# ### 2.Descriptive Statistics

# In[20]:


df.describe()


# ### 3.Check for missing values

# In[4]:


df.isnull().sum()


# It is showing that we don’t have any null values in our dataset

# In[7]:


df.info()


# ### 4. Visualizing the missing values

# In[8]:


sns.heatmap(df.isnull(),cbar=False,cmap='viridis')


# ### 5. Asking Analytical Questions and Visualizations

# Before this let us check the correlation between different variables, this will give us a roadmap on how to proceed further.

# In[9]:


plt.figure(figsize=(10,10))
sns.heatmap(df.corr(),cbar=True,annot=True,cmap='Blues')


# # Positive Correlation

# - Close – Open, High, Low
# 

# Now let us apply domain knowledge and ask the questions which will affect the price of the Close.

# # 1. How does the High affect the Close?

# In[11]:


plt.figure(figsize=(10,10))
plt.scatter(x='High',y='Close',data=df)
plt.xlabel('High')
plt.ylabel('Close')


# We can see that most of the High value lies between 0.24-0.30 has Close mostly between 0.23-0.28, there are outliers also(between 0.30-0.34).

# Let’s see a count between 50-100 i.e univariate analysis of horsepower.

# In[14]:


sns.histplot(df.High,bins=10)


# The average count between 0.26-0.28 is 50 

# # 2. What is the relation between Low and Close?

# In[16]:


plt.figure(figsize=(10,10))
plt.scatter(x='Low',y='Close',data=df)
plt.xlabel('Low')
plt.ylabel('Close')


# We can observe that the pattern is similar to Hight vs Close.

# # 3. How does Open affects Close?

# In[18]:


plt.figure(figsize=(10,10))
plt.scatter(x='Open',y='Close',data=df)
plt.xlabel('Open')
plt.ylabel('Close')


# # Show the candlestick on a chart

# In[30]:


fig = go.Figure(data=[go.Candlestick(
    x = df.index,
    open = df['Open'],
    close = df['Close'],
    high = df['High'],
    low = df['Low'],
    increasing_line_color = 'green',
    decreasing_line_color = 'red'
)])

fig.show()


# # Calculate the Fibonacci Retracement Levels

# In[31]:


maximum_price = df['Close'].max()
minimum_price = df['Close'].min()
difference = maximum_price - minimum_price
first_level = maximum_price - difference * 0.236
second_level = maximum_price - difference * 0.382
third_level = maximum_price - difference * 0.5
fourth_level = maximum_price - difference * 0.618


# In[32]:


top = plt.subplot2grid( (4,4), (0,0), rowspan=3, colspan=4)
top.plot(df.index, df['Close'], label = 'Close')
top.axhline(maximum_price, linestyle='--', alpha=0.5, color = 'red')
top.axhline(first_level, linestyle='--', alpha=0.5, color = 'orange')
top.axhline(second_level, linestyle='--', alpha=0.5, color = 'yellow')
top.axhline(third_level, linestyle='--', alpha=0.5, color = 'green')
top.axhline(fourth_level, linestyle='--', alpha=0.5, color = 'blue')
top.axhline(minimum_price, linestyle='--', alpha=0.5, color = 'purple')
plt.title('Close price for the Dataset')
plt.legend(loc='upper left')
plt.subplots_adjust(hspace=0.75)
plt.gcf().set_size_inches(15,8)


# In[33]:


plt.figure(figsize=(15,7))
plt.plot(df.index, df['High'],label='Low rate')
plt.plot(df.index, df['Low'],label='High rate')
plt.title('values of day by day')
plt.xlabel('Dates')
plt.ylabel('Values')
plt.legend()


# In[34]:


#making new Column to show difference High and Low values
df['Difference']=df['High']-df['Low']


# In[35]:


plt.figure(figsize=(15,7))
plt.plot(df.index, df['High'],label='Low rate')
plt.plot(df.index, df['Difference'],label='Difference')
plt.plot(df.index, df['Low'],label='High rate')
plt.title('values of day by day')
plt.xlabel('Dates')
plt.ylabel('Values')
plt.legend()


# In[36]:


plt.figure(figsize=(50,24))

plt.subplot(2,3,1)
plt.plot(df.index,df.High)
plt.title('Higher Values')
plt.xlabel('Date')
plt.ylabel('High')

plt.subplot(2,3,2)
plt.plot(df.index,df.Low)
plt.title('Lower Values')
plt.xlabel('Date')
plt.ylabel('Low')

plt.subplot(2,3,3)
plt.plot(df.index,df.Difference)
plt.title('Difference Values of High & Low')
plt.xlabel('Date')
plt.ylabel('Difference')


# # Machine Learning

# ### Predict the future price of Dogecoin

# In[37]:


df.head()


# In[42]:


df.drop(['Difference'], axis = 1, inplace=True)


# In[43]:


df.head()


# In[44]:


# Set the index to be the date


# In[45]:


df = df.set_index(pd.DatetimeIndex(df['Date'].values))


# In[46]:


df


# In[47]:


# Get the close price
df = df[['Close']]
df


# In[48]:


#Create a variable to store the number of days into the future that we want to predict
prediction_days = 1
df['Prediction'] = df[['Close']].shift(-prediction_days)
df


# In[49]:


# Create the independent data set (X)
X = np.array(df.drop(['Prediction'], 1))
# Remove the last n+1 rows of data where n is the prediction_days
X = X[:len(df) -prediction_days -1]
print(X)


# In[50]:


#Create a dependent dat set (y)
y = np.array(df['Prediction'])
#Get all of the y values except the last n+1 rows
y = y[:-prediction_days -1]
print(y)


# In[51]:


# Split the data into 80% trining data set and a 20% testing data set
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)


# In[52]:


# Use the RandomForestRegressor for the model
from sklearn.ensemble import RandomForestRegressor
forest = RandomForestRegressor(n_estimators = 2, random_state = 587)
forest.fit(x_train, y_train)
print(forest.score(x_test, y_test))


# In[53]:


# Show the close the predicted value and the actual values are
prediction = forest.predict(x_test)
# Print the predicted test values
print(prediction)
print()
# Print the actual values
print(y_test)


# In[54]:


# Get the validation data for the model
# Create a variable to store all of the rows in the data set except the last n rows
temp_df = df[: -prediction_days]
#Create a variable to store the independent price value
x_val = temp_df.tail(1)['Close'][0]
print(x_val)


# In[55]:


prediction = forest.predict([[x_val]])
# Print the price of Dogecoin for the next n days
print('The price of Dogecoin in', prediction_days, 'days is predicted to be', prediction)
# print the actual value for the next n days
print('The actual price was', temp_df.tail(1)['Prediction'][0])


# In[ ]:


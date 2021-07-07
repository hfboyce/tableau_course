# Asking Question and Exploring Your Data

We spoke earlier that when we make data visualizations it stems from 2 reasons; we have a question we want to answer to we want to provoke new questions with said visualization. 

Before we make our visualization it's important to determine which of those actions we are attempting. 

In today's lesson, we are going to discuss both. 

## What is the Question? 

Let's start with what kind of questions we are asking before we try to answer them. 


<img src="imgs/questions.png"  width = "45%" alt="404 image" />

<br>
<br>

This section is mostly being referenced from [Roger D. Peng and Elizabeth Matsui - The Art of Data Science](https://leanpub.com/artofdatascience)

According to a paper published by Roger and Jeff Leek, understanding the types of questions you are asking is crucial to your interpretation of your final insights and result. 

They state that there are 6 types of data analysis questions. 

1. Descriptive
2. Exploratory
3. Inferential
4. Predictive
5. Causal
6. Mechanistic


### Descriptive 

A descriptive question hopes to summarize a characteristic of a dataset without interpretation. 

Remember summary statistics? This is a question involving those! 

Examples of this type of question include: 

- What is the proportion of high school graduates of Google's employees? 
- What is the mean salary of employees at Schneider Electric? 
- How prevalent is a certain illness among individuals in Canada? 


### Exploratory

An exploratory question is a type of question that analyzes the data for patterns, trends or relationships between variables. This question often is used in hypotheses for additional analysis and studies. 

<img src="imgs/explore2.png"  width = "45%" alt="404 image" />

<br>
<br>

Examples of this type of question include: 

- Is there a relationship between tree location and truck diameter in our `Street-trees.csv` dataset?
- Does profit change with the amount of investment capital for a dataset set containing 1500 start-up companies? 

### Inferential 

Inferential questions are a restatement of a hypothesis we made and answered by analyzing a different dataset. Essentially we made a hypothesis from one dataset and see if this applies to a population (a whole). 

Examples include:

- Does political party voting change with indicators of wealth for all people living in Canada?([Source: Data Science: A First Introduction](https://ubc-dsci.github.io/introduction-to-datascience/index.html#chapter-learning-objectives))
- Does the high school graduation rate affect employment rates in the Indian population? 


### Predictive 

Predictive questions are less interested in what ***causes*** a particular result and more on ***if*** a particular result will occur. It generally asks what particular measurements or categories for an observation will be. 

<img src="imgs/predictive.png"  width = "45%" alt="404 image" />

<br>
<br>

Examples include: 

- What political party will someone vote for in the next Canadian election? ([Source: Data Science: A First Introduction](https://ubc-dsci.github.io/introduction-to-datascience/index.html#chapter-learning-objectives))
- What a house will sell for on the market? 
- If an individual has a particular diagnosis or not. 


### Causal

A causal question asks if a change in one variable will result in a change in another, on average in a population. 

- Does increases sugar quantities in an individual's diet cause an increase in migraines?
- Does wealth lead to voting for a certain political party in Canadian elections?  ([Source: Data Science: A First Introduction](https://ubc-dsci.github.io/introduction-to-datascience/index.html#chapter-learning-objectives))
- Does the level of education increase an individual's income? 


### Mechanistic	

Mechanistic questions generally ask the **how**. How does the effect happen? These are generally quite hard to answer. 

<img src="imgs/how.png"  width = "45%" alt="404 image" />

<br>
<br>

Examples include: 

- How does wealth lead to voting for a certain political party in Canadian elections? ([Source: Data Science: A First Introduction](https://ubc-dsci.github.io/introduction-to-datascience/index.html#chapter-learning-objectives))
- How does diet lead to a reduction of a diabetes diagnosis?
- How does education increase individual income?

Visualizations help us answer **Descriptive** and **Exploratory** questions.

The questions you ask must be of interest to your expected audience. 


## Exploratory Data Analysis (EDA)


<img src="imgs/explore.png"  width = "45%" alt="404 image" />

<br>
<br>


Exploratory data analysis (EDA), is an early on process of your data analysis that you get acquainted and familiar with your data. You are examining the columns (variables/fields)
that you have, the potential relationship between columns and some summary statistics. 

**Why are EDAs important?**     
EDA is important to your analysis and it can help you identify potential issues, shortcomings with your data or help you discover additional questions you may want to explore further. 

Data visualization is so important to this process as it gives an opportunity to identify patterns much easier than otherwise. 

EDA begins after loading the data and glancing at the dataframe. 

What are the columns? What data types are they? What values are contained in certain columns? Are there any particularly interesting summary statistics? What is the range of values of the variable? 

Personally, I find the EDA step of my analysis process the most fun. It's like meeting someone for the first time and finding out what kind of person they are. Generally, you are hoping the person you are meeting is morally good and not full of lies, whereas, with your data, you are hoping it is unbiased and not full of NAs (missing values). 


### How to approach an EDA?

Key steps to do during EDA: 

**1\. Read in your data:**

This step sounds like a natural step but of course, this may a bit more intensive than you think. Reading in your data may require permissions on the server, downloading data from multiple sources and making sure it's being read in correctly. 

**2\. Assessing the columns:**

What columns do you have? Are they all the ones that you need? Are you expecting them to be restrictive? This is also a good time to address if there are any issues with your data and determine how you would resolve them. 

**3\. Look at your data:**

How many observations do you have?  What values are you missing? Is what you have enough to try and answer the question that you posed? 

**4\. Cleaning your data:** 

This step is better done using Tableau Prep, this may mean removing columns, rows or splitting a single column into multiple. 

**5\. Summarize your data:** 

Obtaining key summary statistics such as mean, median, maximum and minimum values can help somewhat understand our data a bit more. This is somewhat like reading the ingredient of a recipe but not seeing the instructions or a picture of the final result. 

**6\. Visualize:**

I like to look at the distributions of the columns I am interested in. It's also a good idea to try and concentrate on the columns that are needed to answer your question. That being said, you may find some useful insights in columns that you don't expect. When making plots for EDA, since it is done mainly for you and getting acquainted with your data, proper axis labels and titles are less of a concern. 


Once you have done your EDA you can collect all the information and produce a report from your insights, a dashboard useful to answer your question, or if your question is predictive you may continue with a predictive statistical or machine learning model. 


## Quick Quiz

1. "What are the most common cancer diagnoses in the world?" is a type of which kind of question? 
2. "Does sun exposure cause an increase in cancer diagnosis?" is a type of which kind of question? 
3. "How does sun exposure lead to an increase in cancer diagnosis?" is a type of which kind of question? 
4. "Does a certain individual have cancer?" is a type of which kind of question? 
5."Is there a relationship between the time exposed in the sun and cancer diagnosis in the Indian population?" is a type of which kind of question? 
6. **True or False**: EDA visualizations are less concerned about plotting details such as axis labels and titles.
7. Which of the following is not a part of EDA?   
a) Obtaining statistics of the data    
b) Understanding the missing values from your data     
c) Visualizing the data     
d) Creating a predictive model from the data      

<!--
```{admonition} Solutions!
:class: dropdown

1. Descriptive
2. Causal
3. Mechanic
4. Predictive
5. Inferential
6. True
7. d)  Creating a predictive model from the data

```
-->


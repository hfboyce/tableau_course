#  Lesson 3: Dashboards and EDA

This exercise will be using the data named `indian_statups.csv` that I've provided for you at [this link from the google drive](https://drive.google.com/file/d/1zIwmqngMXQCy0ScS9VxXUdcl2TA0o-gG/view?usp=sharing). This data was originally obtained from the [**India Startup - 2021**](https://www.kaggle.com/bhararthshiviah/indian-startups-2021?select=2021_registered_companies.csv) Kaggle dataset which has an[Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/) license. This means that I must give attribution to Bharath Shivaiah for the data and indicate the changes I have made. I have wrangled the data, specifically the `state` columns so that any state codes have been converted to full state names and any misspellings have been fixed and added an additional `date` column.

This also means that for my adapted data, the Attribution-NonCommercial-ShareAlike 4.0 International license must hold. 



## Exercise 1: Loading in the data 

1\. Load in the `indian_statups.csv` in Tableau Desktop.           
- How many geographical columns are there?
- How many Measures are there?
- How many continuous columns?
- What is the range (domain) of `Authorized Capital`?
- Are there any date fields?
- How many unique values are there in `Company Type`?

2\. If you have Tableau Prep, try it out and load in the data.              
- Add a **Clean Step** so that you can look that the distributions and values of each column.
- Which `activity_description` is most prominent in the dataset?
- How many rows have over 2 billion dollars in `Paidup Capital`? 
- What percentage of the data is of private class?

## Exercise 2: Explorative Plots 

1\. Let's make a histogram for the distribution of `Paidup Capital`.              
- Change the bin size and exclude any points that are severely outlying by changing the axis range. 
- Change the bin size to something more appropriate. 
- Show a separate distribution for each `Activity Description` using the **Pages** card.

2\. Create a scatter plot of `Paidup Capital` vs `Authorized Capital`.
- Facet this scatter plot by `Category`.
- Add a linear trend line to each facet.
- Which category has a steeper plot?

3\. Create a heat map of the count of values from the columns `Company Type` and `Activity Description`. 
- Which Company Type and Activity Description has the largest count? 
- Which Company Type(s) only have companies from 2 Activities? 

4\. Create a line plot, showing the number of companies registered in 2021. Use the column `Date of Registration` 
- You can facet this row-wise by `Category` and give them independent axes by right-clicking on an axis, clicking **edit axis**, and selecting **Independent axis ranges for each row or column**.
- Do you see something wrong here? Can you explain why this may happen?
- Now try this again using `date` instead. Although this is less precise, it's more accurate and less prone to mistakes.

## Exercise 3: Questions and Visualizations 

1\. Ask 2 questions you will want to attempt to answer using visualizations.     
- Which of the 6 question types do your questions belong to?

2\. Create 2 additional plots that answer your questions above. Remember these are not in the same explorative manner as you did earlier. That means you can recreate some of the plots above without the **Pages** tool or faceting. 

## Exercise 4: Blending data

1\. Connect to a new data source.      
- Load in the `states_india.geojson` *spatial file* that is located in the google drive [here](https://drive.google.com/file/d/1Mw9qKTDot-7ECGGNsWiWGPMR5_-Y65zW/view?usp=sharing). This is the geojson file needed to make the state boundaries of India. Note that this data was acquired from the [following source](https://un-mapped.carto.com/tables/states_india/public/map). 

2\. Connect the two sources by the `State` filed in the `indian_startups` data and the `St Nm` column in the `States_india`.
data source. 
- This will require you to **Edit Blend Relationship**. 


## Exercise 4: Choropleth

1\. Create a choropleth map that shows the **Total** `Paidup Capital` per state.          
- Which state raised the most capital?
- Is this what you expect with your knowledge of the different states? 


## Exercise 5: Creating Dashboards  

1\. Create a new Dashboard page.              
2\. Convert Dashboard **Size** to automatic.                 
3\. From the google drive, download this       [image](https://drive.google.com/file/d/1wLpQDBJZnuqXGeyMNOvjt7f6kn0r_ayB/view?usp=sharing) and add it to your dashboard. I recommend to "fit the image" to the outline.                 
4\. Add a title for your dashboard using a text box.              
5\. Add a selection of the plots you made above but make sure to include the Choropleth graph. Not all of them must be included.                 
6\. Create 2 filters for any of the plots.              
- Adjust these filters so it works for all the plots.                            
7\. Use the Choropleth map as a filter so that the other plots are adjusted based on the state(s) selected.              
- For this to work, the field (column) in both sources must be identical. 

## Exercise 6: Formatting

1\. Give all the plots that you made in this exercise appropriate titles and axis names. Change the colours to something you'd prefer.       


## Attribution

- Data: Indian startups - 2021 List of companies registered in India - 2021 by Bharath Shivaiah obtained from [Kaggle](https://www.kaggle.com/bhararthshiviah/indian-startups-2021).
- Data: India States spatial data - [CARTO](https://carto.com/help/working-with-data/attribution/) obtained from [un-mapped.carto.com](https://un-mapped.carto.com/tables/states_india/public/map)
- Image: <a href="https://unsplash.com/@myhq?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">myHQ Workspaces</a> on <a href="https://unsplash.com/s/photos/india-startup?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  





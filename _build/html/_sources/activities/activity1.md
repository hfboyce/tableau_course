#  Lesson 1: Making Your First Viz

I believe that in order to firmly grasp a concept, it requires some application.

HR has provided me with some sample data that many of you will, or have worked with. I'm going to build some tasks for your to try on your own using the skills you learned during the class. 

## Exercise 1: Connecting to the data and asking questions 
I'll provide you with the sample data given to me by one of your colleagues. We will be using the excel spreadsheet named `compensation.xlsx`.

Please download it at the link below stored on my google drive [here](https://drive.google.com/file/d/1Qg0KbWzqlEFsOreaMcrrjIjo94sCSaP3/view?usp=sharing).

1. Connect Tableau to the `compensation` excel sheet. 

2. Convert the `CTC` column to a number. 

3. Go to sheet 1. Did tableau generate any columns that were not there before? If so, which ones? 

4. How many geographical dimensions are there? 

5. How many date measures are there? 

6. Are there any questions that you have from this dataset? Write down a few questions you want to explore in the data. 


## Exercise 2: Making a Bar Plot 

1. We want to know how many employees there are in each country. Use the appropriate columns to generate a bar plot. 

2. Sort these values in descending order.
  - Which country has the largest number of employees?
  - Which country has the least amount of employees? 
  
3. Can you transpose your plot? 

4. Change the colour of your plot to a colour of your choice. 

5. Try decreasing the width of the bars. 

## Exercise 3: Map 

1. Make a new worksheet.

2. Create a world map using the latitude and longitude fields. 

3. We want to now explore what is the AVERAGE CTC is of each country. Do some countries have higher a higher CTC value than others? We are first going to have to drag the `Country` column to the `Detail` option on the **Marks** card. Without doing this, Tableau will not know to give an average to any of the countries since that field is not used in the plot! 

4. Let's specify AVERAGE CTC by colour. Drag this column to the **Color** Mark. 

5. Is this giving the average value? Can you change it to reflect the average stip percentage now?

6. Which countries have higher average CTC values?

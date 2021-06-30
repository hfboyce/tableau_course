# Plot types and the Dashboard 

## More Plotting Examples

Alright, let's now take a shot at creating some of the plots we just learned about. 

### Pie Chart

Let's say we want to see the proportion of trees planted with root barriers to trees planted without root barriers. 

First, make a new worksheet. 

**Step by Step Instructions**

1\. Drag the `Root Barrier` field to the **Color** icon.  

<img src="imgs/pie1.png"  width = "85%" alt="404 image" />

<br>
<br>


2\. Drag the `Tree Id` field to the **Area** icon.  

<img src="imgs/pie2.png"  width = "85%" alt="404 image" />

<br>
<br>


3\. Convert the `Tree Id` field to a **Count** **Measure** by right-clicking it and selecting from the dropdown menu.

<img src="imgs/pie3.png"  width = "85%" alt="404 image" />

<br>
<br>


4\. Click on the **Show Me** menu on the top right side of the workspace.  

<img src="imgs/pie4.png"  width = "85%" alt="404 image" />

<br>
<br>


5\. Select the pie chart icon. 

<img src="imgs/pie5.png"  width = "85%" alt="404 image" />

<br>
<br>

And voila! We <del>baked</del> made a pie chart 🥧!


<img src="imgs/pie6.png"  width = "85%" alt="404 image" />

<br>
<br>



### Stacked Bars 

A pie chart may not be the best visualization to see the proportion of trees planted with root barriers to trees planted without root barriers. 

Let's see how it looks like as a stacked Bar chart. 

Make a new worksheet or clear the current sheet you are on. 

**Step by Step Instructions**

1\. Drag the `Tree Id` field to the **Rows** shelf.  

<img src="imgs/stacked1.png"  width = "85%" alt="404 image" />

<br>
<br>


2\.Convert this field to a **Count** **Measure** by right-clicking and selecting the appropriate measure.

<img src="imgs/stacked2.png"  width = "85%" alt="404 image" />

<br>
<br>


3\. We can now add the stacking part of this bar chart by dragging `Root Barrier` to the **Color** icon in the **Marks** card.

<img src="imgs/stacked3.5.png"  width = "85%" alt="404 image" />

<br>
<br>


4\. Let's transpose this graph so it's a little clearer by clicking the **Swap Rows and Columns** icon in the toolbar.

<img src="imgs/stacked3.png"  width = "85%" alt="404 image" />

<br>
<br>

Great! Here is our stacked bar chart!

<img src="imgs/stacked4.png"  width = "85%" alt="404 image" />

<br>
<br>



### Side-by-Side Bars 

Still maybe not the right plot for this question. Let's go with a barplot with the categories side-by-side.



**Step by Step Instructions**

1\. Drag the `Root Barrier` field to the **Columns** shelf.  

<img src="imgs/ssb1.png"  width = "85%" alt="404 image" />

<br>
<br>




2\. Drag the `Tree Id` field to the **Rows** shelf again.  

<img src="imgs/ssb1.5.png"  width = "85%" alt="404 image" />

<br>
<br>

You may have to indicate that want to **Add All Members**

<img src="imgs/ssb2.png"  width = "85%" alt="404 image" />


3\. Convert the `Tree Id` field to a **Count** **Measure** by right-clicking and selecting the appropriate measure.

<img src="imgs/ssb3.png"  width = "85%" alt="404 image" />

<br>
<br>



4\. Let's add a little bit of colour to this plot. This isn't a necessary step, however, we are doing this for consistency to compare to the last three charts.

<img src="imgs/ssb3.5.png"  width = "85%" alt="404 image" />

<br>
<br>

Now that we've done that, which plot out of the pie, stacked bars and side-by-side plot do you most prefer?

<img src="imgs/ssb4.png"  width = "85%" alt="404 image" />

<br>
<br>

### Scatter Plot 

With this particular data source, we don't really have 2 good continuous numeric columns. To demonstrate how to make a scatter plot, we are going to use what we have and make the best of it. 

Let's plot and see if there is a relationship between the diameter of the trees' trunks and their height. 

**Step by Step Instructions**

1\. First, let's convert the `Height Range Id` column to a **Measure**. We can do this by right-clicking on it and selecting **Measure**.   

<img src="imgs/scat2.png"  width = "85%" alt="404 image" />

<br>
<br>




2\. Drag the newly transformed `Height Range Id` measure to the **Columns** shelf.  Note that this is going to change it to a **SUM** aggregate. This is ok because we will be summing over the values of `Tree ID` and thankfully this is a unique column!

<img src="imgs/scat3.png"  width = "85%" alt="404 image" />

<br>
<br>


3\. Next drag the `Diameter` **Measure** to the **Rows** shelf. This will again transform into an aggregate **SUM**. 

<img src="imgs/scat4.png"  width = "85%" alt="404 image" />

<br>
<br>




This only gives us a single point. We need to split it up so we have a point for each tree. 



4\. Dragging `Tree Id` to the **Details** icon in **Marks** Card will cause another popup window where we can "Add all members".

<img src="imgs/scat5.png"  width = "85%" alt="404 image" />

<br>
<br>

5\. We then can change the mark type to a **Circle**...

<img src="imgs/scat6.png"  width = "85%" alt="404 image" />

<br>
<br>

6\. ...And decrease the point size. 

<img src="imgs/scat9.png"  width = "85%" alt="404 image" />

<br>
<br>

Great! 

<img src="imgs/scat9.9.png"  width = "85%" alt="404 image" />

<br>
<br>


### Line Graph

We are now interested in answering the question ***How many trees were planted over the years?*** 

Before you start, let's make a new worksheet. 

**Step by Step Instructions**

1\. Drag the `Date Planted` field to the **Columns** shelve and the `tree Id` field to the **Rows** shelf.

<img src="imgs/ts1.png"  width = "85%" alt="404 image" />

<br>
<br>

2.\ We are again interested in the number of trees planted at selected dates so once again, we want to transform this field to a **Count** **Measure**. 

<img src="imgs/ts2.png"  width = "85%" alt="404 image" />

<br>
<br>

3\. Since `Date Planted` is a continuous variable, it's a good idea to right-click and transform this field into a **Continuous** Dimension. 

<img src="imgs/ts4.png"  width = "85%" alt="404 image" />

<br>
<br>


4\. This automatically generates the number of trees planted each year (but there are null values!)

<img src="imgs/ts5.png"  width = "85%" alt="404 image" />

<br>
<br>

4\. We can change the `YEAR(Date Planted)` field to:

- `MONTH(Date Panted)` (top month choice when right-clicking) - which aggregates months together for all years.
    
<img src="imgs/ts6.png"  width = "85%" alt="404 image" />

<br>
<br>


<img src="imgs/ts7.png"  width = "85%" alt="404 image" />

<br>
<br>
    
    
- `MONTH(Date Panted)` (Bottom month choice when right-clicking) - which will make a sequential plot.
    
    
<img src="imgs/ts8.png"  width = "85%" alt="404 image" />

<br>
<br>


<img src="imgs/ts9.png"  width = "85%" alt="404 image" />

<br>
<br>
    
We are going to stick with the year dimension though! 

<img src="imgs/ts10.png"  width = "85%" alt="404 image" />

<br>
<br>
    
    
<img src="imgs/ts11.png"  width = "85%" alt="404 image" />

<br>
<br>
    
    
5\. We can add a circle for clarity at each year as part of our line graph by dragging a second  `Tree Id` field to the **Rows** shelf. 

<img src="imgs/ts12.png"  width = "85%" alt="404 image" />

<br>
<br>

```{warning}
You may get a popup warning when you do this where I specify **Add All Members** since we are converting it to a COUNT measure after this. 

<img src="imgs/ts13.png"  width = "85%" alt="404 image" />
```
    
6\. We need to make sure we also convert it to a `Count` measure. 

<img src="imgs/ts14.png"  width = "85%" alt="404 image" />

<br>
<br>

At first, we should get 2 graphs on top of each other. 

<img src="imgs/ts15.png"  width = "85%" alt="404 image" />

<br>
<br>

7\. We can right-click one of them and select "**Dual Axis**". 

<img src="imgs/ts16.png"  width = "85%" alt="404 image" />

<br>
<br>


This will superimpose one on another with a left and a right axis title.


<img src="imgs/ts17.png"  width = "85%" alt="404 image" />

<br>
<br>


8\. We can hide the one on the right by right-clicking the axis and unticking the "**Show Header**" option. 

<img src="imgs/ts18.png"  width = "85%" alt="404 image" />

<br>
<br>


<img src="imgs/ts19.png"  width = "85%" alt="404 image" />

<br>
<br>

9\. In the **Marks** card, select the `CNT(Tree Id)(2), and from the dropdown, select **circle**. 

<img src="imgs/ts20.png"  width = "85%" alt="404 image" />

<br>
<br>

Now we have a line plot with points! 

<img src="imgs/ts21.png"  width = "85%" alt="404 image" />

<br>
<br>


10\. To change the colour of the line and the points, we need to make sure we change the colour of both measures by selecting the "**All**" tab under the "**Marks**" card on the right. 


<img src="imgs/ts22.png"  width = "85%" alt="404 image" />

<br>
<br>

11\. Don't forget to give it a title and edit the y-axis label as we did before!.  

<img src="imgs/ts23.png"  width = "85%" alt="404 image" />

<br>
<br>

### Histograms

Let's now start practicing making distributions. Tableau doesn't easily facilitate density plots, so we are going to stick with learning how to make histograms.

Perhaps we are interested in the distribution of tree trunk diameter length. Remember histograms are used to visualize the distribution of a numeric continuous variable. 

**Step by Step Instructions**

1\. First, drag the `Diameter` **Measure** to the **Columns** shelf

<img src="imgs/easy_hist1.png"  width = "85%" alt="404 image" />

<br>
<br>


2\. You can then go to the **Show Me** menu and click on the ***Histogram*** option. Tableau will then assign the correct measures to the shelves and cards. 

<img src="imgs/easy_hist2.png"  width = "85%" alt="404 image" />

<br>
<br>


3\. And there you have a histogram! Now, this already seems a little problematic because we didn't choose the bin size and clearly our distribution is skewed. 

<img src="imgs/easy_hist3.png"  width = "85%" alt="404 image" />

<br>
<br>

It might also be helpful to see this distribution shape without the outliers on the far right and with different bin size.       
The majority of the data looks like it's between 0-50 so let's make the bin size 2 and limit the axis to 0-50. 



4\. You'll notice that Tableau's been kind and has actually made us a new continuous dimension named `Diameter (bin)`. Right-click on this new field and click on **Edit** from the dropdown menus. 

This is where we are going to change the bin size. 

<img src="imgs/easy_hist4.png"  width = "85%" alt="404 image" />

<br>
<br>

5\. This will result in a popup window where we can change the size of the bins. Let's go ahead and change it to 2. Remember bin size can cause bias in your plots so be careful when choosing this value. Click **OK**. 

<img src="imgs/easy_hist5.png"  width = "85%" alt="404 image" />

<br>
<br>

6\. Now we can see that our bars are a lot thinner (If only exercising was this easy). 

<img src="imgs/easy_hist6.png"  width = "85%" alt="404 image" />

<br>
<br>


7\. Let's fix the axis range now. You'll not have to do this often but for this particular problem and question, removing the outliers could give us a bit of a clearer distribution shape. 

Right-click the axis we want to limit and from the dropdown click **Edit Axis...**. 

<img src="imgs/easy_hist7.png"  width = "85%" alt="404 image" />

<br>
<br>




8\. From the popup, select a **Fixed Range** and Fixed end at 50 for this plot. 

<img src="imgs/easy_hist8.png"  width = "85%" alt="404 image" />

<br>
<br>

Great! 



9\. We Are going to go one step forward and change the tick mark intervals too. Click on the **Tick Marks** option at the top of the popup window. 

<img src="imgs/easy_hist9.png"  width = "85%" alt="404 image" />

<br>
<br>



10\. We can decrease the tick interval to 2 to help make our bar values easier to identify. 

<img src="imgs/easy_hist10.png"  width = "85%" alt="404 image" />

<br>
<br>

And we did it!

<img src="imgs/easy_hist11.png"  width = "85%" alt="404 image" />

<br>
<br>

 We now can see that the majority of trees in Vancouver have a diameter between 2 and 3 cms. We also see that it's very skewed to the right. 

### Boxplot

Although there is an option to make boxplots using the **Show Me** menu, I find that it can often plot things differently than how I want them to. These are the steps I generally take. 

Suppose that we want to see if the difference between the distributions of trunk diameter between trees planted with root barriers and without root barriers. 

**Step by Step Instructions**

1\. Begin by dragging `Root Barrier` to the **Columns** shelf. 

<img src="imgs/box1.png"  width = "85%" alt="404 image" />

<br>
<br>


2\. Next, you'll want to drag the `Diameter` field to the **Rows** shelf. You'll have a beautiful bar plot now measuring the sum of all the trees diameters for each barrier type.  

<img src="imgs/box2.png"  width = "85%" alt="404 image" />

<br>
<br>


3\. Since we want individual observations for each tree (somewhat), we need to drag the `Tree Id` field to the **Detail** icon in the **Marks** card. This will populate the message where we indicate that we want to ** Add all members**. 

<img src="imgs/box3.png"  width = "85%" alt="404 image" />

<br>
<br>


4\. Let's change the mark. Convert the mark from Automatic to **Circle**. 

<img src="imgs/box5.png"  width = "85%" alt="404 image" />

<br>
<br>

This will produce a circle for each tree now. 


5\. This is where we make the box part of our boxplot! Right-click on the axis with the continuous variable - in our case, that's `Diameter`. Select the **Add Reference Line** option. 

<img src="imgs/box6.png"  width = "85%" alt="404 image" />

<br>
<br>

6\. When we select this option, a popup with many different option tabs displays. We want the **Boxplot** tab!

<img src="imgs/box7.png"  width = "85%" alt="404 image" />

<br>
<br>


7\. Here we want to "Hide the underlying marks (except outliers)". The reason we are hiding them, in this case, is because we have THOUSANDS of them! If our dataset was smaller, it might be a good idea to show all the underlying marks. 

<img src="imgs/box8.png"  width = "85%" alt="404 image" />

<br>
<br>


8\. We can also change the colour of the box **Fill** to a green palette which goes nicely with our tree theme. 

<img src="imgs/box9.png"  width = "85%" alt="404 image" />

<br>
<br>

We can now leave this popup screen by clicking **OK**. 

<img src="imgs/box10.png"  width = "85%" alt="404 image" />

9\. Ok, so our outlying observations are rather large right now. Let's decrease the size.

<img src="imgs/box11.png"  width = "85%" alt="404 image" />

<br>
<br>

Ahh, that's a bit cleaner.

<img src="imgs/box12.png"  width = "85%" alt="404 image" />

<br>
<br>

10\. We can also change the points to a green colour to go with the rest of the plot. This can be done by clicking the **Color** icon.

<img src="imgs/box13.png"  width = "85%" alt="404 image" />

<br>
<br>

11\. This is a completed boxplot! One thing you can do to get a better idea of the distributions is to transpose it.

<img src="imgs/box14.png"  width = "85%" alt="404 image" />

<br>
<br>
  
Ahh, beautiful! 

<img src="imgs/box15.png"  width = "85%" alt="404 image" />

<br>
<br>

```{admonition} Tip!
:class: tip
When you have multiple boxplots and you want to sort them in some order, using the sorting buttons in the toolbar won't quite sort them properly or may not sort them how you are intending them to. 

The best way to sort your boxplots to some criteria is as follows: 

1\. Click on the dimension field - here it's our `Root Barrier` column and from the dropdown select **Sort...**

<img src="imgs/boxsort1.png"  width = "85%" alt="404 image" />

<br>
<br>

2\. This will produce a popup window where we selected a **Nested** option to sort our data by. 

<img src="imgs/boxsort2.png"  width = "85%" alt="404 image" />

<br>
<br>


3\. We can select if we want the field to be sorted in **Ascending** or **Descending** order and then choose an Aggregation. Here we are going to be selecting **Median** which is the center line of our boxes in the boxplot. 

<img src="imgs/boxsort3.png"  width = "85%" alt="404 image" />

<br>
<br>

```

### Heatmap

Let's see what the joint distribution is for the presence of a curb and if the tree has root barriers or not. 

This will need a heat map or a heat map with a size channel. let's explore the former first. 

**Step by Step Instructions**

1\. Drag the `Root Barrier` to the **Columns** shelf- here we will first drag the `Root Barrier` column. 

<img src="imgs/heat1.png"  width = "85%" alt="404 image" />

<br>
<br>

2\. We then can drag our second discrete dimension to the **Rows** shelf. We will drag the `Crub` column. 

<img src="imgs/heat2.png"  width = "85%" alt="404 image" />

<br>
<br>


3\. To add a count field, we will drag the `Tree Id` to the **Detail** icon in the **Marks** card. As we have done before, we "Add all members" when prompted by the popup.

<img src="imgs/heat3.png"  width = "85%" alt="404 image" />

<br>
<br>


4\. We now transform this field to a **Count Measure** by right-clicking and selecting it from the drop-down.   

<img src="imgs/heat4.png"  width = "85%" alt="404 image" />

<br>
<br>

<img src="imgs/heat5.png"  width = "85%" alt="404 image" />


5\. Although we already have square marks, let solidify it and convert the **Automatic** mark to a **Square** mark. This is to make sure nothing is transformed when we add additional fields to our graph.  

<img src="imgs/heat6.png"  width = "85%" alt="404 image" />

<br>
<br>

6\. We can include a value in each quadrant by dragging the `Tree Id` to the **Label** mark. 

<img src="imgs/heat7.png"  width = "85%" alt="404 image" />

<br>
<br>


7\. We then must convert it to a **Count Measure** by right-clicking and selecting it accordingly. 

<img src="imgs/heat8.png"  width = "85%" alt="404 image" />

<br>
<br>

Nice! 

<img src="imgs/heat9.png"  width = "85%" alt="404 image" />

<br>
<br>

### Heatmap with Size Channel

If we also want to include an area channel in the plot, we can continue from the steps of the heatmap. 

1\. Here we will add all the counts of the trees by dragging the `Tree Id` to the **Size** icon. 

<img src="imgs/heat10.png"  width = "85%" alt="404 image" />

<br>
<br>

2\. As we have seen many times before we transform the dimension to a **Count Measure** by clicking and selecting from the dropdown menu. 

<img src="imgs/heat11.png"  width = "85%" alt="404 image" />


<img src="imgs/heat12.png"  width = "85%" alt="404 image" />

<br>
<br>

9\. The labels seem to ruin the esthetics of this plot, so let's remove this from the plot by right-clicking and selecting **Remove**. 

<img src="imgs/heat13.png"  width = "85%" alt="404 image" />

<br>
<br>

That's better. Nice job! 

<img src="imgs/heat14.png"  width = "85%" alt="404 image" />

<br>
<br>


## Quick Quiz

1. **True or False**: Sorting a boxplot can be done by using the sort buttons on the toolbar.
2. **True or False**: Histograms can be made with a click from the **Show Me** window. 
3. What column type are the fields used in the **Columns** and **Rows** shelf - Continuous or discrete? 
4. Which of the following fields acts as a hierarchy by default `Row Id`, `Date Issued`, `Gender`, `Latitude`? 
5. What mark shape is needed for a heatmap? 



<!--
```{admonition} Solutions!
:class: dropdown

1. False 
2. True
3. Continuous
4. `Date Issued`
5. Square

```
-->

## Dashboards

The moment we've all been waiting for! This is where we can take our visualizations from our worksheets, combine them into 1 page (or multiple) and add filters making them dynamic in nature. 

Let's begin by creating a new Dashboard. 

1\. Click on the Dashboard icon at the bottom of your workspace. 

<img src="imgs/dash0.png"  width = "85%" alt="404 image" />

<br>
<br>

<img src="imgs/dash00.png"  width = "85%" alt="404 image" />

<br>
<br>

Here we can displays images, worksheets, filters  and even website pages. 

### Workspace 

Here we can examine the buttons are tools we will need to create our dashboards. 

<img src="imgs/dash_workspace.png"  width = "100%" alt="404 image" />

<br>
<br>

<p style="font-size:30px; color:#FFF995">Size</p>

<p style="font-size:30px; color:#73FCD6">Sheets</p>

<p style="font-size:30px; color:#76D6FF">Tiled/Floating</p>

#### Tiled example 


#### Floating example 

<p style="font-size:30px; color:#FF85FF">Objects</p>

#### images

#### webpage

#### Text

#### Download 


<p style="font-size:30px; color:#9437FF">Device Preview</p>



### Adding elements 

#### sheets

#### images

#### webpage

### 


### Changes to all sheets 

### Connecting sheets 

### Filtering 

## Publishing data sources

## Quick Quiz

1. **True or False:** Using the same data, a histogram’s shape can change depending on the bin size.
2. **True or False:** When we are visualizing data from a single column, we are (usually) more interested in the shape/distribution in general, than individual points.
3. What does the middle line of a box plot represent?
4. Which visualization type can show multiple summary statistics of data as well as their distributions?  
5. What is another name for a density plot?
6. What plot type is most appropriate if we are interested in visualizing the relationship between two numeric/quantitative columns?



<!--
```{admonition} Solutions!
:class: dropdown

1. True
2. True
3. Median
4. Violin plot
5. Kernel Density Estimate (KDE)
6. Scatter plot

```
-->

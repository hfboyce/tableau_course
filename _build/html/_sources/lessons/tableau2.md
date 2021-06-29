# Plot types and the Dashboard 

## More Plotting Examples

Alright, let's now take a shot at creating some of the plots we just learned about. 

### Pie Chart

Let's say we want to see the proportion of trees planted with root barriers to trees planted without root barriers. 

First, make a new worksheet. 

**Step by Step Instructions**

1\. Drag the `Root Barrier` field to the **Color** mark icon.  

<img src="imgs/pie1.png"  width = "85%" alt="404 image" />

<br>
<br>


2\. Drag the `Tree Id` field to the **Area** mark icon.  

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




2\. Drag the newly transformed `Height Range Id` measure to the **Columns** shelf.  Note that this is going to change it to a **SUM** aggregate. This is ok because we will be summing over values of `Tree ID` and thankfully this is a unique column!

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

### Boxplot

### Heatmap

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


## Dashboards

### Layout 

### Filtering 

### Tooltips 

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




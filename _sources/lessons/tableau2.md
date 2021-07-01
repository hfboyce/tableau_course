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

It's important that you select the size of the screen your dashboard is expected to be displayed on. 
The [options](https://help.tableau.com/current/pro/desktop/en-us/dashboards_organize_floatingandtiled.htm) are:

- Fixed: The dashboard remains the same size no matter the screen used to display it. If the dashboard is bigger than the designated window, the dashboard will be scrollable. 
- Range: The dashboard scales between minimum and maximum sizes that you specify.
- **Automatic** - This is what I generally suggest since the dashboard will automatically resize to fit the screen it's display on. When using Automatic I also firmly suggest using a **Tiled** dashboard layout (explained below). 

<img src="imgs/dash_size1.png"  width = "85%" alt="404 image" />

<br>
<br>

<img src="imgs/dash_size2.png"  width = "85%" alt="404 image" />

<br>
<br>

<p style="font-size:30px; color:#73FCD6">Sheets</p>

Here is where we can select the plots we made on the worksheets and bring them together collectively on a dashboard. 

All we have to do, is drag the sheet to the visualization space. 

<img src="imgs/dash_sheet1.png"  width = "85%" alt="404 image" />

<br>
<br>

<img src="imgs/dash_sheet2.png"  width = "85%" alt="404 image" />

<br>
<br>

<p style="font-size:30px; color:#76D6FF">Tiled/Floating</p>

#### Tiled example 

You'll notice that when we dragged these sheet they snapped into a position. This is creating tiles. I only recommend using this layout method when using the Automatic sizing option. 


<img src="imgs/tiled.png"  width = "85%" alt="404 image" />

<br>
<br>

#### Floating example 

If we instead used the floating option, we could place the plot anywhere but it can prove problematic when the screen size is fixed. 

<img src="imgs/floating.png"  width = "85%" alt="404 image" />

<br>
<br>

<p style="font-size:30px; color:#FF85FF">Objects</p>

We are not restricted to only putting worksheets and graphs on our dashboard. We can also add images, webpages inbedded in the sheets as well as Text boxes, downloading and navigation button options.

#### images

We can place images in our dashboards just as easily as we cant sheets. 

**Step by Step Instructions**

1\. We first drag the **Image** option where we wish to place it in the dashboard. 

<img src="imgs/image1.png"  width = "85%" alt="404 image" />

<br>
<br>

2\. We then must select our desired images from our file directory, here I'm using the `trees.png` file which I've also made available on the Google drive [here](https://drive.google.com/drive/folders/1IP1Vs8bJnGElKfqZ8VkNlLVX-VXJZfaVhttps://drive.google.com/drive/folders/1IP1Vs8bJnGElKfqZ8VkNlLVX-VXJZfaV).

<img src="imgs/image2.png"  width = "85%" alt="404 image" />

<br>
<br>


3\. I select the **Fit Image** option so that the image is fix to the dimension of the dashboard tile. 
<img src="imgs/image3.png"  width = "85%" alt="404 image" />

<br>
<br>

And there you have it! 
<img src="imgs/image4.png"  width = "85%" alt="404 image" />

<br>
<br>



#### webpage

We can even embed complete working websites in our dashboards. 

**Step by Step Instructions**

1\. We drag the **Web Page** option to the dashboard and it will result in a popup asking for the desired page. 

<img src="imgs/object2.png"  width = "85%" alt="404 image" />

<br>
<br>

And it's as simple of that! We have the website active now! 

<img src="imgs/object3.png"  width = "85%" alt="404 image" />

<br>
<br>


#### Text

Adding text for titles or explanations (I've even added axis titles using this option when in a pinch) works the same as images and webpages. We can drag and then format our text. 

<img src="imgs/object5.png"  width = "85%" alt="404 image" />

<br>
<br>

<img src="imgs/object6.png"  width = "85%" alt="404 image" />


#### Download

To create an option to download a static copy of your dashboard, you can add a button allowing the viewer to do so. 

**Step by Step Instructions**

1\. Like the other object, we drag the **Download** icon to the dashboard.
<img src="imgs/object7.png"  width = "85%" alt="404 image" />

<br>
<br>

2\. To format it, we need to double click and select the desired export or button type and format the font. 
<img src="imgs/object8.png"  width = "85%" alt="404 image" />


3\. We can also adjust the background colour.

<img src="imgs/object9.png"  width = "85%" alt="404 image" />

<br>
<br>

<img src="imgs/object10.png"  width = "85%" alt="404 image" />


#### Navigation

There often time where on your dashboard you'd like to navigate to either a different dashboard or perhaps dive deeper into a worksheet. I needed this for my own dashboards when I had the list of customers pop up with certain filters and I wanted to navigate back to the main dashboard. 

**Step by Step Instructions**

1\.This can be down by dragging the **Navigation** icon onto the dashboard.
<img src="imgs/object11.png"  width = "85%" alt="404 image" />

<br>
<br>

2\. We don't need to do this for our dashboard, but you can then select where clicking this button with navigate you to. 

<img src="imgs/object12.png"  width = "85%" alt="404 image" />



#### Extensions 

For certain additional actions and features we can also add extensions that other people have made and shared publicly. 

We will discuss this in the 4th lesson if we have time. 


<p style="font-size:30px; color:#9437FF">Device Preview</p>


You can check and preview what your dashboard will look for other devices by clicking this **Device Preview** and scrolling through the options like **Desktop**, **Tablet** and **Phone**

<img src="imgs/preview1.png"  width = "85%" alt="404 image" />

<br>
<br>

<img src="imgs/preview2.png"  width = "85%" alt="404 image" />

<br>
<br>

<img src="imgs/preview3.png"  width = "85%" alt="404 image" />


## Filtering 

Here is where the fun starts! Since Tableau is an excellent tool to use for dynamic plots, let's go ahead and see why first hand. 

**Step by Step Instructions**

1\. Click on the sheet you wish to filter. On the right side of the plot you'll see a **More Options** button. 

<img src="imgs/filter2.png"  width = "85%" alt="404 image" />

<br>
<br>

This will produce a dropdown where we want to select a field to filter on. Under **Filters** we can then select the columns displayed. These are currently the ones we are using in the plot already. We will show you how to filter on additional columns momentarily. For now let's select  `Sum of Diameter`.

<img src="imgs/filter3.png"  width = "85%" alt="404 image" />

<br>
<br>

2\. Selecting the field desired will then produce a filter! 

<img src="imgs/filter4.png"  width = "85%" alt="404 image" />

<br>
<br>




3\.let's add another. Let's add the `Sum of Height Range Id` as a filter too.

<img src="imgs/filter6.png"  width = "85%" alt="404 image" />

<br>
<br>

<img src="imgs/filter7.png"  width = "85%" alt="404 image" />

<br>
<br>

I'm going to move the plot so that we can focus of the filters and see all the popups here 

<img src="imgs/filter8.png"  width = "85%" alt="404 image" />

<br>
<br>


4\. If we click on the filter we can then see a **More Options** icon. 

<img src="imgs/filter9.png"  width = "85%" alt="404 image" />

This is where we can see all the filter style options. 


<img src="imgs/filter10.png"  width = "85%" alt="404 image" />

Since both of these fields as measures, we can filters in the following ways: 

- **Range of Values/Dates:** This means you can filter the data to include or exclude more values. You can pick the minimum and maximum values. 

- **At Least/Starting Date:** This has a fixed maximum value and with an open ended minimum value that the user chooses.

- **At Most/Ending Date:** This has a fix minimum values with an open ended maximum value that the user chooses.

For time periods there are are 2 more called **Relative to Now** and **Browse periods** where the values must be continuous. 



5\. In order to filter the graphs by other columns, we must add it to the **Filters** card on the Worksheet page of the plot. 

Locate yourself to the appropriate sheet using the tab at the bottom. Select the column you wish to filter the plot on and drag it to the **Filters** card. Here we are going to drag the **Neighbourhood Name** column. 

<img src="imgs/filter0.png"  width = "85%" alt="404 image" />

<br>
<br>

This will create a pop-up where we can select the categories and values we wish to include. I will be selecting **All**

<img src="imgs/filter11.png"  width = "85%" alt="404 image" />

<br>
<br>

<img src="imgs/filter12.png"  width = "85%" alt="404 image" />

<br>
<br>

6\. We can then return to our dashboard, click on the plot and see that `Neighbourhood Name` has need added to the choice of filters. 

<img src="imgs/filter14.png"  width = "85%" alt="404 image" />

<br>
<br>

This produces a list of all the neighbourhoods now. 
<img src="imgs/filter00.png"  width = "85%" alt="404 image" />

<br>
<br>


7\. Clicking on this filter and selecting the **More Option** icon, you'll see all the different filtering styles.

<img src="imgs/filter15.png"  width = "85%" alt="404 image" />

<br>
<br>

`Neighbourhood Name` is a Dimension. Dimensions have the following possible filtering styles ([Source: help.tableau.com](https://help.tableau.com/current/pro/desktop/en-us/filtering.htm)): 

- **Single Value (List):** A full list of all the possible values of the filter as radio buttons but only 1 can be selected at a time.

- **Multiple Values (List):** Shows all the values in the filter as a list of check boxes where multiple values can be selected.

- **Single Value (Dropdown):** Displays the values of the filter in a drop-down list where only a single value can be selected at a time.

- **Multiple Values(Dropdown):** Displays the values of the filter in a drop-down list where multiple values can be selected.

- **Single Value (Slider):** Displays the values of the filter along the range of a slider. Only a single value can be selected at a time. This option is useful for dimensions that have an implicit order such as dates.

- **Multiple Values (Custom List):** Displays a text box where you can type a few characters and search for the value. 

- **Wildcard Match:** Displays a text box where you can type a few characters. All values that match those characters are automatically selected. 
 

We are going to select the Multiple Values(Dropdown)


<img src="imgs/filter16.png"  width = "85%" alt="404 image" />

<br>
<br>


### Filter All Sheets 


### Plots as filters 



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

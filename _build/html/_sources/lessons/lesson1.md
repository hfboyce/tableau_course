#  Visualization Importance

## Why do we Visualize? 

When you are trying to make sense of data that you have, you can present it in multiples ways. You can communicate the insights and the statistics you obtained using tables, numbers or words but sometimes the most effective way to relay your discoveries in an efficient and effective way through data visualization. 


Data visualization is representing these statistics and insights using the positions, lengths, and colours of different shapes and lines. 

<img src="imgs/shapes.png"  width = "100%" alt="404 image" />

We usually visualize our data to either:

1) Solve a problem by answering a question (we will look into these types of questions later in this course)

2) Explore our data to discover new questions that we may have 


Let's take a look at an example and experience exactly **how** visualizations are sometimes more effective.       
(Source: Joel Ostblom - [Data Visualization](https://viz-learn.mds.ubc.ca/en/module1) derived from [Francis Anscombe](https://en.wikipedia.org/wiki/Anscombe%27s_quartet))


Look at the four sets of numbers. 

We have X and Y values for 4 sets of numbers labelled A through D. 

<table border="1" style="width:40%; float:center; margin-right:40px">
<thead style="text-align: center">
  <col>
  <colgroup span="4"></colgroup>
  <colgroup span="4"></colgroup>
  <tr>
    <th colspan="2" scope="colgroup" style="width: 25%; text-align:center">A</th>
    <th colspan="2" scope="colgroup" style="width: 25%; text-align:center">B</th>
    <th colspan="2" scope="colgroup" style="width: 25%; text-align:center">C</th>
    <th colspan="2" scope="colgroup" style="width: 25%; text-align:center">D</th>
  </tr>
  <tr>
    <th scope="col" style="width: 12.5%; text-align:center">X</th>
    <th scope="col" style="width: 12.5%; text-align:center">Y</th>
    <th scope="col" style="width: 12.5%; text-align:center">X</th>
    <th scope="col" style="width: 12.5%; text-align:center">Y</th>
    <th scope="col" style="width: 12.5%; text-align:center">X</th>
    <th scope="col" style="width: 12.5%; text-align:center">Y</th>
    <th scope="col" style="width: 12.5%; text-align:center">X</th>
    <th scope="col" style="width: 12.5%; text-align:center">Y</th>
  </tr>
  <tr>
    <td>10</td>
    <td>8.04</td>
    <td>10</td>
    <td>9.14</td>
    <td>10</td>
    <td>7.46</td>
    <td>8</td>
    <td>6.58</td>
  </tr>
  <tr>
    <td>8</td>
    <td>6.95</td>
    <td>8</td>
    <td>8.14</td>
    <td>8</td>
    <td>6.77</td>
    <td>8</td>
    <td>5.76</td>
  </tr>

  <tr>
    <td>13</td>
    <td>7.58</td>
    <td>13</td>
    <td>8.74</td>
    <td>13</td>
    <td>12.74</td>
    <td>8</td>
    <td>7.71</td>
  </tr>

  <tr>
    <td>9</td>
    <td>8.81</td>
    <td>9</td>
    <td>8.77</td>
    <td>9</td>
    <td>7.11</td>
    <td>8</td>
    <td>8.84</td>
  </tr>

  <tr>
    <td>11</td>
    <td>8.33</td>
    <td>11</td>
    <td>9.26</td>
    <td>11</td>
    <td>7.81</td>
    <td>8</td>
    <td>8.47</td>
  </tr>

  <tr>
    <td>14</td>
    <td>9/96</td>
    <td>14</td>
    <td>8.10</td>
    <td>14</td>
    <td>8.84</td>
    <td>8</td>
    <td>7.04</td>
  </tr>

  <tr>
    <td>6</td>
    <td>7.24</td>
    <td>6</td>
    <td>6.14</td>
    <td>6</td>
    <td>6.08</td>
    <td>8</td>
    <td>5.25</td>
  </tr>

 <tr>
    <td>4</td>
    <td>4.26</td>
    <td>4</td>
    <td>3.10</td>
    <td>4</td>
    <td>5.39</td>
    <td>19</td>
    <td>12.50</td>
  </tr>

 <tr>
    <td>12</td>
    <td>10.84</td>
    <td>12</td>
    <td>9.13</td>
    <td>12</td>
    <td>8.15</td>
    <td>8</td>
    <td>5.56</td>
  </tr>

 <tr>
    <td>7</td>
    <td>4.81</td>
    <td>7</td>
    <td>7.26</td>
    <td>7</td>
    <td>6.43</td>
    <td>8</td>
    <td>7.91</td>
  </tr>

 <tr>
    <td>5</td>
    <td>5.68</td>
    <td>5</td>
    <td>4.74</td>
    <td>5</td>
    <td>5.73</td>
    <td>8</td>
    <td>6.89</td>
  </tr>
</table>

<br>

How is easy is it for us to find any trends, similarities or contrasts from these four sets?

Can you see the differences in the general trends between these four sets of numbers?

We can use some calculations or more formally called summary statistics to help shed some light on the data and compare and contrast between the 4 sets.
 
 Summary statistics can be calculations such as the mean, median, standard deviation, maximum and minimum values or even the range. 

These can help give some idea as we can see here for our 4 sets. 


<table border="1" style="width:55%; float:center; margin-right:40px">
<thead style="text-align: center">
  <col>
  <colgroup span="4"></colgroup>
  <colgroup span="4"></colgroup>
  <tr>
    <th colspan="3" scope="colgroup" style="width: 25%; text-align:center">A</th>
    <th colspan="3" scope="colgroup" style="width: 25%; text-align:center">B</th>
    <th colspan="3" scope="colgroup" style="width: 25%; text-align:center">C</th>
    <th colspan="3" scope="colgroup" style="width: 25%; text-align:center">D</th>
  </tr>
  <tr>
    <th scope="col" style="width: 9%; text-align:center"></th>
    <th scope="col" style="width: 8%; text-align:center">Y</th>
    <th scope="col" style="width: 8%; text-align:center">X</th>
    <th scope="col" style="width: 9%; text-align:center"></th>
    <th scope="col" style="width: 8%; text-align:center">X</th>
    <th scope="col" style="width: 8%; text-align:center">Y</th>
    <th scope="col" style="width: 9%; text-align:center"></th>
    <th scope="col" style="width: 8%; text-align:center">X</th>
    <th scope="col" style="width: 8%; text-align:center">Y</th>
    <th scope="col" style="width: 9%; text-align:center"></th>
    <th scope="col" style="width: 8%; text-align:center">X</th>
    <th scope="col" style="width: 8%; text-align:center">Y</th>
  </tr>
  <tr>
<th scope="row">mean</th>
    <td>9.00</td>
    <td>7.5</td>
<th scope="row">mean</th>
    <td>9.00</td>
    <td>7.5</td>
<th scope="row">mean</th>
    <td>9.00</td>
    <td>7.5</td>
<th scope="row">mean</th>
    <td>9.00</td>
    <td>7.5</td>
  </tr>
  <tr>
<th scope="row">std</th>
    <td>3.32</td>
    <td>2.03</td>
<th scope="row">std</th>
    <td>3.32</td>
    <td>2.03</td>
<th scope="row">std</th>
    <td>3.32</td>
    <td>2.03</td>
<th scope="row">std</th>
    <td>3.32</td>
    <td>2.03</td> 
  </tr>
</table>

<br>


They tell us in this case that they all share the same mean and standard deviation to 2 decimal places. That means the sets all has the same center and spread among the points. 

That being said, using 2 measures for all our data points, doesn't give us the full story about the data and fails to show us exactly how these 4 sets differ. 

If we plotted the sets, we would get the following visualizations. 

<img src="imgs/sets.png"  width = "100%" alt="404 image" />

So although they do share similar means, and standard deviations, we can clearly see that they are vastly different from one another. 

Another great illustration to drive home our point is the graphic below from <a href="https://www.autodesk.com/research/publications/same-stats-different-graphs" target="_blank">
Matejka and Fitzmaurice, 2017</a>. 

![](https://blog.revolutionanalytics.com/downloads/DataSaurus%20Dozen.gif)

This shows multiple datasets with similar means and standard deviations to 2 decimals places but are quite different in appearance when visualized. 

The moral of the story here is although statistics and calculation can help describe our data, a visualization sometimes really is worth a thousand words here. 

This is why it's so important to use visualizations to effectively communicate our data insights. 


## Why Good Data Visualization is so Important 

Sometimes it's best to actually experience a case where analysis improvements occurred to really solidify the effect of good visualizations. Using a case study from the course [Data Visualization](https://viz-learn.mds.ubc.ca/en/module2) that I co-developed and its source from [here](https://www.cs.ubc.ca/~tmm/courses/547-19/slides/borkin-artery-subset-slides.pdf), let's experience a real occurrence, where changing the visualizations resulted in concrete analysis improvements. 


Heart disease is a range of conditions that affect your heart including blood vessel disease and Heart rhythm problems. It is known as the leading cause of death globally with an estimated 17.9 million people dying from it in 2019 [(source)](https://www.who.int/news-room/fact-sheets/detail/cardiovascular-diseases-(cvds)),

ESS (Which stands for Endothelial Shear Stress) measures the tangential stress due to the friction of the flowing blood on the endothelial surface of the arterial wall. Long story short, low ESS is associated with plaque progression and if doctors can detect regions in the arteries where ESS is low, they can diagnose the patient and take actions early on which improves the patient's chance of survival. 

The regular way of evaluating ESS is using a digital 3D representation of the arteries using blue-red-and green colouring. 
- Blue indicates areas that could be problematic as ESS is lower here. 
- Red indicates areas where ESS is higher and not as concerning. 

<img src="imgs/heart1.png"  width = "80%" alt="404 image" />


Using this visualization, doctors were able to identify the areas of concern 39% of the time. 

Researchers then went off to see how changes to this visualization affected identification rates.

Researchers changed the colour to something more interpretable. It's important to note that colourblindness affects many individuals particularly the specific red-green colour blindness. Not only that but it's not always completely clear what values are the ones doctors should be particularly concerned with. The researchers adapted the colours so that low ESS stands out more, and highlighted the area with a red colour, and the rest are in black and white.

<img src="imgs/heart21.png"  width = "80%" alt="404 image" />

With this small modification, doctors were then able to identify the areas of low ESS much better than before and the average identification rate increased to 71%!


Following the change of colour, researchers then changed the number of dimensions that the arteries and blood vessels were shown in. 

Researchers then converted the 3D representations of the vessels to 2D. We will talk more about the problems of 3D later on, but generally, it's difficult for our human brains to assess and a 2D view can be more straightforward to understand. 


<img src="imgs/heart3.png"  width = "80%" alt="404 image" />


This definitely was the case for the doctors as the 2D representation changed the ESS identification rates from 71% to 91%. 

This goes to show how important colour and dimensionality are to effective visualization and thus your analysis. 

<br> 
<br> 

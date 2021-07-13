# Choropleths, Formatting and Dashboard Extra's

## Making a Choropleth Map

Let's try to create another map but this time let's try and answer how many trees there are in each Vancouver neighbourhood. We can visualize this by using a choropleth map. 

**Step by Step Instructions**

1\. Locate yourself to the spatial dataset that we connected to the Data Source  `local-area-boundary.geojson`.

<img src="imgs/choro1.png"  width = "85%" alt="404 image" />

<br>
<br>

2\. Drag the Geometry Dimension to the **Details** icon in our **Marks** card.

<img src="imgs/choro2.png"  width = "85%" alt="404 image" />

<br>
<br>

Right away, a map with all our neighbourhoods will be visible. Tableau is using `Latitude` and `Longitude` fields created from this `geojson` file to create a map this time.

<img src="imgs/choro3.png"  width = "85%" alt="404 image" />

<br>
<br>

3\. Now let's use our `street-trees` data to count the number of trees in each neighbourhood. From the **Data** tab, navigate yourself to the `street-trees` data source.

<img src="imgs/choro4.png"  width = "85%" alt="404 image" />

<br>
<br>

4\. Drag the `Tree Id` field to the colour icon in the **Marks** card so that we can use a colour channel to communicate the number of trees. 

<img src="imgs/choro5.png"  width = "85%" alt="404 image" />

<br>
<br>

```{Warning} 
This may generate a popup winder informing us that we need to add a relationship to our primary data source. 

<img src="imgs/choro6.png"  width = "85%" alt="404 image" />

<br>
<br>


We can blend the data sources now by clicking the chains next to the `Neighbourhood Name` field so that they turn red and now link the 2 sources. 

<img src="imgs/choro7.png"  width = "85%" alt="404 image" />

<br>
<br>

```


5\. Once the 2 sources are blended and there is a red chain icon next to our `Neighbourhood Name` field, we can convert the `Tree Id` field from our colour channel and convert it to a **Count Measure** by clicking it and selecting **Measure** followed by **Count** from the dropdown menu.

<img src="imgs/choro8.png"  width = "85%" alt="404 image" />

<br>
<br>

We are still not quite at a choropleth map; we need one more thing! 

<img src="imgs/choro9.png"  width = "85%" alt="404 image" />

<br>
<br>

6\. Drag the `Neighbourhood Name` field from the primary source (the source we did not use the latitude and longitude fiends to make the map from) to the **Details** field in the **Marks** card.

<img src="imgs/choro10.png"  width = "85%" alt="404 image" />

<br>
<br>

Ahhh! How we have a choropleth map! 

<img src="imgs/choro11.png"  width = "85%" alt="404 image" />


7\. If when we hover over the map, it shows us the number of trees in each neighbourhood!

<img src="imgs/choro13.png"  width = "85%" alt="404 image" />

<br>
<br>

Easy Peasy right?!

## Calculations Functions 

- lists 
- LOD ?

## Sets 


## Groups 


## Formatting title, Axis, Charts and Dashboard

- Gridlines
-Dashboard font
- Selectively highlight and annotate data with color and text
## Dashboard Extras
- Tooltip 
- Shapes
- Clicks and hovers  


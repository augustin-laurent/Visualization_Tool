# Visualization-Tool
The project that I'm currently working on for my internship in Cardiff University, you will find here every steps i've done.
I'll will use this README as a logbook.
## Explanation 
To conclude my Two-year university degree in technology (DUT) or HND if you prefer, in computing science and electronical, I need to do an internship of 3 Months.
The subject of the internship is to create a visualization tool to visualiaze data from [AIHabitat](https://aihabitat.org/) with D3.JS.
# Steps
## First
The first things I've done is too learn about ORBSlam Algorthim and how D3.JS work here is a link on a full course to understand this library : https://www.youtube.com/watch?v=_8V5o2UHG0E (Quit long but contain all the details).
## Second
I started to work on how I will set up 3 type of graphs with D3.JS, I needed to create a graph with parrallels coordinate.
* There are 3 different categorys for the moment :
	* Succes rate.
	* SPL.
		* $\frac{1}{N}\sum_{i=1}^N S_i\frac{l_i}{max(p_i,l_i)}$
		* Here is the formula to calculate the SPL.  
		* $l_i$ is the length between the start and the end of an episode.
		* $p_i$ is the length of path taken by the agent in an episode
		* $S_i$ is the binary of the succes in the episode.
	* Collision rate.
	
With this graph we can make some interactions, like sort, select and adjust the axes positions.
We can vizualise a specified episode with a flow chart and the trajectory on this episode.
## Third
After taking knowledge of what I've got to do I started by creating a virtual environnement in python to contain all the library.
Then as I got to work with Javascript to vizualise the date, I need to extract the data with Python and write them in a format compatible with Javascript so a webserver is required.
Flask is the choice here.
Currently I'm writing the code in Javascript so when I will get further i will update this.

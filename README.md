# Estimation of parameters of heating of a roof by solar energy.
![IMG_5562](https://user-images.githubusercontent.com/60693273/82786946-2904e800-9e6e-11ea-9ed7-dc08732474c2.JPG)
## What does our program do?

The system of estimation of parameters of a roof will allow the user to count the prospects of the location. Using the information on the average insolation and wind speed in a particular region and roof square, the program will provide the user with quantitative advice on the prospects of introducing this system of ventilation and heating of the room on his roof.

The result of the project was this web application, which is hosted on the address http://shepherdy.pythonanywhere.com/. Using which, the user with the help of three stages gets the information he needs. The user can get a map or report avout calculations of region power.

![Знімок екрана 2020-05-25 о 15 02 17](https://user-images.githubusercontent.com/60693273/82811479-895d4f00-9e99-11ea-872d-8cc96173c0cb.png)

![Знімок екрана 2020-05-25 о 15 09 15](https://user-images.githubusercontent.com/60693273/82811580-c3c6ec00-9e99-11ea-83ae-e33b26da0d51.png)

### What information does the user provide and receive?

The user must provide the following information:
- choose on the map of Ukraine the region in which his house is located;
- select the period for which the statistics interest him
- indicate the area of the roof facing south;
- on the diagram select the coefficient that depends on the angle of rotation to the south and the angle of the roof.

This program will provide the user with the following information (for the selected period):
- quantitative characteristics of solar energy that could be concentrated on its roof;
- information on the average wind speed;
- comparative aspects of the regions of Ukraine about the prospects of such a system;
- graphs of average wind speed in the regions of Ukraine.

More information about the project is available on the [Wiki](https://github.com/pastukh77/homework0/wiki) pages

## Required modules to install:
- pip install bs4
- pip install urllib
- pip install seaborn
- pip install matplotlib
- pip install flask
- pip install folium
- pip install json

## Modules:

* soup.py - module that uses bs4 (BeautifulSoup) to scrape data (monthly level of insolation) from internet resource, pandas seaborn, matplotlib to vizualize data;
* wind.py - module that uses pandas to get data from wind_Ukraine.tsv file. Also seborn and matplotlib to vizualize;
* adt.py - module for realizing Region, RegionPower ADT. Makes main calculations, creates representing for str and html;
* main.py - main module to draw a map using folium;
* flask_app.py - module to realize GET and POST methods, redirecting, using flask;
* menu.html - web page for taking all data from user and post it to flas_app.py;
* my_map.html - map, that creates using folium;
* result.html - web page for getting analysis.


The class diagram can be seen [here](https://github.com/pastukh77/homework0/blob/master/ADT_diagram.jpg)

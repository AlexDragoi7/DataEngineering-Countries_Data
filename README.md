##Extract-Transform-Load (ETL) project - Data Engineering

ETL project based on web-scraped data from Worldometer website.

The dataset contains:
- All countries in the world and their respective continents (Australia and Pacific based islands are included in Oceania)
- Population (from 2024)
- Land Area
- Population Density
- Land Area per Capita

*Data was extracted and transformed accordingly - e.g. Population / land area data was cleared of commas or dashes, while being correctly formatted (float, int).

**The entire Jupyter notebook is available as a html file in the project files.

Technologies used:
- Jupyter Notebook
- Python 
- PostgreSQL + SQL (to be added)
- SQLAlchemy (engine)
- Seaborn / Matplotlib - data visualizations (to be added)
- Cronjob (if necessary)


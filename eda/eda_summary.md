## Gather Data + EDA for Final Project

### Description of Datasets and Why Chosen
I am using a combination of two public datasets: 
1) World Development Indicators from World Bank Group 
 
The World Development Indicators dataset is "a comprehensive collection of global development data, providing key economic, social, and environmental statistics. It includes almost 1,500 indicators covering more than 200 countries and territories, with data spanning several decades." — World Development Indicators, Data Catalog, World Bank Group. The World Bank Group is an international financial institution that works to reduce poverty and support economic development around the world. The structure of the dataset is one row per country-indicator pair where an indicator is some variable that helps measure a country's development. Each row should have a value for that country-indicator pair from 1960 - 2024. This dataset is relevant because it can help discover what factors actually have an impact on a country's happiness which will help me in my goal of predicting country happiness scores.

2) World Happiness Report from kaggle 

The World Happiness Report is a dataset that ranks between 150-160 countries by happiness score which is calculated through a combination of various indicators of happiness. It contains data for 2015-2019, covering factors such as family, life expectency, etc for the countries available in the report. The data comes from The Sustainable Development Solutions Network (SDSN), which is a global initiative launched by the United Nations to support and promote practical solutions for sustainable development. The structure of the dataset is one row per country, and each row has a happiness score as well as the values of the indicators used to calculate happiness scores. This dataset is relevant because it provides the target signal to help train my model when combined with the world development indicators per country. It also gives me some domain knowledge on which world development indicators will likely make good features.


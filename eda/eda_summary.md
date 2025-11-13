## Gather Data + EDA for Final Project

### Description of Datasets and Why Chosen
I am using a combination of two public datasets: 
1) World Development Indicators from World Bank Group 
 
The World Development Indicators (WDI) dataset is "a comprehensive collection of global development data, providing key economic, social, and environmental statistics. It includes almost 1,500 indicators covering more than 200 countries and territories, with data spanning several decades." — World Development Indicators, Data Catalog, World Bank Group. The World Bank Group is an international financial institution that works to reduce poverty and support economic development around the world. The structure of the dataset is one row per country-indicator pair where an indicator is some variable that helps measure a country's development. Each row should have a value for that country-indicator pair from 1960 - 2024. This dataset is relevant because it can help discover what factors actually have an impact on a country's happiness which will help me in my goal of predicting country happiness scores.

2) World Happiness Report from kaggle 

The World Happiness Report (WHR) is a dataset that ranks between 150-160 countries by happiness score which is calculated through a combination of various indicators of happiness. It contains data for 2015-2019, covering factors such as family, life expectency, etc for the countries available in the report. The data comes from The Sustainable Development Solutions Network (SDSN), which is a global initiative launched by the United Nations to support and promote practical solutions for sustainable development. The structure of the dataset is one row per country, and each row has a happiness score as well as the values of the indicators used to calculate happiness scores. This dataset is relevant because it provides the target signal to help train my model when combined with the world development indicators per country. It also gives me some domain knowledge on which world development indicators will likely make good features.

### Learnings from EDA
#### Key Variables
The key variables are the indicators from the WDI and the Happiness Scores from WHR. Specific indicators I expect to be key are those that thematically overlap with those in the WHR such as ones relating to family, GDP, life expectancy, etc. To know which indicators will actually be key, I will need to perform feature importance analysis.
#### Data Volume
The WDI contains data for 266 countries and 1516 unique indicators. This means there are 403,256 rows. Each row contains a spot for the indicator value for the years 1960-2024 regardless of missingness. The WHR is split up into datasets for each year from 2015-2019. The number of countries (one row exists per country) varies from around 155-165 countries per dataset. There are 29 countries that do not appear in all 5 datasets, 170 countries total across all 5 datasets, and 151 countries that appear in all datasets.
#### Missingness
World Happiness Report:

![missingness](./visuals/whr_missingness.PNG)

This missingness is not fully accurate because some columns refer to the same variable with different names. After some cleaning, this level of missingness should decrease. The level of missingness for this dataset is not very relevant to my work because I am only using it for country happiness scores across the years.

World Development Indicators:

![missingness](./visuals/wdi_missingness.PNG)

I only checked the missingness of WDI for the years 2015-2019 because those are the years I have target signal for. There are over 100 indicators that have little missingness. This number is inflated by indicators that are one indicator split into sections (i.e. population by age group and sex split into multiple indicators).
#### Potential Signals
Target Signals:

The target signal is very clearly the happiness score. My goal is predicting happiness scores for countries so it makes sense to use that value as my target signal.

Interaction Signals:

Although feature importance analysis will need to validate the actual interaction signals, I am expecting the indicators from WDI that vary most with happiness scores are the ones that overlap in concept with the indicators from the WHR. For example, the WHR has an indicator that represents a score for GDP, so I expect to see WDI indicators containing "GDP" in the indicator name varying with happiness score.

![correlation](./visuals/correlation.PNG)

Combining happiness scores and indicators from WDI, I filtered to only data from 2015 as a start. I interpolated values that were missing for 2015 using a range of + or - 5 years. From that data, the above indicators were found to correlate most with happiness score. Some of them, such as life expectancy, I was expecting to see. My hypothesis was correct to some extent in expecting to see factors used in calculating happiness scores to show up as highly correlated with happiness. It is interesting to see an indicator about refugees being so highly correlated, but this makes sense from domain knowledge. It makes sense that countries with refugees would be happier because they would not be mandated to take in refugees if their population was not already taken care of to a high extent.
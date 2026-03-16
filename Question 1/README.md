# Q1 Analysis – Milestone II

## Overview
This script begins the analysis for Question 1 of our term project: examining whether provinces with higher job vacancy rates vote differently for certain political parties.

The program reads two datasets:
1. Job vacancy rates by province/territory
2. Federal election vote percentages by political party and province

The user provides the name of a political party as a command-line parameter, and the program extracts the vote percentages for that party across all provinces.


## What Has Been Completed

**1. Pre-processing step**
* Filtering both files and making sure that the Province names match in both files 

**2. Reading Command-Line Input**
* The program accepts a political party name as input when the script is executed.

**3. Loading the Job Vacancy Dataset**
* The CSV file containing job vacancy rates is read using `csv.DictReader`.
* Province names and vacancy rates are extracted and stored in a dictionary (`job_vacancy`).
* Vacancy rates are converted from strings to floating-point numbers.

**4. Loading the Election Results Dataset**
* The election results CSV file is read using `csv.DictReader`.
* The program identifies the row corresponding to the selected political party.
* Vote percentages for each province are extracted and stored in a dictionary (`vote_percentages`).

**5. Data Encoding**
* Numeric values from both datasets are converted to floats to allow future analysis.

These steps successfully prepare the two datasets for comparison.


## Next Steps
The following tasks will be implemented next:

**1. Combine the Datasets**
* Match provinces between the job vacancy dataset and the election results dataset.

**2. Produce Combined Output**
* Display the job vacancy rate and vote percentage for each province.

**3. Data Analysis / Visualization**
* Create a visualization (likely a scatter plot) to analyze the relationship between job vacancy rates and vote percentages for the selected political party.

This will allow us to investigate whether provinces with higher job vacancy rates tend to vote differently for certain political parties.


## How to Run the Script

Run the script from the command line with the desired political party as a parameter.

Example:
python3 q1_analysis.py "Liberal Party of Canada"


## Note, Question 2: 

We have not yet started on Question 2's coding, we will do it for milestone II 
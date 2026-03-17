#!/usr/bin/env python3

'''
question1.py
  Author(s): Hafsa Ahmed [1396772], Marcus Le [1385741], Avraj Pannu [1376060]


  Project: Milestone 3
  Date of Last Update: Mar 17, 2026.

  Functional Summary
    This script compares job vacancy rates across Canadian provinces with the vote share of a 
    specified political party in the 43rd Canadian federal election. It reads two CSV files:
    * "job_vacancy.csv" – job vacancy rates by province/territory. 
    * "election_results.csv" – vote share by party for each province/territory.
    The program loads and cleans the data, then compares the job vacancy rates with 
    the vote share of the specified political party across provinces.

     Commandline Parameters:
     Political Party
        

     References:
        * Elections Canada (2022): "Voting Results for the 43rd General Election",
            https://www.elections.ca/content.aspx?section=res&dir=rec/eval/pes2019/vtsa&document=index&lang=e
        * Government of Canada (2022): "43rd General Election:
            Official Voting Results", Record ID:
            https://open.canada.ca/data/en/dataset/199e5070-2fd5-49d3-aa21-aece08964d18/resource/12df72de-795e-44c4-8e94-fa86b6708ca5
'''


import csv
import sys
import matplotlib.pyplot as plt # for the graph


"""
Function #1: Load vacancy data (Data source #1):
    This function reads job vacancy data from a CSV file and stores it in a dictionary

Parameter(s): 
    - filename: A path to the CSV file that contains job vacancy data

Return(s): 
    dict, a dictionary where:
    - key = province/territory name
    - value = job vacancy rate
""" 
def load_job_vacancy(filename):
    job_vacancy = {}

    # Open the CSV file (with UTF-8 encoding to handle special characters)
    with open(filename, newline='', encoding="utf-8-sig") as file:
        # Reads CSV as dictionaries 
        reader = csv.DictReader(file)

        # Loop through each row in the CSV file
        for row in reader:
            # Extract the province name & vacancy rate from row
            province = row["Province/territory"]
            # Convert vacancy rate to float for numerical comparison and plotting
            vacancy = float(row["Job_Vacancy_Rate_Q2_2021"]) 

            # Store in the dictionary created
            job_vacancy[province] = vacancy

    return job_vacancy



"""
Function #2: Load election results (Data source #2)
    Reads election results from a CSV file & extracts vote percentages 
    for a specific political party

Parameter(s):
    - filename: A path to the CSV file that contains election results
    - political_party: Name of the political party 

Return(s):
    dict, a dictionary where:
    - key = province/territory name
    - value = Vote percentage for the selected party
"""
def load_vote_percentages(filename, political_party):
    vote_percentages = {}

    # Open the CSV file (with UTF-8 encoding to handle special characters)
    with open(filename, newline='', encoding="utf-8-sig") as file:
        # Reads CSV as dictionaries 
        reader = csv.DictReader(file)

        # Loop through each row in the file to find the selected political party
        for row in reader:
            # Allow case-insensitive matching for user input
            if political_party.lower() in row["Political Party"].lower():
                # Loop through all the columns in the row
                for province in row:
                    # Skip the political party column since it's not a province
                    if province != "Political Party":
                        # Store vote percentage for each province 
                        vote_percentages[province] = float(row[province])

    return vote_percentages



"""
Function #3: Compare data (Data source #1 + Data source #2)
    Compares job vacancy rates with vote percentages across provinces and
    visualizes the data using a scatter plot 

Parameter(s):
    - job_vacancy: Match each province/territory to its job vacancy rate
    - vote_percentages: Maps each province/territory to the selected party
    - political_party: Name of the selected political party's vote share

Return(s):
    - None
"""
def compare_data(job_vacancy, vote_percentages, political_party):
    # Print a clear & descriptive title header for the table
    print("Province | Job Vacancy Rate (%) | Vote %")
    print("----------------------------------------")

    # Lists to store data for the graph
    vacancy_rates = []
    vote_rates = []
    provinces = []

    # Loop through provinces in the vote data
    for province in vote_percentages:
        # Only compare if the province exists in both datasets
        if province in job_vacancy:

            vacancy = job_vacancy[province]
            vote = vote_percentages[province]

            # Print separators for a formatted row comparison
            print(province, "|", vacancy, "|", vote)

            # Store values for the graph 
            vacancy_rates.append(vacancy)
            vote_rates.append(vote)
            provinces.append(province)

    # Create a scatter plot to visualize the relationship of the data results
    plt.scatter(vacancy_rates, vote_rates, color="green")

    plt.title(f"Job Vacancy Rate vs Vote % for {political_party}") # Add a title to the graph
    plt.xlabel("Job Vacancy Rate (%)", color="maroon") # Add an x axis label
    plt.ylabel("Vote %", color="maroon") # Add an y axis label 
    plt.grid() # Add a grid
    plt.show() # Display the plot 



"""
Function #4: Main Function
    Entry point of the program. Validates command-line input, loads both datasets,
    and coordinates the comparison and visualization of results.
"""
def main():
    # Check that the user provided a political party as a command-line argument & error handle if needed
    if len(sys.argv) < 2: 
        print("usage: python question1.py 'Political Party Name'")
        sys.exit(1)

    # Get political party from command line
    political_party = sys.argv[1]

    # Load both datasets
    job_vacancy = load_job_vacancy("data/job_vacancy.csv")
    vote_percentages = load_vote_percentages("data/election_results.csv", political_party)

    # Compare and visualize the data
    compare_data(job_vacancy, vote_percentages, political_party)

if __name__ == "__main__":
    main()
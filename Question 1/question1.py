#!/usr/bin/env python3

'''
question1.py
  Author(s): Hafsa Ahmed [1396772], Marcus Le [1385741], Avraj Pannu [1376060]


  Project: Milestone 3
  Date of Last Update: Mar 16, 2026.

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
        * Government of Canada (2022): "43th General Election:
            Official Voting Results", Record ID:
            https://open.canada.ca/data/en/dataset/199e5070-2fd5-49d3-aa21-aece08964d18/resource/12df72de-795e-44c4-8e94-fa86b6708ca5
'''

import csv
import sys

# Function #1: Load vacancy data (Data source #1)
def load_job_vacancy(filename):
    job_vacancy = {}

    with open(filename, newline='', encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        for row in reader:
            province = row["Province/territory"]
            vacancy = float(row["Job_Vacancy_Rate_Q2_2021"])

            job_vacancy[province] = vacancy

    return job_vacancy



# Function #2: Load election results (Data source #2)
def load_vote_percentages(filename, political_party):
    vote_percentages = {}

    with open(filename, newline='', encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if political_party.lower() in row["Political Party"].lower():
                for province in row:
                    if province != "Political Party":
                        vote_percentages[province] = float(row[province])

    return vote_percentages



# Function #3: Compare data (Data source #1 + Data source #2)
def compare_data(job_vacancy, vote_percentages, political_party):
    print("Province | Job Vacancy Rate (%) | Vote %")
    print("----------------------------------------")

    vacancy_rates = []
    vote_rates = []
    provinces = []

    for province in vote_percentages:
        if province in job_vacancy:

            vacancy = job_vacancy[province]
            vote = vote_percentages[province]

            print(province, "|", vacancy, "|", vote)

            vacancy_rates.append(vacancy)
            vote_rates.append(vote)
            provinces.append(province)
        


# Function #4: Main function
def main():
    if len(sys.argv) < 2: 
        print("usage: python question1.py 'Political Party Name'")
        sys.exit(1)

    political_party = sys.argv[1]

    job_vacancy = load_job_vacancy("data/job_vacancy.csv")
    vote_percentages = load_vote_percentages("data/election_results.csv", political_party)

    compare_data(job_vacancy, vote_percentages, political_party)

if __name__ == "__main__":
    main()
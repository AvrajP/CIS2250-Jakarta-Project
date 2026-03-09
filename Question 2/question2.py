'''
question2.py
  Author(s): Hafsa Ahmed [1396772], Marcus Le [1385741], Avraj Pannu [1376060]


  Project: Milestone 3
  Date of Last Update: Mar 9, 2026.

  Functional Summary
        This script focuses on the 43rd Canadian federal election data.
        It reads two CSV files:
          * "43rd Election Age Groups.csv" – voter turnout percentages by age group
            and province/territory.
          * "43rd Election Turnout by Affiliation.csv" – vote share by party
            for each province/territory.
        After loading and cleaning the data, the program determines the winning
        party in each province, then merges the age‑group turnout information
        with the winning party.

     Commandline Parameters: none
        

     References:
        * Elections Canada (2022): "Voting Results for the 43rd General Election",
            https://www.elections.ca/content.aspx?section=res&dir=rec/eval/pes2019/vtsa&document=index&lang=e
        * Government of Canada (2022): "43th General Election:
            Official Voting Results", Record ID:
            https://open.canada.ca/data/en/dataset/199e5070-2fd5-49d3-aa21-aece08964d18/resource/12df72de-795e-44c4-8e94-fa86b6708ca5
'''


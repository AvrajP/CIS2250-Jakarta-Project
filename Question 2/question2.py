import csv
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
import matplotlib.pyplot as plt

def get_winning_party(filename):

    winning_parties = {}
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            headers = next(reader)
            provinces = headers[1:]
            
            max_votes = {prov: -1.0 for prov in provinces}
            winners = {prov: "" for prov in provinces}
            
            for row in reader:
                party_name = row[0]
                for i, prov in enumerate(provinces):
                    try:
                        vote_pct = float(row[i+1])
                        if vote_pct > max_votes[prov]:
                            max_votes[prov] = vote_pct
                            winners[prov] = party_name
                    except ValueError:
                        pass 
            for prov in provinces:
                winning_parties[prov] = winners[prov]
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        return None

    return winning_parties

def get_turnout_by_age(filename):
    turnout_data = {}
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            headers = next(reader)
            provinces = headers[1:]

            current_prov = None 
            for row in reader:
                if not row or len(row) < 5:
                    continue

                prov_col = row [0].strip()
                if prov_col:
                    current_prov = prov_col
                    if current_prov not in turnout_data:
                        turnout_data[current_prov] = []
                
                age_group = row[1].strip()
                turnout_pct_str = row[4].strip()
                
                if current_prov and age_group and turnout_pct_str:
                    try:
                        turnout_pct = float(turnout_pct_str)

                        turnout_data[current_prov].append((age_group, turnout_pct))
                    except ValueError:
                        pass 
                        
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        return None
    return turnout_data

def main():
    affiliation_file = "43rd Election Turnout by Affiliation.csv"
    age_groups_file = "43rd Election Age Groups.csv"

    winning_parties = get_winning_party(affiliation_file)
    turnout_data = get_turnout_by_age(age_groups_file)

    if not winning_parties or not turnout_data:
        print("Failed to load necessary data. Exiting.")
        return
    
    valid_provinces = list(winning_parties.keys())

    while True:
        prov = input(f"\nEnter a province/territory abbreviation ({', '.join(valid_provinces)}) or 'q' to quit: ").strip().upper()
        
        if prov == 'Q':
            break
            
        if prov not in valid_provinces:
            print(f"Invalid province abbreviation. Please enter one of: {', '.join(valid_provinces)}")
            continue
            
        if prov not in turnout_data:
            print(f"No turnout data found for province {prov}.")
            continue

        winning_party = winning_parties[prov]
        prov_turnout = turnout_data[prov]
        
        print(f"\n--- Results for {prov} ---")
        print(f"Winning Party: {winning_party}")
        print("Voter Turnout by Age Group:")
        
        ages = []
        turnouts = []



if __name__ == "__main__":
    main()


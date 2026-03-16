import csv
import sys
'''
question2.py
  Author(s): Hafsa Ahmed [1396772], Marcus Le [1385741], Avraj Pannu [1376060]


  Project: Milestone 3
  Date of Last Update: Mar 16, 2026.

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

     Commandline Parameters: Province
        

     References:
        * Elections Canada (2022): "Voting Results for the 43rd General Election",
            https://www.elections.ca/content.aspx?section=res&dir=rec/eval/pes2019/vtsa&document=index&lang=e
        * Government of Canada (2022): "43th General Election:
            Official Voting Results", Record ID:
            https://open.canada.ca/data/en/dataset/199e5070-2fd5-49d3-aa21-aece08964d18/resource/12df72de-795e-44c4-8e94-fa86b6708ca5
'''
import matplotlib.pyplot as plt

# function #1: Get winning party for each province
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

#function #2: Get voter turnout by age group for each province
def get_turnout_by_age(filename):
    turnout_data = {}
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            headers = next(reader)
            provinces = headers[1:]

            current_prov = None 
            total_votes = {}
            
            # calculates total amount of votes for each province
            for row in reader: 
                if not row or len(row) < 5:
                    continue

                prov_col = row [0].strip()
                if prov_col:
                    current_prov = prov_col
                    if current_prov not in turnout_data:
                        turnout_data[current_prov] = []
                
                
                votes_cast = int(row[3].strip().replace(',', ''))

                if current_prov not in total_votes:
                    total_votes[current_prov] = 0

                total_votes[current_prov] += votes_cast
            
            # resets file pointer to beginning to calculate turnout percentages
            f.seek(0)
            next(reader)

            # calculates turnout percentage for each age group in each province
            for row in reader:
                if not row or len(row) < 5:
                    continue

                prov_col = row [0].strip()
                if prov_col:
                    current_prov = prov_col
                    if current_prov not in turnout_data:
                        turnout_data[current_prov] = []
                
                age_group = row[1].strip()
                votes_cast = int(row[3].strip().replace(',', ''))

                if current_prov and age_group and votes_cast:
                    try:
                        turnout_pct = (votes_cast / total_votes[current_prov]) * 100

                        turnout_data[current_prov].append((age_group, turnout_pct))
                    except ValueError:
                        pass 
                        
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        return None
    return turnout_data

#function #3: Main function to run the program
def main(argv):
    if len(argv) != 2:
        print("Usage: question2.py <province_abbreviation>")
        sys.exit(1)
        
    affiliation_file = "43rd Election Turnout by Affiliation.csv"
    age_groups_file = "43rd Election Age Groups.csv"

    winning_parties = get_winning_party(affiliation_file)
    turnout_data = get_turnout_by_age(age_groups_file)

    if not winning_parties or not turnout_data:
        print("Failed to load necessary data. Exiting.")
        return
    
    valid_provinces = list(winning_parties.keys())

    prov = argv[1].strip().upper()
        
    if prov not in valid_provinces:
        print(f"Invalid province abbreviation. Please enter one of: {', '.join(valid_provinces)}")
        
    if prov not in turnout_data:
        print(f"No turnout data found for province {prov}.")

    winning_party = winning_parties[prov]
    prov_turnout = turnout_data[prov]
    
    print(f"\n--- Results for {prov} ---")
    print(f"Winning Party: {winning_party}")
    print("Voter Turnout by Age Group:")
    
    ages = []
    turnouts = []
    # prints the turnout percentages for each age group in the specified province
    for age_group, turnout_pct in prov_turnout:
        print(f"  {age_group}: {turnout_pct:.2f}%")
        ages.append(age_group)
        turnouts.append(turnout_pct)

    # Plotting the bar chart using matplotlib
    plt.bar(ages, turnouts, color='deepskyblue')
    plt.xlabel('Age Group', color='maroon')
    plt.ylabel('Voter Turnout (%)', color='maroon')
    plt.title(f'Voter Turnout by Age Group in {prov} (Winning Party: {winning_party})')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main(sys.argv)


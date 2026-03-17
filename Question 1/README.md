# Q1 Analysis – Milestone III

## Description
This program analyzes the relationship between job vacancy rates and voting patterns across Canadian provinces in the 43rd federal election.

The script uses two datasets:
- `job_vacancy.csv`: Contains job vacancy rates by province/territory 
- `election_results.csv`: Contains vote percentages for political parties across provinces for the 44th

The user provides a political party as a command-line argument, then the program:
- Loads and processes both datasets using `csv.DictReader`
- Extracts vote percentages for the selected political party
- Matches provinces between both datasets
- Prints a formatted comparison table showing:
  - Province
  - Job vacancy rate (%)
  - Vote percentage (%)
- Generates a scatter plot using `matplotlib` to visualize the relationship

This allows users to explore whether provinces with higher job vacancy rates tend to vote differently for a specific political party.

---


## Limitations
- **Strict column names:** The program depends on exact column names in the CSV files (e.g.,        `"Province/territory"` and `"Job_Vacancy_Rate_Q2_2021"`).
- **Ignored data:** Provinces that are not present in both datasets are ignored
- **Single dataset:** The analysis only considers Q2 2021 job vacancy data and the 43rd federal election, so it does not reflect trends over time.
- **Basic visualization:** The scatter plot does not label provinces or include advanced styling.

---


## How to Run the Program
Execute the program from the command line:
    python3 question1.py "Political Party Name"

Example:
    python3 question1.py "Conservative"
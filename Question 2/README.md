# Q2 Analysis – Milestone III

## Description
This program analyzes the relationship between the pecercentage of votes by age group and the winning party of a selected province/territory.

The script uses two datasets:
- `43rd Election Age Groups.csv`: Contains voter turnout data by geography and age group
- `43rd Election Turnout by Affiliation.csv`: Contains vote percentages for political parties across provinces for the 43rd election

The user provides a province/territory as a command-line argument, then the program:
- Loads and processes both datasets using `csv.reader`
- Calculates the winning party for each province
- Calculates the percentage of votes each age group consists.
- Matches provinces between both datasets
- Prints a formatted comparison table showing:
  - Winning party of selected province
  - Age groups (x to y years)
  - Vote percentage (%)
- Generates a bar chart using `matplotlib` to visualize the relationship

This allows users to explore whether provinces with higher/lower turnouts voter turnouts from specific age groups rates tend to vote differently for a specific political party.

---


## Limitations
- **Strict input format:** The program relies on exact CSV structure and column positions.
- **Province abbreviation dependency:** The user must input a valid province/territory abbreviation exactly as it appears in the dataset or the program will not return results.
- **Single dataset:** The analysis is limited to the 43rd federal election and does not account for trends across multiple elections or years.
- **Basic visualization:** The bar chart uses basic formatting and does not include advanced features such as comparisons across provinces or interactive elements.

---


## How to Run the Program
Execute the program from the command line:
    python3 question2.py "Province/Territory 2 letter abbreviation"

Example:
    python3 question2.py "NL"
# Election_Analysis
Overview of the Project
to complete election audit for a congressional election using Python, Visual Studio Code, and Git.
To write a Python script for 
- total number of votes cast
- A complete list of candidates who received votes
- Total number of votes each candidate receives
- Percentage of votes each candidate won
- The winner of the election based on popular vote
Election-Audit Results:
1. How many votes were cast in this congressional election?
- There were 369,711 votes
# Initialize a total vote counter
total_votes = 0
for row in reader:
# Add to the total vote count
total_votes = total_votes + 1
2. Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
- County Votes:
    Jefferson: 38,855 (10.5%)
    Denver: 306,055 (82.8%)
    Arapahoe: 24,801 (6.7%)
3. Which county had the largest number of votes?
- County with largest votes: Denver
4. Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
- Charles Casper Stockham: 85,213 (23.0%)
- Diana DeGette: 272,892 (73.8%)
- Raymon Anthony Doane: 11,606 (3.1%)
5. Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
- Winner: Diana DeGette
- Winner vote count: 272,892
- Winner percentage of total votes: 73.8%

winning_candidate_summary = (
f"-------------------------\n"
f"Winner: {winning_candidate}\n"
f"Winning Vote Count: {winning_count:,}\n"
f"Winning Percentage: {winning_percentage:.1f}%\n"


To the election commission:
This code could be used for other election by
1. creating an election list and election votes dictionary
2. Then use a 'for' loop to get the election name and election votes


we should save election data with specific .csv name:

file_to_load = os.path.join("Resources", "**election_results.csv**")
Election_results file should have an identifier to differentiate the file each time

Also, the output should be with specific identifier
file_to_save = os.path.join("analysis", "**election_analysis.txt**")
# Election Analysis
Python project

## Overview of Election Audit

We are assisting Tom, Colorado board of election employee to perform an Audit of the tabulated results for U.S.  congressional precinct in Colorado.

The totals and percentage of votes corresponding to all candidates and winner will be reported, reviewing the data from various voting methods as Mail-in ballot, punch cards and direct recording electronic.

At the end, the vote count report will certify the results of this u.s congressional race. 

## Election-Audit Results

### • 369,711 votes were cast in this congressional election.

### • The total votes per county were:

‣ Jefferson: 38,855 votes with 10.5%

‣ Denver: 306,055 votes with 82.8%

‣ Arapahoe: 24,801 votes with 6.7%

    # 6a: Write a repetition statement to get the county from the county dictionary.
    for county_name in county_votes:
        # 6b: Retrieve the county vote count.
        CountysVotes = county_votes.get(county_name)
        # 6c: Calculate the percent of total votes for the county.
        CountysVote_percentage = float(CountysVotes) / float(total_CountysVotes) * 100
        counties_results = (
            f"{county_name}: {CountysVote_percentage:.1f}% ({CountysVotes:,})\n")

         # 6d: Print the county results to the terminal.
        print(counties_results)

### • Denver has the largest number of votes, with 82.8%

### • Votes per candidate

‣ Charles Casper Stockham: 23.0% - 85,213 votes

‣ Diana DeGette: 73.8% - 272,892 votes

‣ Raymon Anthony Doane: 3.1% - 11,606 votes

    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)

### • Election winner
    ‣ Diana DeGette 
      272,892 votes
      73.8%

            
## Election-Audit Summary


The audit of the tabulated results for the U.S. congressional precinct in Colorado worked successfully by reviewing the data set coming from the different voting methods and providing detailed votes counts per candidate and counties. The report certified the mentioned results of the U.S Congressional race.

This script can easily be modified to be used for other elections audit processes. It automates the analysis process and provides a detailed report of the results by going through the whole data set and extract from the same date. These results can be analyzed from different perspectives.

### Examples

- The path of the CSV can be modified to analyze a different dataset.
- Variables can be modified according to the new dataset data
- Changing the printing statements to be relevant and precise to the new election process. 



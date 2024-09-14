'''Module: Rueckert Analytics - Data Interpretations
This module provides a simple, reusable foundation for my analytics projects. 
'''

import statistics

has_international_clients: bool = True
years_in_operation: int = 6
skills_offered: list = ["GitHub", "RStudio", "Python"]
client_satisfaction_scores: list = [4.7, 4.8, 4.8, 5.0, 4.9]
client_ages: list = [34, 42, 53, 67, 98]

# Calculate basic statistics using built-in functions and the statistics module
min_score: float = min(client_satisfaction_scores)
max_score: float = max(client_satisfaction_scores)
mean_score: float = statistics.mean(client_satisfaction_scores)
stdev_score: float = statistics.stdev(client_satisfaction_scores)
min_age: float = min(client_ages)
max_age: float = max(client_ages)
mean_age: float = statistics.mean(client_ages)
stdev_age: float = statistics.stdev(client_ages)

byline: str = f"""
----------------------------------------------------------
Rueckert Analytics: Data Interpretations
----------------------------------------------------------
Has International Clients:                        {has_international_clients}
Years in Operation:                               {years_in_operation}
Skills Offered:                                   {skills_offered}
Client Satisfaction Scores:                       {client_satisfaction_scores}
Minimum Client Satisfaction Score:                {min_score}
Maximum Client Satisfaction Score:                {max_score}
Mean Client Satisfaction Score:                   {mean_score}
Standard Deviation of Client Satisfaction Scores: {stdev_score}
Minimum Client Age:                               {min_age}
Maximum Client Age:                               {max_age}
Mean Client Age:                                  {mean_age}
Standard Deviation of Client Ages:                {stdev_age}
"""

def get_byline() -> str:
   '''Return a byline for my analytics projects.'''
   return byline

def main() -> None:
   '''Print the byline to the console when this function is called.'''
   print(get_byline())

if __name__ == '__main__':
    main()

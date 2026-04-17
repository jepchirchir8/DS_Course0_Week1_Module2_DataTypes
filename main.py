# CodeGrade step0

# Run this cell without changes

import pandas as pd
import sqlite3

# Create the connection
# Note the connect is 'conn1' since there will be multiple .db used
conn1 = sqlite3.connect('DS_Course1_Week1_Module2_SQLQueries/planets.db')

# Select all
pd.read_sql("""SELECT * FROM planets; """, conn1)

# CodeGrade step1
# Replace None with your code
df_no_moons = pd.read_sql("""
SELECT * FROM planets
                          WHERE num_of_moons =0
""",conn1)
df_no_moons

# CodeGrade step2
# Replace None with your code
df_name_seven = pd.read_sql("""
SELECT name, mass
                            FROM planets
                            WHERE LENGTH(name)=7
""",conn1)
df_name_seven

# CodeGrade step3
# Replace None with your code
df_mass = pd.read_sql("""
SELECT name,mass
                      FROM planets
                      WHERE mass <=1.00

""",conn1)
df_mass

# CodeGrade step4
# Replace None with your code
df_mass_moon = pd.read_sql("""
SELECT * FROM planets
                           WHERE num_of_moons >=1 AND mass < 1.00
""",conn1)
df_mass_moon

# CodeGrade step5
# Replace None with your code
df_blue = pd.read_sql("""
SELECT name, color
                      FROM planets
                      WHERE color LIKE '%blue%';
""",conn1)
df_blue

# CodeGrade step0

# Run this cell without changes

# Create a connection
# Note the connect is 'conn2' since they will be multiple .db used
conn2 = sqlite3.connect('DS_Course1_Week1_Module2_SQLQueries/dogs.db')

# Select all
pd.read_sql("SELECT * FROM dogs;", conn2)

# CodeGrade step6
df_hungry = pd.read_sql("""
SELECT name, age, breed
FROM dogs
WHERE hungry = 1
ORDER BY id ASC
""", conn2)

# CodeGrade step7
# Replace None with your code
df_hungry_ages = pd.read_sql("""
SELECT name, age, hungry
                             FROM dogs
                             WHERE hungry == 1 and age BETWEEN 2 AND 7
                             ORDER BY name ASC
""",conn2)
df_hungry_ages

## CodeGrade step8
df_4_oldest = pd.read_sql("""
SELECT name, age, breed
FROM dogs
ORDER BY age DESC, id DESC
LIMIT 4
""", conn2)
# CodeGrade step0

# Run this cell without changes

# Create a connection
# Note the connect is 'conn3' since they will be multiple .db used
conn3 = sqlite3.connect('DS_Course1_Week1_Module2_SQLQueries/babe_ruth.db')

# Select all
pd.read_sql("""
SELECT * FROM babe_ruth_stats; """, conn3)

# CodeGrade step9
# Replace None with your code
df_ruth_years = pd.read_sql("""
SELECT  COUNT(year) AS total_no_of_years
                            FROM babe_ruth_stats
""", conn3)
df_ruth_years

# CodeGrade step10
# Replace None with your code
df_hr_total = pd.read_sql("""
SELECT  SUM(HR) AS total_no_of_homeruns
                            FROM babe_ruth_stats
""", conn3)
df_hr_total

# CodeGrade step11
# Replace None with your code
df_teams_years = pd.read_sql("""
SELECT  team , COUNT(year) AS number_years
                            FROM babe_ruth_stats
                             GROUP BY team
                             
""", conn3)
df_teams_years

# CodeGrade step12
# Replace None with your code
df_at_bats = pd.read_sql("""
SELECT team , AVG(at_bats) AS average_at_bats
                        FROM babe_ruth_stats
                         GROUP BY team
                         HAVING average_at_bats >200 
""",conn3)
df_at_bats

# Run this cell without changes

conn1.close()
conn2.close()
conn3.close()
Netflix Data Analysis & Business Intelligence ProjectAuspify Data Analysis Internship ProjectAuthor: Muhammad Shaheer Nawaz
Repository: Auspify-Data-Analysis-Internship
Tools & Tech: Python, Pandas, Matplotlib, Seaborn, Git, VS Code
📌 Executive Summary
This repository contains an end-to-end exploratory data analysis (EDA) and data visualization suite conducted on the Netflix Movies and TV Shows dataset ($8,790$ records). The project cleans raw metadata, evaluates global distribution metrics, tracks production timeline trends, analyzes content maturity ratings, and synthesizes key business insights into executive dashboard visualizations.
🛠 Project Structure & Key FilesE:\Auspify_Internship\Task_1_Netflix_Data_Cleaning\
│
├── Dataset.csv                       # Raw Netflix Dataset
├── cleaned_netflix_dataset.csv       # Cleaned & Processed Dataset
│
├── clean_data.py                     # Task 1: Data Cleaning Script
├── content_type_analysis.py          # Task 2: Content Type Script
├── country_analysis.py               # Task 3: Country Analysis Script
├── trend_analysis.py                 # Task 4: Release Trend Script
├── rating_genre_analysis.py          # Task 5: Rating & Genre Script
├── business_insights_report.py       # Task 6: BI Dashboard Script
│
├── content_type_dashboard.png        # Task 2 Dashboard Output
├── country_content_analysis.png      # Task 3 Visualization Output
├── yearly_trend_analysis.png         # Task 4 Visualization Output
├── rating_genre_dashboard.png        # Task 5 Dashboard Output
└── executive_business_dashboard.png  # Task 6 Executive BI Dashboard
📋 Task Breakdown & Key FindingsTask 1:
 Data Cleaning & PreparationScript: clean_data.pyOutput: cleaned_netflix_dataset.csvKey Actions: Stripped leading/trailing whitespaces across string features (type, country, rating, title, director), converted date_added into standardized datetime64 objects, and handled missing values across $8,790$ total content entries.
 Task 2: 
 Content Type Analysis DashboardScript: content_type_analysis.pyVisualization: content_type_dashboard.pngKey Findings:Movies: $6,126$ titles ($69.7\%$)TV Shows: $2,664$ titles ($30.3\%$)Movies dominate Netflix's library, accounting for over two-thirds of all available catalog items.
 Task 3: 
 Country-Wise Content DistributionScript: country_analysis.pyVisualization: country_content_analysis.pngTop Production Hubs:United States: $3,240$ titlesIndia: $1,057$ titlesUnited Kingdom: $638$ titlesPakistan: $421$ titlesCanada: $271$ 
 titlesTask 4: Production Trend Analysis (2000–2021)Script: 
 trend_analysis.pyVisualization: yearly_trend_analysis.pngKey Findings:Movie additions peaked in 2018 ($767$ titles released).TV Show additions peaked in 2020 ($436$ titles released).Rapid content library expansion occurred between $2015$ and $2019$.
 Task 5: Content Rating & Genre AnalysisScript: 
 rating_genre_analysis.pyVisualization: rating_genre_dashboard.pngKey Findings:Top Rating: TV-MA ($3,205$ titles) followed by TV-14 ($2,157$ titles), confirming Netflix's focus on mature and teen audiences.Top Genres: International Movies ($2,752$), Dramas ($2,426$), and Comedies ($1,674$).
 Task 6: Executive Business Intelligence DashboardScript: 
 business_insights_report.pyVisualization: executive_business_dashboard.pngStrategic Takeaways:Capital Allocation: Shift production budget toward multi-season original TV series to maximize user retention.Regional Expansion: Expand local original content production hubs across emerging Asian and European markets.Audience Broadening: Develop high-quality family/kids (TV-Y7, PG) programming to boost multi-user household subscriptions.🚀 How to Run LocallyClone the Repository:git clone https://github.com/nawazshaheer66-ui/Auspify-Data-Analysis-Internship.git
cd Auspify-Data-Analysis-Internship
Install Required Packages:pip install pandas matplotlib seaborn
Execute Any Task Script:python clean_data.py
python content_type_analysis.py
python country_analysis.py
python trend_analysis.py
python rating_genre_analysis.py
python business_insights_report.py

import pandas as pd
import random
# Generate random data helpers
def random_choice(options, size):
    return [random.choice(options) for _ in range(size)]

def random_int_range(start, end, size):
    return [random.randint(start, end) for _ in range(size)]

def random_float_range(start, end, size, decimals=2):
    return [round(random.uniform(start, end), decimals) for _ in range(size)]
num_entries = 200
# Fake dataset for startups
startups = pd.DataFrame({
    "Startup ID": range(1, num_entries + 1),
    "Name": [f"Startup_{i}" for i in range(1, num_entries + 1)],
    "Industry": random_choice(["AI","Fintech","HealthTech","EdTech","AgriTech","E-commerce","CleanTech","Renewable Energy","Logistics","FoodTech","Biotech","TravelTech","Gaming","Property Technology","SaaS","MediaTech","RetailTech","Cybersecurity","IoT","Robotics"], num_entries),
    "Stage": random_choice(["Pre Seed", "Seed", "Series A", "Series B", "Series C"], num_entries),
    "Funding Required": random_int_range(50000, 2000000, num_entries),
    "Target Audience": random_choice(["B2B", "B2C", "B2G", "D2C"], num_entries),
    "Location": random_choice(["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh","Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka","Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram","Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana","Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"], num_entries),
    "Preferred Entity": random_choice(["Investor", "Incubator"], num_entries),
    "Revenue": random_int_range(10000, 500000, num_entries),
    "Team Size": random_int_range(2, 50, num_entries),
    "Pitch Deck": [f"https://pitchdeck.com/{i}" for i in range(1, num_entries + 1)]
})
# Fake dataset for incubators
incubators = pd.DataFrame({
    "Incubator ID": range(1, num_entries + 1),
    "Name": [f"Incubator_{i}" for i in range(1, num_entries + 1)],
    "Sector Focus": random_choice(["AI","Fintech","HealthTech","EdTech","AgriTech","E-commerce","CleanTech","Renewable Energy","Logistics","FoodTech","Biotech","TravelTech","Gaming","Property Technology","SaaS","MediaTech","RetailTech","Cybersecurity","IoT","Robotics"], num_entries),
    "Services": random_choice(["Mentoring", "Funding Support", "Workspace", "Networking"], num_entries),
    "Location": random_choice(["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh","Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka","Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram","Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana","Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"], num_entries),
    "Mentor Availability": random_choice(["Yes", "No"], num_entries),
    "Partnerships": random_int_range(1, 20, num_entries),
    "Funding Support": random_choice(["Yes", "No"], num_entries),
    "Funds Available": random_choice(["Fund of Funds for Startups (FFS)","SIDBI Make in India Loan for Enterprises (SMILE)","Credit Guarantee Scheme for Startups (CGSS)","Startup India Seed Fund Scheme (SISFS)","Atal Innovation Mission (AIM)","National Initiative for Developing and Harnessing Innovations (NIDHI)","Electronics Development Fund (EDF)","Support for International Patent Protection in Electronics and Information Technology (SIP-EIT)","Multisectoral Support for Entrepreneurs (MUDRA Yojana)","ASPIRE - A Scheme for Promotion of Innovation, Rural Industries, and Entrepreneurship","Pradhan Mantri Kaushal Vikas Yojana (PMKVY)","Digital India Initiative Support","Stand-Up India Scheme","National Skill Development Initiative","Technology Development Programme (TDP)"], num_entries)
})
# Fake dataset for investors
investors = pd.DataFrame({
    "Investor ID": range(1, num_entries + 1),
    "Name": [f"Investor_{i}" for i in range(1, num_entries + 1)],
    "Preferred Sector": random_choice(["AI","Fintech","HealthTech","EdTech","AgriTech","E-commerce","CleanTech","Renewable Energy","Logistics","FoodTech","Biotech","TravelTech","Gaming","Property Technology","SaaS","MediaTech","RetailTech","Cybersecurity","IoT","Robotics"], num_entries),
    "Minimum Investment": random_int_range(10000, 50000, num_entries),
    "Maximum Investment": random_int_range(50000, 500000, num_entries),
    "Stage Focus": random_choice(["Seed", "Series A", "Series B", "Series C"], num_entries),
    "Location": random_choice(["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh","Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka","Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram","Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana","Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"], num_entries),
    "Portfolio Size": random_int_range(5, 50, num_entries),
    "Active Investments": random_int_range(1, 30, num_entries)
})
# Save datasets to CSV files
startups.to_csv("startups.csv", index=False)
incubators.to_csv("incubators.csv", index=False)
investors.to_csv("investors.csv", index=False)
# Display the first few rows of each dataset
print("Startups:")
print(startups.head())
print("\nIncubators:")
print(incubators.head())
print("\nInvestors:")
print(investors.head())
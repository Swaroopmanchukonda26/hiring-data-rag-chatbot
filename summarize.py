import pandas as pd

df = pd.read_csv("layoffs.csv")

top_company = df.groupby("company")["total_laid_off"].sum().idxmax()
top_company_total = df.groupby("company")["total_laid_off"].sum().max()
total_layoffs = df["total_laid_off"].sum()
top_industry = df.groupby("industry")["total_laid_off"].sum().idxmax()

with open("real_data.txt", "w") as f:
    f.write(f"The company with the highest total layoffs is {top_company}, with {int(top_company_total)} employees laid off.\n")
    f.write(f"The total number of layoffs across all companies in this dataset is {int(total_layoffs)}.\n")
    f.write(f"The industry with the highest total layoffs is {top_industry}.\n")

print("Done! Check real_data.txt")
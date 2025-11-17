# UC Berkeley Admissions Analysis — Team Beta

![Python](https://img.shields.io/badge/python-v3.12+-blue.svg) ![License](https://img.shields.io/badge/license-MIT-green.svg)

## Project Overview
This repository analyzes the UC Berkeley 1973 graduate admissions dataset to demonstrate Simpson's Paradox: aggregate gender bias can appear even when department‑level analysis shows no systematic discrimination. The analysis includes exploratory data analysis, statistical testing, and logistic regression models.

## Team
- Rachel Anita Sibale 
- Jimmy Edward Matewere 

## Key Findings
- Overall: Males had a higher admission rate (≈44% vs 35%).  
- By Department: No consistent bias against women when controlling for department.  
- Root cause: Women applied disproportionately to more competitive departments, producing the aggregate effect. These departments, based on speculation could be highly STEM related as is a common trend seen in most university applications.

## Dataset
- Source: UC Berkeley Graduate Admissions (1973)  - [berkely.csv](https://waf.cs.illinois.edu/discovery/berkeley.csv)
- Size: 4,526 applications  
- Variables: Year, Major, Sex, Admission Status  
- Departments: A, B, C, D, E, F, Other

## Technologies
- Python 3.8+  
- pandas, numpy, matplotlib, seaborn  
- scikit-learn (LogisticRegression)  
- SciPy (stats)

## Quick Start / Installation
```bash
# Clone repository
git clone https://github.com/Jimmy-JayJay/berkeley-admissions-analysis.git
cd berkeley-admissions-analysis

# (Windows)
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Launch Jupyter
jupyter notebook
```

## Project Structure
- data/              — Raw data downloaded from: [berkely.csv](https://waf.cs.illinois.edu/discovery/berkeley.csv)
- notebooks/         — Jupyter notebooks for the analysis  
- src/               — Helper modules (data loading, modeling)  
- outputs/           — Figures and reports  


## Notebooks (recommended order)
1. 01_exploratory_analysis.ipynb  
2. 02_statistical_testing.ipynb  
3. 03_logistic_regression.ipynb  
4. 04_simpsons_paradox_visualization.ipynb


## Results Summary

Logistic regression (example results shown in notebooks):

- Naive model (Gender only): Coef ≈ +0.61 → Odds Ratio ≈ 1.84 (males more likely)  
- Full model (Gender + Dept): Coef ≈ -0.10 → Odds Ratio ≈ 0.91 (effect reverses/attenuates)

Statistical tests:
- Overall chi-square: p < 0.001 (significant)  
- Department-level chi-squares: mixed — no systematic female disadvantage

## Visuals
Generated figure: outputs/figures/simpsons_paradox_analysis.png

## Methodology
1. Data cleaning and encoding  
2. EDA: admission rates by gender and department  
3. Chi-square tests for independence  
4. Logistic regression (gender-only vs gender+department)  
5. Interpretation to demonstrate Simpson's Paradox

## References
- Bickel, P. J., Hammel, E. A., & O'Connell, J. W. (1975). "Sex Bias in Graduate Admissions: Data from Berkeley". Science, 187(4175), 398–404.  
- Pearl, J. (2014). "Understanding Simpson's Paradox". The American Statistician.

## Contacts

| Member | Linkedin | Email |
|-|-|-|
|Jimmy Edward Matewere | [Jimmy Matewere](https://www.linkedin.com/in/jimmy-matewere/) |jmatewere265@gmail.com|
|Rachel Anita Sibale| [Rachel Anita](https://www.linkedin.com/in/racheal-anita-sibale-136746208/)|



## License
MIT License

---

**Tags**: Simpson's Paradox, Logistic Regression, Data Science, Statistical Analysis, Bias Detection

-----

# Sales and Employee Performance Analysis

## Overview

This project is a data analysis and visualization script that simulates employee and sales data for a fictional company. It uses Python with `pandas` for data manipulation, `numpy` for numerical operations, and `seaborn`/`matplotlib` for creating a dashboard of key performance indicators.

The script performs the following main tasks:

1.  **Generates synthetic data** for a list of employees, including roles, salaries, and personal details.
2.  **Simulates a full year of sales data** for each salesperson, incorporating seasonality and individual performance factors.
3.  **Performs data analysis** to calculate key metrics.
4.  **Visualizes the results** in a 2x2 dashboard, providing insights into salary distribution, sales performance, and trends.

## Key Libraries

  * `pandas`
  * `numpy`
  * `matplotlib`
  * `seaborn`

## Data Simulation

Two primary DataFrames are created:

#### 1\. Employees DataFrame (`df_funcionarios`)

This DataFrame contains information about each employee:

  - `nome`: Employee's name
  - `data_nascimento`: Date of birth
  - `data_criacao`: Hire date
  - `salario`: Monthly salary
  - `cargo`: Job role (e.g., 'vendedor', 'rh', 'gerente')
  - `idade`: Calculated age

#### 2\. Sales DataFrame (`df_vendas`)

This DataFrame contains simulated monthly sales records for each salesperson (`vendedor`). The simulation logic includes:

  - **Seasonality**: Sales are boosted in November/December and reduced in January/February.
  - **Individual Performance**: Top-performing salespeople ('Ana', 'Elena') receive a bonus to their sales figures.
  - **Randomness**: Sales, region, and product data are randomized to create a diverse dataset.
  - **Calculated Fields**: A `comissao` (commission) column is calculated based on a percentage of sales.

## Visualizations

The script generates a dashboard with four key plots:

1.  **Average Salary by Job Role**: A bar plot showing the mean salary for each position within the company.
2.  **Total Sales by Salesperson**: A bar plot ranking salespeople by their total annual sales, identifying top performers.
3.  **Monthly Sales Evolution**: A line plot tracking total sales across all months, clearly showing seasonal peaks and dips.
4.  **Age vs. Salary Relationship**: A scatter plot that explores the relationship between employee age and salary, with data points colored by job role.

## Summary Statistics

After displaying the plots, the script prints key metrics to the console, including:

  - Total number of salespeople.
  - Total annual sales revenue.
  - Average monthly sales.
  - The name of the top-performing salesperson and their total sales.
  - The average salary across the company.

## How to Run

1.  Ensure you have all the required libraries installed: `pip install pandas numpy matplotlib seaborn`.
2.  Run the Python script.
3.  The dashboard with the four plots will be displayed, and the summary statistics will be printed to the console.
# 📊 Sales Data Analysis Project

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-2.0-150458?style=for-the-badge&logo=pandas)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.7-orange?style=for-the-badge)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter)

> A complete end-to-end Sales Data Analysis project using Python — analyzing revenue, profit, regional performance, product trends, and seasonal patterns from a real-world retail dataset.

---

## 📁 Project Structure

```
Sales-Data-Analysis/
│
├── 📓 notebooks/
│   └── Sales_Analysis.ipynb        # Main Jupyter Notebook (full analysis)
│
├── 📊 charts/
│   ├── sales_by_category.png       # Bar chart - category performance
│   ├── monthly_trend.png           # Line chart - seasonal trends
│   ├── top_products.png            # Horizontal bar - top 10 products
│   ├── region_pie.png              # Pie chart - region distribution
│   ├── profit_heatmap.png          # Heatmap - monthly profit
│   └── sales_vs_profit.png         # Scatter plot - sales vs profit
│
├── 📁 data/
│   └── superstore.csv              # Dataset (Kaggle Superstore)
│
├── 📄 reports/
│   └── Sales_Analysis_Report.xlsx  # Exported Excel summary report
│
├── sales_analysis.py               # Python script version (no Jupyter needed)
├── requirements.txt                # All dependencies
└── README.md                       # Project documentation
```

---

## 🎯 Project Objectives

| # | Business Question | Answered? |
|---|---|---|
| 1 | Which product sells the most? | ✅ |
| 2 | Which region generates the highest revenue? | ✅ |
| 3 | What are the seasonal sales trends? | ✅ |
| 4 | Which products/categories make losses? | ✅ |
| 5 | What is the monthly profit pattern? | ✅ |
| 6 | Which customer segment is most profitable? | ✅ |

---

## 📈 Key Findings

- 🏆 **Top Category:** Technology leads in total revenue
- 🌍 **Best Region:** West region contributes the highest sales
- 📅 **Peak Season:** November–December (Holiday season spike)
- ⚠️ **Loss Alert:** Furniture category has the lowest profit margins
- 👥 **Best Segment:** Corporate segment drives the most consistent revenue

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|---|---|
| **Python 3.10+** | Core programming language |
| **Pandas** | Data loading, cleaning, and analysis |
| **Matplotlib** | Chart and graph creation |
| **Seaborn** | Advanced data visualization |
| **OpenPyXL** | Excel report generation |
| **Jupyter Notebook** | Interactive analysis environment |

---

## 🚀 How to Run This Project

### Step 1 — Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/Sales-Data-Analysis.git
cd Sales-Data-Analysis
```

### Step 2 — Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3 — Add the Dataset
- Download the Superstore dataset from [Kaggle](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)
- Place the CSV file inside the `data/` folder
- Rename it to `superstore.csv`

### Step 4 — Run the Notebook
```bash
jupyter notebook notebooks/Sales_Analysis.ipynb
```

Or run the Python script directly:
```bash
python sales_analysis.py
```

---

## 📊 Sample Visualizations

### Monthly Sales Trend
> Line chart showing how sales fluctuate month-by-month across multiple years

### Sales by Category
> Bar chart comparing Technology, Furniture, and Office Supplies performance

### Top 10 Products
> Horizontal bar chart showing best-performing products by revenue

### Region Distribution
> Pie chart showing East, West, Central, South contribution to total sales

---

## 📂 Dataset Info

- **Source:** [Kaggle - Superstore Sales Dataset](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)
- **Rows:** ~9,994 records
- **Columns:** 21 features including Order Date, Region, Category, Sales, Profit, Discount

---

## 👤 About

**Project Type:** Data Analysis Portfolio Project  
**Skill Level:** Beginner–Intermediate  
**Domain:** Retail Sales Analytics  

---

## 📬 Connect

Feel free to fork this project, raise issues, or connect with me on LinkedIn!

---

*Made with ❤️ using Python and Jupyter Notebook*

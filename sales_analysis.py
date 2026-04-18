# =============================================================
#   SALES DATA ANALYSIS PROJECT
#   Author  : Your Name
#   Dataset : Kaggle Superstore Sales Dataset
#   Tools   : Python, Pandas, Matplotlib, Seaborn
# =============================================================

# ── STEP 1: Import Libraries ──────────────────────────────────
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import warnings
import os

warnings.filterwarnings('ignore')
sns.set_theme(style="whitegrid")

# Create output folders if they don't exist
os.makedirs('charts', exist_ok=True)
os.makedirs('reports', exist_ok=True)

print("=" * 55)
print("       SALES DATA ANALYSIS — STARTING")
print("=" * 55)


# ── STEP 2: Load Dataset ──────────────────────────────────────
print("\n[1] Loading dataset...")
df = pd.read_csv('data/superstore.csv', encoding='latin-1')
print(f"    ✅ Loaded {df.shape[0]:,} rows and {df.shape[1]} columns")


# ── STEP 3: Understand the Data ───────────────────────────────
print("\n[2] Dataset Overview:")
print(f"    Columns : {df.columns.tolist()}")
print(f"    Missing Values:\n{df.isnull().sum()[df.isnull().sum() > 0]}")


# ── STEP 4: Clean the Data ───────────────────────────────────
print("\n[3] Cleaning data...")

# Remove duplicates
before = len(df)
df = df.drop_duplicates()
print(f"    Removed {before - len(df)} duplicate rows")

# Convert date columns
df['Order Date']  = pd.to_datetime(df['Order Date'])
df['Ship Date']   = pd.to_datetime(df['Ship Date'])

# Extract time features
df['Year']       = df['Order Date'].dt.year
df['Month']      = df['Order Date'].dt.month
df['Month Name'] = df['Order Date'].dt.strftime('%b')
df['Quarter']    = df['Order Date'].dt.quarter

print("    ✅ Data cleaned and date columns extracted")


# ── STEP 5: Business Overview ─────────────────────────────────
print("\n[4] Business KPIs:")
print(f"    💰 Total Revenue  : ${df['Sales'].sum():>12,.2f}")
print(f"    📈 Total Profit   : ${df['Profit'].sum():>12,.2f}")
print(f"    📦 Total Orders   : {df['Order ID'].nunique():>12,}")
print(f"    🛒 Unique Products: {df['Product Name'].nunique():>12,}")
print(f"    👥 Customers      : {df['Customer Name'].nunique():>12,}")
print(f"    🌍 Regions        : {df['Region'].nunique():>12}")


# ── STEP 6: Analysis — Category ──────────────────────────────
print("\n[5] Sales by Category:")
category_sales = df.groupby('Category')[['Sales','Profit']].sum().sort_values('Sales', ascending=False)
print(category_sales.to_string())


# ── STEP 7: Analysis — Sub-Category ──────────────────────────
subcategory_sales = df.groupby('Sub-Category')[['Sales','Profit']].sum().sort_values('Sales', ascending=False)


# ── STEP 8: Analysis — Region ─────────────────────────────────
print("\n[6] Sales & Profit by Region:")
region_sales = df.groupby('Region')[['Sales','Profit']].sum().sort_values('Sales', ascending=False)
print(region_sales.to_string())


# ── STEP 9: Top 10 Products ───────────────────────────────────
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)


# ── STEP 10: Loss-Making Products ────────────────────────────
loss_products = df.groupby('Product Name')['Profit'].sum()
loss_products = loss_products[loss_products < 0].sort_values().head(10)
print("\n[7] Top 10 Loss-Making Products:")
print(loss_products.to_string())


# ── STEP 11: Monthly Trend ────────────────────────────────────
monthly_sales = df.groupby(['Year','Month','Month Name'])['Sales'].sum().reset_index()
monthly_profit = df.groupby(['Year','Month'])['Profit'].sum().reset_index()


# ══════════════════════════════════════════════════════════════
#   VISUALIZATIONS
# ══════════════════════════════════════════════════════════════
print("\n[8] Generating charts...")

COLORS = ['#2563EB','#16A34A','#DC2626','#D97706','#7C3AED']

# ── Chart 1: Sales by Category (Bar) ─────────────────────────
fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(category_sales.index, category_sales['Sales'], color=COLORS[:3], edgecolor='white', linewidth=1.5)
ax.set_title('Total Sales by Category', fontsize=15, fontweight='bold', pad=15)
ax.set_xlabel('Category', fontsize=11)
ax.set_ylabel('Sales ($)', fontsize=11)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'${x:,.0f}'))
for bar in bars:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2000,
            f'${bar.get_height():,.0f}', ha='center', va='bottom', fontsize=9, fontweight='bold')
plt.tight_layout()
plt.savefig('charts/sales_by_category.png', dpi=150, bbox_inches='tight')
plt.close()
print("    ✅ charts/sales_by_category.png")


# ── Chart 2: Monthly Sales Trend (Line) ──────────────────────
fig, ax = plt.subplots(figsize=(13, 5))
for i, year in enumerate(sorted(df['Year'].unique())):
    data = monthly_sales[monthly_sales['Year'] == year].sort_values('Month')
    ax.plot(data['Month'], data['Sales'], marker='o', linewidth=2.5,
            markersize=6, label=str(year), color=COLORS[i % len(COLORS)])
ax.set_title('Monthly Sales Trend by Year', fontsize=15, fontweight='bold', pad=15)
ax.set_xlabel('Month', fontsize=11)
ax.set_ylabel('Sales ($)', fontsize=11)
ax.set_xticks(range(1, 13))
ax.set_xticklabels(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'${x:,.0f}'))
ax.legend(title='Year')
plt.tight_layout()
plt.savefig('charts/monthly_trend.png', dpi=150, bbox_inches='tight')
plt.close()
print("    ✅ charts/monthly_trend.png")


# ── Chart 3: Top 10 Products (Horizontal Bar) ────────────────
fig, ax = plt.subplots(figsize=(10, 6))
top_products.sort_values().plot(kind='barh', ax=ax, color='#2563EB', edgecolor='white')
ax.set_title('Top 10 Products by Revenue', fontsize=15, fontweight='bold', pad=15)
ax.set_xlabel('Sales ($)', fontsize=11)
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'${x:,.0f}'))
plt.tight_layout()
plt.savefig('charts/top_products.png', dpi=150, bbox_inches='tight')
plt.close()
print("    ✅ charts/top_products.png")


# ── Chart 4: Region Pie Chart ────────────────────────────────
region_pie = df.groupby('Region')['Sales'].sum()
fig, ax = plt.subplots(figsize=(7, 7))
wedges, texts, autotexts = ax.pie(
    region_pie, labels=region_pie.index, autopct='%1.1f%%',
    colors=COLORS[:4], startangle=140,
    wedgeprops=dict(edgecolor='white', linewidth=2))
for at in autotexts:
    at.set_fontsize(11)
    at.set_fontweight('bold')
ax.set_title('Sales Distribution by Region', fontsize=15, fontweight='bold', pad=15)
plt.tight_layout()
plt.savefig('charts/region_pie.png', dpi=150, bbox_inches='tight')
plt.close()
print("    ✅ charts/region_pie.png")


# ── Chart 5: Sales vs Profit Scatter ─────────────────────────
fig, ax = plt.subplots(figsize=(9, 6))
categories = df['Category'].unique()
palette = {'Technology':'#2563EB', 'Furniture':'#DC2626', 'Office Supplies':'#16A34A'}
for cat in categories:
    subset = df[df['Category'] == cat]
    ax.scatter(subset['Sales'], subset['Profit'], alpha=0.5, s=25,
               label=cat, color=palette.get(cat, 'grey'))
ax.axhline(0, color='black', linewidth=1, linestyle='--', alpha=0.5)
ax.set_title('Sales vs Profit by Category', fontsize=15, fontweight='bold', pad=15)
ax.set_xlabel('Sales ($)', fontsize=11)
ax.set_ylabel('Profit ($)', fontsize=11)
ax.legend()
plt.tight_layout()
plt.savefig('charts/sales_vs_profit.png', dpi=150, bbox_inches='tight')
plt.close()
print("    ✅ charts/sales_vs_profit.png")


# ── Chart 6: Profit Heatmap by Month & Year ──────────────────
pivot = df.pivot_table(values='Profit', index='Year', columns='Month', aggfunc='sum')
pivot.columns = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
fig, ax = plt.subplots(figsize=(13, 4))
sns.heatmap(pivot, annot=True, fmt='.0f', cmap='RdYlGn', linewidths=0.5,
            ax=ax, cbar_kws={'label': 'Profit ($)'})
ax.set_title('Monthly Profit Heatmap (by Year)', fontsize=15, fontweight='bold', pad=15)
plt.tight_layout()
plt.savefig('charts/profit_heatmap.png', dpi=150, bbox_inches='tight')
plt.close()
print("    ✅ charts/profit_heatmap.png")


# ── Chart 7: Sub-Category Sales & Profit (Grouped Bar) ───────
fig, ax = plt.subplots(figsize=(13, 6))
x = range(len(subcategory_sales))
width = 0.4
ax.bar([i - width/2 for i in x], subcategory_sales['Sales'],   width=width, label='Sales',  color='#2563EB', alpha=0.85)
ax.bar([i + width/2 for i in x], subcategory_sales['Profit'],  width=width, label='Profit', color='#16A34A', alpha=0.85)
ax.set_xticks(list(x))
ax.set_xticklabels(subcategory_sales.index, rotation=45, ha='right')
ax.axhline(0, color='black', linewidth=0.8)
ax.set_title('Sales & Profit by Sub-Category', fontsize=15, fontweight='bold', pad=15)
ax.set_ylabel('Amount ($)', fontsize=11)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f'${v:,.0f}'))
ax.legend()
plt.tight_layout()
plt.savefig('charts/subcategory_comparison.png', dpi=150, bbox_inches='tight')
plt.close()
print("    ✅ charts/subcategory_comparison.png")


# ══════════════════════════════════════════════════════════════
#   EXPORT EXCEL REPORT
# ══════════════════════════════════════════════════════════════
print("\n[9] Exporting Excel report...")

with pd.ExcelWriter('reports/Sales_Analysis_Report.xlsx', engine='openpyxl') as writer:
    # Sheet 1 — Overview
    overview = pd.DataFrame({
        'Metric': ['Total Revenue', 'Total Profit', 'Total Orders', 'Unique Products', 'Total Customers'],
        'Value':  [f"${df['Sales'].sum():,.2f}", f"${df['Profit'].sum():,.2f}",
                   df['Order ID'].nunique(), df['Product Name'].nunique(), df['Customer Name'].nunique()]
    })
    overview.to_excel(writer, sheet_name='Overview', index=False)

    # Sheet 2 — Category Sales
    category_sales.to_excel(writer, sheet_name='Category Sales')

    # Sheet 3 — Sub-Category
    subcategory_sales.to_excel(writer, sheet_name='Sub-Category Sales')

    # Sheet 4 — Region
    region_sales.to_excel(writer, sheet_name='Region Sales')

    # Sheet 5 — Top Products
    top_products.to_excel(writer, sheet_name='Top 10 Products')

    # Sheet 6 — Loss Products
    loss_products.to_excel(writer, sheet_name='Loss Products')

    # Sheet 7 — Monthly Sales
    monthly_sales.to_excel(writer, sheet_name='Monthly Trend', index=False)

print("    ✅ reports/Sales_Analysis_Report.xlsx")

print("\n" + "=" * 55)
print("   ✅ ANALYSIS COMPLETE!")
print("   📊 7 charts saved in  → charts/")
print("   📄 Report saved in    → reports/")
print("=" * 55)

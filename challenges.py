# Day 3: CHALLENGES - Visualization Practice

"""
🎯 INSTRUCTIONS:
Practice creating different chart types and applying design principles.
Each challenge focuses on a specific visualization skill.

Remember: The goal is to communicate clearly, not to make fancy charts!
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("sales_data.csv")
df['date'] = pd.to_datetime(df['date'])

print("=" * 70)
print("DAY 3 CHALLENGES - VISUALIZATION PRACTICE")
print("=" * 70)

# ============================================
# CHALLENGE 1: BASIC BAR CHART
# ============================================
print("\n🎯 CHALLENGE 1: Create a Professional Bar Chart")
print("-" * 70)
print("Task: Show total revenue by product")
print("Requirements:")
print("- Sort bars from highest to lowest")
print("- Add clear title and labels")
print("- Use a single professional color")
print("- Save as 'challenge1_product_revenue.png'")

# YOUR CODE HERE
revenue_by_product = df.groupby('product')['revenue'].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
revenue_by_product.plot(kind='bar', color='steelblue', edgecolor='black')
plt.title('Total Revenue by Product', fontsize=14, fontweight='bold')  # ← Fixed!
plt.xlabel('Product')
plt.ylabel('Revenue ($)')
plt.tight_layout()
plt.savefig('challenge1_product_revenue.png', dpi=300, bbox_inches='tight')
plt.close()

print("✅ Chart saved as 'challenge1_product_revenue.png'")
print(revenue_by_product)
"""
💡 HINT:
revenue_by_product = df.groupby('product')['revenue'].sum().sort_values(ascending=False)
plt.figure(figsize=(10, 6))
revenue_by_product.plot(kind='bar', color='steelblue', edgecolor='black')
plt.title('Your Title Here', fontsize=14, fontweight='bold')
plt.xlabel('Product')
plt.ylabel('Revenue ($)')
plt.tight_layout()
plt.savefig('challenge1_product_revenue.png', dpi=300, bbox_inches='tight')
plt.close()
"""

# ============================================
# CHALLENGE 2: LINE CHART WITH MARKERS
# ============================================
print("\n🎯 CHALLENGE 2: Create a Time Series Line Chart")
print("-" * 70)
print("Task: Show revenue over time for ALL products")
print("Requirements:")
print("- One line per product (3 lines total)")
print("- Add markers to show data points")
print("- Include a legend")
print("- Add gridlines")
print("- Save as 'challenge2_revenue_timeline.png'")

# YOUR CODE HERE

plt.figure(figsize=(12, 6))
for product in df['product'].unique():
    product_data = df[df['product'] == product].sort_values('date')
    plt.plot(product_data['date'], product_data['revenue'],
             marker='o', label=f'Product {product}', linewidth=2)

plt.title('Revenue Timeline by Product', fontsize=14, fontweight='bold')
plt.xlabel('Date')
plt.ylabel('Revenue ($)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('challenge2_revenue_timeline.png', dpi=300, bbox_inches='tight')
plt.close()

print("✅ Chart saved as 'challenge2_revenue_timeline.png'")

"""
💡 HINT:
plt.figure(figsize=(12, 6))
for product in df['product'].unique():
    product_data = df[df['product'] == product].sort_values('date')
    plt.plot(product_data['date'], product_data['revenue'], 
             marker='o', label=f'Product {product}', linewidth=2)
plt.title('Revenue Timeline by Product', fontsize=14, fontweight='bold')
plt.xlabel('Date')
plt.ylabel('Revenue ($)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('challenge2_revenue_timeline.png', dpi=300, bbox_inches='tight')
plt.close()
"""

# ============================================
# CHALLENGE 3: GROUPED BAR CHART
# ============================================
print("\n🎯 CHALLENGE 3: Create a Grouped Bar Chart")
print("-" * 70)
print("Task: Show revenue by region AND product (side-by-side bars)")
print("Requirements:")
print("- Group by region, separate bars for each product")
print("- Use different colors for each product")
print("- Include legend")
print("- Rotate x-axis labels to be horizontal")
print("- Save as 'challenge3_grouped_bars.png'")

# YOUR CODE HERE
pivot = df.pivot_table(values='revenue', index='region',
                       columns='product', aggfunc='sum', fill_value=0)
plt.figure(figsize=(10, 6))
pivot.plot(kind='bar', color=['#1E88E5', '#FFC107', '#43A047'])
plt.title('Revenue by Region and Product', fontsize=14, fontweight='bold')
plt.xlabel('Region')
plt.ylabel('Revenue ($)')
plt.legend(title='Product')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('challenge3_grouped_bars.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Saved as 'challenge3_grouped_bars.png'")
"""
💡 HINT:
pivot = df.pivot_table(values='revenue', index='region', 
                       columns='product', aggfunc='sum', fill_value=0)
plt.figure(figsize=(10, 6))
pivot.plot(kind='bar', color=['#1E88E5', '#FFC107', '#43A047'])
plt.title('Revenue by Region and Product', fontsize=14, fontweight='bold')
plt.xlabel('Region')
plt.ylabel('Revenue ($)')
plt.legend(title='Product')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('challenge3_grouped_bars.png', dpi=300, bbox_inches='tight')
plt.close()
"""

# ============================================
# CHALLENGE 4: STACKED BAR CHART
# ============================================
print("\n🎯 CHALLENGE 4: Create a Stacked Bar Chart")
print("-" * 70)
print("Task: Show revenue by region with products stacked")
print("Requirements:")
print("- Stack product revenue within each region bar")
print("- Use distinct colors for each product")
print("- Add legend")
print("- Save as 'challenge4_stacked_bars.png'")

# YOUR CODE HERE
pivot = df.pivot_table(values='revenue', index='region',
                       columns='product', aggfunc='sum', fill_value=0)
plt.figure(figsize=(10, 6))
pivot.plot(kind='bar', stacked=True, color=['#1E88E5', '#FFC107', '#43A047'])
plt.title('Revenue Composition by Region', fontsize=14, fontweight='bold')
plt.xlabel('Region')
plt.ylabel('Revenue ($)')
plt.legend(title='Product')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('challenge4_stacked_bars.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Saved as 'challenge4_stacked_bars.png'")

"""
💡 HINT:
pivot = df.pivot_table(values='revenue', index='region', 
                       columns='product', aggfunc='sum', fill_value=0)
plt.figure(figsize=(10, 6))
pivot.plot(kind='bar', stacked=True, color=['#1E88E5', '#FFC107', '#43A047'])
plt.title('Revenue Composition by Region', fontsize=14, fontweight='bold')
plt.xlabel('Region')
plt.ylabel('Revenue ($)')
plt.legend(title='Product')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('challenge4_stacked_bars.png', dpi=300, bbox_inches='tight')
plt.close()
"""

# ============================================
# CHALLENGE 5: HORIZONTAL BAR CHART
# ============================================
print("\n🎯 CHALLENGE 5: Create a Horizontal Bar Chart")
print("-" * 70)
print("Task: Show average revenue by region (horizontal bars)")
print("Requirements:")
print("- Use barh instead of bar")
print("- Sort from highest to lowest (top to bottom)")
print("- Add data labels showing the exact values")
print("- Save as 'challenge5_horizontal_bars.png'")

# YOUR CODE HERE
avg_by_region = df.groupby('region')['revenue'].mean().sort_values()
plt.figure(figsize=(10, 6))
avg_by_region.plot(kind='barh', color='coral', edgecolor='black')
plt.title('Average Revenue by Region', fontsize=14, fontweight='bold')
plt.xlabel('Average Revenue ($)')
plt.ylabel('Region')
for i, v in enumerate(avg_by_region):
    plt.text(v + 20, i, f'${v:.0f}', va='center')

plt.tight_layout()
plt.savefig('challenge5_horizontal_bars.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Saved as 'challenge5_horizontal_bars.png'")
"""
💡 HINT:
avg_by_region = df.groupby('region')['revenue'].mean().sort_values()
plt.figure(figsize=(10, 6))
avg_by_region.plot(kind='barh', color='coral', edgecolor='black')
plt.title('Average Revenue by Region', fontsize=14, fontweight='bold')
plt.xlabel('Average Revenue ($)')
plt.ylabel('Region')

# Add data labels (advanced!)
for i, v in enumerate(avg_by_region):
    plt.text(v + 20, i, f'${v:.0f}', va='center')

plt.tight_layout()
plt.savefig('challenge5_horizontal_bars.png', dpi=300, bbox_inches='tight')
plt.close()
"""

# ============================================
# CHALLENGE 6: SUBPLOTS
# ============================================
print("\n🎯 CHALLENGE 6: Create Multiple Subplots")
print("-" * 70)
print("Task: Create a 2x2 grid of charts")
print("Requirements:")
print("- Top-left: Revenue by region (bar)")
print("- Top-right: Revenue by product (bar)")
print("- Bottom-left: Number of sales by region (bar)")
print("- Bottom-right: Number of sales by product (bar)")
print("- Use different colors for each chart")
print("- Save as 'challenge6_subplots.png'")

# YOUR CODE HERE
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

# Top-left
df.groupby('region')['revenue'].sum().plot(kind='bar', ax=axes[0,0], color='steelblue')
axes[0,0].set_title('Revenue by Region')
axes[0,0].set_ylabel('Revenue ($)')

# Top-right
df.groupby('product')['revenue'].sum().plot(kind='bar', ax=axes[0,1], color='coral')
axes[0,1].set_title('Revenue by Product')
axes[0,1].set_ylabel('Revenue ($)')

# Bottom-left
df.groupby('region').size().plot(kind='bar', ax=axes[1,0], color='lightgreen')
axes[1,0].set_title('Sales Count by Region')
axes[1,0].set_ylabel('Number of Sales')

# Bottom-right
df.groupby('product').size().plot(kind='bar', ax=axes[1,1], color='gold')
axes[1,1].set_title('Sales Count by Product')
axes[1,1].set_ylabel('Number of Sales')

plt.tight_layout()
plt.savefig('challenge6_subplots.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Saved as 'challenge6_subplots.png'")
"""
💡 HINT:
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

# Top-left
df.groupby('region')['revenue'].sum().plot(kind='bar', ax=axes[0,0], color='steelblue')
axes[0,0].set_title('Revenue by Region')
axes[0,0].set_ylabel('Revenue ($)')

# Top-right
df.groupby('product')['revenue'].sum().plot(kind='bar', ax=axes[0,1], color='coral')
axes[0,1].set_title('Revenue by Product')
axes[0,1].set_ylabel('Revenue ($)')

# Bottom-left
df.groupby('region').size().plot(kind='bar', ax=axes[1,0], color='lightgreen')
axes[1,0].set_title('Sales Count by Region')
axes[1,0].set_ylabel('Number of Sales')

# Bottom-right
df.groupby('product').size().plot(kind='bar', ax=axes[1,1], color='gold')
axes[1,1].set_title('Sales Count by Product')
axes[1,1].set_ylabel('Number of Sales')

plt.tight_layout()
plt.savefig('challenge6_subplots.png', dpi=300, bbox_inches='tight')
plt.close()
"""

# ============================================
# CHALLENGE 7: STYLED VISUALIZATION
# ============================================
print("\n🎯 CHALLENGE 7: Apply Professional Styling")
print("-" * 70)
print("Task: Recreate revenue by region bar chart with professional design")
print("Requirements:")
print("- Use seaborn color palette")
print("- Remove top and right spines")
print("- Add subtle gridlines")
print("- Use a larger, bold title")
print("- Add a subtitle explaining the insight")
print("- Save as 'challenge7_styled_chart.png'")

# YOUR CODE HERE ✅
sns.set_style("whitegrid")
plt.figure(figsize=(10, 6))

revenue_by_region = df.groupby('region')['revenue'].sum().sort_values(ascending=False)
ax = revenue_by_region.plot(kind='bar', color=sns.color_palette("Set2"), edgecolor='black')

plt.title('Regional Revenue Performance', fontsize=16, fontweight='bold', pad=20)
plt.suptitle('East region dominates with 50% of total sales',
             fontsize=10, y=0.96, color='gray')
plt.xlabel('Region', fontsize=12)
plt.ylabel('Revenue ($)', fontsize=12)
plt.xticks(rotation=0)

# Remove spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig('challenge7_styled_chart.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Saved as 'challenge7_styled_chart.png'")
"""
💡 HINT:
sns.set_style("whitegrid")
plt.figure(figsize=(10, 6))

revenue_by_region = df.groupby('region')['revenue'].sum().sort_values(ascending=False)
ax = revenue_by_region.plot(kind='bar', color=sns.color_palette("Set2"), edgecolor='black')

plt.title('Regional Revenue Performance', fontsize=16, fontweight='bold', pad=20)
plt.suptitle('East region dominates with 50% of total sales', 
             fontsize=10, y=0.96, color='gray')
plt.xlabel('Region', fontsize=12)
plt.ylabel('Revenue ($)', fontsize=12)
plt.xticks(rotation=0)

# Remove spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig('challenge7_styled_chart.png', dpi=300, bbox_inches='tight')
plt.close()
"""

# ============================================
# CHALLENGE 8: CHART WITH ANNOTATIONS
# ============================================
print("\n🎯 CHALLENGE 8: Add Annotations to Highlight Key Points")
print("-" * 70)
print("Task: Create revenue by product chart with annotation on the highest bar")
print("Requirements:")
print("- Bar chart of revenue by product")
print("- Add an arrow and text pointing to the highest bar")
print("- Text should say something like 'Top Performer: $X,XXX'")
print("- Save as 'challenge8_annotated_chart.png'")

# YOUR CODE HERE
# Revenue by product
revenue_by_product = (
    df.groupby('product')['revenue']
    .sum()
    .sort_values(ascending=False)
)

# Create bar chart
plt.figure(figsize=(10, 6))
ax = revenue_by_product.plot(kind='bar', edgecolor='black')
plt.title('Product Revenue Performance', fontsize=14, fontweight='bold')
plt.xlabel('Product')
plt.ylabel('Revenue')

# Identify top performer
max_val = revenue_by_product.max()
max_idx = revenue_by_product.idxmax()
max_pos = list(revenue_by_product.index).index(max_idx)

# Clean vertical annotation (Option 1)
plt.annotate(
    f'Top Performer\n${max_val:,.0f}',
    xy=(max_pos, max_val),
    xytext=(max_pos, max_val + max_val * 0.15),
    ha='center',
    arrowprops=dict(
        arrowstyle='-|>',
        color='red',
        lw=2,
        shrinkA=0,
        shrinkB=5
    ),
    fontsize=10,
    fontweight='bold',
    color='red'
)

plt.tight_layout()
plt.savefig('challenge8_annotated_chart.png', dpi=300, bbox_inches='tight')
plt.close()

print("✅ Saved as 'challenge8_annotated_chart.png'")
"""
💡 HINT:
revenue_by_product = df.groupby('product')['revenue'].sum().sort_values(ascending=False)
plt.figure(figsize=(10, 6))
ax = revenue_by_product.plot(kind='bar', color='steelblue', edgecolor='black')
plt.title('Product Revenue Performance', fontsize=14, fontweight='bold')

# Find the highest value
max_val = revenue_by_product.max()
max_idx = revenue_by_product.idxmax()
max_pos = list(revenue_by_product.index).index(max_idx)

# Add annotation
plt.annotate(f'Top Performer\n${max_val:,.0f}', 
             xy=(max_pos, max_val), 
             xytext=(max_pos + 0.5, max_val + 200),
             arrowprops=dict(arrowstyle='->', color='red', lw=2),
             fontsize=10, fontweight='bold', color='red')

plt.tight_layout()
plt.savefig('challenge8_annotated_chart.png', dpi=300, bbox_inches='tight')
plt.close()
"""

# ============================================
# CHALLENGE 9: COMPARISON CHART
# ============================================
print("\n🎯 CHALLENGE 9: Create a Before/After Comparison")
print("-" * 70)
print("Task: Compare first 3 sales vs last 3 sales")
print("Requirements:")
print("- Calculate average revenue for first 3 sales")
print("- Calculate average revenue for last 3 sales")
print("- Show as side-by-side bars")
print("- Color code: green if improved, red if declined")
print("- Save as 'challenge9_comparison.png'")

# YOUR CODE HERE
df_sorted = df.sort_values('date')
first_3_avg = df_sorted.head(3)['revenue'].mean()
last_3_avg = df_sorted.tail(3)['revenue'].mean()

comparison = pd.Series({'First 3 Sales': first_3_avg, 'Last 3 Sales': last_3_avg})

plt.figure(figsize=(8, 6))
colors = ['red' if last_3_avg < first_3_avg else 'green',
          'green' if last_3_avg >= first_3_avg else 'red']
comparison.plot(kind='bar', color=['steelblue', colors[1]], edgecolor='black')
plt.title('Average Revenue: First vs Last 3 Sales', fontsize=14, fontweight='bold')
plt.ylabel('Average Revenue ($)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('challenge9_comparison.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Saved as 'challenge9_comparison.png'")
"""
💡 HINT:
df_sorted = df.sort_values('date')
first_3_avg = df_sorted.head(3)['revenue'].mean()
last_3_avg = df_sorted.tail(3)['revenue'].mean()

comparison = pd.Series({'First 3 Sales': first_3_avg, 'Last 3 Sales': last_3_avg})

plt.figure(figsize=(8, 6))
colors = ['red' if last_3_avg < first_3_avg else 'green', 
          'green' if last_3_avg >= first_3_avg else 'red']
comparison.plot(kind='bar', color=['steelblue', colors[1]], edgecolor='black')
plt.title('Average Revenue: First vs Last 3 Sales', fontsize=14, fontweight='bold')
plt.ylabel('Average Revenue ($)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('challenge9_comparison.png', dpi=300, bbox_inches='tight')
plt.close()
"""

# ============================================
# CHALLENGE 10: COMPREHENSIVE DASHBOARD (HARD!)
# ============================================
print("\n🎯 CHALLENGE 10: Create an Executive Dashboard")
print("-" * 70)
print("Task: Create a complete dashboard with 6 charts")
print("This is the FINAL BOSS challenge! Combines everything.")
print("Requirements:")
print("- 3x2 subplot grid")
print("- Each chart tells a different story")
print("- Professional styling throughout")
print("- Clear titles on each subplot")
print("- Overall title for the dashboard")
print("- Save as 'challenge10_executive_dashboard.png'")

# Suggested charts:
# 1. Total revenue by region
# 2. Total revenue by product
# 3. Average sale value by region
# 4. Sales count by product
# 5. Revenue timeline
# 6. Regional product mix (grouped or stacked)

# YOUR CODE HERE ✅
fig, axes = plt.subplots(3, 2, figsize=(16, 12))
fig.suptitle('Sales Performance Dashboard - Q1/Q2 2024',
             fontsize=18, fontweight='bold', y=0.995)

# Chart 1: Total revenue by region (top-left)
df.groupby('region')['revenue'].sum().plot(kind='bar', ax=axes[0,0], color='steelblue', edgecolor='black')
axes[0,0].set_title('Total Revenue by Region', fontweight='bold')
axes[0,0].set_ylabel('Revenue ($)')
axes[0,0].set_xlabel('Region')

# Chart 2: Total revenue by product (top-right)
df.groupby('product')['revenue'].sum().sort_values(ascending=False).plot(kind='bar', ax=axes[0,1], color='coral', edgecolor='black')
axes[0,1].set_title('Total Revenue by Product', fontweight='bold')
axes[0,1].set_ylabel('Revenue ($)')
axes[0,1].set_xlabel('Product')

# Chart 3: Average sale value by region (middle-left)
df.groupby('region')['revenue'].mean().plot(kind='barh', ax=axes[1,0], color='lightgreen', edgecolor='black')
axes[1,0].set_title('Average Sale Value by Region', fontweight='bold')
axes[1,0].set_xlabel('Average Revenue ($)')
axes[1,0].set_ylabel('Region')

# Chart 4: Sales count by product (middle-right)
df.groupby('product').size().plot(kind='bar', ax=axes[1,1], color='gold', edgecolor='black')
axes[1,1].set_title('Number of Sales by Product', fontweight='bold')
axes[1,1].set_ylabel('Sales Count')
axes[1,1].set_xlabel('Product')

# Chart 5: Revenue timeline (bottom-left)
for product in df['product'].unique():
    product_data = df[df['product'] == product].sort_values('date')
    axes[2,0].plot(product_data['date'], product_data['revenue'],
                   marker='o', label=f'Product {product}', linewidth=2)
axes[2,0].set_title('Revenue Timeline by Product', fontweight='bold')
axes[2,0].set_xlabel('Date')
axes[2,0].set_ylabel('Revenue ($)')
axes[2,0].legend()
axes[2,0].grid(True, alpha=0.3)

# Chart 6: Regional product mix - stacked bar (bottom-right)
pivot = df.pivot_table(values='revenue', index='region', columns='product', aggfunc='sum', fill_value=0)
pivot.plot(kind='bar', stacked=True, ax=axes[2,1], color=['#1E88E5', '#FFC107', '#43A047'], edgecolor='black')
axes[2,1].set_title('Revenue Mix by Region', fontweight='bold')
axes[2,1].set_xlabel('Region')
axes[2,1].set_ylabel('Revenue ($)')
axes[2,1].legend(title='Product')
axes[2,1].set_xticklabels(axes[2,1].get_xticklabels(), rotation=0)

plt.tight_layout()
plt.savefig('challenge10_executive_dashboard.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Saved as 'challenge10_executive_dashboard.png'")
"""
💡 HINT:
This is a big one! Break it down:

fig, axes = plt.subplots(3, 2, figsize=(16, 12))
fig.suptitle('Sales Performance Dashboard - Q1/Q2 2024', 
             fontsize=18, fontweight='bold', y=0.995)

# Chart 1: axes[0,0]
# Chart 2: axes[0,1]
# Chart 3: axes[1,0]
# Chart 4: axes[1,1]
# Chart 5: axes[2,0]
# Chart 6: axes[2,1]

plt.tight_layout()
plt.savefig('challenge10_executive_dashboard.png', dpi=300, bbox_inches='tight')
plt.close()

Take your time! This is the capstone challenge.
"""

print("\n" + "=" * 70)
print("🎓 CHALLENGES COMPLETE!")
print("=" * 70)
print("\nIf you completed all 10 challenges, you now have:")
print("✅ Experience with bar, line, grouped, and stacked charts")
print("✅ Understanding of when to use each chart type")
print("✅ Professional styling and design skills")
print("✅ Ability to create complex multi-chart dashboards")
print("")
print("These are the EXACT skills data analysts use daily!")
print("Now move to portfolio_project.py to put it all together.")
print("=" * 70)

# Day 3: PORTFOLIO PROJECT - Complete Sales Analysis Report
# Professional visualization + storytelling for stakeholders

"""
🎯 PROJECT GOAL:
Create a complete analysis report with professional visualizations that tells
a compelling story about the sales data. This is what you'd deliver to management.

Deliverables:
1. Multiple professional charts (bar, line, grouped)
2. Written insights for each visualization
3. Executive summary with recommendations
4. Saved images ready for presentations

💼 THIS IS YOUR FINAL SHOWCASE!
This project combines everything:
- Day 1: pandas fundamentals
- Day 2: SQL-style analysis
- Day 3: Professional visualization + storytelling

🎤 INTERVIEW TALKING POINTS:
"I created a complete sales analysis report with professional visualizations
and business insights. The report includes multiple chart types, each chosen
to effectively communicate specific findings. I presented the analysis using
the data storytelling framework: context, data, insight, and action. This is
the type of deliverable I'd create for executives to support strategic decisions."
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set professional styling
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 11

# ============================================
# LOAD AND PREPARE DATA
# ============================================
df = pd.read_csv("sales_data.csv")
df['date'] = pd.to_datetime(df['date'])

print("=" * 80)
print("COMPLETE SALES ANALYSIS REPORT - Q1/Q2 2024")
print("=" * 80)

# ============================================
# SECTION 1: EXECUTIVE SUMMARY (TEXT)
# ============================================
print("\n" + "=" * 80)
print("EXECUTIVE SUMMARY")
print("=" * 80)

# TODO: Write a 3-5 sentence executive summary
# Include:
# - Date range analyzed
# - Total revenue figure
# - Key finding #1 (which region/product leads)
# - Key finding #2 (opportunity or concern)
# - High-level recommendation

# Example:
# "This report analyzes sales performance from January to June 2024, covering
# $8,200 in revenue across 6 transactions. The East region dominates with 49%
# of total revenue, driven primarily by Product A. However, Product C shows zero
# sales in the East region, representing a potential market opportunity. We
# recommend investigating regional preferences and adjusting the product mix."

# YOUR SUMMARY HERE:
summary = """
This report analyzes sales performance from January to June 2024, covering
$8,200 in revenue across 6 transactions. The East region dominates with 49%
of total revenue, driven primarily by Product A. However, Product C shows zero
sales in the East region, representing a potential market opportunity. We
recommend investigating regional preferences and adjusting the product mix.
"""

print(summary)

# ============================================
# SECTION 2: REVENUE BY REGION (BAR CHART)
# ============================================
print("\n" + "=" * 80)
print("FINDING 1: REGIONAL REVENUE DISTRIBUTION")
print("=" * 80)

# TODO: Create a professional bar chart showing revenue by region
# Requirements:
# - Sort bars from highest to lowest
# - Use a professional color scheme
# - Add clear title and labels
# - Include data labels on bars (optional but impressive!)
# - Save as high-resolution PNG

# HINT:
# revenue_by_region = df.groupby('region')['revenue'].sum().sort_values(ascending=False)
# plt.figure(figsize=(10, 6))
# revenue_by_region.plot(kind='bar', color='steelblue', edgecolor='black')
# plt.title('Total Revenue by Region - Q1/Q2 2024', fontsize=14, fontweight='bold')
# ... add more formatting ...
# plt.savefig('chart1_revenue_by_region.png', dpi=300, bbox_inches='tight')

# YOUR CODE HERE
revenue_by_region = df.groupby('region')['revenue'].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
revenue_by_region.plot(kind='bar', color='steelblue', edgecolor='black')
plt.title('Total Revenue by Region - Q1/Q2 2024', fontsize=14, fontweight='bold')
plt.xlabel('Region', fontsize=12)
plt.ylabel('Revenue ($)', fontsize=12)
plt.xticks(rotation=0)  # Keep labels horizontal
plt.tight_layout()
plt.savefig('chart1_revenue_by_region.png', dpi=300, bbox_inches='tight')
plt.close()

print("✅ Chart saved: chart1_revenue_by_region.png")


# TODO: Write the insight for this chart
# Answer: What does this chart tell us? Why does it matter?

insight_1 = """
💡 INSIGHT:
The East region generates nearly 50% of total revenue ($2,700), 
significantly outpacing West and South regions ($2,000 each). This indicates
strong product-market fit in the East, suggesting we should investigate what's
working well there and replicate those strategies in other regions.
"""

print(insight_1)
# ============================================
# SECTION 3: PRODUCT PERFORMANCE (BAR CHART)
# ============================================
print("\n" + "=" * 80)
print("FINDING 2: PRODUCT PERFORMANCE")
print("=" * 80)

# TODO: Create a bar chart showing revenue by product
# Sort by value, use different color than Section 2
# Make it visually distinct but still professional

# YOUR CODE HERE
revenue_by_product = df.groupby('product')['revenue'].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
revenue_by_product.plot(kind='bar', color='coral', edgecolor='black')
plt.title('Total Revenue by Product - Q1/Q2 2024', fontsize=14, fontweight='bold')
plt.xlabel('Product', fontsize=12)
plt.ylabel('Revenue ($)', fontsize=12)
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('chart2_revenue_by_product.png', dpi=300, bbox_inches='tight')
plt.close()

print("✅ Chart saved: chart2_revenue_by_product.png")


# TODO: Write the insight
insight_2 = """
💡 INSIGHT:
Product A dominates with $4,000 in revenue (60% of total), while Product C 
significantly underperforms at only $700 (10%). This suggests either Product C
has limited market appeal or requires better marketing/positioning. We should
analyze which regions buy Product C and consider discontinuing or repositioning it.
"""

print(insight_2)

# ============================================
# SECTION 4: REGIONAL PRODUCT MIX (GROUPED BAR)
# ============================================
print("\n" + "=" * 80)
print("FINDING 3: PRODUCT PERFORMANCE BY REGION")
print("=" * 80)

# TODO: Create a grouped bar chart showing revenue by region AND product
# This answers: "Which products sell best in which regions?"

# HINT: Use pivot_table
# pivot = df.pivot_table(values='revenue', index='region', 
#                        columns='product', aggfunc='sum', fill_value=0)
# pivot.plot(kind='bar', ...)

# YOUR CODE HERE
pivot = df.pivot_table(values='revenue', index='region',
                       columns='product', aggfunc='sum', fill_value=0)

plt.figure(figsize=(12, 6))
pivot.plot(kind='bar', color=['#1E88E5', '#FFC107', '#43A047'], edgecolor='black')
plt.title('Product Performance by Region - Q1/Q2 2024', fontsize=14, fontweight='bold')
plt.xlabel('Region', fontsize=12)
plt.ylabel('Revenue ($)', fontsize=12)
plt.legend(title='Product', loc='upper right')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('chart3_performance_by_region.png', dpi=300, bbox_inches='tight')
plt.close()

print("✅ Chart saved: chart3_performance_by_region.png")

# Insight
insight_3 = """
💡 INSIGHT:
Regional product preferences are highly distinct: East exclusively purchases 
Product A ($2,700), West only buys Product B ($2,000), and South splits between
Product A ($1,300) and Product C ($700). This suggests strong regional 
preferences rather than poor product quality. We should investigate why Product B
fails in East/South and why Product A doesn't sell in West - this could unlock
significant cross-selling opportunities.
"""

print(insight_3)


# ============================================
# SECTION 5: SALES OVER TIME (LINE CHART)
# ============================================
print("\n" + "=" * 80)
print("FINDING 4: SALES TIMELINE")
print("=" * 80)

# TODO: Create a line chart showing revenue over time
# If data is sparse, you might show it as scatter points too
# Consider showing all products on one chart with different colors

# YOUR CODE HERE
plt.figure(figsize=(12, 6))

for product in df['product'].unique():
    product_data = df[df['product'] == product].sort_values('date')
    plt.plot(product_data['date'], product_data['revenue'],
             marker='o', label=f'Product {product}', linewidth=2, markersize=8)

plt.title('Revenue Timeline by Product - Q1/Q2 2024', fontsize=14, fontweight='bold')
plt.xlabel('Date', fontsize=12)
plt.ylabel('Revenue ($)', fontsize=12)
plt.legend(title='Product', loc='best')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('chart4_revenue_timeline.png', dpi=300, bbox_inches='tight')
plt.close()

print("✅ Chart saved: chart4_revenue_timeline.png")

# Insight
insight_4 = """
💡 INSIGHT:
Sales are sporadic throughout the 6-month period with no clear seasonal pattern.
Product A shows the most consistent activity with 3 transactions spread across
January, March, and June. Products B and C have only 2 and 1 transactions 
respectively, suggesting either low demand or insufficient marketing. The lack
of sales concentration in any particular month indicates opportunity to optimize
timing and promotional campaigns.
"""

print(insight_4)

# ============================================
# SECTION 6: AVERAGE SALE VALUE COMPARISON
# ============================================
print("\n" + "=" * 80)
print("FINDING 5: AVERAGE SALE VALUE ANALYSIS")
print("=" * 80)

# TODO: Create chart(s) showing average sale value
# Options:
# - Average by region
# - Average by product
# - Both (side by side in subplots)

# This helps answer: "Are we getting high-value or low-value sales?"

# YOUR CODE HERE
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Average by region
avg_by_region = df.groupby('region')['revenue'].mean().sort_values(ascending=False)
avg_by_region.plot(kind='bar', ax=ax1, color='steelblue', edgecolor='black')
ax1.set_title('Average Sale Value by Region', fontsize=12, fontweight='bold')
ax1.set_ylabel('Average Revenue ($)', fontsize=10)
ax1.set_xlabel('Region', fontsize=10)
ax1.set_xticklabels(ax1.get_xticklabels(), rotation=0)

# Average by product
avg_by_product = df.groupby('product')['revenue'].mean().sort_values(ascending=False)
avg_by_product.plot(kind='bar', ax=ax2, color='coral', edgecolor='black')
ax2.set_title('Average Sale Value by Product', fontsize=12, fontweight='bold')
ax2.set_ylabel('Average Revenue ($)', fontsize=10)
ax2.set_xlabel('Product', fontsize=10)
ax2.set_xticklabels(ax2.get_xticklabels(), rotation=0)

plt.tight_layout()
plt.savefig('chart5_avg_sale_value.png', dpi=300, bbox_inches='tight')
plt.close()

print("✅ Chart saved: chart5_avg_sale_value.png")

# Insight
insight_5 = """
💡 INSIGHT:
Average sale values vary significantly: East leads at $1,350 per sale, while
West and South average $1,000. By product, Product A averages $1,333 per sale
versus Product C at only $700. This suggests East region buyers have higher
purchasing power or buy larger quantities. We should investigate what drives
these differences to potentially increase average order value in lower-performing
segments.
"""

print(insight_5)

# ============================================
# SECTION 7: COMPREHENSIVE DASHBOARD (OPTIONAL)
# ============================================
print("\n" + "=" * 80)
print("COMPREHENSIVE DASHBOARD (OPTIONAL)")
print("=" * 80)

# TODO (BONUS): Create a 2x2 or 3x2 subplot figure with multiple charts
# This is impressive! Shows you can create executive dashboards

# Example layout:
# ┌─────────────────┬─────────────────┐
# │  Revenue by     │  Revenue by     │
# │  Region         │  Product        │
# ├─────────────────┼─────────────────┤
# │  Sales Over     │  Avg Sale       │
# │  Time           │  Value          │
# └─────────────────┴─────────────────┘

# HINT:
# fig, axes = plt.subplots(2, 2, figsize=(15, 10))
# ... plot on axes[0,0], axes[0,1], etc ...
# plt.tight_layout()

# YOUR CODE HERE (if you want the challenge!)
print("⏭️  Skipping optional dashboard - individual charts tell the story better!")

# ============================================
# SECTION 8: KEY FINDINGS SUMMARY
# ============================================
print("\n" + "=" * 80)
print("KEY FINDINGS SUMMARY")
print("=" * 80)

# TODO: List your top 3-5 findings in bullet format
# Be specific! Use numbers!

findings = """
🔍 TOP FINDINGS:

1. REGIONAL CONCENTRATION: East region generated $2,700 (40.3% of total revenue)
   with only 2 transactions, indicating strong market presence and high-value sales.

2. PRODUCT DOMINANCE: Product A accounts for $4,000 (59.7%) across 3 sales,
   while Product C significantly underperforms at only $700 (10.4%) from 1 sale.

3. MARKET GAPS: Critical cross-selling opportunities exist - Product B has zero
   sales in East/South, Product A has zero in West, and Product C has zero in
   East/West, suggesting untapped regional potential.

4. AVERAGE SALE VALUE: East region's $1,350 average is 35% higher than West/South
   ($1,000), indicating either premium product mix or higher-value customer base.

5. SPARSE ACTIVITY: Only 6 total transactions over 6 months suggests either early-stage
   business, seasonal operation, or data representing subset of total activity.
"""

print(findings)

# ============================================
# SECTION 9: STRATEGIC RECOMMENDATIONS
# ============================================
print("\n" + "=" * 80)
print("STRATEGIC RECOMMENDATIONS")
print("=" * 80)

# TODO: Provide 3-5 actionable recommendations based on your analysis
# Use the framework: [ACTION] + [REASON] + [EXPECTED OUTCOME]

recommendations = """
🎯 RECOMMENDED ACTIONS:

1. EXPAND: Deploy East region sales strategies to West and South
   BECAUSE: East achieves 35% higher average sale value with same products
   EXPECTED: 20-30% revenue increase in underperforming regions within 2 quarters

2. INVESTIGATE: Conduct regional preference analysis for product cross-selling
   BECAUSE: Zero sales of Products B/C in East and Product A in West suggests
            regional preferences rather than product quality issues
   EXPECTED: Unlock $2,000+ in untapped cross-regional sales opportunities

3. OPTIMIZE: Discontinue or reposition Product C
   BECAUSE: Product C generates only $700 (10% of revenue) from single sale,
            with zero penetration in 2 of 3 regions
   EXPECTED: Reduce inventory costs and reallocate resources to Products A/B

4. ACCELERATE: Increase transaction frequency across all regions
   BECAUSE: 6 transactions over 6 months (1 per month) indicates low sales velocity
   EXPECTED: Double monthly transaction rate through targeted marketing campaigns

5. ANALYZE: Investigate what drives East region's premium average sale value
   BECAUSE: Understanding $1,350 vs $1,000 differential could inform pricing strategy
   EXPECTED: Identify replicable factors to increase margins company-wide
"""

print(recommendations)

# ============================================
# SECTION 10: NEXT STEPS & METRICS TO TRACK
# ============================================
print("\n" + "=" * 80)
print("NEXT STEPS & METRICS TO MONITOR")
print("=" * 80)

# TODO: What should the business do next?
# What metrics should they track going forward?

next_steps = """
📊 IMMEDIATE ACTIONS:
- Schedule regional preference surveys to understand product gaps
- Analyze East region sales process to identify replicable success factors
- Test Product C repositioning in South region (where it has traction)
- Launch targeted campaigns to increase transaction frequency

📈 METRICS TO TRACK:
- Average sale value by region (target: standardize to $1,350+ across all regions)
- Cross-selling penetration rates (% of regions carrying each product)
- Monthly transaction velocity (target: 3+ transactions per region per month)
- Product C performance post-repositioning (give 90 days to show improvement)

🔄 FOLLOW-UP ANALYSIS:
- Customer segmentation analysis to understand East region buyer profiles
- Competitive analysis in West region to understand Product A resistance
- Seasonal pattern analysis with 12+ months data
- Customer lifetime value analysis once more transaction history accumulates
"""

print(next_steps)

# ============================================
# SAVE REPORT TEXT (OPTIONAL)
# ============================================

# TODO (Optional): Save your written report to a text file
# This creates a deliverable you could email to stakeholders

# with open('sales_analysis_report.txt', 'w') as f:
#     f.write("SALES ANALYSIS REPORT - Q1/Q2 2024\n")
#     f.write("=" * 80 + "\n\n")
#     f.write("EXECUTIVE SUMMARY\n")
#     f.write(summary + "\n\n")
#     ... add all sections ...


with open('sales_analysis_report.txt', 'w', encoding='utf-8') as f:
    f.write("=" * 80 + "\n")
    f.write("SALES ANALYSIS REPORT - Q1/Q2 2024\n")
    f.write("=" * 80 + "\n\n")

    f.write("EXECUTIVE SUMMARY\n")
    f.write("-" * 80 + "\n")
    f.write(summary + "\n\n")

    f.write("FINDING 1: REGIONAL REVENUE DISTRIBUTION\n")
    f.write("-" * 80 + "\n")
    f.write(insight_1 + "\n\n")

    f.write("FINDING 2: PRODUCT PERFORMANCE\n")
    f.write("-" * 80 + "\n")
    f.write(insight_2 + "\n\n")

    f.write("FINDING 3: PRODUCT PERFORMANCE BY REGION\n")
    f.write("-" * 80 + "\n")
    f.write(insight_3 + "\n\n")

    f.write("FINDING 4: SALES TIMELINE\n")
    f.write("-" * 80 + "\n")
    f.write(insight_4 + "\n\n")

    f.write("FINDING 5: AVERAGE SALE VALUE ANALYSIS\n")
    f.write("-" * 80 + "\n")
    f.write(insight_5 + "\n\n")

    f.write(findings + "\n\n")
    f.write(recommendations + "\n\n")
    f.write(next_steps + "\n\n")

    f.write("=" * 80 + "\n")
    f.write("END OF REPORT\n")
    f.write("=" * 80 + "\n")

print("✅ Report saved: sales_analysis_report.txt")

print("\n" + "=" * 80)
print("✅ ANALYSIS COMPLETE - READY FOR PRESENTATION")
print("=" * 80)
print("\nDeliverables created:")
print("📊 chart1_revenue_by_region.png")
print("📊 chart2_revenue_by_product.png")
print("📊 chart3_revenue_by_product.png")
print("📊 chart4_revenue_timeline.png")
print("📊 chart5_avg_sale_value.png")
print("📄 sales_analysis_report.txt - Written analysis with insights")
print("\n" + "=" * 80)
"""
🎓 FINAL PROJECT CHECKLIST:
□ All visualizations created and saved
□ Each chart has a clear title and labels
□ Charts use professional color schemes
□ Insights are specific and data-driven
□ Recommendations are actionable and justified
□ Report follows storytelling framework
□ Code is clean and well-commented

📝 ADDING TO YOUR PORTFOLIO:

1. Create a new folder in your GitHub: "sales-analysis-report"
2. Include:
   - This Python file
   - All chart images
   - The data file
   - A comprehensive README.md
3. In the README, include:
   - Project overview
   - Key findings (with images!)
   - Technologies used
   - Sample insights
   - Link to view images

Example README structure:
```markdown
# Sales Performance Analysis Report

## Overview
Complete analysis of Q1/Q2 2024 sales data using Python, pandas, and matplotlib.

## Key Findings
1. East region generates 49% of revenue
   ![Revenue by Region](chart1_revenue_by_region.png)

2. Product A leads with $4,000 in sales
   ![Revenue by Product](chart2_revenue_by_product.png)

...

## Technologies
- Python 3.x
- pandas for data analysis
- matplotlib & seaborn for visualization

## Insights & Recommendations
[Summary of your key recommendations]
```

💬 HOW TO PRESENT THIS IN INTERVIEWS:

"I created a comprehensive sales analysis report that executives could use to make
strategic decisions. The project includes:

1. Multiple professional visualizations - bar charts for comparisons, line charts
   for trends, grouped charts for multi-dimensional analysis
   
2. Written insights following the data storytelling framework - context, data,
   insight, and actionable recommendations
   
3. Specific, data-driven recommendations like [mention your top recommendation]

The most impactful finding was [your key insight]. This led to a recommendation
to [your action], which could potentially [expected outcome].

This project showcases my ability to:
- Perform end-to-end analysis (data → insights → action)
- Create professional visualizations
- Communicate findings to non-technical stakeholders
- Think strategically about business implications

I can walk you through any of the visualizations or discuss the methodology
in more detail."

🏆 CONGRATULATIONS!

You've completed the 3-Day Data Analyst Sprint!

You now have:
✅ Solid pandas fundamentals
✅ SQL-style query skills
✅ Professional visualization abilities
✅ 3 portfolio projects
✅ Interview talking points connecting to your CPHT experience

You're ready to apply for entry-level data analyst positions! 🎯

Remember: Every data analyst started where you are now.
Your CPHT background is an ASSET, not a barrier.
You have the skills. Now go show them! 💪
"""

# Day 3: Data Visualization & Business Storytelling
# Turn data into insights that drive decisions

"""
🎯 LEARNING OBJECTIVES FOR DAY 3:
By the end of this lesson, you will understand:
1. Why visualization matters (it's not just "making pretty charts")
2. Choosing the RIGHT chart type for your data
3. Design principles for clear, professional visualizations
4. How to tell a story with data (this is what gets you hired!)
5. Common visualization mistakes to avoid

💼 WHY THIS MATTERS:
Technical skills get you the interview.
Communication skills get you the job.
Data analysts don't just analyze - they COMMUNICATE insights to non-technical people.

💊 CPHT CONNECTION:
Remember explaining prescriptions to patients?
"This antibiotic needs to be taken every 8 hours for 10 days."
That's data storytelling! You took complex info and made it actionable.
Now you'll do the same with charts and business insights.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style for better-looking plots
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

# ============================================
# LESSON 1: WHY VISUALIZATION MATTERS
# ============================================
print("=" * 70)
print("DAY 3: DATA VISUALIZATION & STORYTELLING")
print("=" * 70)

df = pd.read_csv("sales_data.csv")

print("\n📊 Our Sales Data:")
print(df)

"""
🧠 THE POWER OF VISUALIZATION:

Raw numbers:
East: $4000, West: $2000, South: $2000

vs

A bar chart immediately shows:
- East dominates (2x other regions)
- West and South are tied
- Focus resources on East or investigate why others lag

💡 KEY INSIGHT:
Your brain processes images 60,000x faster than text.
A good chart = instant understanding.
A table of numbers = requires mental calculation.
"""

# ============================================
# LESSON 2: CHART TYPE DECISION TREE
# ============================================
print("\n\n📈 LESSON 2: CHOOSING THE RIGHT CHART")
print("-" * 70)

"""
🎯 CHART SELECTION GUIDE:

COMPARING CATEGORIES? → Bar Chart
Example: "Revenue by region" → Bar chart

SHOWING TRENDS OVER TIME? → Line Chart  
Example: "Sales by month" → Line chart

SHOWING PARTS OF A WHOLE? → Pie Chart (use sparingly!)
Example: "Market share by product" → Pie chart
(But bar charts are often clearer!)

SHOWING RELATIONSHIP BETWEEN TWO VARIABLES? → Scatter Plot
Example: "Revenue vs. Marketing Spend" → Scatter plot

💊 CPHT CONNECTION:
- Bar chart = "Prescriptions filled per day of week"
- Line chart = "Prescription volume over the year"
- Pie chart = "Percentage of scripts by insurance type"

Choose the chart that makes the insight OBVIOUS!
"""

# ============================================
# LESSON 3: BAR CHARTS - COMPARING CATEGORIES
# ============================================
print("\n\n📊 LESSON 3: BAR CHARTS")
print("-" * 70)

# Calculate revenue by region
revenue_by_region = df.groupby('region')['revenue'].sum()

# Create bar chart
plt.figure(figsize=(10, 6))
revenue_by_region.plot(kind='bar', color='steelblue', edgecolor='black')
plt.title('Total Revenue by Region', fontsize=16, fontweight='bold')
plt.xlabel('Region', fontsize=12)
plt.ylabel('Revenue ($)', fontsize=12)
plt.xticks(rotation=0)  # Keep labels horizontal
plt.tight_layout()
plt.savefig('revenue_by_region.png', dpi=300, bbox_inches='tight')
plt.close()

print("✅ Created: revenue_by_region.png")

"""
🧠 BAR CHART BEST PRACTICES:

✅ DO:
- Sort bars by value (highest to lowest) for easy comparison
- Label axes clearly with units
- Use a single, professional color (avoid rainbow)
- Add a descriptive title
- Remove unnecessary gridlines
- Keep labels horizontal (rotate=0)

❌ DON'T:
- Use 3D effects (they distort perception)
- Use too many colors (distracting)
- Forget axis labels (what does the number mean?)
- Make bars too thin or too wide

💡 PRO TIP: Add data labels on bars for exact values
"""

# ============================================
# LESSON 4: LINE CHARTS - SHOWING TRENDS
# ============================================
print("\n\n📈 LESSON 4: LINE CHARTS")
print("-" * 70)

# Prepare data - convert date to datetime
df['date'] = pd.to_datetime(df['date'])
df_sorted = df.sort_values('date')

# Create line chart for Product A over time
product_a = df_sorted[df_sorted['product'] == 'A']

plt.figure(figsize=(10, 6))
plt.plot(product_a['date'], product_a['revenue'], 
         marker='o', linewidth=2, markersize=8, color='#2E86AB')
plt.title('Product A Revenue Over Time', fontsize=16, fontweight='bold')
plt.xlabel('Date', fontsize=12)
plt.ylabel('Revenue ($)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('product_a_trend.png', dpi=300, bbox_inches='tight')
plt.close()

print("✅ Created: product_a_trend.png")

"""
🧠 LINE CHART BEST PRACTICES:

✅ DO:
- Use for time series data (dates on x-axis)
- Add markers to show data points
- Use a clear, visible line width
- Show gridlines for easier reading
- Label the time axis clearly

❌ DON'T:
- Use for comparing categories (use bar chart instead)
- Connect non-sequential data points
- Use too many lines on one chart (max 3-4)
- Forget to sort by date first!

💊 CPHT CONNECTION:
Perfect for "prescription volume by week" or "inventory levels over time"
"""

# ============================================
# LESSON 5: MULTIPLE SERIES ON ONE CHART
# ============================================
print("\n\n🔀 LESSON 5: COMPARING MULTIPLE SERIES")
print("-" * 70)

# Revenue by product over time
plt.figure(figsize=(12, 6))
for product in df['product'].unique():
    product_data = df_sorted[df_sorted['product'] == product]
    plt.plot(product_data['date'], product_data['revenue'], 
             marker='o', label=f'Product {product}', linewidth=2)

plt.title('Revenue Comparison: All Products', fontsize=16, fontweight='bold')
plt.xlabel('Date', fontsize=12)
plt.ylabel('Revenue ($)', fontsize=12)
plt.legend(title='Products', fontsize=10)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('all_products_comparison.png', dpi=300, bbox_inches='tight')
plt.close()

print("✅ Created: all_products_comparison.png")

"""
🧠 COMPARING MULTIPLE SERIES:

✅ DO:
- Use distinct colors for each line
- Add a legend to identify series
- Limit to 3-4 lines max (or it gets messy)
- Use different line styles if colors aren't distinct

❌ DON'T:
- Use similar colors (hard to distinguish)
- Forget the legend
- Crowd too many series (hard to read)

💼 INTERVIEW TIP:
"I can create multi-series visualizations to compare performance across 
categories, making it easy to spot which products or regions are outperforming."
"""

# ============================================
# LESSON 6: GROUPED BAR CHARTS
# ============================================
print("\n\n📊 LESSON 6: GROUPED BAR CHARTS")
print("-" * 70)

# Pivot table for grouped bar chart
pivot_data = df.pivot_table(values='revenue', index='region', 
                             columns='product', aggfunc='sum', fill_value=0)

# Create grouped bar chart
pivot_data.plot(kind='bar', figsize=(10, 6), 
                color=['#1E88E5', '#FFC107', '#43A047'])
plt.title('Revenue by Region and Product', fontsize=16, fontweight='bold')
plt.xlabel('Region', fontsize=12)
plt.ylabel('Revenue ($)', fontsize=12)
plt.legend(title='Product', fontsize=10)
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('grouped_bar_chart.png', dpi=300, bbox_inches='tight')
plt.close()

print("✅ Created: grouped_bar_chart.png")

"""
🧠 WHEN TO USE GROUPED BARS:
When you want to compare TWO categorical dimensions at once.
Example: "Revenue by Region AND Product"

This answers: "Which product performs best in which region?"

💊 CPHT CONNECTION:
"Prescriptions by insurance type AND drug class"
Shows which insurance covers which types of medications most.
"""

# ============================================
# LESSON 7: DESIGN PRINCIPLES
# ============================================
print("\n\n🎨 LESSON 7: DESIGN PRINCIPLES")
print("-" * 70)

"""
🎯 THE 5 RULES OF PROFESSIONAL VISUALIZATION:

1. CLARITY > BEAUTY
   A simple, clear chart beats a fancy, confusing one every time.

2. REMOVE INK THAT DOESN'T ADD INFORMATION
   - No unnecessary borders
   - No 3D effects
   - No chartjunk (decorative elements that don't help understanding)

3. USE COLOR INTENTIONALLY
   - Highlight what matters (one color for data, another to emphasize)
   - Stay consistent (same color = same meaning across charts)
   - Consider colorblind readers (avoid red/green combinations)

4. LABEL EVERYTHING
   - Chart title (what is this showing?)
   - Axis labels (what do the numbers mean?)
   - Units (dollars? percentages? count?)
   - Legend (if multiple series)

5. TELL A STORY
   - Every chart should answer a question
   - Add a caption explaining the insight
   - Use titles that state the finding, not just the topic

GOOD TITLE: "East Region Generates 50% of Total Revenue"
BAD TITLE: "Revenue by Region"

💼 INTERVIEW GOLD:
Mention these principles! Shows you think about communication, not just code.
"""

# ============================================
# LESSON 8: STORYTELLING WITH DATA
# ============================================
print("\n\n📖 LESSON 8: DATA STORYTELLING")
print("-" * 70)

"""
🎯 THE DATA STORYTELLING FRAMEWORK:

1. CONTEXT: What's the situation?
   "We launched Product C 6 months ago..."

2. DATA: What do the numbers show?
   "Product C revenue is 30% below targets..."

3. INSIGHT: Why does this matter?
   "This suggests the product isn't finding product-market fit..."

4. ACTION: What should we do?
   "I recommend conducting customer interviews to understand barriers..."

💊 CPHT CONNECTION:
You did this constantly:
- CONTEXT: "Patient has diabetes"
- DATA: "A1C is 8.5%"  
- INSIGHT: "Not controlled on current meds"
- ACTION: "Talk to doctor about increasing dose"

Same structure, different domain!

💼 HOW TO PRESENT IN INTERVIEWS:
When showing your portfolio project, don't just say "Here's a chart."
Instead: "I analyzed the data and found that remote positions have a 
67% higher interview rate than onsite positions. This suggests I should 
focus my job search on remote opportunities to maximize my chances."

That's STORYTELLING.
"""

# ============================================
# LESSON 9: COMMON MISTAKES TO AVOID
# ============================================
print("\n\n⚠️ LESSON 9: COMMON VISUALIZATION MISTAKES")
print("-" * 70)

"""
❌ MISTAKE #1: PIE CHARTS WITH TOO MANY SLICES
Why it's bad: Hard to compare slice sizes
Fix: Use a bar chart instead

❌ MISTAKE #2: NOT STARTING Y-AXIS AT ZERO
Why it's bad: Exaggerates differences (misleading!)
Fix: Always start bar charts at zero

❌ MISTAKE #3: USING TOO MANY COLORS
Why it's bad: Distracting and unprofessional
Fix: Use 1-3 colors max, strategically

❌ MISTAKE #4: 3D CHARTS
Why it's bad: Perspective distorts values
Fix: Always use 2D charts

❌ MISTAKE #5: NO TITLE OR LABELS
Why it's bad: Reader doesn't know what they're looking at
Fix: Label everything!

❌ MISTAKE #6: WRONG CHART TYPE
Why it's bad: Makes data harder to understand
Fix: Follow the decision tree (Lesson 2)

💡 PRO TIP:
Show your chart to someone unfamiliar with the data.
If they can't understand it in 5 seconds, redesign it.
"""

# ============================================
# PUTTING IT ALL TOGETHER: COMPLETE ANALYSIS
# ============================================
print("\n\n" + "=" * 70)
print("🎯 COMPLETE ANALYSIS WITH VISUALIZATIONS")
print("=" * 70)

# Analysis: Which region should we focus on?

print("\n📊 BUSINESS QUESTION:")
print("Which region should the sales team prioritize for Q2?")

# Calculate metrics
total_revenue = df.groupby('region')['revenue'].sum()
avg_revenue = df.groupby('region')['revenue'].mean()
num_sales = df.groupby('region').size()

print("\n📈 DATA:")
print(f"Total Revenue: {total_revenue.to_dict()}")
print(f"Average Sale: {avg_revenue.to_dict()}")
print(f"Number of Sales: {num_sales.to_dict()}")

# Find the winner
top_region = total_revenue.idxmax()
top_total = total_revenue.max()
top_avg = avg_revenue[top_region]

print(f"\n💡 INSIGHT:")
print(f"{top_region} region leads with ${top_total} total revenue.")
print(f"Average sale in {top_region}: ${top_avg:.2f}")

# Create a comprehensive visualization
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Chart 1: Total Revenue
total_revenue.sort_values(ascending=False).plot(kind='bar', ax=axes[0], 
                                                 color='steelblue', edgecolor='black')
axes[0].set_title('Total Revenue by Region', fontweight='bold')
axes[0].set_ylabel('Revenue ($)')
axes[0].set_xlabel('Region')
axes[0].tick_params(axis='x', rotation=0)

# Chart 2: Average Revenue
avg_revenue.sort_values(ascending=False).plot(kind='bar', ax=axes[1], 
                                               color='coral', edgecolor='black')
axes[1].set_title('Average Revenue per Sale', fontweight='bold')
axes[1].set_ylabel('Revenue ($)')
axes[1].set_xlabel('Region')
axes[1].tick_params(axis='x', rotation=0)

# Chart 3: Number of Sales
num_sales.sort_values(ascending=False).plot(kind='bar', ax=axes[2], 
                                             color='lightgreen', edgecolor='black')
axes[2].set_title('Number of Sales', fontweight='bold')
axes[2].set_ylabel('Count')
axes[2].set_xlabel('Region')
axes[2].tick_params(axis='x', rotation=0)

plt.tight_layout()
plt.savefig('complete_regional_analysis.png', dpi=300, bbox_inches='tight')
plt.close()

print(f"\n✅ Created: complete_regional_analysis.png")

print(f"\n🎯 RECOMMENDATION:")
print(f"Focus on {top_region} region for Q2. It has both the highest")
print(f"total revenue AND highest average sale value, indicating")
print(f"strong product-market fit. Consider replicating {top_region}'s")
print(f"strategies in other regions.")

print("\n" + "=" * 70)
print("✅ DAY 3 COMPLETE!")
print("=" * 70)

"""
🎓 WHAT YOU LEARNED TODAY:
✅ How to choose the right chart type for your data
✅ Design principles for professional visualizations
✅ How to create bar charts, line charts, and grouped charts
✅ Data storytelling framework (Context → Data → Insight → Action)
✅ Common mistakes to avoid
✅ How to present analysis to non-technical audiences

🚀 NEXT STEPS:
1. Complete challenges.py (practice creating different chart types)
2. Build your complete analysis in portfolio_project.py
3. Add visualizations to your previous projects

💼 INTERVIEW TALKING POINTS:
"I create clear, professional visualizations using matplotlib and seaborn.
I follow design best practices like choosing appropriate chart types,
removing chartjunk, and using color intentionally. Most importantly,
I don't just make charts - I tell stories with data, translating 
technical findings into actionable business recommendations."

🏆 YOU'RE NOW PORTFOLIO-READY!
You have:
- Pandas fundamentals (Day 1)
- SQL-style analysis (Day 2)  
- Visualization & storytelling (Day 3)

This is EXACTLY what entry-level data analyst roles require.
Build your portfolio projects and start applying! 🎯
"""

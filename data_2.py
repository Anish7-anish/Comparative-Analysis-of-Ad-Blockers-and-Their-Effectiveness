import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load all data files
baseline_path = '/Users/anish/Documents/Privacy/Privacy Project/combined_no_adblocker__data.csv'
ublock_path = '/Users/anish/Documents/Privacy/Privacy Project/combined_ublock_data.csv'
adblock_plus_path = '/Users/anish/Documents/Privacy/Privacy Project/combined_adblock_plus_data.csv'
ghostery_path = '/Users/anish/Documents/Privacy/Privacy Project/combined_ghostery_data.csv'
adblock_data_path = '/Users/anish/Documents/Privacy/Privacy Project/combined_adblock_data.csv'

# Reading data into DataFrames
baseline_df = pd.read_csv(baseline_path)
ublock_df = pd.read_csv(ublock_path)
adblock_plus_df = pd.read_csv(adblock_plus_path)
ghostery_df = pd.read_csv(ghostery_path)
adblock_df = pd.read_csv(adblock_data_path)

# Standardize column names for comparison
baseline_df = baseline_df.rename(columns={"Ads Found": "Ads Blocked", "Trackers Found": "Trackers Blocked"})

# List of ad-blocker data for analysis
adblocker_data = [
    ("uBlock", ublock_df),
    ("Adblock Plus", adblock_plus_df),
    ("Ghostery", ghostery_df),
    ("Adblock", adblock_df)
]

# Function 1: Compare average number of ads blocked per website by each adblocker
def compare_ads_blocked():
    ads_blocked = []
    for name, df in adblocker_data:
        avg_ads = df["Ads Blocked"].mean()  # Calculate average instead of sum
        ads_blocked.append({"Adblocker": name, "Ads Blocked (Average)": avg_ads})

    ads_blocked_df = pd.DataFrame(ads_blocked)
    plt.figure(figsize=(10, 6))
    sns.barplot(data=ads_blocked_df, x="Adblocker", y="Ads Blocked (Average)", palette="viridis")
    plt.title("Average Ads Blocked by Each Adblocker")
    plt.ylabel("Average Number of Ads Blocked per Website")
    plt.show()

# Function 2: Combined bar graph for average ads blocked and ads found in baseline (no adblocker)
def compare_with_baseline():
    avg_ads_found = baseline_df["Ads Blocked"].mean()  # Average ads found in baseline
    ads_data = [{"Category": "No Adblocker (Ads Found)", "Average": avg_ads_found}]
    for name, df in adblocker_data:
        avg_ads_blocked = df["Ads Blocked"].mean()
        ads_data.append({"Category": f"{name} (Ads Blocked)", "Average": avg_ads_blocked})

    ads_df = pd.DataFrame(ads_data)
    plt.figure(figsize=(12, 6))
    sns.barplot(data=ads_df, x="Category", y="Average", palette="muted")
    plt.title("Average Ads Found (Baseline) vs Ads Blocked by Adblockers")
    plt.ylabel("Average Number of Ads")
    plt.xticks(rotation=45, ha="right")
    plt.show()

# Function 3: Calculate average ads blocked by all adblockers and compare with baseline
def average_ads_blocked():
    avg_ads_found = baseline_df["Ads Blocked"].mean()
    avg_ads_blocked = sum(df["Ads Blocked"].mean() for _, df in adblocker_data) / len(adblocker_data)
    print(f"Average Ads Found in No Adblocker: {avg_ads_found:.2f}")
    print(f"Average Ads Blocked by Adblockers: {avg_ads_blocked:.2f}")

    plt.figure(figsize=(8, 6))
    categories = ["No Adblocker (Ads Found)", "Average Ads Blocked"]
    values = [avg_ads_found, avg_ads_blocked]
    sns.barplot(x=categories, y=values, palette="coolwarm")
    plt.title("Average Ads Blocked vs Ads Found in No Adblocker")
    plt.ylabel("Average Number of Ads")
    plt.show()

# Function 4: Generate heatmaps for all adblockers
# Function 4 (Updated): Generate a single heatmap for all combined adblocker data
def generate_combined_heatmap():
    # Combine all adblocker data into a single DataFrame
    combined_data = pd.DataFrame()
    for name, df in adblocker_data:
        df["Adblocker"] = name  # Add a column to identify the adblocker
        combined_data = pd.concat([combined_data, df], ignore_index=True)
    
    # Select relevant columns for the heatmap
    heatmap_data = combined_data[["Ads Blocked", "Trackers Blocked", "Page Load Time (s)", "CPU After (%)", "Memory After (%)"]]

    # Generate heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(heatmap_data.corr(), annot=True, cmap="coolwarm")
    plt.title("Combined Heatmap for All Adblockers")
    plt.show()


# Function 5: Calculate efficiency of using adblocker vs no adblocker
def calculate_efficiency():
    avg_ads_found = baseline_df["Ads Blocked"].mean()
    for name, df in adblocker_data:
        avg_ads_blocked = df["Ads Blocked"].mean()
        efficiency = (avg_ads_blocked / avg_ads_found) * 100  # Efficiency as a percentage
        print(f"Efficiency of {name}: {efficiency:.2f}%")
        print()

# Combined bar graphs for page load time, CPU usage, and memory usage
# Function 6: Average page load time (Baseline vs. Each Adblocker)
def compare_page_load_time():
    avg_load_time = [{"Category": "No Adblocker (Baseline)", "Average": baseline_df["Page Load Time (s)"].mean()}]
    for name, df in adblocker_data:
        avg_load_time.append({"Category": name, "Average": df["Page Load Time (s)"].mean()})

    load_time_df = pd.DataFrame(avg_load_time)
    plt.figure(figsize=(10, 6))
    sns.barplot(data=load_time_df, x="Category", y="Average", palette="pastel")
    plt.title("Average Page Load Time: Baseline vs. Adblockers")
    plt.ylabel("Average Page Load Time (s)")
    plt.xticks(rotation=45, ha="right")
    plt.show()

# Function 7: Average CPU usage (Before and After for Each Adblocker vs. Baseline)
def compare_cpu_usage():
    cpu_usage = [{"Category": "No Adblocker (Before)", "Average": baseline_df["CPU Before (%)"].mean()},
                 {"Category": "No Adblocker (After)", "Average": baseline_df["CPU After (%)"].mean()}]
    for name, df in adblocker_data:
        cpu_usage.append({"Category": f"{name} (Before)", "Average": df["CPU Before (%)"].mean()})
        cpu_usage.append({"Category": f"{name} (After)", "Average": df["CPU After (%)"].mean()})

    cpu_usage_df = pd.DataFrame(cpu_usage)
    plt.figure(figsize=(12, 6))
    sns.barplot(data=cpu_usage_df, x="Category", y="Average", palette="coolwarm")
    plt.title("Average CPU Usage: Baseline vs. Adblockers")
    plt.ylabel("Average CPU Usage (%)")
    plt.xticks(rotation=45, ha="right")
    plt.show()

# Function 8: Average memory usage (Before and After for Each Adblocker vs. Baseline)
def compare_memory_usage():
    memory_usage = [{"Category": "No Adblocker (Before)", "Average": baseline_df["Memory Before (%)"].mean()},
                    {"Category": "No Adblocker (After)", "Average": baseline_df["Memory After (%)"].mean()}]
    for name, df in adblocker_data:
        memory_usage.append({"Category": f"{name} (Before)", "Average": df["Memory Before (%)"].mean()})
        memory_usage.append({"Category": f"{name} (After)", "Average": df["Memory After (%)"].mean()})

    memory_usage_df = pd.DataFrame(memory_usage)
    plt.figure(figsize=(12, 6))
    sns.barplot(data=memory_usage_df, x="Category", y="Average", palette="Blues")
    plt.title("Average Memory Usage: Baseline vs. Adblockers")
    plt.ylabel("Average Memory Usage (%)")
    plt.xticks(rotation=45, ha="right")
    plt.show()

# Function 9: Trade-Off Analysis: Scatter plot to compare page load time with ads blocked
def trade_off_analysis():
    trade_off_data = pd.DataFrame()
    for name, df in adblocker_data:
        df["Adblocker"] = name
        trade_off_data = pd.concat([trade_off_data, df], ignore_index=True)

    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=trade_off_data, x="Page Load Time (s)", y="Ads Blocked", hue="Adblocker", palette="Set2")
    plt.title("Trade-Off Analysis: Ads Blocked vs. Page Load Time")
    plt.xlabel("Page Load Time (s)")
    plt.ylabel("Ads Blocked")
    plt.legend(title="Adblocker")
    plt.show()





# Execute all functions
compare_ads_blocked()           # Function 1
compare_with_baseline()         # Function 2
average_ads_blocked()           # Function 3
generate_combined_heatmap()     # Function 4
calculate_efficiency()          # Function 5
# Execute the new functions

# Execute new functions
compare_page_load_time()        # Function 6
compare_cpu_usage()             # Function 7
compare_memory_usage()          # Function 8
trade_off_analysis()            # Function 9  # Scatter plots for trade-off analysis


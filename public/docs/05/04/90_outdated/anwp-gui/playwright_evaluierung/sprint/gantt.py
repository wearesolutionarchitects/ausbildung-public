import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

# Task definitions
tasks = [
    {"Task": "Installation and Configuration of Playwright", "Start": datetime(2024, 10, 29), "Duration": 1},
    {"Task": "Project and Test Structure Setup", "Start": datetime(2024, 10, 30), "Duration": 1},
    {"Task": "Test Strategy and Requirement Analysis", "Start": datetime(2024, 11, 1), "Duration": 1},
    {"Task": "Creating Test Cases for Main Pages", "Start": datetime(2024, 11, 2), "Duration": 2},
    {"Task": "Creating Test Cases for Subpages", "Start": datetime(2024, 11, 6), "Duration": 2},
    {"Task": "Developing UI Test Scripts", "Start": datetime(2024, 11, 8), "Duration": 2},
    {"Task": "Automated Visual Regression Tests", "Start": datetime(2024, 11, 10), "Duration": 1},
    {"Task": "Conducting Performance Tests", "Start": datetime(2024, 11, 11), "Duration": 1},
    {"Task": "Cross-Browser Tests with Playwright", "Start": datetime(2024, 11, 12), "Duration": 1},
    {"Task": "Collecting and Documenting Results", "Start": datetime(2024, 11, 13), "Duration": 1},
    {"Task": "Final Meeting and Bug Fixes", "Start": datetime(2024, 11, 14), "Duration": 1},
]

# Calculate End Date
for task in tasks:
    task["End"] = task["Start"] + timedelta(days=task["Duration"] - 1)

# Convert tasks data into a DataFrame for plotting
df_tasks = pd.DataFrame(tasks)

# Create a Gantt chart using Matplotlib
fig, ax = plt.subplots(figsize=(12, 8))

# Define colors and bar height
color = 'skyblue'
bar_height = 0.6

# Plot each task as a horizontal bar
for i, task in enumerate(df_tasks.itertuples()):
    ax.barh(task.Task, (task.End - task.Start).days + 1, left=task.Start, color=color, height=bar_height)
    ax.text(task.Start, i, f"{task.Start.strftime('%Y-%m-%d')} to {task.End.strftime('%Y-%m-%d')}", 
            va='center', ha='left', fontsize=8, color='black')

# Format the x-axis with date labels
ax.xaxis.set_major_locator(mdates.DayLocator(interval=2))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
plt.xticks(rotation=45, ha='right')
ax.set_title("Project Gantt Chart for Web App Testing Plan")
ax.set_xlabel("Timeline")
ax.set_ylabel("Tasks")

# Show plot
plt.tight_layout()
plt.show()

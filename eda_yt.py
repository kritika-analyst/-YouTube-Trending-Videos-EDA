# Project : Exploratory Data Analysis (EDA)
# Author : Kritika 
# Exploratory Data Analysis on YouTube Videos Dataset

# Importing necessary libraries 
import pandas as pd                # managing tables
import matplotlib.pyplot as plt    # data visualization
import seaborn as sns              # improving graph appearance

df= pd.read_csv("INvideos.csv")    # loading dataset

print(df.head())                   # displays first 5 rows
print(df.info())                   # gives info about dataset
print(df.isnull().sum())           # checks and counts missing values


# Top 10 Categories of YouTube videos

top_categories= df["category_id"].value_counts().head(10) 

sns.set_style("whitegrid")   # Creates graph cleaner and prettier

top_categories.plot(kind= "bar")    # Creating bar graph

plt.title("Top 10 Trending YouTube Categories in India")    # title
plt.xlabel("Category ID")                                   # x-axis label
plt.ylabel("Number of Trending Videos")                     # y-axis label

print(df["views"].head())         # displays first 5 rows of views column

plt.grid(True, alpha= 0.3)
plt.tight_layout()

plt.savefig("top10_categories.png")

plt.show()


# Views Distribution on YT videos - views distributed among trending videos

print(df.head(5))     # displays first 5 rows

plt.figure(figsize=(10,6))         # sets figure size
plt.hist(df["views"],bins= 30)     # creates histogram wiht 30 bins
plt.xscale("log")        # log scale to better visualize distribution of views 

plt.title("Distribution of Video Views")
plt.xlabel("Views")
plt.ylabel("Number of videos")

plt.grid(True, alpha= 0.3)     # adds grid with some transparency
plt.tight_layout()             # adjusts layout to prevent overlap of elements

plt.savefig("views_distribution.png")

plt.show()


# Views vs Likes - whether videos with more views also get more likes.
 
plt.figure(figsize=(10,6))

plt.scatter(df["views"], df["likes"], s= 8)   # creates scatter plot with views on x-axis and likes on y-axis, dot size = 8

plt.xscale("log")
plt.yscale("log")

plt.title("Likes vs Views")
plt.xlabel("Views")
plt.ylabel("Likes")

plt.grid(True, alpha= 0.3)
plt.tight_layout()

plt.savefig("likes_vs_views.png")

plt.show()


# Correlation Heatmap 

# calculates correlation between views, likes, dislikes, and comment_count
corr= df[["views", "likes", "dislikes", "comment_count"]].corr()  

plt.figure(figsize=(8,6))
sns.heatmap(corr, annot= True)  # creates heatmap with correlation values annoted on the cells

plt.title("Correlation Heatmap")
plt.savefig("correlation_heatmap.png")

plt.show()


# Most Active Channels

plt.figure(figsize=(12,8))   # sets figure size

top_channels= df["channel_title"].value_counts().head(10)

top_channels.plot(kind="bar")

plt.title("Top 10 Most Active Channels")
plt.xlabel("Channel Name")
plt.ylabel("Number of Trending Videos")

plt.xticks(rotation=45, ha="right")  # rotates x-axis labels for better visibilty
plt.grid(True, alpha= 0.3)
plt.tight_layout()

plt.savefig("top_channels.png")

plt.show()


# Publishing Time Analysis

df["publish_time"]= pd.to_datetime(df["publish_time"])  # converts publish time column to datetime format

df["hour"]= df["publish_time"].dt.hour   # extracts hour from publish time and creates new column "hour"

hourly_posts= df["hour"].value_counts().sort_index()  # counts no. of videos published in each hour and sorts by hour

hourly_posts.plot(kind="bar")

plt.title("Video Publishing Time Analysis") 
plt.xlabel("Hour of Day") 
plt.ylabel("Number of Videos")

plt.grid(True, alpha= 0.3)
plt.tight_layout()

plt.savefig("publishing_time_analysis.png")

plt.show()

print("\nEDA Completed Successfully!")

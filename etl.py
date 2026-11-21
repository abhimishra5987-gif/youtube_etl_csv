
import pandas as pd

# STEP 1: EXTRACT
df = pd.read_csv(r"C:\youtube_etl_project1\USvideos.csv\USvideos.csv")
print("Data aa gaya, total videos:", len(df))

# STEP 2: TRANSFORM
df = df[['title', 'channel_title', 'views', 'likes', 'publish_time']]

df = df.dropna()

# Remove videos with zero views
df = df[df['views'] > 0].copy()

# Calculate like ratio
df['like_ratio'] = (df['likes'] / df['views'] * 100).round(2)

print("Data clean")
print(df.head())

# STEP 3: LOADprint("Data saaf ho gaya")
print(df.head())

df.to_csv("clean_data.csv", index=False)
print("done! clean_data.csv ban gayi")

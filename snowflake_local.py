import pandas as pd
import os

# Load the CSV
file_path = r"C:\Users\Micow\Desktop\infra\film_actor_join.csv"
df = pd.read_csv(file_path)

# Drop nulls and trim whitespace
df = df.dropna()
df.columns = df.columns.str.strip()

# Output directory
output_dir = r"C:\Users\Micow\Desktop\infra\output_snowflake"
os.makedirs(output_dir, exist_ok=True)

# Create dim_actor
dim_actor = df[['actor_id', 'first_name', 'last_name']].drop_duplicates()
dim_actor.to_csv(os.path.join(output_dir, 'dim_actor_snowflake.csv'), index=False)

# Create dim_language (mocked name)
dim_language = df[['language_id']].drop_duplicates()
dim_language['language_name'] = 'English'
dim_language.to_csv(os.path.join(output_dir, 'dim_language_snowflake.csv'), index=False)

# Create dim_rating
dim_rating = df[['rating']].drop_duplicates().reset_index(drop=True)
dim_rating['rating_id'] = dim_rating.index + 1
dim_rating.to_csv(os.path.join(output_dir, 'dim_rating_snowflake.csv'), index=False)

# Create dim_film with normalized rating
dim_film = df[['film_id', 'title', 'description', 'release_year', 'language_id', 'rating']].drop_duplicates()
dim_film = dim_film.merge(dim_rating, on='rating', how='left')
dim_film = dim_film[[
    'film_id', 'title', 'description', 'release_year', 'language_id', 'rating_id'
]]
dim_film.to_csv(os.path.join(output_dir, 'dim_film_snowflake.csv'), index=False)

# Create fact_film_actor
fact_film_actor = df[['film_id', 'actor_id']].drop_duplicates()
fact_film_actor.to_csv(os.path.join(output_dir, 'fact_film_actor_snowflake.csv'), index=False)

print("Snowflake transformation complete. Files saved to /output_snowflake.")

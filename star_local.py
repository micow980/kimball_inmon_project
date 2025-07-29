import pandas as pd
import os

# Load the CSV
file_path = r"C:\Users\Micow\Desktop\infra\film_actor_join.csv"
df = pd.read_csv(file_path)

# Drop nulls and trim whitespace
df = df.dropna()
df.columns = df.columns.str.strip()

# Create dimension tables
dim_film = df[['film_id', 'title', 'description', 'release_year', 'language_id']].drop_duplicates()
dim_actor = df[['actor_id', 'first_name', 'last_name']].drop_duplicates()
dim_language = df[['language_id', 'language_name']].drop_duplicates()

# Create fact table
fact_film_actor = df[['film_id', 'actor_id']].drop_duplicates()

# Output locally
output_dir = r"C:\Users\Micow\Desktop\infra\output_star"
os.makedirs(output_dir, exist_ok=True)

dim_film.to_csv(os.path.join(output_dir, 'dim_film_star.csv'), index=False)
dim_actor.to_csv(os.path.join(output_dir, 'dim_actor_star.csv'), index=False)
dim_language.to_csv(os.path.join(output_dir, 'dim_language_star.csv'), index=False)
fact_film_actor.to_csv(os.path.join(output_dir, 'fact_film_actor_star.csv'), index=False)

print("Star schema transformation complete. Files saved to /output_star.")

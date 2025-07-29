import pandas as pd
import boto3
from io import StringIO
from datetime import datetime

# AWS S3 setup
s3 = boto3.client("s3")
bucket = "data-modeling-michael980"  # <-- update or use env var
raw_key = "raw/film_actor_join.csv"
staging_prefix = "staging/"
star_prefix = "star_schema/"
timestamp = datetime.utcnow().strftime("%Y%m%d")

# Read raw CSV from S3
response = s3.get_object(Bucket=bucket, Key=raw_key)
df = pd.read_csv(response["Body"])
df = df.dropna()
df.columns = df.columns.str.strip()

# Save cleaned file to staging
staging_buffer = StringIO()
df.to_csv(staging_buffer, index=False)
s3.put_object(
    Bucket=bucket, 
    Key=f"{staging_prefix}film_actor_staged_{timestamp}.csv", 
    Body=staging_buffer.getvalue()
)

# Helper function to write to S3 with timestamped filename
def write_to_s3(df_part, folder_name):
    buffer = StringIO()
    df_part.to_csv(buffer, index=False)
    key = f"{star_prefix}{folder_name}/{folder_name}_{timestamp}.csv"
    s3.put_object(
        Bucket=bucket,
        Key=key,
        Body=buffer.getvalue()
    )

# Create and write dimension/fact tables
write_to_s3(df[['film_id', 'title', 'description', 'release_year', 'language_id']].drop_duplicates(), "dim_film")
write_to_s3(df[['actor_id', 'first_name', 'last_name']].drop_duplicates(), "dim_actor")
write_to_s3(df[['language_id']].drop_duplicates().assign(language_name='English'), "dim_language")
write_to_s3(df[['film_id', 'actor_id']].drop_duplicates(), "fact_film_actor")

print("Glue star schema transformation complete. Timestamped files written to S3 folders.")

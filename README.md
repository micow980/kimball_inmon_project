# 📊 Kimball vs Inmon: A Hands-On Comparison Using Star and Snowflake Schemas in PostgreSQL

> A real-world experiment comparing the performance, structure, and usability of **star** vs. **snowflake** schema models using PostgreSQL and the same raw dataset.

---

## 📁 Project Overview

The way you model data can directly impact cloud costs, query speed, and developer experience. In this project, I take a single CSV dataset and build two data warehouses:

- 🟣 A **Star Schema** following the Kimball methodology (denormalized)
- 🔷 A **Snowflake Schema** following the Inmon methodology (normalized)

Each schema is then loaded into PostgreSQL and benchmarked using real SQL queries. This repo contains all the code, CSV outputs, and observations from that side-by-side analysis.

---

## 🛠️ Tech Stack

- **PostgreSQL 17**
- **pgAdmin 4**
- **Pandas (Python 3.10)**
- **Local & AWS workflows**
- **Kimball & Inmon modeling principles**

---

## 🗂️ Folder Structure

├── data/
│ └── film_actor_join.csv # Raw dataset
├── output_star/
│ └── dim_.csv, fact_.csv # Star schema outputs
├── output_snowflake/
│ └── dim_.csv, fact_.csv # Snowflake schema outputs
├── star_local.py # Local script for star schema
├── snowflake_local.py # Local script for snowflake schema
├── sql/
│ └── create_tables_star.sql
│ └── create_tables_snowflake.sql
├── benchmarks/
│ └── explain_analyze_results.txt # Query timings and comparisons
└── README.md 


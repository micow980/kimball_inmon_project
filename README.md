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

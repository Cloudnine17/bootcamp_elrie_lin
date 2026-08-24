# S&P 500 Historical Asset Return & Volatility Prediction

## Problem Statement
Quantitative portfolio managers need reliable predictive models to understand short-term asset return dynamics and price volatility. Evaluating asset behavior over historical market regimes helps quantitative analysts design robust allocation strategies and quantify downside risks.
This project utilizes a static 5-year historical daily dataset of the S&P 500 index (2020–2025) stored in `data/raw/sp500_daily_history.csv`. The goal is to build a quantitative modeling pipeline that engineers technical features and fits predictive models to forecast next-day index returns and volatility.

## Stakeholder & User
* **Primary Stakeholder:** Portfolio Manager (PM) and Investment Committee.
* **End User:** Quantitative Research Analyst evaluating strategy feasibility.
* **Workflow Context:** Batch model evaluation based on fixed historical backtesting data to inform risk management policy.

## Useful Answer & Decision
* **Answer Type:** Predictive (Quantitative Point Forecast & Volatility Bands).
* **Primary Metric:** Root Mean Squared Error (RMSE) for return predictions and $R^2$ for goodness of fit.
* **Artifact Delivered:** Predictive model pipeline, diagnostic report, and feature importance analysis based on historical dataset.

## Assumptions & Constraints
* **Data Source:** Static historical daily OHLCV dataset (`sp500_daily_history.csv`). No live API dependency required during model development.
* **Scope:** Daily time-frequency sampling over a fixed 5-year window.
* **Constraint:** Model evaluation must account for transaction frictions and regime shifts within the historical timeframe.

## Known Unknowns / Risks
* **Non-stationarity:** Financial time series non-stationarity causing baseline OLS assumption violations.
* **Overfitting Risk:** Spurious correlations among engineered technical features (mitigated via out-of-sample split and regularization).

## Lifecycle Mapping
- Scope problem & set static dataset → Problem Framing & Scoping (Stage 01) → Stakeholder Memo & README
- Feature engineering on historical CSV → Data Prep & Feature Engineering (Stage 02-09) → Pipeline Scripts in `src/`
- Build OLS baseline & check diagnostics → Modeling (Stage 10a) → OLS Diagnostic Plots & Metric Tables
- Evaluate time series/GARCH volatility → Modeling (Stage 10b) → Time Series Models & Final Evaluation

## Repo Plan
- `data/`: `raw/sp500_daily_history.csv` and processed feature matrices.
- `src/`: Modular Python scripts for feature creation and modeling.
- `notebooks/`: Exploratory Data Analysis and regression diagnostics.
- `docs/`: Stakeholder memos and project documentation.

## Data Storage (Stage 05)

### 1. Data Folder Structure
The repository establishes a strict lifecycle separation between raw and processed environments:
- `data/raw/`: Stores immutable raw CSV files acquired during API ingestion and Web Scraping.
- `data/processed/`: Stores binary Parquet files converted from raw files for downstream analytics and modeling.

### 2. File Formats Used & Rationale
- **CSV (`.csv`)**: Used in `data/raw/` for initial ingestion snapshots to allow human inspection and simple diffing.
- **Parquet (`.parquet`)**: Used in `data/processed/` for efficient binary storage. Preserves column data types (such as `datetime64`) natively, reduces disk I/O, and speeds up read performance for modeling.

### 3. Dynamic File Reading & Storage Pipeline
- **Environment-Driven Paths**: Paths are managed securely via `.env` (`DATA_DIR_RAW` and `DATA_DIR_PROCESSED`) to avoid hardcoded absolute directory strings.
- **Automated Latest File Resolution**: The pipeline uses dynamic filename matching (`glob`) to locate and load the latest timestamped raw CSV file from `data/raw/`.
- **Validation & Transformation**: Reads the latest raw CSV, validates shape and data type parity against in-memory data, and transforms it into `.parquet` in `data/processed/`.
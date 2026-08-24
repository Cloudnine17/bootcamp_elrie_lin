# Stage 05 Data Storage Layer

## Data Storage Architecture

### 1. Directory Hierarchy
- `data/raw/`: Holds raw immutable data snapshots saved as standard CSVs.
- `data/processed/`: Holds processed analytical datasets saved in optimized Parquet binary format.

### 2. File Format Comparison & Usage
- **CSV (`data/raw/`)**: Used during ingestion for external inspection and human readability.
- **Parquet (`data/processed/`)**: Used for analytical pipeline stages. Offers columnar storage compression and retains metadata dtypes natively.

### 3. Environment Variable Configuration
All file I/O operations retrieve root directories dynamically via `.env`:
```env
DATA_DIR_RAW=data/raw
DATA_DIR_PROCESSED=data/processed
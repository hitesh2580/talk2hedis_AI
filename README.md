# talk2hedis_AI
## 🚀 1. Prerequisites

Before you begin, make sure you have the following installed on your system:
- 🐍 **Python 3.9+**
- 💻 **Git**
- 🧰 **VS Code** (or any IDE you prefer)
- 📦 **Supabase credentials** (provided separately)

---

## ⚙️ 2. Clone the Repository

Open your terminal (or VS Code terminal) and run:

```bash
git clone https://github.com/<your-org>/TALK2HEDIS_AI.git
cd TALK2HEDIS_AI
```

---

## 🧱 3. Create a Virtual Environment

Creating a virtual environment ensures all dependencies are isolated from your global Python setup.

### On Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
```

✅ You should now see `(.venv)` in your terminal prompt, meaning your environment is active.

---

## 📦 4. Install Dependencies

All required Python packages are listed in `requirements.txt`.

Install them using:
```bash
pip install -r requirements.txt
```

This installs:
- `supabase` → to connect to Supabase API  
- `pandas` → for DataFrame handling  
- `python-dotenv` → to load credentials from `.env`

---

## 🔐 5. Add Your `.env` File

Each teammate needs their own `.env` file with Supabase credentials.

In the **project root folder**, create a file named `.env` and add:

```bash
SUPABASE_URL=https://your-project-id.supabase.co
SUPABASE_KEY=your-anon-or-service-role-key
```

⚠️ Do **not** push this file to GitHub — it contains sensitive credentials.

It’s already listed in `.gitignore`.

---

## 🧠 6. Connect to Supabase and Fetch Data

Once your environment is set up, run the main connection script:

```bash
python src/db_connection.py
```

This script will:
1. Load your `.env` credentials  
2. Connect securely to the Supabase database  
3. Fetch data from tables like:
   - `member_enrollment`
   - `medical_claims`
   - `provider`
4. Store the results in **Pandas DataFrames**
5. Print sample records in the console

You can edit the `fetch_table()` calls in `db_connection.py` to query additional tables.

---

## 🧩 7. Example: Fetch Data from a Table

If you want to fetch specific data inside your own notebook or script, use the helper function:

```python
from src.db_connection import fetch_table

claims_df = fetch_table("medical_claims", limit=100)
print(claims_df.head())
```

This returns the table as a Pandas DataFrame you can analyze or visualize.

---
## 8. making your name directory
please make your own folder and add your code files in that folder.


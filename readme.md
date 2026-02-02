# Renewable Power Monitor

Lightweight project to fetch and visualise UK electricity generation mix using the Carbon Intensity API.

## Quickstart

Follow these steps to download and run the project on your local machine.

1. **Clone the repository**

```bash
git clone <your-repo-url>
```

> Replace `<your-repo-url>` with the HTTPS or SSH URL of the Git repository.

2. **Set up a Python virtual environment**

```bash
# Create a virtual environment
python3 -m venv venv

# Activate it
# macOS/Linux:
source venv/bin/activate
# Windows:
venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

> Ensure `requirements.txt` includes `pandas`, `streamlit`, `plotly`, and any other required packages.

4. **Pull from the Carbon Intensity API**

```bash
python fetchdata.py
```

This step retrieves historical electricity generation data and stores it locally.

5. **Run the Streamlit app**

```bash
streamlit run visualisedata.py
```

* Streamlit will start a local server and provide a URL (usually `http://localhost:8501`).
* Open this URL in your browser to view the interactive app.

6. **Interact with the app**

* Use the fuel selection multiselect to pick fuels.
* View both charts:

  * All fuels (line or stacked chart).
  * Renewables vs Non-Renewables.
* Scroll through the raw data table.


## Data source

This project uses the Carbon Intensity API generation endpoint:

https://api.carbonintensity.org.uk/generation/{start_ISO}/{end_ISO}

If the API requires a key, download it and store it in the project `.env` file.

## Current scope

- Start-off focus: wind generation only.
- Basic fetching and visualization pipeline with Streamlit.

## Included files

- `fetchdata.py` — data retrieval logic (initial fetch script).
- `visualisedata.py` — Streamlit app that displays the generation mix and charts.
- `generation_mix.csv` — example / persisted dataset exported for quick testing.
- `requirements.txt` — Python dependencies.
- `.env` — environment variables (API keys, etc.) - hidden from git commits
- `.gitignore`

## Planned next steps

1. Smooth data  
2. Make data frame filterable (by date, fuel type, region) 
3. Deploy streamlit page 
4. Clean up and modularise code
5. Build model to predict output for one wind farm - will need to use new APIs (Assumed National Grid and Met Office)

## Notes

- To inspect or modify the data fetching, see `fetchdata.py`.  
- To update the UI or visualisations, see `visualisedata.py`.
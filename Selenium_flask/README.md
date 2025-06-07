by flask/
│
├── Backend(Selenium Script)/
│   └── main.py               # Selenium scraper script
│
├── Frontend(Streamlit UI)/
│   └── Streamlit_app.py      # Streamlit user interface
│
├── app.py                    # Flask backend API
├── requirements.txt          # Required dependencies
└── README.md                 


## How It Works

1. Streamlit UI calls the Flask API endpoint `/scrape`.
2. Flask runs the Selenium script (`main.py`) which scrapes IT company data from Google Maps.
3. Scraped data is returned as JSON to Streamlit.
4. Streamlit displays the data in a table and provides a download option.

 # Frontend (Streamlit):
(use this in terminal : streamlit run streamlit_app.py)
Provides a simple UI with a button to scrape data.
Displays scraped IT company data (Name, Phone, Address).
Allows CSV download.

# Backend (Selenium):
Opens Google Maps in a headless browser.
Searches for “IT companies in Noida”.
Extracts company info.
Saves it to it_companies_noida.csv.

## Access home page:
http://127.0.0.1:5000/

##  Scrape images by query:
http://127.0.0.1:5000/scrape
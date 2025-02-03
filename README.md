
# Price Scraping with Selenium

This project is designed to scrape pricing data from a webpage using Selenium, process the information, and save the results to a CSV file. It takes pickup and dropoff locations, searches for a product and its price, and logs the data along with the date and time of the query.

## Requirements

Before running the script, make sure you have the following dependencies installed:

- Python 3.x
- Chrome WebDriver (managed automatically by `webdriver_manager`)
- Google Chrome installed on your system

Install the required libraries using `pip`:

```bash
pip install selenium webdriver-manager pandas python-dotenv
```

## Setup

1. Clone this repository or download the script files to your local machine.
2. Create a `.env` file in the root directory with the following variables:

```bash
GOOGLE_PATH=<Path to your Google Chrome user profile>
URL=<URL of the webpage to scrape>
WORD=<Word to search for within the page>
```

Make sure to replace `<Path to your Google Chrome user profile>`, `<URL of the webpage>`, and `<Word to search for>` with the correct values.

For your google profile path you can get it from writting chrome://version on your google search bar and copy the Executable path line that will appear!

## Usage

1. Run the script with the following command:

```bash
python scrapper.py
```

2. The script will scrape pricing information from the specified webpage, using the pickup and dropoff locations provided in the code, and store the results in a CSV file (`results.csv` by default).

### Customization

You can customize the following:

- **Pickup and Dropoff Locations:** Modify the `pickup_locations` and `dropoff_locations` lists inside the `main()` function to include the locations you'd like to query.
- **CSV Filename:** The results are saved in a CSV file. If you'd like to save them to a different file, you can change the `filename` parameter in the `save_to_csv()` function.

## Project Structure

```
.
├── .env                  # Environment variables for configuration
├── script.py             # Main Python script
├── results.csv           # CSV file for storing results (generated automatically)
└── README.md           # README file with the instruction for the project
```

## Notes

- This project uses the `selenium` library to automate browser interaction, and `webdriver_manager` ensures that the correct version of the Chrome WebDriver is installed.
- The scraping process involves interacting with a form on the page to input pickup and dropoff locations and then extracting the product (the WORD env variable) and price information.
- The results will be saved in a CSV file, with each row containing the following columns: `Pickup`, `Dropoff`, `Price`, `Product`, `Date`, and `Hour`.
- Make sure that you dont have an active google chrome instance, or the scrapper wont work correctly
- If the page that you are visting need some kind of log in, make sure to do that step before the use of the web scrapper

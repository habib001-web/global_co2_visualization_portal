# NOAA CO₂ Monthly Mean Data Viewer

An interactive web application that visualizes global CO₂ concentration data from NOAA's Mauna Loa Observatory. The project fetches, processes, and displays atmospheric carbon dioxide measurements from 2010 onwards with rich interactive charting capabilities.

## Features

### Core Functionality
- **Real-time Data Fetching**: Automatically retrieves the latest CO₂ measurements from NOAA's official JSON API
- **Statistical Analysis**: Calculates and displays maximum, minimum, and average CO₂ concentrations
- **Interactive Time-Series Chart**: Visualizes CO₂ trends over time using Chart.js
- **5-Year Moving Average**: Displays smoothed trendline showing long-term CO₂ trends
- **Dynamic Year Filtering**: Filter data by specific years using an intuitive dropdown menu
- **URL Parameter Support**: Direct links to specific years via `?year=YYYY` query parameters
- **Responsive Design**: Beautiful gradient UI that works seamlessly on desktop and mobile devices

### New in Round 2
- **Dark/Light Mode Toggle**: Switch between light and dark themes with persistent preference storage
- **Summary Statistics Table**: Comprehensive yearly breakdown showing max, min, and average values
- **Enhanced Visualization**: Dual-line chart displaying both raw data and 5-year moving average
- **Improved Data Processing**: Extended `data.json` with pre-calculated moving average data

## Setup Instructions

### Prerequisites

- Python 3.6 or higher (for data fetching script)
- Modern web browser (Chrome, Firefox, Safari, or Edge)
- Internet connection (for fetching NOAA data and Chart.js CDN)

### Installation

1. Clone or download this repository to your local machine

2. No additional dependencies required - the project uses:
   - Python standard library only
   - Chart.js loaded via CDN in the HTML file

### Running the Data Fetcher (Optional)

The repository includes pre-generated `data.json`, but you can update it:
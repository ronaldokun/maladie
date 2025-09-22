# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview
**maladie** is a health data visualization dashboard for analyzing time series blood marker data. It's a single-page web application that creates interactive charts from CSV health data, allowing users to track biomarker evolution over time and identify out-of-range values.

## Repository Structure

### Development Branches
- `main`: Basic project setup (README, LICENSE)
- `chart`: Contains the complete application code and data

### Core Files (on chart branch)
- `index.html`: Complete interactive dashboard with embedded CSS/JavaScript
- `blood_markers_pivot.csv`: Health data in pivot format (columns are dates, rows are analytes)

## Key Architecture

### Data Model
- **Input Format**: CSV with analytes as rows, datetime columns, and reference ranges
- **Data Categories**: Organized into functional groups (Inflammatory, Hematology, Kidney, Liver, etc.)
- **Value Handling**: Supports numeric values, special markers ("----", "Inferior a 0.5", "Raras")

### Frontend Architecture
- **Technology**: Pure HTML/CSS/JavaScript with Plotly.js for charting
- **Loading**: Automatic CSV loading with fallback to manual file picker
- **Visualization**: Interactive time series with reference ranges, historical min/max, median trends
- **Analysis**: Real-time detection of out-of-range values with percentage deviations

### Key Features
1. **Interactive Charts**: Zoom, pan, range slider for temporal navigation
2. **Reference Ranges**: Visual indication with green shaded areas
3. **Trend Analysis**: Historical minimum/maximum lines, median trends
4. **Focus Box**: Highlights latest out-of-range measurements with directional arrows
5. **Data Export**: Both pivot table and tidy format CSV downloads
6. **Responsive Design**: Mobile-friendly interface

## Common Development Tasks

### Running the Application
```bash
# Serve locally (required due to CORS restrictions with CSV loading)
uv run python -m http.server 8000
# Then open http://localhost:8000/index.html
```

### Working with Data
```bash
# Switch to chart branch where code lives
git checkout chart

# Check data structure
head blood_markers_pivot.csv

# View recent changes to data
git --no-pager log --oneline -10
```

### Data Updates
The project expects CSV data in a specific pivot format:
- First column: Analyte names
- Middle columns: DateTime values (DD/MM/YY HH:MM format)  
- Last column: Reference ranges with units
- Values can be numeric, "----" (missing), or special text values

### Testing Local Changes
```bash
# Start local server for testing
uv run python -m http.server 8000

# View application at:
# http://localhost:8000/index.html
```

## Data Categories and Groupings
The application organizes analytes into functional groups:
- **Inflammatory**: Proteína C reativa, Calprotectina  
- **Hematology**: Complete blood count parameters
- **Kidney**: Creatinina, Ureia
- **Liver**: Liver function tests (TGO, TGP, Bilirubin, etc.)
- **Electrolytes/Minerals**: Sodium, Potassium, Calcium, etc.
- **Lipids**: Cholesterol panel
- **Hormones**: Thyroid, reproductive hormones
- **Vitamins**: B12, Folate, Vitamin D

## Browser Compatibility
- Requires modern browser with ES6+ support
- Uses Plotly.js CDN for charting
- Implements manual file picker fallback for local file:// access

## Data Privacy
- No server-side storage or processing
- All analysis happens client-side
- Patient information should be anonymized in CSV data
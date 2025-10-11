# Quarto Multi-Page Site Setup

This document describes the Quarto configuration for the maladie health tracking website.

## Structure

The site is now a multi-page Quarto website with the following pages:

- **Home** (`/` or `/index.html`) - The main page from README.md containing supplement schedule and health goals
- **Blood Markers** (`/blood.html`) - Interactive blood test results visualization
- **Medications** (`/meds.html`) - Medication and supplementation timeline visualization

## Files Created

### Configuration
- `_quarto.yml` - Main Quarto configuration file

### Page Files
- `index.qmd` - Copy of README.md, serves as the home page
- `blood.qmd` - Page that embeds the blood markers visualization
- `meds.qmd` - Page that embeds the medications timeline

### Standalone HTML Files (embedded via iframe)
- `blood_markers.html` - Original index.html with blood markers analysis
- `meds.html` - Copy of meds_and_supplements/meds.html

### Data Files (automatically copied to docs/)
- `blood_markers_pivot.csv` - Blood test data
- `reports.json` - Medical reports metadata
- `meds_and_supplements/med_schedule.json` - Medication schedule data

## Building the Site

To rebuild the site after making changes:

```bash
quarto render
```

This will regenerate all HTML files in the `docs/` directory.

## Deployment

The site is configured to deploy to GitHub Pages from the `docs/` directory.

### GitHub Pages Settings
1. Go to repository Settings → Pages
2. Set Source to "Deploy from a branch"
3. Set Branch to "main" (or your default branch)
4. Set Folder to "/docs"
5. Save

The site will be available at: https://maladie.ronaldo.tech

## Maintenance

### Adding New Pages
1. Create a new `.qmd` file in the root directory
2. Add the page to the navbar in `_quarto.yml`
3. Run `quarto render` to regenerate the site

### Updating Data
- Update CSV/JSON files in the root directory
- The data files are automatically copied to `docs/` during render
- Run `quarto render` to update

### Modifying Standalone Visualizations
- Edit `blood_markers.html` or `meds.html`
- Run `quarto render` to copy changes to docs/

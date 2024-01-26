# Medicare-Part-D-Data-Analysis

# Drug Prescription Dashboard

## Overview
The Drug Prescription Dashboard is a sophisticated data filtering tool designed to analyze the most prescribed drugs in US hospitals. Its primary aim is to aid policy makers, healthcare professionals, data analysts, and researchers in the pharmaceutical industry in understanding prescription patterns, identifying top prescribed drugs, and exploring their associated costs and claims.

## Key User Groups
- **Data Analysts**: For in-depth analysis of prescription data and trends.
- **Healthcare Professionals**: To understand drug usage patterns and support clinical decisions.
- **Researchers in the Pharmaceutical Industry**: For researching drug popularity and usage.
- **Policy Makers in the Healthcare Sector**: To inform decisions on drug subsidy and healthcare policies.

## User Objectives
- **Understand Prescription Patterns**: Analyze Medicare Part D prescription patterns at the state level.
- **Identify Top Prescribed Drugs**: Discover the most commonly prescribed drugs and analyze their costs.
- **Explore Correlations**: Investigate the relationship between prescribers, total claims, and drug usage.

## Features
- **Interactive Visualizations**: Heatmaps and bar charts for easy interpretation of data.
- **Search Functionality**: Allows users to look up specific drugs and view detailed data.
- **Dockerization**: Ensures easy deployment and environment consistency.
- **GitHub Codespaces Compatibility**: Facilitates development and deployment directly via GitHub.
- **RESTful API Integration**: Supports both POST and GET methods for efficient data handling.
- **FHIR Data Format**: Utilizes FHIR bundle format for medical data representation.

## Installation and Setup
Ensure Docker is installed on your system before proceeding.
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Yllezaahmeti/Medicare-Part-D-Data-Analysis
   ```
2. **Navigate to the Project Directory**:
   ```bash
   cd Medicare-Part-D-Data-Analysis
   ```
3. **Build the Docker Image**:
   ```bash
   docker build -t drug-prescription-dashboard .
   ```
4. **Run the Docker Container**:
   ```bash
   docker run -p 5000:5000 drug-prescription-dashboard
   ```

## Usage
1. **Accessing the Dashboard**: Navigate to `http://localhost:5000` in your browser.
2. **Searching for Drugs**: Use the search box to find data on specific drugs.
3. **Interacting with Visualizations**: Click and hover over the charts for more details.

## Data Structure
The FHIR bundle JSON data is structured as follows:
```json
{
    "resourceType": "Bundle",
    "type": "collection",
    "entry": [
        {
            // Data Entries
        }
    ]
}
```
*Data included in `static/data/fhir_bundle.json`.*

## Contributing
Interested in contributing? Here's how you can help:
1. Fork the repository.
2. Create a new feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -am 'Add some YourFeature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Create a new Pull Request.

## License
This project is released under the [MIT License](LICENSE).

## Contact
- **Name**: [Ylleza.ahmeti@stud.th-deg.de](mailto:Ylleza.ahmeti@stud.th-deg.de)
- **Project Link**: [https://github.com/Yllezaahmeti/Medicare-Part-D-Data-Analysis](https://github.com/Yllezaahmeti/Medicare-Part-D-Data-Analysis)

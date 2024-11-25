Comparative Analysis of Ad Blockers and Their Effectiveness
===========================================================

This repository provides a comprehensive analysis of various ad blockers, including Adblock Plus, uBlock Origin, AdBlock, and Ghostery. The study was conducted across four devices (two Windows and two macOS) to ensure consistency.

Repository Structure
--------------------

-   **Browser Extensions**:

    -   `adblock_plus.crx`
    -   `ublock_origin.crx`
    -   `adblock.crx`
    -   `ghostery.crx`
-   **Data Files**:

    -   `combined_adblock_data.csv`
    -   `combined_ublock_data.csv`
    -   `summary_adblocker_analysis.csv`
-   **Python Scripts**:

    -   `adblock_final.py`
    -   `csv_combine.py`
    -   `data_2.py`
-   **Documentation**:

    -   `README.md`

Browser Extensions
------------------

The `.crx` files are Chrome extension packages for the respective ad blockers. To test with different ad blockers, you can download and install these files in your Chrome browser.

Data Collection
---------------

Data was collected by running tests on four devices:

-   2 Windows machines
-   2 macOS machines

This approach ensured consistency and reliability in the analysis.

Python Scripts
--------------

The repository includes several Python scripts used for data processing and analysis:

1.  **`adblock_final.py`**:

    -   **Purpose**: Processes raw data collected from the ad blockers and performs initial analysis.
    -   **Usage**:

        bash

        Copy code

        `python adblock_final.py`

    -   **Dependencies**:
        -   `pandas`
        -   `numpy`
2.  **`csv_combine.py`**:

    -   **Purpose**: Merges multiple CSV files into a single file for consolidated analysis.
    -   **Usage**:

        bash

        Copy code

        `python csv_combine.py`

    -   **Dependencies**:
        -   `pandas`
3.  **`data_2.py`**:

    -   **Purpose**: Performs advanced data analysis and visualization on the combined data.
    -   **Usage**:

        bash

        Copy code

        `python data_2.py`

    -   **Dependencies**:
        -   `pandas`
        -   `matplotlib`
        -   `seaborn`

How to Run the Scripts
----------------------

1.  **Clone the Repository**:

    bash

    Copy code

    `git clone https://github.com/Anish7-anish/Comparative-Analysis-of-Ad-Blockers-and-Their-Effectiveness.git`

2.  **Navigate to the Directory**:

    bash

    Copy code

    `cd Comparative-Analysis-of-Ad-Blockers-and-Their-Effectiveness`

3.  **Install Dependencies**: Ensure you have Python installed. Install the required Python packages using pip:

    bash

    Copy code

    `pip install pandas numpy matplotlib seaborn`

4.  **Run the Scripts**: Execute the scripts in the following order:

    bash

    Copy code

    `python adblock_final.py
    python csv_combine.py
    python data_2.py`

Each script will process the data and generate outputs accordingly.

Notes
-----

-   Ensure that the CSV files are in the correct format and located in the appropriate directories as expected by the scripts.
-   Review the scripts for any hardcoded paths or specific configurations that may need adjustment based on your environment.

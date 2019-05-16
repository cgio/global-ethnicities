![Global Ethnicities](logo-500px.png)

## Background

This project, Global Ethnicities, exists because an alternative comprehensive list of ethnicities does not. Multiple, reputable sources are used to generate a list of 750+ world ethnicities in various formats: TXT, JSON, CSV, and YAML.

Want to go straight to the list? Visit the **output** folder. If you want a specific list, for example, ethnicities from the U.S. United States Census Bureau only, see sources_local/census.txt.

Why use multiple sources? Single ethnicity lists or databases are often incomplete. For example, the data retrieved by **ipums.py** excludes Navajo but includes Cherokee. This is remedied by the inclusion of **reld.txt**, a list of ethnicities from the National Academies, which would also be incomplete on its own.

### Structure

* **main.py**: A Python script that generates ethnicity lists through aggregating local and remote sources. These sources are all of the TXT files in **sources_local** and all of the Python scripts in **sources_remote**. 

* **config**: a folder containing configuration files. Mainly, you may want to edit **exclude.py** in case the generated ethnicity lists contain ethnicities you may want to exclude (e.g. U.S. state names). If any ethnicities need spelling or other corrections, specify the corrections in **correct.py**. Ethnicities that demonstrably exist yet are not available from source files can be included in **include.py**.

* **output**: a folder containing the generated/master ethnicity lists in various formats.

* **sources_remote:** a folder containing Python scripts for execution by main.py. Each script retrieves remote ethnicity data and writes a TXT file containing ethnicities. If you want to write your own script for aggregating ethnicities from a specific source, feel free to use **ipums.py** as a reference and put your script in this folder. If the data source (a webpage) accessed via ipums.py significantly changed, ipums.py would require updating.

* **sources_local:** a folder containing ethnicity lists in TXT format. For example, **reld.txt** is included and explained below. In some cases, it may be preferable to copy and paste a reputable ethnicity list into a TXT file yourself rather than spend time writing a Python script for sources_remote.

## Data sources

### Remote

* **ipums.py**: Source(s): U.S. Census Bureau, IPUMS USA. Citation: *Steven Ruggles, Sarah Flood, Ronald Goeken, Josiah Grover, Erin Meyer, Jose Pacas, and Matthew Sobek. IPUMS USA: Version 9.0 [dataset]. Minneapolis, MN: IPUMS, 2019. https://doi.org/10.18128/D010.V9.0*

### Local

* **reld.txt**: Source(s): Institute of Medicine of the National Academies. Citation: *Institute of Medicine (US) Subcommittee on Standardized Collection of Race/Ethnicity Data for Healthcare Quality Improvement; Ulmer C, McFadden B, Nerenz DR, editors. Race, Ethnicity, and Language Data: Standardization for Health Care Quality Improvement. Washington (DC): National Academies Press (US); 2009. Appendix G, Kaiser Permanente: Evolution of Data Collection on Race, Ethnicity, and Language Preference Information. Available from: https://www.ncbi.nlm.nih.gov/books/NBK219763/ Race, Ethnicity, and Language Data: Standardization for Health Care Quality Improvement. See https://www.ncbi.nlm.nih.gov/books/NBK219763/.*

* **census.txt** Source(s): United States Census Bureau, https://factfinder.census.gov/faces/nav/jsf/pages/searchresults.xhtml?refresh=t

    The ethnicities in census.txt were obtained via:

        1. Visit the U.S. Census Bureau American FactFinder URL listed above.

        2. Create a file called SearchResults.aff with the following contents:

        <query schema-version="1.0" lang="en" type="search" sig="fjkp5NmRDhl57U6_H-cM86XSbcw">
          <search-config>
            <topic-search dimension-name="d_people_age_and_sex" dimension-value-name="Age"/>
            <category-search type="popgroup" id="-00" name="All available races"/>
          </search-config>
        </query>

        3. Using the panel on the left of the FactFinder website, upload the search file. This produces a search with data associated with "All available races". Download the data as CSV. 
        
        4. Format the data to resemble census_csv.txt. Note that a trivial processing script for FactFinder CSV data has been excluded for succinctness.

## Formatting

Do you have your own script or a list from a reliable source? Please follow these general formatting rules to keep your data consistent.

1. For formatting examples, please refer to **ethnicities.txt** in the output folder.

2. When in doubt, consider how most end-users will likely search for ethnicity.

3. Remote and local source files must produce valid TXT, CSV, JSON, and YAML output.

4. Use Pythonic file names for all source file names. 

5. Try to be inclusive and historically respectful. For example, for historical reasons, Czech and Czechoslovakian are listed separately. Some individuals may prefer to identify as one rather than the other.

## Notes

* Ethnicities may be included for non-existent countries. Some individuals may choose to identify as such regardless of country status.

* From first-hand experience, I can attest that U.S. state names (e.g. Florida) are commonly selected as ethnicities over other applicable choices, e.g. Cuban American. In some cases, U.S. state names may be considered invalid ethnicities. For convenience, exclude.py has a list of state names that may be uncommented for exclusion. However, U.S. state names are included by default.

* Consider adding "Other" and "Other combination" ethnicity options with an input area to capture ethnicities or variations. 

* In some cases, exclusion of generalized ethnicities such as "Two or more races" may be preferred.

* U.S. Census Bureau's American FactFinder will be obsolete after June 2019. Use data.census.gov instead.

## Contribute

Have a correction or suggestion? Please make a submission or pull request.

## License

With written attribution visible to end-users, you may use this project for any purpose. Please include my name (Chad Gosselin) and the GitHub URL (https://github.com/cgio/global-ethnicities).

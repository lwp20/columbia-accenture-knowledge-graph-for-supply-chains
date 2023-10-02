"""
John Como 
Oct 1 2023 // Week 1 

Script to define functionality for scraping Google Scholar PDF's. 

Package Documentation : https://github.com/ferru97/PyPaperBot

Be sure to follow instructions to bring PyPaperBot into local env. 
"""
import os

def scrape_google_scholar(query: str,
                          scholar_pages: str,
                          download_dir: str,
                          min_year: int,
                          ):
    """
    Wrapper for cmd line call for Google Scholar sraper

    Params:
        query : Query to be submitted to Google scholar
        scholar_pages : Number of pages to inspect. Each page has maximum of 10.
                        Total possible papers upper bounded by (scholar_pages x 10)
        download_dir : Directory to place downloaded files
        min_year : Minimum publication year to download

    Returns
        None
    """
    query_str = f'"{query}"'
    download_str = f'"{download_dir}"'

    cmd = f'python -m PyPaperBot --query={query_str} --scholar-pages={scholar_pages} --min-year={min_year} --dwn-dir={download_str}'

    os.system(cmd)

# Sample call
scrape_google_scholar(query = "supply chain",
                      scholar_pages = 1,
                      download_dir=f"{os.getcwd()}",
                      min_year = 1950)

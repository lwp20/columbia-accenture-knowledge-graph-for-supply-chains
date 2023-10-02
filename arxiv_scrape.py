# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 14:55:05 2023

@author: zhang
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 14:52:39 2023

@author: zhang
"""

from paperscraper.arxiv import get_and_dump_arxiv_papers

from paperscraper.pdf import save_pdf_from_dump


"""covid19 = ['COVID-19', 'SARS-CoV-2']
ai = ['Artificial intelligence', 'Deep learning', 'Machine learning']
mi = ['Medical imaging']
query = [covid19, ai, mi]
get_and_dump_arxiv_papers(query, output_filepath='covid19_ai_imaging.jsonl')
save_pdf_from_dump('covid19_ai_imaging.jsonl', pdf_path='.', key_to_save='doi')
"""
sc=["supply chain"]
field=["industry","economics","finance"]
query=[sc,field]
get_and_dump_arxiv_papers(query, output_filepath='supply_chain.jsonl')













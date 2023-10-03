# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 14:55:05 2023

@author: zhang
"""

import arxiv

import numpy as np
test_query="au:del_maestro ANDNOT (ti:checkerboard OR ti:Pyrochlore)"
query="ti:%22supply+chain%22+AND+cat:econ qfin"

titles=[]
def scrape_pdf(title,categories,max_results):
    category_condition = " OR ".join(["cat:" + c for c in categories])
    ti_condition = " AND ".join(["ti:" +"\""+c+"\"" for c in title])
    abs_condition = " AND ".join(["abs:" +"\""+c+"\"" for c in title])
    query="("+"("+abs_condition+")"+"OR"+"("+ti_condition+")"+")"+" AND "+"("+category_condition+")"
    print(query)
    search = arxiv.Search(
      query = query,
      max_results = max_results,
      sort_by = arxiv.SortCriterion.Relevance
    )
    count=0
    for result in search.results():
        titles.append(result.title)
        title="_".join(result.title.split())
        #result.download_pdf()
        try:
            result.download_pdf()
            count=count+1
        except:
            pass
        
        if count%10==0:
            print(count)
            print(result.title)
    print(count)
title=["supply chain"]
categories=["econ.EM","econ.GN","econ.TH","stat.AP","q-fin.EC","q-fin.GN"]
scrape_pdf(title,categories,100)

titles=np.array(titles)
np.save("titles.npy",titles)











# Knowledge Graph for Supply Chains

### Group members Name UNI 
- Weipeng Li wl2864 (Team captain)
- Yunjie Qian yq2354
- Ruochen Zhang rz2597
- Lingjun Zhang lz2873
- John Thomas Como jtc2182

Emails  wl2864@columbia.edu

**Accenture mentor & co-mentors:** Rajkumar Subramanian, Bikash Mahato, Tanusree De

**Instructor/CA:** Vivian Zhang, Ju-Chin Chao

The project aims to address the complex challenges in supply chain management and inventory decisions through the innovative solution, KnowledgeGraph+. By seamlessly integrating cutting-edge Large Language Models (LLMs) with Knowledge Graphs, the project aims to redefine efficiency and optimization in various industries.

![4](https://github.com/lwp20/columbia-accenture-knowledge-graph-for-supply-chains/assets/111889976/b2fa5a1f-b6f2-4675-a700-f3fe51439c27)


Overall, we built a Q&A system leveraging the LLM's understanding of user queries and the extracted relevant content, personalized recommendations will be provided to the users.We also evaluated the level of hallucinations of different LLMs using triplets extracted from relevant content and answers,providing qualitative and quantitive analysis.

![model](https://github.com/lwp20/columbia-accenture-knowledge-graph-for-supply-chains/assets/111889976/2029c11d-4cb3-4991-9df6-8a1975fe8e64)


According to our research, adding a knowledge graph improves the quality of question answering with large language models by including more related information while reducing hallucination. Besides, larger models tend to have a lower level of hallucination. Further work will focus on optimizing the knowledge graph with more data to further improve the chatbot.

**Directory tree**
```
│   README.md
| 
├───codes
│       chatbot_triplet_pipeline.ipynb
├───────data_collection
│         arxiv_scrape.py
│         google_chrome_scraper.py
├───────divided_models
│         Llama2_inference.ipynb
│         Sparql_Generation.ipynb
├───────evaluation
│         evaluation.ipynb
├───────knowledge_graph
│         Triple_Extraction_with_BLOOM_Neo4j.ipynb
│         Triple_Retrieval_Workflow.ipynb
├───────text-extraction_embedding
│         Text Extraction.ipynb
│         Text_Splitting.ipynb
│         sentence_embedding_pipeline.ipynb
```

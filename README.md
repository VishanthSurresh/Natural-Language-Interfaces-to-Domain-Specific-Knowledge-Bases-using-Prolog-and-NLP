# COMP-6591---Introduction-to-Knowledge-Base-Systems
Course Project on Natural Language Interfaces to Domain Specific Knowledge Bases using Prolog and NLP


![Knowledge Base System](https://user-images.githubusercontent.com/35566310/185734682-91f8649f-95dc-4c89-b9c1-ce7345f51356.jpg)

#### Introduction

<p align="justify">
The knowledge-based configuration has been used in numerous applications, with natural language processing being just one of them (NLP). It can be challenging to apply one's skills and expertise to choose the optimal model from among the dataset that are often created and useful for machine learning applications. Making sense of unstructured data sets using natural language processing (NLP) enables the automation of crucial decision-making procedures that would otherwise demand time and labour to complete manually. The task of natural language inference (NLI), which has attracted a lot of interest in the field of natural language processing, is to determine if one statement logically implies another. Making software that can comprehend natural language is difficult.\cite{rohil2018natural} The reasoning program should be knowledgeable about both general knowledge and the viewpoints, goals, and objectives of its users. The declarative nature of Prolog makes it potentially simple to write grammar based on the user's objectives. As some of the capabilities of unification and backtracking processes are more suited to NLP, Prolog is appropriate for the construction of natural language interfaces for software applications. Using examples from the domain, such as a small vocabulary, few relationships, and the majority of users making simple queries, we demonstrate how creating NLI for domain-specific knowledge bases and databases is relatively easier.
</p>

#### Overall Architecture

![image](https://user-images.githubusercontent.com/35566310/185734775-cfc4974d-8b56-4dbc-970a-34bcade6b74e.png)

#### Working
1. Obtain the user input as a string.
2. Once the input is read, the program uses the NLTK libraries to pre-process the text. Stemming, lemmatization, emoji conversion, and stop words removal are all          included in pre-processing.
3. Cleaned, error-free data after pre-processing is received.
4. The Pyswip module in Python, which links Python with Prolog, is used to feed this data as input to Prolog.
5. Based on the user’s input its respective prolog rules and queries are called.
6. Prolog returns the findings.

#### Steps to run the Application

Step 1: You can use any one of the IDE to run the Application [Pycharm, Spyder]. <br/>
Step 2: Create a Python file. <br/>
Step 3: Import the following Libraries <br/>
   &emsp; &emsp; &ensp;     1. Pyswip <br/>
   &emsp; &emsp; &ensp;     2. NLTK <br/>
   &emsp; &emsp; &ensp;     3. Pandas <br/>
   &emsp; &emsp; &ensp;     4. re <br/>
Step 4: Copy paste the entire code. <br/>
Step 5: Right click on the file and click RUN or under RUN tab click Run. <br/>
Step 6: Console will ask user to enter the Input. <br/>
Step 7: Enter the Input. <br/>
Step 8: Console gives the Output. <br/>
Step 9: To Exit, Click STOP from Console. <br/>

#### Areas of Knowledge Base System Utilized
1. Prolog facts, rules & queries.
2. Complex structures.
3. Lists & it’s manipulation.
4. Extended logic programming – Python.
5. Categorial syllogism.

#### Conclusion
An integration between the logical programming of Prolog and the most widely utilized scripting language Python have been performed in this paper. It provides us a wide array of learning experiences, both with Prolog and NLP.

#### Future Work
<p align="justify">
As per the current implementation, we have utilised dictionaries to identify the elements in the periodic table. For future work. we can train an NLP model to automatically detect the names of elements as soon as the user types. This reduces the threshold of storing additional hard-coded data and leverages the use of more powerful NLP concepts. 
</p>



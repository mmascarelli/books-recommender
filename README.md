# Project Overview
* Using data from Goodreads, I built a recommedation system using cosine similarity. A simple webapp was also built using Flask.
<br/>
<img width="545" alt="image" src="https://github.com/mmascarelli/books-recommender/assets/116842582/0efda8a2-1c03-4379-be04-5ae264dde6f3">



# The Data
1. User Data:
   
2. Book Data:
   
3. Author Data:
   
Data Source: https://mengtingwan.github.io/data/goodreads.html#datasets


# Cosine Similarity
The data was set up with every row being a unique book and every column being a unique user. Cosine similarity was used to find similarity scores for every book. 
<br/>


<img width="455" alt="image" src="https://github.com/mmascarelli/books-recommender/assets/116842582/a24680d0-94e1-40fe-b3aa-9c696fd69be7">


# Web App
The web app was built using the python library Flask. Typing in the name of a book results in a page with 50 recommended books with the title, author, and image (if available).

<br/>

<img width="669" alt="image" src="https://github.com/mmascarelli/books-recommender/assets/116842582/85650eb7-cea9-4f61-a77f-1d2f2a8c2260">

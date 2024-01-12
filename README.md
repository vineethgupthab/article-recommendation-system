# Article recommendation system

## Project Overview

This project aims to create a simple article recommendation engine using word vectors (word2vec), specifically leveraging Stanford's GloVe project. The recommendation engine is complemented by a web server that displays a list of BBC articles and provides recommendations for related articles.

## Project Structure

The project is divided into two parts:

### Part 1: Building the Recommendation Database

- **File:** `doc2vec.py`
- **Objective:** Implement functions to build a database of recommendations.
- **Instructions:**
  - Download the GloVe word vectors and BBC articles dataset.
  - Run `python doc2vec.py ~/data/glove.6B.300d.txt ~/data/bbc`.
  - Verify the generation of `articles.pkl` and `recommended.pkl` files.
 
### Part 2: Implementing the Web Server

- **File:** `server.py`
- **Templates:**
  - `templates/articles.html`
  - `templates/article.html`
  - *Instructions:**
  - Implement Flask routes for the main list of articles and individual article pages.
  - Use Jinja2 template language to generate HTML for the web pages.
 

### Home Page Would look like the following image
<img width="1404" alt="Screenshot 2024-01-11 at 6 48 09 PM" src="https://github.com/vineethgupthab/article_recommendation/assets/138868502/ff687f6c-53f2-4c02-a570-2dab69d7af0a">

### If you click on any article, it will be redirected to the specific article and opens the content of the article on the left along with the similar articles suggested by our recommendation system to the right.
<img width="1443" alt="Screenshot 2024-01-11 at 6 48 30 PM" src="https://github.com/vineethgupthab/article_recommendation/assets/138868502/01b9ca68-889a-4620-99ac-199e020c447d">

## Discussion
### Article Word-Vector Centroids
- The recommendation engine relies on word vectors to determine the similarity between articles. The centroid of a document's cloud of word vectors is computed, and related articles are identified based on proximity in the 300-dimensional space.

## Efficiency of Loading the GloVe File
### Efficient memory usage is crucial when processing the GloVe file. It is recommended to process the file one line at a time to optimize memory consumption.

### Customization:
- You could use this project as a template to build similar or advanced recommendation system. You should be able to have the data in the ~/data folder (in the Home folder) then then follow Part 1 and Part 2 instructions.
- You may be required to make small changes in the `articles.py` or `server.py` codes.

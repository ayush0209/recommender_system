# recommender_system
The recommender system is based on user based collaborative filtering approach.

# detailed description
Providing recommendations to any user (let's say x) generally requires to rank all predicted ratings. In user based collaborative filtering, the approach to predict the rating of a particular item (let's say y) for user x is based on simple idea, which is to find users similar to user x who have previously rated the item y.
Predicted rating is simply a weighted average of ratings of similar users, with weights being the similarity score. The similarity score of two users is calculated by projecting users in items vector space and taking cosine of angle between two user vectors. 

This project implements the user based collaborative filtering method described above.  Evaluation metrics used to analyze the performance of built model are Root Mean Squared Error (RMSE), Precision @ Top K and Spearman Rank Correlation.

# installation
The requirements for running this program on your local machine are as follows-
1. Python 3.7 need to be installed on your machine.
2. The inbuilt libraries in Python to be installed are -
   xlrd, math, numpy, scipy, timeit, random, sklearn, multiprocessing
  
# usage
Download all the required files and dataset need to be present in the same folder where files containing code are present.
Run the program by executing command "python recommend.py" on your terminal or command prompt.

# assumptions
1.	For calculation of precision @ top K, the threshold rating for recommendation and relevance is taken to be 3.5.
2.	Minimum 10 users were used as neighbors for estimating the rating in Collaborative Filtering.
3. Before calculating the simlarity score, the ratings have been averaged out across users to handle generous and strict raters.

# recommender_system
The recommender system is based on user based collaborative filtering approach.
# detailed description
Providing recommendations to any user (let's say x) generally requires to rank all predicted ratings. In user based collaborative filtering, the approach to predict the rating of a particular item (let's say y) for user x is based on simple idea, which is to find users similar to user x who have previously rated the item y.
Predicted rating is simply a weighted average of ratings of similar users, with weights being the simlarity score. The simlarity score of two users is calculated by projecting users in items vector space and taking cosine of angle between two user vectors. 

This project implements the user based collaborative filtering method descibed above .Evaluation metrics used to analyze the performance of built model are Root Mean Squared Error (RMSE), Precision @ Top K and Spearman Rank Correlation.

# installation



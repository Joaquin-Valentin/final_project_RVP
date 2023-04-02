Final Bootcamp Project 
Ironhack Data Analytics Bootcamp


Restaurant viability predictor using data from Google Places API (6300 restaurants in the city of Madrid) and public data from (datos.madrid.es) to enrich the original dataset, information on income, population, rent prices, among other things.

Product roadmap:

Data Collection: Collect data on restaurants in the desired city including type of restaurant, rating, price level, concept, and geographical data. Also, gather information about demographics in the city.

Data Preprocessing: Clean and preprocess the data to make it suitable for modeling. This may include handling missing values, converting categorical data into numerical data, and normalizing continuous data.

Exploratory Data Analysis: Explore the data to gain insights into the relationships between various features and the target variable (restaurant ability to operate). This could involve creating visualizations and conducting statistical tests to identify patterns and relationships.

Feature Engineering: Create new features that can improve the performance of the model. This could include combining existing features, creating interaction terms, or transforming variables.

Model Selection: Select the best machine learning algorithm for the task by testing several models and comparing their performance. A Gradient Boosting Classifier was selected and trained with cross validation. SMOTE was used to correct imbalance.

Model Training: Train the selected model on the processed data to make predictions about the success of restaurants.

Model Evaluation: Evaluate the performance of the model using appropriate metrics such as accuracy, precision, recall (around 88-90%)

Deployment: Deploy the model, building a Flask app, creating a user-friendly interface that can be used by stakeholders to predict the viability of a restaurant concept in a given city. 


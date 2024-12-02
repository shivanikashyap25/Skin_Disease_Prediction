# My-Skin
ML model trained on DermaNet dataset to detect skin diseases connected to a telegram bot for familiar and user friendly interface

refer for machine learning model : https://www.kaggle.com/code/medianosandie/skin-diseases-classification/notebook

train and test data : https://www.kaggle.com/code/medianosandie/skin-diseases-classification/input

Steps to follow :

- open the ML_Model file in editor of your choice(i used jupyter notebook)
- download datasets from above links
- train your model(if you need it done quickly train it for a few diseases)
- after training completes save the ml model in your device
- open telegram_bot_interface.py and specifiy the path to the ML model saved in your device
- go to telegram, create a bot and get the api key
- paste the api key and run the python script 
- go to your telegram and start the bot


Skin Disease Prediction Web Application
This project is a web-based platform designed to predict skin diseases using machine learning models. The application provides users with an intuitive interface to upload images of skin conditions and receive diagnostic predictions, aiding early detection and management of skin diseases.

# Key Features:
Image Upload: Users can upload images of skin lesions or conditions directly through the interface.
Machine Learning Integration: The platform utilizes pre-trained machine learning models to analyze images and predict potential skin diseases.
Prediction Results: Displays the predicted skin condition along with confidence scores, helping users understand the likelihood of each diagnosis.
User-Friendly Interface: The design ensures ease of use, making it accessible to both medical professionals and general users.
Responsive Design: The platform is optimized for use across various devices, including desktops and mobile phones.

# Technical Aspects:
Front-End: Built using HTML, CSS, and JavaScript for a smooth user experience.
Back-End: Utilizes Python and frameworks like Flask to handle image processing and model predictions.
Machine Learning Models: Includes models trained on relevant datasets to provide accurate predictions.
Data Security: Ensures that user-uploaded images are handled securely and processed efficiently.

# Purpose:
The Skin Disease Prediction Web Application aims to facilitate early diagnosis and awareness of skin conditions. By leveraging machine learning, it provides users with insights that can prompt timely medical consultations and interventions.

This project demonstrates the potential of combining AI and healthcare, offering a valuable tool for both users seeking preliminary insights and developers interested in AI-driven healthcare solutions.

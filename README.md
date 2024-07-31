# Filmfinder: Your Personal Movie Maestro 


![Screenshot](movie.png)

## Overview
This project is a Movie Recommender System developed using Python, Pandas, scikit-learn, and difflib, with a user-friendly interface designed with Streamlit. The system provides precise movie recommendations based on cosine similarity and TF-IDF. The project demonstrates expertise in data processing and UX principles.

## Features
- **User-friendly Interface**: Built with Streamlit to ensure ease of use.
- **Accurate Recommendations**: Uses cosine similarity and TF-IDF to provide precise movie recommendations.
- **Enhanced User Input**: Utilizes difflib to improve user input handling.
- **Comprehensive Dataset**: Includes a detailed movie dataset for recommendations.

## Technologies Used
- **Python**: Core programming language.
- **Pandas**: For data manipulation and analysis.
- **scikit-learn**: For machine learning and similarity computations.
- **difflib**: For enhancing user input.
- **Streamlit**: For creating the web application interface.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/movierecommender.git
    ```
2. Navigate to the project directory:
    ```bash
    cd movierecommender
    ```
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the application:
    ```bash
    streamlit run app.py
    ```

## Usage
1. Open your web browser and go to `http://localhost:8501`.
2. Enter a movie name in the search box.
3. Get personalized movie recommendations based on the entered movie.

## How It Works
1. **Data Processing**: The movie dataset is loaded and preprocessed using Pandas.
2. **Feature Extraction**: TF-IDF is used to convert textual data into numerical features.
3. **Similarity Calculation**: Cosine similarity is calculated to find movies similar to the user input.
4. **User Input Enhancement**: difflib is used to handle user input variations and improve search accuracy.
5. **Recommendation Generation**: The system generates and displays a list of recommended movies based on the input.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

## Contact
If you have any questions or suggestions, please feel free to contact me at [shettyjanav@example.com](shettyjanav@example.com).


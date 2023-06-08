# ChatGPT with personal data (TEST)

## Description
This project utilizes the OpenAI API and langchain to enable "conversational interaction with your data". In this particular test, we work with a dataset of Red Bull beverages obtained from Kaggle, which can be found at this link: [Red Bull Dataset](https://www.kaggle.com/datasets/omarsobhy14/redbull-and-heart-rates).

## Project Structure
The repository is organized as follows:

### DATA
The `DATA` folder contains the `Redbull.csv` file, which is used to test the functionality of the langchain agent.

### CODES
The `CODES` folder contains a Jupyter notebook named `test.ipynb`, where users can experiment with the syntax and various ways of formulating questions.

Within the `CODES` folder, there is a subfolder `deployment` that houses an API implemented using FastAPI and uvicorn for deploying the chatbot in a production environment. The source code of the API and a file containing the pipeline and data preprocessing are included. The API can be executed using the following command: `uvicorn app.main:app --reload`

## Getting Started
To run the project, you need to have an `OPENAI_API_KEY`. Ensure you have set this key as an environment variable for added security.
### NOTE: 
The OpenAI API has a free trial quota. If you exceed it, you have to pay.

## Dependencies
Make sure you have the following dependencies installed:
- langchain
- OpenAI
- pandas
- tabulate
- fastapi
- uvicorn

*Specific versions on the `requirements.txt`*

## Usage
1. Set the `OPENAI_API_KEY` environment variable to your OpenAI API key.
2. Run the API using the command specified above (or directly from the jupyter notebook file).
3. Access the API endpoints to interact with the chatbot and explore the data.

## License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

import pandas as pd
import tabulate 
from langchain.agents import create_pandas_dataframe_agent
from langchain.llms import OpenAI
import os

# Get the OpenAI API key from the environment variable
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

# To track changes
__version__ = "0.0.1"

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('../../DATA/Redbull.csv')
# Drop unnecesary columns and rename the rest
df.drop(['Unnamed: 5','Volunteer_ID'],axis=1,inplace=True)
df.rename(columns={'agegrp':'Age Group',
                   'bp_before': 'BPM Before',
                   'bp_after': 'BPM After'
                  },inplace=True)

# Create a Langchain agent using the OpenAI language model and the DataFrame
agent = create_pandas_dataframe_agent(OpenAI(temperature=0.9,openai_api_key=OPENAI_API_KEY),df,verbose=False)
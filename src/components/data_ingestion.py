import os
import sys
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.logger import logging
from src.exception import CustomException




@dataclass
class DataIngestionConfig():

    train_path = os.path.join('artifacts', 'train.csv')
    test_path = os.path.join('artifacts', 'test.csv')
    raw_data_path = os.path.join('artifacts', 'raw.csv')




class DataIngestion():

    def __init__(self):

        self.ingestion_config = DataIngestionConfig()



    
    def initiate_data_ingestion(self):

        logging.info('Entered the data ingestion method')

        try:
            df = pd.read_csv(r"C:\Users\Priya Bhaskar\Machine learning projects\notebook\data\StudentsPerformance.csv")
            logging.info('data is being read and created dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            train_data, test_data = train_test_split(df, test_size=0.2, random_state=42)

            train_data.to_csv(self.ingestion_config.train_path, index=False, header=True)

            test_data.to_csv(self.ingestion_config.test_path, index=False, header=True)

            logging.info('Data ingestion has completed')

            return self.ingestion_config.train_path, self.ingestion_config.test_path
        


        

        except Exception as e:
            raise CustomException(e, sys)
        

if __name__ == '__main__':

    obj = DataIngestion()
    obj.initiate_data_ingestion()
            








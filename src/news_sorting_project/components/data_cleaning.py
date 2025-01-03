from src.news_sorting_project.entity.config_entity import DataCleaningConfig
from src.news_sorting_project.utils.common import save_object, save_csv
from src.news_sorting_project.constants import *
from sklearn.preprocessing import LabelEncoder
from src.news_sorting_project import logger
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from tqdm import tqdm
import pandas as pd
import string
import re 

# Define a dictionary of common contractions and their expanded forms
contractions_dict = {
    "isn't": "is not",
    "aren't": "are not",
    "can't": "cannot",
    "couldn't": "could not",
    "didn't": "did not",
    "doesn't": "does not",
    "don't": "do not",
    "hadn't": "had not",
    "hasn't": "has not",
    "haven't": "have not",
    "he'd": "he would",
    "he'll": "he will",
    "he's": "he is",
    "i'd": "I would",
    "i'll": "I will",
    "i'm": "I am",
    "i've": "I have",
    "i'd've": "I would have",
    "i'm": "I am",
    "let's": "let us",
    "mightn't": "might not",
    "must've": "must have",
    "mustn't": "must not",
    "needn't": "need not",
    "shan't": "shall not",
    "she'd": "she would",
    "she'll": "she will",
    "she's": "she is",
    "should've": "should have",
    "shouldn't": "should not",
    "that's": "that is",
    "there's": "there is",
    "they'd": "they would",
    "they'll": "they will",
    "they're": "they are",
    "they've": "they have",
    "wasn't": "was not",
    "weren't": "were not",
    "what's": "what is",
    "who's": "who is",
    "who've": "who have",
    "you'd": "you would",
    "you'll": "you will",
    "you're": "you are",
    "you've": "you have"
}


class DataCleaning:
    def __init__(self, config: DataCleaningConfig):
        self.data_cleaning_config = config
        self.stop_words = set(stopwords.words('english'))
   
    # Function to expand contractions in a text
    @staticmethod
    def expand_contractions(text):
        # Use regular expression to find contractions and replace them
        pattern = re.compile(r'\b(' + '|'.join(contractions_dict.keys()) + r')\b')
        expanded_text = pattern.sub(lambda x: contractions_dict[x.group()], text)
        return expanded_text
    
    @staticmethod
    def remove_curruncies(text):
        """
        removes different curruancies from text
        e.g., $1,000, ₹500, €10.99

        Args: text (str)

        Returns: text (str)
        """
        try:
            # Currency regex pattern (includes symbols and codes)
            currency_pattern = r'[\₹\$\€\¥\£\₣\₽]?\d{1,3}(?:,\d{3})*(?:\.\d+)?(?:[mbn]{1,2})?|\b(?:USD|EUR|INR|GBP|JPY|CAD|AUD|CNY)\b|[\₹\$\€\¥\£\₣\₽]'


            currency_free_text = re.sub(currency_pattern, '', text)

            return currency_free_text
        except Exception as e:
            raise e

    @staticmethod
    def remove_percentage(text):
        """ 
        removes percentages
        ex.,  25%, 5.5%, 1,000%
        """
        try:
            # Regex pattern to remove percentages
            percentage_pattern = r'\d{1,3}(?:,\d{3})*(?:\.\d+)?%'

            # Remove all percentage values
            cleaned_text = re.sub(percentage_pattern, '', text)

            return cleaned_text
        except Exception as e:
            raise e
        
    @staticmethod
    def remove_numbers(text):
        """ 
        removes numbers from text
        ex., 
        - Integers (e.g., 100, 20)
        - Decimals (e.g., 5.5, 1000.99)
        - Numbers with commas (e.g., 1,000, 1,000,000)
        """
        try:
            # Regex pattern to remove numbers
            number_pattern = r'\b\d+(?:,\d{3})*(?:\.\d+)?\b'

            # Remove all numbers
            cleaned_text = re.sub(number_pattern, '', text)

            return cleaned_text
        except Exception as e:
            raise e
    
    @staticmethod
    def remove_punctuation(text):
        """
        Removes all punctuation from the text.
        
        Args:
        text (str): Input string containing text with punctuation.
        
        Returns:
        str: Text with punctuation removed.
        """
        try:
            # Regex pattern to match any punctuation character
            punctuation_pattern = r'[' + re.escape(string.punctuation) + r']'
            
            # Replace all punctuation marks with an empty string
            cleaned_text = re.sub(punctuation_pattern, '', text)
            
            return cleaned_text
        except Exception as e:
            raise e
        
    @staticmethod
    def remove_special_characters(text):
        """
        Removes special characters (non-alphanumeric characters) from the text.
        
        Args:
        text (str): Input string containing special characters.
        
        Returns:
        str: Text with special characters removed.
        """
        try:
            # Regex pattern to match any character that is not a letter or a digit
            special_characters_pattern = r'[^a-zA-Z0-9\s]'  # Allow only letters, digits, and spaces
            
            # Replace all special characters with an empty string
            cleaned_text = re.sub(special_characters_pattern, ' ', text)
            
            return cleaned_text
        except Exception as e:
            raise e
        
    @staticmethod
    def remove_multiple_spaces(text):
        """
        removes multiple spaces
        """
        try:
            cleaned_text = re.sub(r'\s+', ' ', text)
            return cleaned_text
        except Exception as e:
            raise e
             
    # Define a function to process each text entry
    @staticmethod
    def remove_stopwords(text: str, stop_words: list):
        # Convert text to lowercase and split into words
        words = text.lower().split()
        
        # Remove stop words and punctuation
        words = [word.strip(string.punctuation) for word in words if word not in stop_words]
        
        # Return the cleaned text
        return ' '.join(words)
    
    @staticmethod
    def remove_distances(text):
        """
        Removes distances from the text (e.g., 30ft, 10m, 5km, etc.).
        
        Args:
        text (str): Input string containing distances.
        
        Returns:
        str: Text with distances removed.
        """
        try:
            # Regex pattern to match distances (integers or decimals followed by distance units)
            distance_pattern = r'\d+(?:\.\d+)?\s*(ft|m|km|cm|mm|yd|mi)\b'
            
            # Replace all occurrences of the distance pattern with an empty string
            cleaned_text = re.sub(distance_pattern, '', text)
            
            return cleaned_text
        except Exception as e:
            raise e
        
    @staticmethod
    def remove_centuries(text):
        """
        Removes centuries (e.g., 18th, 21st) from the text.
        
        Args:
        text (str): Input string containing centuries.
        
        Returns:
        str: Text with centuries removed.
        """
        try:
            # Regex pattern to match centuries (e.g., 18th, 21st, 5th, 20th)
            century_pattern = r'\d{1,2}(st|nd|rd|th)\b'
            
            # Replace all occurrences of centuries with an empty string
            cleaned_text = re.sub(century_pattern, '', text)
            
            return cleaned_text
        except Exception as e:
            raise e
    
    @staticmethod
    #Lemmatize the dataset
    def lemma_corpus(data, pos):
        lemmatizer=WordNetLemmatizer()
        out_data=""
        for words in data:
            out_data+= lemmatizer.lemmatize(words, pos)
        return out_data
    
    def data_preprocessing(self, text):
        try:
            # normalizing
            text = text.lower()

            # remove curruncies : businesss, entertainment
            text = self.remove_curruncies(text)

            # remove percentage : businesss
            text = self.remove_percentage(text)

            # remove distance : entertainment
            text = self.remove_distances(text)

            # remove conturies : entertainment
            text = self.remove_centuries(text)

            # remove numbers
            text = self.remove_numbers(text)

            # remove special characters
            text = self.remove_special_characters(text)

            # remove punctuations
            text = self.remove_punctuation(text)

            # remove multilpe spaces
            text = self.remove_multiple_spaces(text)

            # remove stopwords
            text = self.remove_stopwords(text, self.stop_words)

            # lemmatize
            text = self.lemma_corpus(text, 'v')

            return text
        except Exception as e:
            raise e


    def get_data_transformer_object(self):
        return LabelEncoder()
        
    def initiate_data_cleaning(self):   
        try:
            # loading data
            train_df = pd.read_csv(self.data_cleaning_config.raw_data_file)

            logger.info("Reading raw data file successfully!")

            # loading target encoder
            preprocessing_obj=self.get_data_transformer_object()

            # names of columns to consider
            target_column_name="Category"
            text_column_name = "Text"

            logger.info("Data Cleaning Started!")
            
            # process bar for each text processing
            clean_text = []
            for text in tqdm(train_df[text_column_name], desc="Cleaning Text"):
                clean_text.append(self.data_preprocessing(text))

            logger.info("Data Cleaned Successfully!")
            
            ## target encoding
            logger.info("Data Encoding Started!")

            encoded_target =preprocessing_obj.fit_transform(train_df[target_column_name])

            logger.info("Data Encoding Successfully!")


            clean_df = pd.DataFrame({
                "text": clean_text,
                "label": encoded_target
            })

            save_csv(clean_df, self.data_cleaning_config.clean_data_file)
            
            logger.info(f"Saved cleand data")


            save_object(
                obj=self.data_cleaning_config.preprocessing_obj,
                file_path=self.data_cleaning_config.preprocessing_obj
            )
            logger.info(f"Saved preprocessing object")

        except Exception as e:
            raise e
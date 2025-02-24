import rdkit
import numpy as np 
from typing import List, Union, Optional

class Preprocessor: 
    def load_data(self, filepath:str ) -> List: 
        """ 
        Function to read SMILES strings from a file
        Args: 
        - file_path: path to input file
        Returns: 
        - smiles_list (list)
        """
        try: 
            with open(filepath, 'r') as file:
                smiles_list = file.read().split()
        except:
            raise Exception(f"Failed loading file, raised excepcion: {Exception}")
        return smiles_list 
    
    def clean_smiles(self, smiles) -> List: 
        """
        Use RDKit for canonicalization and cleaning of SMILES
        
        Args:
        - smiles: str or list of smiles strings
        """

        if isinstance(smiles, str): 
            pass
        elif isinstance(smiles, list): 
            for smile in smiles: 
                pass
        else:
            raise TypeError(f"Only str and List are accepted, instead got: {type(smiles)}")

    def filter_smiles(self, smiles_list): 
        """
        Method to filter smiles list based on different criteria 
        (remove duplicates, unwanted characters...) 
        Args: 
        - smiles_list 
        - filter ({Duplicates})"""
        pass

    def process(self, filepath): 
        "Method combines loading, cleaning and filtering of smiles"
        pass


class Tokenizer:
    def __init__(self):
        self.preprocessor = Preprocessor()

    def __format__(self, format_spec):
        pass

    def build_vocab(self, smiles_list): 
        """
        Generate vocabulary (token-to-index mapping) from dataset
        
        Args:
        - smiles_list
        """
        # First build the vocabulary from the dataset
        vocab = set()
        for smiles in smiles_list:
            try:
                tokens = self.tokenize(smiles)
                vocab.update(tokens)
            except Exception as e:
                print(f"Problem with smiles {smiles}", e)

        # Encode vocabulary from str to index
        return vocab 
    
    def tokenize(self, smiles:str, multi_char_tokens:Optional[List[str]]=None) -> List[str]: 
        """
        Tokenizes a single SMILES string into a list of tokens,
        preserving multi-character atoms and stereochemistry tokens.
        
        Args:
        - smiles(str): A raw SMILES string (e.g., "C@@H")
        - multi_char_tokens(Optional[List[str]]): A list of strings containing multi character
        tokens e.g. "Cl", "Br", "Si"
        
        Returns:
        - tokens (List[str]): List of tokens representing the SMILES.
        e.g., ["C", "@@", "H"]
        """
        tokens = []

        i = 0

        # Default multi_car_tokens set 
        if multi_char_tokens is None:
            multi_char_tokens = {"Cl", "Br", "Si", "Li", "Na", "Al", "Se", "@@"}  
        while i < len(smiles):
            if i < (len(smiles) - 1) and smiles[i:i+2] in multi_char_tokens:
                tokens.append(smiles[i:i+2])
                i += 2
            else: 
                if smiles[i:i+1] not in tokens:
                    tokens.append(smiles[i:i+1])
                i += 1

        return tokens
 

    def detokenize(self, token_list): 
        """
        Convert list of token back into a SMILES string

        Args: 
        - token_list
        """
        pass

    def save_vocab(self, filepath): 
        """
        Save generated vocabulary

        Args:
        - filepath
        """
        pass

    def load_vocab(self, filepath): 
        """
        Load a previously saved vocabulary 

        Args:
        - filepath: Path to vocabulary to be loaded 
        """
        vocab = self.preprocessor.load_data(filepath=filepath)

        return vocab

         

def main(): 
    """
    Preprocessing pipeline
    """
    
    preprocess =  Preprocessor()
    smiles_list = preprocess.load_data("../data/smiles.txt") 


if __name__=="__main__":
    main()
import rdkit
import numpy as np 

class Preprocessor: 
    def __init__(self, filepath):
        self.file_path = filepath

    def load_data(self, filepath): 
        """ 
        Function to read SMILES strings from a file
        Args: 
        - file_path: path to input file
        """
        pass

    def clean_smiles(self, smiles): 
        """
        Use RDKit for canonicalization and cleaning of SMILES
        
        Args:
        - smiles
        """
        pass

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
        pass

    def __format__(self, format_spec):
        pass

    def build_vocab(self, smiles_list): 
        """
        Generate vocabulary (token-to-index mapping) from dataset
        
        Args:
        - smiles_list
        """
        pass
    
    def tokenize(self, smiles): 
        """
        Convert a SMILES string into a list of tokens of integer indice
        
        Args:
        - smiles
        """
        pass

    def detokenize(self, token_list): 
        """
        Convert list of token back into a SMILES string
        """
        pass

    def save_vocab(self, filepath): 
        """
        Save generated vocabulary
        """
        pass

    def load_vocab(self, filepath): 
        """
        Load a previously saved vocabulary 
        """
        pass

def main(): 
    """
    Preprocessing pipeline
    """
    pass


if __name__=="__main__":
    main()
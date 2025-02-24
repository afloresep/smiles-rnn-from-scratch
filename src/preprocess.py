import rdkit
import numpy as np 
from typing import List, Union, Optional, Dict, Tuple
import json

def _string_to_list_chars(string:str) -> List[str]:
    """Helper function to take a string and return a list of 
    characters based on SMILES alphabet. Multi-character 

    Args:
        string (str): 

    Returns:
        List[str]: List of characters from the string

    Example:  
    "CNNC(=O)C1=CC=C([N+](=O)[O-])N1C" -> ["C", "N", "N", "C", "(", "=", "O", ")",..., "C"]
    """
    str_token = [string[i:i+1] for i in range(len(string))]

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
    
    #TODO: Implement clean smiles
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

    #TODO: Implement filter smiles
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
        self.token2index: Dict[str, int] = {}
        self.index2token: Dict[int, str] = {}

    def __format__(self, format_spec):
        pass
 
    def build_vocab(self, smiles_list: List[str], return_dict: bool = False
        ) -> Optional[Tuple[Dict[str, int], Dict[int, str]]]:
    
        """
        Generate two vocabularies (token-to-index and index-to-token mapping) from dataset
        
        Args:
        - smiles_list: List[str]: List of smiles strings

        Returns:
        - token2index (Dict[str, int]): Mapping from token (str) to integer index.
        - index2token (Dict[int, str]): Mapping from integer index to token (str).
        """
        # Build the vocabulary from the dataset
        vocab = set()
        for smiles in smiles_list:
            try:
                # This method will treat each character as one int. For multicharacter support
                # one must pass a custom dict
                tokens = _string_to_list_chars(smiles)
                vocab.update(tokens)
            except Exception as e:
                print(f"Problem with smiles {smiles}", e)
        
        # Encode vocabulary from str to index
        index = 0
        
        # Create both dicts so its easier to then detokenize 
        token2index = {}
        index2token = {} 

        # Assign to each word a different integer
        for word in vocab:
            token2index[word] = index
            index2token[index] = word
            index += 1
            
        # Create self attribute so it can be used in other methods
        self.token2index = token2index
        self.index2token = index2token

        if return_dict: 
            return token2index, index2token

 
    def tokenize(self, smiles:str, vocab:dict = None) -> List[int]: 
        """
        Tokenizes a single SMILES string into a list of tokens,
        preserving multi-character atoms and stereochemistry tokens.
        
        Args:
        - smiles(str): A raw SMILES string (e.g., "C@@H")
        - vocab(dict): Vocabulary that allows tokenization str -> int. Can be 
        passed as argument or created with `build_vocab(smiles_list)`. Should have format
        dict[character] = int
        
        Returns:
        - tokens (List[int]): List of tokens representing the SMILES converted to integers using
        predefined vocabulary
        e.g., ["C", "@@", "H"] -> [1, 10, 5]
        """
        # Check if vocab is provided; otherwise, use self.vocab
        if vocab is None:
            if self.index2token is None:
                raise TypeError(
                    "Vocabulary is required but was not provided. "
                    "Either call `build_vocab(smiles_list)` first or pass a `vocab` argument."
                )
            vocab = self.index2token # Use self.vocab if available

        # First we split the smiles into separated chars
        string_tokens = _string_to_list_chars(smiles)
        
        index_tokens = []
        for string in string_tokens:
            index_tokens.append(self.token2index[string])
 
        return index_tokens


    def detokenize(self, tokenize_smiles:List[int], vocab:dict = None) -> str: 
        """
        Convert list of token back into a SMILES string

        Args: 
        - token_list: List[int]: List of tokens integers to be converted to detokenize
        i.e. converted back to SMILEs
        - vocab: dict: Vocabulary that allows detokenization int -> str. Can be passed as argument
        """
        # Check if vocab is provided; otherwise, use self.vocab
        if vocab is None:
            if self.index2token is None:
                raise TypeError(
                    "Vocabulary is required but was not provided. "
                    "Either call `build_vocab(smiles)` first or pass a `vocab` argument."
                )
            vocab = self.index2token # Use self.vocab if available


        detokenize_smiles = []
        for token in tokenize_smiles: 
            detokenize_smiles.append(self.index2token[token])
        
        # Join list of characters into a single smiles
        smiles = ''.join(detokenize_smiles)

        return smiles
        

    def save_vocab(self, 
        filepath: str,
        token2index: Dict[str, int]=None,
        index2token: Dict[int, str]=None,
    ) -> None:
        """
        Saves vocabulary dictionaries to a JSON file.

        Args:
        - token2index (Dict[str, int]): Mapping from token (str) to integer ID.
        - index2token (Dict[int, str]): Mapping from integer ID back to token (str).
        - filepath (str): Output file path (e.g., "vocab.json").
        """

        # Logic to check whether the dicts are self attributes or passed as arguments
        # ---------------------------------------------------------------------------
        if token2index is None: 
            # If there's not a `self` attribute for both or one of them, raise Error
            if self.token2index is None: 
                raise TypeError(
                    "No token2index found or provided "
                    "Either call `build_vocab(smiles)` first or pass a `token2index` argument.")
            token2index = self.token2index 

        if index2token is None:
            if self.index2token is None:
                raise TypeError(
                    "No index2token found or provided "
                    "Either call `build_vocab(smiles)` first or pass a `index2token` argument.")
            index2token = self.index2token

        # Save vocabulary in JSON 
        #------------------------------
        vocab_data = {
            "token2index": token2index,
            "index2token": {str(k): v for k, v in index2token.items()} # JSON does not support int keys
        }

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(vocab_data, f, ensure_ascii=False, indent=2)


    def load_vocab(self, filepath: str) -> (Dict[str, int] | Dict[int, str]):
        """
        Loads vocabulary dictionaries from a JSON file.

        Args:
        - filepath (str): Path to the JSON file (e.g., "vocab.json").

        Returns:
        - token2index (Dict[str, int]): Mapping from token (str) to integer ID.
        - index2token (Dict[int, str]): Mapping from integer ID back to token (str).
        """
        with open(filepath, "r", encoding="utf-8") as f:
            vocab_data = json.load(f)
        token2index = vocab_data["token2index"]
        index2token = {int(k): v for k, v in vocab_data["index2token"].items()}
        self.token2index = token2index
        self.index2token = index2token


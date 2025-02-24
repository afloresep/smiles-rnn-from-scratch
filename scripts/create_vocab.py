# Script to create the JSON file for the vocabulary 
# from a text file where each line is a different entry 
# in the SMILES alphabet


def create_vocab_json(input_file: str, output_file: str) -> None:
    import json
    from typing import Dict
    import os
    """
    Creates a JSON file containing 'token2index' and 'index2token' dictionaries.
    Assumes each line in 'input_file' contains a single character/token.
    
    Args:
    - input_file (str): Path to the text file with one token per line.
    - output_file (str): Path to the JSON file where vocab will be saved.
    
    Returns:
    - None
    """
    with open(input_file, "r", encoding="utf-8") as f:
        tokens = [line.strip() for line in f if line.strip()]
    
    token2index: Dict[str, int] = {}
    index2token: Dict[int, str] = {}
    
    for idx, token in enumerate(tokens):
        token2index[token] = idx
        index2token[idx] = token
    
    vocab_data = {
        "token2index": token2index,
        "index2token": {str(k): v for k, v in index2token.items()}
    }
    
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(vocab_data, f, ensure_ascii=False, indent=2)

    print("file saved at", os.path.abspath(output_file)) 

if __name__=="__main__":
    create_vocab_json(input_file="your_path", output_file="vocab.json")
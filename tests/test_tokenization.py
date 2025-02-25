from src.preprocess import Preprocessor, Tokenizer

def test_tokenize_and_detokenize():
    # Given: a tokenizer instance and a sample SMILES string
    tokenizer = Tokenizer()

   #TODO: ADD LOAD VOCAB FROM DATA TO TEST TOKENIZER 
    smiles_list = [
        "C[C@@H](N)Cl",        
        "CC(C)Cc1ccc(C)cc1",  
        "[Na+].[Cl-]",       
        "C1=CC=CC=C1"       
    ]
    
    for smiles in smiles_list:
        tokenized_smiles = tokenizer.tokenize(smiles)
        reconstructed_smiles = tokenizer.detokenize(tokenized_smiles)
        
        assert reconstructed_smiles == smiles, (
            f"Detokenized SMILES '{reconstructed_smiles}' does not match original '{smiles}'"
        )
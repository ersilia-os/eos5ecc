# Initializing and importing necessary libararies
import tensorflow as tf
from rdkit import Chem
import os
import pystow
import pickle
import re
from repack import helper
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"


# Print tensorflow version
print("Tensorflow version: "+tf.__version__)

# Always select a GPU if available
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

# Scale memory growth as needed
gpus = tf.config.experimental.list_physical_devices("GPU")
for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu, True)

#Modified Carolina-carcablop
# current file directory
root = os.path.dirname(os.path.abspath(__file__))
pystow_home = os.path.abspath(os.path.join(root, "..",".."))

os.environ['PYSTOW_HOME']= pystow_home

# checkpoints directory
default_path= pystow.join("checkpoints")

# Load the packed model forward
reloaded_reverse = tf.saved_model.load(default_path.as_posix()+"/translator_reverse")

def translate_reverse(iupacname: str) -> str:
    """Takes user input splits them into words and generates tokens.
    Tokens are then passed to the model and the model predicted tokens are retrieved.
    The predicted tokens gets detokenized and the final result is returned in a string format.

    Args:
        iupacname (str): user input IUPAC names in string format.

    Returns:
        result (str): The predicted SMILES in string format.
    """

    # Load important pickle files which consists the tokenizers and the maxlength setting
    targ_lang = pickle.load(open(default_path.as_posix()+"/assets/tokenizer_input.pkl", "rb"))
    inp_lang = pickle.load(open(default_path.as_posix()+"/assets/tokenizer_target.pkl", "rb"))
    inp_max_length = pickle.load(open(default_path.as_posix()+"/assets/max_length_targ.pkl", "rb"))

    splitted_list = list(iupacname)
    tokenized_IUPACname = " ".join(map(str, splitted_list))
    decoded = helper.tokenize_input(tokenized_IUPACname, inp_lang, inp_max_length)

    result_predited = reloaded_reverse(decoded)
    result = helper.detokenize_output(result_predited, targ_lang)

    return result

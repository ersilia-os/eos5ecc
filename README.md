# IUPAC NAME TO SMILES TRANSLATION  

## Model Identifiers

- Slug: <iaupac2smiles>
- Ersilia ID: <eos5ecc>
- Tags: <iupac-names-to-smiles>

## Model Description

Translator from IUPAC names to SMILES. This model uses a deep learning neural machine translation (NMT) approach that allows conversion from an IUPAC (International Union of Pure and Applied Chemistry) name to SMILES

- Input: STRING with IUPAC NAMES 
- Output: SMILES
- Model type: Translation
- Mode of training: Pretrained

## Source Code

Cite the source publication
Rajan, K., Zielesny, A. & Steinbeck, C. STOUT: SMILES to IUPAC names using neural machine translation. J Cheminform 13, 34 (2021). https://doi.org/10.1186/s13321-021-00512-4

- Code: https://github.com/Kohulan/Smiles-TO-iUpac-Translator
- Checkpoints: https://storage.googleapis.com/decimer_weights/models.zip.

## License

State the licences used which are GPL v3 license used by Ersilia and the license used by the source code MIT 2.0

## History

- January 4, 2023 was downloaded and incorporated into Ersilia on January 12, 2023
- Modified the original stout.py file:

    In the original model, using an unzip function, the trained and tokenized models are downloaded to a default location ($HOME/.data directory). After downloading the zipped file the function unzips the file automatically. If the model exists on the default location this function will not work.

    Using the pystow module, the trained models were saved in a default path /home/username/.data, and from that path they were read to be loaded.

    All the functionality mentioned above is removed from the file and other functionality is made: The trained models are downloaded directly, the files are unzipped and saved in the checkpoint folder (folder assets and folder translator_reverse), and the environment variable PYSTOW_HOME is set to the path where the models are located, that is, in the checkpoint folder.

    The part corresponding to the translate_forward function, which predicts smiles from an iupac name, has been removed from the code.


## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission or [volunteer](https://www.ersilia.io/volunteer) with us!

FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN pip install git+https://github.com/Kohulan/Smiles-TO-iUpac-Translator.git
RUN pip install STOUT-pypi==2.0.1

WORKDIR /repo
COPY . /repo

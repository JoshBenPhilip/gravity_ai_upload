from cProfile import label
from cmath import pi
from gravityai import gravityai as grav
import pickle 
import pandas as pd

model = pickle.load(open(''))
tfidf_vectorizer = pickle.load(open(''))
label_encoder = pickle.load(open(''))

def process(inPath, outPath):
    # read input file
    input_df = pd.read_csv(inPath)
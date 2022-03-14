# -*- coding: utf-8 -*-
"""
Compare two text inputs
"""

import pandas as pd
from nltk.corpus import stopwords
from wordcloud import WordCloud 
import matplotlib.pyplot as plt 
import matplotlib 
matplotlib.use('Agg')


class CompareText:
    """This is a class to compare two text inputs"""
    
    def __init__ (self):
        """Initialise important words"""
        self.stop_words = stopwords.words('english')
        self.remove_words = pd.read_csv("remove_words.txt")['remove_words']
        
    def cleanse_text(self, text):
        """Clean text and split into tokens"""
         
        text = '' if pd.isnull(text) else str(text)         
        text = text.replace("/"," ")
        text = text.lower()
        text = "".join(l for l in text if l not in set('!"$%&\'()*+,-./:;<=>?@[\\]^_`{|}~’“”'))
        text = set(text.split()) - set(self.remove_words)
        return text


    def jaccard_matching(self, x, y):
        """Jaccard similarity score"""
        
        x1 = self.cleanse_text(x)
        y1 = self.cleanse_text(y)
    
        intersect = x1 & y1
        union = x1 | y1        
        denominator =  len(union)
             
        jaccard = len(intersect)/denominator 
        return(jaccard)       



def plot_wordcloud(input_text, filename):
    """Word cloud plot to local file"""
    
    mywordcloud = WordCloud().generate(input_text)
    fig = plt.figure(figsize=(20,10))
    plt.imshow(mywordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.savefig(filename + '.png')
        
        
def main():
    
    """Read two text blobs and calculate similarity"""
    
    chokri = ""
    f1 = open('chokri.txt')
    for line in f1:
        chokri = chokri + " " + line
    
    sheeran = ""
    f2 = open('sheeran.txt')
    for line in f2:
        sheeran = sheeran + " " + line
        
    compare = CompareText()
    jaccard = compare.jaccard_matching(chokri, sheeran)
    
    print('\nSimilarity:')
    print(str(round(jaccard*100,2)) + "%\n")
    
    plot_wordcloud(chokri, "chokri_oh_why")
    plot_wordcloud(sheeran, "sheeran_shape_of_u")
    
    
if __name__ == "__main__":
    main()
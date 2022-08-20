# -*- coding: utf-8 -*-
"""
Pycharm Editor
This is a Project Implementation script file.
"""
"""
Import Statements
"""
from pyswip import Prolog
import nltk
import string
import re
import pandas
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem.porter import PorterStemmer
import warnings
from pyswip import Functor, Variable, Query, call
warnings.filterwarnings("ignore")

""" Function Declarations """
pstem = PorterStemmer()
def clean_text(text):
    text = text.lower()
    text = re.sub('[0-9]','',text)
    text = re.sub(r"won\'t", "will not", text)
    text = re.sub(r"can\'t", "can not", text)
    text = re.sub(r"n\'t", " not", text)
    text = re.sub(r"\'re", " are", text)
    text = re.sub(r"\'s", " is", text)
    text = re.sub(r"\'d", " would", text)
    text = re.sub(r"\'ll", " will", text)
    text = re.sub(r"\'t", " not", text)
    text = re.sub(r"\'ve", " have", text)
    text = re.sub(r"\'m", " am", text)
    text = re.sub(r" amp ", " and ", text)
    text  = "".join([char for char in text if char not in string.punctuation])
    tokens = word_tokenize(text)
    tokens=[pstem.stem(word) for word in tokens]
    print("After Stemming",tokens)
    tokens=[lemmatizer.lemmatize(word) for word in tokens]
    print("After Lemmatization", tokens)
    print("Before Stopwords Removal",tokens)
    tokens=[word for word in tokens if word not in stopwords.words('english')]
    print("After stopwords removal",tokens)
    text = ' '.join(tokens)
    return text

EMOJIS = {':)': 'smile', ':-)': 'smile', ';d': 'wink', ':-E': 'vampire', ':(': 'sad',
          ':-(': 'sad', ':-<': 'sad', ':P': 'raspberry', ':O': 'surprised',
          ':-@': 'shocked', ':@': 'shocked',':-$': 'confused', ':\\': 'annoyed',
          ':#': 'mute', ':X': 'mute', ':^)': 'smile', ':-&': 'confused', '$_$': 'greedy',
          '@@': 'eyeroll', ':-!': 'confused', ':-D': 'smile', ':-0': 'yell', 'O.o': 'confused',
          '<(-_-)>': 'robot', 'd[-_-]b': 'dj', ":'-)": 'sadsmile', ';)': 'wink',
          ';-)': 'wink', 'O:-)': 'angel','O*-)': 'angel','(:-D': 'gossip', '=^.^=': 'cat'}
URLPATTERN        = r"((http://)[^ ]*|(https://)[^ ]*|( www\.)[^ ]*)"


""" List of Elements in Periodic Table"""

periodic_table_list = ['hydrogen','helium','lithium','beryllium','boron','carbon','nitrogen','oxygen',
                       'fluorine','neon','sodium','magnesium','aluminum','silicon','phosphorus','sulfur',
                       'chlorine','argon','potassium','calcium','scandium','titanium','vanadium','chromium',
                       'manganese','iron','cobalt','nickel','copper','zinc','gallium','germanium','arsenic',
                       'selenium','bromine','krypton','rubidium','strontium','yttrium','zirconium','niobium',
                       'molybdenum','technetium','ruthenium','rhodium','palladium','silver','cadmium','indium','tin',
                       'antimony','tellurium','iodine','xenon','cesium','barium','lanthanum','cerium','praseodymium',
                       'neodymium','promethium','samarium','europium','gadolinium','terbium','dysprosium','holmium','erbium',
                       'thulium','ytterbium','lutetium','hafnium','tantalum','wolfram','rhenium','osmium','iridium','platinum',
                       'gold','mercury','thallium','lead','bismuth','polonium','astatine','radon','francium','radium','actinium',
                       'thorium','protactinium','uranium','neptunium','plutonium','americium','curium','berkelium','californium',
                       'einsteinium','fermium','mendelevium','nobelium','lawrencium','rutherfordium','dubnium','seaborgium','bohrium',
                       'hassium','meitnerium','darmstadtium ','roentgenium ','copernicium ','nihonium','flerovium','moscovium',
                       'livermorium','tennessine','oganesson']

periodic_symbols = ['h','he','li','be','b','c','n','o','f','ne','na','mg','al','si','p','s','cl','ar','k','ca','sc','ti','v','cr','mn',
                    'fe','co','ni','cu','zn','ga','ge','as','se','br','kr','rb','sr','y','zr','nb','mo','tc','ru','rh','pd','ag','cd','in'
                    ,'sn','sb','te','i','xe','cs','ba','la','ce','pr','nd','pm','sm','eu','gd','tb','dy','ho','er','tm','yb','lu','hf','ta',
                    'w','re','os','ir','pt','au','hg','tl','pb','bi','po','at','rn','fr','ra','ac','th','pa','u','np','pu','am','cm','bk',
                    'cf','es','fm','md','no','lr','rf','db','sg','bh','hs','mt','ds ','rg ','cn ','nh','fl','mc','lv','ts','og']


periodic_table_properties = ['magnet','type','name','discover','metal','phase','number','atom','radio','all','typeof','radioact','densiti','nonmet','nonmagnet','discov']


def preprocess_text(text):
    text = re.sub(URLPATTERN,' URL',text)
    ### Replacing EMOJI
    for emoji in EMOJIS.keys():
        text = text.replace(emoji,EMOJIS[emoji])
    print("Preprocessing",text)
    return text



"""
User Input
"""

while True:

    user_input = input('Kindly please enter the input\n')
    print(user_input)

    if(user_input=='stop'):
        break

    """ Finding the String Length """
    string_length = len(user_input)

    """ Converting String into Tokens """
    word_tokens = word_tokenize(user_input)
    print("Tokens",word_tokens)

    """Finding word Length"""
    sentence_length = len(word_tokens)
    print("Word length in a sentence",sentence_length)

    pstem = PorterStemmer()
    lemmatizer = WordNetLemmatizer()
    data = preprocess_text(user_input)

    print("Preprocessing is done using NLTK")

    prolog = Prolog()
    prolog.consult("C:/Users/visha/Desktop/Knowledge Base Systems/periodic_table.pl")

    X_element = Variable()
    X_symbol = Variable()
    all_values = Variable()
    metals_flag = Variable()
    non_value = Variable()
    location = int()
    data = clean_text(data)
    print("Data is cleaned")
    data = data.split()
    print(data)
    for i in range(0,len(data)):
        if data[i] == 'all':
            all_values = data[i]
        if data[i] in periodic_table_properties:
            x_property = data[i]
        if data[i] in periodic_table_list:
            X_element = data[i]
        if data[i]=='list':
            metals_flag = 1
        if data[i] == 'non':
            non_value = 1
        if data[i] in periodic_symbols:
            X_symbol = data[i]
            location = periodic_symbols.index(data[i])

    """print("property of x is ",x_property,metals_flag,X_symbol,location)"""

    if x_property in periodic_table_properties and x_property=='densiti':
        d = list(prolog.query("density("+X_element+",D)"))
        print("The Density of "+ X_element+ " is",d[0]['D'])


    elif x_property in periodic_table_properties:

        if x_property=='radioact' or x_property=='radio':
            if metals_flag==1 or all_values=='all':
                x_values = list(prolog.query("radioactive_list(List)"))
                output = x_values[0]['List']
                for o in output:
                    print(o)

        if x_property=='nonmagnet' or x_property=='magnet' and non_value==1:
            if all_values=='all' or metals_flag==1:
                x_values = list(prolog.query("non_magnetic(List)"))
                output = x_values[0]['List']
                for o in output:
                    print(o)

        if x_property=='metal' and non_value!=1:
            if all_values=='all' or metals_flag==1:
                x_values = list(prolog.query("all_metals(List)"))
                output = x_values[0]['List']
                for o in output:
                    print(o)

        if x_property=='metal' or x_property=='nonmet' or non_value==1:
            if all_values=='all' or metals_flag==1:
                x_values = list(prolog.query("all_non_metals(List)"))
                output = x_values[0]['List']
                for o in output:
                    print(o)

        if x_property=='discover' or x_property=='discov':
            d = list(prolog.query("discoverer(" + X_element + ",Discoverer)"))
            print("Discoverer of " + X_element + " is", d[0]['Discoverer'])

        if x_property=='phase':
            d = list(prolog.query("phases(" + X_element + ",T)"))
            print("Phase of " + X_element + " is", d[0]['T'])

        if x_property=='type' or x_property=='typeof':
            d = list(prolog.query("types(" + X_element + ",T)"))
            print("Type of " + X_element + " is", d[0]['T'])

        if x_property=='name':
            print("The Element name of ",X_symbol," is ",periodic_table_list[location])

        if x_property=='number' or x_property=='atom':
            print("The Atomic number is ", location+1)

        if metals_flag!=1:
            if x_property=='radioact' or x_property=='radio':
                d = list(prolog.query("radioactive(" + X_element + ",R)"))
                if (d[0]['R'] == 'yes'):
                    print(X_element + " is Radioactive")
                else:
                    print(X_element + " is Not Radioactive")

        if x_property=='metal' or x_property=='nonmet':
            if metals_flag!=1:
                d = list(prolog.query("metal_or_nonmetal(" + X_element + ",Y)"))
                if (d[0]['Y'] == 'yes'):
                    print(X_element + " is Metal")
                else:
                    print(X_element + " is not a Metal")

        if x_property=='magnet' and metals_flag!=1:
            d = list(prolog.query("magnetism(" + X_element + ",T)"))
            print("Magnetic property of " + X_element + " is", d[0]['T'])


    else:
        print("Invalid")



import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv("C:/Users/Gaelim/Desktop/Datasets/Segmentation Data/Mall_Customers.csv")

df.head()
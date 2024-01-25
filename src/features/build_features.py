import yaml
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.preprocessing import StandardScaler
import sys
# feature engenineering




def drop_columns(data,*c):
    df=data.drop(columns=[*c])
    return df

def standardization(data):
    scaler = StandardScaler()
    df = scaler.fit_transform(data)
    return df

def io(data,target):
    df=pd.read_csv(data)
    x=df.drop(columns=[target])
    y=df[target]
    return x,y
def decomposition(data,n_comonents,svd,tol):
    pca = PCA(n_components=n_comonents,svd_solver=svd,tol=tol)  # Adjust the number of components
    principal_components = pca.fit_transform(data)
    columns = [f'Principal Component {i+1}' for i in range(pca.n_components_)]
    pca_df = pd.DataFrame(data=principal_components, columns=columns)
    return pca_df
    
def save_train_test():
    pass

input_data_path=sys.argv[1]
params_file=sys.argv[2]
params = yaml.safe_load(open(params_file))['build_features']
list_of_dropped_columns=params['list_of_dropped_columns']
target=params['target']


df=drop_columns(data_path,list_of_dropped_columns)
data=standardization(df,target)
x,y=io(data,target)
final_df=decomposition()










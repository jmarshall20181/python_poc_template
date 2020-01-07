#load libs
import os
import sys
import glob
from pathlib import Path
import pandas as pd

###### get all .csv  files from folder in SIA folder directory
in_path = r'\\apgccfs03\Workgroups\SIA\Analytics Project Documents\rest of path address'
out_path = r'\\apgccfs03\Workgroups\SIA\Analytics Project Documents\rest of path address'
file_name = "file_name.csv"

def get_all_external_csv_data_from_directory(in_path, out_path, file_name):
    #get all .csv files from directory
    files = glob.glob(in_path +  "/*.csv")
    #test
    #print(files)
    
    #initiate empty list to hold results
    csv_file_list = []
    #for each file in the directory
    for file in files:
        #test
        #print(file)
        #set df to read_csv 
        df = pd.read_csv(file, index_col = None, header = 0)
        
        #select cols if needed
        #cols_list = []
        #df = df[cols_list]
        
        #append the df to the csv file list
        csv_file_list.append(df)
        
        #concat dfs from list into single df
        output_df = pd.concat(csv_file_list, axis = 0)
                
    #create outpath variable
    output_path_and_file = os.path.join(out_path, file_name)
    #write out to data folder for project
    output_df.to_csv(output_path_and_file, index = False)
    return
#test
#get_all_external_csv_data_from_directory(in_path = in_path, out_path = out_path, file_name = file_name)

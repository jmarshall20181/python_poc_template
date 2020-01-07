#load libs
import os
import sys
import glob
from pathlib import Path
import pandas as pd

#read in .csx or .xslx files
#use the data/data_processed folder in this project as the output

#import csv data
from helper.helper import get_all_external_csv_data_from_directory
#import xlsx data
from helper.helper import get_all_external_xlsx_data_from_directory

#sample_1
#in_path = r'\\apgccfs03\Workgroups\SIA\Analytics Project Documents\rest of path address'
#out_path = r'\\apgccfs03\Workgroups\SIA\Analytics Project Documents\rest of path address'
#file_name = "file_name.csv"

##### sample_2 from .csv to .csv
#in_path = r'data\data_raw\sample_csv'
#out_path = r'data\data_processed\Sample_csv'
#file_name = "test_file_name.csv"

#load sample .csv data from data_raw csv folder to data_processed csv folder
#get_all_external_csv_data_from_directory(in_path = in_path, out_path = out_path, file_name = file_name)

#sample_3 from .xlsx to .csv
#in_path = r'data\data_raw\Sample_xlsx'
#out_path = r'data\data_processed\Sample_csv'
#file_name = "test_file_name_2.csv"

#load sample .xlsx data from data_raw .xslx folder to data_processed csv folder
#get_all_external_xlsx_data_from_directory(in_path = in_path, out_path = out_path, file_name = file_name)

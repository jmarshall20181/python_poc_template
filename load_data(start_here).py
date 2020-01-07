#load libs
import os
import sys
import glob
from pathlib import Path
import pandas as pd
import helper
#read in .csx or .xslx files
#use the data/data_processed folder in this project as the output

#import csv data
from helper.helper import get_all_external_csv_data_from_directory
#import xlsx data
from helper.helper import get_all_external_xlsx_data_from_directory

#sample
#in_path = r'\\apgccfs03\Workgroups\SIA\Analytics Project Documents\rest of path address'
#out_path = r'\\apgccfs03\Workgroups\SIA\Analytics Project Documents\rest of path address'
#file_name = "file_name.csv"




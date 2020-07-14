import os
from pathlib import Path
import numpy as np
from variables import *

print(fastq_fastmode)
path1 = Path(fastq_fastmode)
print(path1)

full_list = np.loadtxt(Path(fastq_fastmode), skiprows = 1, dtype = str)
ref_list = np.loadtxt(Path(fastq_hacmode), skiprows = 1, usecols = 1, dtype = str)

full_list_flattened = full_list[:,2]
mask_flattened = np.in1d(full_list_flattened, ref_list, assume_unique=True)

# remove  first col
full_list_aligned = full_list[:, 1:]

mask = np.isin(full_list_aligned, ref_list)
mask_plain = mask[:,1]

filtered = full_list[mask_flattened]
f = np.shape(ref_list)[0]

# header_array = np.loadtxt(Path(fastq_hacmode), skiprows = 0, dtype = str)[0]
# header_str = str(header_array)

print("ref_count: ", f)
print("filtered_count: ", np.shape(filtered)[0])

print("began...")
np.savetxt('reads4.txt', filtered, fmt='%s', delimiter = '	')
print("processing done.")
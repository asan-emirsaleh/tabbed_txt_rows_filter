from pathlib import Path
import numpy as np
from variables import *

full_list = np.loadtxt(Path(fastq_fastmode), skiprows = 1, dtype = str)
# Load only the reads names into array
ref_list = np.loadtxt(Path(fastq_hacmode), skiprows = 1, usecols = 2, dtype = str)

# MinKNOW generated txt contain the fast5 filename column being absent 
# in default Guppy generated txt file. That's why we need to retrieve 
# only readnames from data loaded. The mask using binominal pattern
# created on the readnames datta. Unique lines must be selected.

full_list_flattened = full_list[:,2]
mask_flattened = np.in1d(full_list_flattened, ref_list, assume_unique=True)

# another way to mask only by reads
# remove first col
#
# full_list_aligned = full_list[:, 1:]
# mask = np.isin(full_list_aligned, ref_list)
# mask_plain = mask[:,1]

filtered = full_list[mask_flattened]

#count the number of lines in reference txt
ref_count = np.shape(ref_list)[0]

# Must be reviewed
# header_array = np.loadtxt(Path(fastq_hacmode), skiprows = 0, dtype = str)[0]
# header_str = str(header_array)

print("ref_count: ", ref_count)
print("filtered_count: ", np.shape(filtered)[0])

print("began...")
# use the same columns delimeter as in original txt files
np.savetxt('reads.txt', filtered, fmt='%s', delimiter = '	')
print("processing done.")

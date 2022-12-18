import pysam as ps

bam_file = ps.AlignmentFile('merged-normal.bam', 'rb')
# count returns number of reads in a region if region is not specified, takes whole file
total_number_of_reads = bam_file.count()  

fetched_file = bam_file.fetch() #iterator
# fetch reads aligned in a specified region
# Without a contig or region all mapped reads in the file will be fetched

# first_read is AligmentSegment
first_read = next(fetched_file)   # next returns next item in the iterator
print(first_read)

# mate(AligmentSegment) of AligmentFile 
mate_first_read = bam_file.mate(first_read)
print("This is mate first read \n", mate_first_read)

info_first_read = first_read.to_dict() # or .to_string
print('Inspected first read\n', info_first_read)
flag = info_first_read['flag']
print('Inspected flag of the first read\n', flag)

'''
flag_fields = []
for read in fetched_file:
    read_to_dict = read.to_dict()
    flag_fields.append(read_to_dict['flag'])
print(flag_fields)
'''

number_of_unmapped = bam_file.unmapped
print('Number of unmapped reads\n', number_of_unmapped)


# for mapping quality of a AligmentSegment use atribute mapping_quality
"""
map_qual = first_read.mapping_quality
print(map_qual)
"""
# count number of reads with mapping quality = 0
mapping_quality_zero = 0
sum_of_map_quality = 0
number_not_zero = 0     # number of reads with map_quality not zero
for read in fetched_file:
    sum_of_map_quality += read.mapping_quality
    if read.mapping_quality == 0:
       mapping_quality_zero += 1
    else:
        number_not_zero += read.mapping_quality
    
avg_map_qual = sum_of_map_quality/total_number_of_reads
print('Average mapping quality for all the reads\n', avg_map_qual)
print('Number of reads with mapping quality = 0\n', mapping_quality_zero)

avg_without_zero = number_not_zero/(total_number_of_reads - mapping_quality_zero)
print('Average mapping quality without reads with maping quality = 0\n', avg_without_zero)

'''
for read in fetched_file:
    read_to_dict = read.to_dict()
    if read_to_dict['map_quality'] == '0':
        mapping_quality_zero += 1

print(mapping_quality_zero)
'''
def concatenate_files(filename1, filename2, new_filename):
    fp1 = open(filename1)
    fp2 = open(filename2)
    content1 = fp1.read()
    content2 = fp2.read()

    new_string = content1 + content2 
    fp3 = open(new_filename, 'w')
    fp3.write(new_string)
    
    fp1.close()
    fp2.close()
    fp3.close()
    
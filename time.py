def moveFile(root,number_of_files, to):

    list_of_file = [0 for i in range(number_of_files + 1)]

    index = 0
    for folderName, subfolders, filenames in os.walk(root):
        for filename in filenames:
            if filename.endswith('.pdf'):
                list_of_file[index] = filename
                index = index + 1

    ist_of_file.sort()

    for file in list_of_file:
        name = root + str(file)

        dest = to + str(file)

        shutil.move( name, dest ) 
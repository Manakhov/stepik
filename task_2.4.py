with open("dataset_24465_4 (1).txt", "r") as file_read, open("dataset_new.txt", "w") as file_write:
    text_file = []
    i = 0
    for read in file_read:
        text_file.append(read)
        i = i + 1
    for count in range(i):
        file_write.write(text_file.pop())



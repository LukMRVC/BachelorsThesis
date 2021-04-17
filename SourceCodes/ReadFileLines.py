
if __name__ == '__main__':
    
    with open('my_supa_file.txt', 'r') as supa_file:
        for line in supa_file:
            # strip tease
            stripped_line = line.strip()
            print(stripped_line)

    print('My work here is done!')
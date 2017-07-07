# Reading/Writing 
def read_file(data):
    with open(data) as f:
        return f.read()

def write_to_file(data, content, mode='w'):
    with open(data, mode=mode) as f:
        f.write(content)

if __name__ == '__main__':
    # Reading:
    print(read_file('new.txt'))
    # Writing:
    write_to_file('new.txt', 'I can write!')  # rewrites
    write_to_file('existing.txt', 'I can add!\n', mode='a')  # adds


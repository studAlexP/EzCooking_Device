import sys
import os
import hashlib

def main():
    hash_one = get_hash("data/data.txt")

    # Gets the hash which was saved at last
    with open(os.path.join(sys.path[0], "data/old.txt")) as file:
        hash_two = file.read()
        file.close()
    compare_hash(hash_one, hash_two)

#TODO sends data on hash change
def send_data(data):
    # ? Sockets or Firebase or Bluetooth
    pass

def compare_hash(hash_one, hash_two):
    """
    Compares two hashes

    :param hash_one: MD5 hash of audio_data.txt file
    :param hash_two: Last saved MD5 hash of audio_data.txt 
    :returns: Nothing
    """
    if hash_one == hash_two:
        pass
    else:
        with open(os.path.join(sys.path[0], "data/old.txt"), "w") as file:
            file.write(hash_one)
            file.close()
            # TODO call send data with the data to send 

def get_hash(file_name):
    """
    Gets the hash of a file

    :param file_name: file from which to get the hash
    :returns: Returns an md5 checksum
    """
    with open(os.path.join(sys.path[0], file_name), "rb") as file:
        data = file.read()
        md5_hash = hashlib.md5(data).hexdigest()
        file.close()
    
    return md5_hash 

if __name__ == "__main__":
    main()
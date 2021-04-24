from hashlib import sha256
import time
MAX_NONCE = 100000000000  # Max Computation Power


def SHA256(text):
    # Converts The Text To SHA256 Type
    return sha256(text.encode("ascii")).hexdigest()


def mine(block_number, transactions, previous_hash, prefix_zeroes):
    prefix_str = '0'*prefix_zeroes
    for nonce in range(MAX_NONCE):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print(
                f"Yah! Successfully Mined Bitcoins With Nonce Value: {nonce}")
            return new_hash

    raise BaseException(
        f"Couldn;t Find Correct Has After Trying {MAX_NONCE} times")


if __name__ == '__main__':
    transactions = '''
    Sam->Shubham->10,
    Jaya>Vikrum->80
    '''
    difficulty = 10 # No Of Zeroes Before Hash Value
    start = time.time()
    print("Mining Started...")
    new_hash = mine(
        5, transactions, '000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f', difficulty)
    total_time = str((time.time() - start))
    print(f"Mining Ended. Mining Took: {total_time} seconds")
    print(new_hash)

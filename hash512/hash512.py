import os
import hashlib

def split_file(filename, chunk_size):
    try:
        file_size = os.path.getsize(filename) 
        with open(filename, 'rb') as file:
            index = 0
            while True:
                data = file.read(chunk_size)
                if not data:
                    break

                
                hash_object = hashlib.sha512(data)
                sha512_hash = hash_object.hexdigest()

                
                chunk_size_actual = len(data)

                
                print(f"Chunk {index+1} SHA-512 Hash: {sha512_hash}")
                print(f"Chunk {index+1} Boyutu: {chunk_size_actual} bytes")

                index += 1

           
            last_chunk_size = file_size % chunk_size
            print(f"Son Parça Boyutu: {last_chunk_size} bytes")

    except FileNotFoundError:
        print("Dosya bulunamadı!")


dosya_adi = "Free_Test_Data_10.5MB_PDF.txt"
parca_boyutu = 1024 * 1024  

split_file(dosya_adi, parca_boyutu)

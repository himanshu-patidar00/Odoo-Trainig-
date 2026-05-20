import zlib 

data = b"hello world!hello world!hello world!hello world!" 
# b is used because zlib required raw binary(bytes) data not text 

compressed_data = zlib.compress(data)
decompressed_data = zlib.decompress(compressed_data) 

print(f"original  data:= {len(data)} bytes") 
print(f"compressed data := {len(compressed_data)} bytes")  



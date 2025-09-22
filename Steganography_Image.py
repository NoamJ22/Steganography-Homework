from PIL import Image
import io

# Load image and convert to BMP bytes
image = Image.open("picture.png")
bmp_buffer = io.BytesIO()
image.save(bmp_buffer, format="BMP")
bmp_bytes = bytearray(bmp_buffer.getvalue())  # Convert to a bytearray

#secret message will be in ASCII
message = "house"
message_bytes = message.encode("ascii")

# Embed message at offset 54 (start of pixel data)
start_offset = 54
bmp_bytes[start_offset:start_offset+len(message_bytes)] = message_bytes

# Save modified BMP
with open("modified_output.bmp", "wb") as f:
    f.write(bmp_bytes)




# Read modified file
with open("modified_output.bmp", "rb") as f:
    data = f.read()

# Extract message
start_offset = 54
print(data[start_offset:start_offset+len(message_bytes)].decode('ascii')) 


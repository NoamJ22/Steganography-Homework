import base64
import hashlib
with open(r"C:\Users\noame\Desktop\stuff\סייבר\בסטגנוגרפיה\document_for_metadata.txt", 'r', encoding='utf-8') as file:
    lines = file.readlines()


import base64

def hideMetadata(lines):
    metadata_index = -1
    text = ""
    for index, line in enumerate(lines):
        text += line
        if "metadata" in line.lower():
            metadata_index = index
            break

    if metadata_index != -1:
        metadata_lines = lines[metadata_index + 1:]
    else:
        return None

    for line in metadata_lines:
        encoded = base64.b64encode(line.encode()).decode()
        text += encoded + "\n"
    return text

def revealMetadata(hidden):
    metadata_index = -1
    lines = hidden.splitlines()
    text = ""
    for index, line in enumerate(lines):
        text += line + "\n"
        if "metadata" in line.lower():
            metadata_index = index
            break

    if metadata_index != -1:
        metadata_lines = lines[metadata_index + 1:]
    else:
        return None

    for line in metadata_lines:
        try:
            decoded_line = base64.b64decode(line.encode()).decode()
            text += decoded_line + "\n"
        except Exception as e:
            text += f"[Error decoding line: {line}]\n"
    return text



hidden_metadata = hideMetadata(lines)
print("Hidden with metadata encoded:\n", hidden_metadata)

revealed = revealMetadata(hidden_metadata)
print("\nRevealed with metadata decoded:\n", revealed)

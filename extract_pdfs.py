import os
from pypdf import PdfReader

files = [
    r"c:\Users\sebaf\Desktop\dataroom-lili-2026-main\12_Pitch_Deck\01_Pitch_Deck_Investor_ESP.pdf",
    r"c:\Users\sebaf\Desktop\dataroom-lili-2026-main\12_Pitch_Deck\02_The_Pitch_Deck_ENG.pdf",
    r"c:\Users\sebaf\Desktop\dataroom-lili-2026-main\12_Pitch_Deck\Pitch_Deck_LiLi_2026.pdf"
]

for file_path in files:
    filename = os.path.basename(file_path)
    print(f"===== FILE: {filename} =====")
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        print("===== END FILE =====")
        continue
        
    try:
        reader = PdfReader(file_path)
        full_text = ""
        for page in reader.pages:
            text = page.extract_text()
            if text:
                full_text += text + "\n"
        
        if full_text.strip():
            print(full_text)
        else:
            print("No text found. This PDF might be a scanned image or empty.")
    except Exception as e:
        print(f"Error processing file: {e}")
    
    print("===== END FILE =====")
    print()

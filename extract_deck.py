import sys
from pypdf import PdfReader
sys.stdout.reconfigure(encoding='utf-8')
r = PdfReader(r'C:\Users\sebaf\Desktop\LiLi Documentos\Pitch Deck - LiLi 2026  (5).pdf')
for i, p in enumerate(r.pages):
    print(f'--- PAGE {i+1} ---')
    print(p.extract_text())
    print()

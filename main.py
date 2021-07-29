import argparse
from s3.client import ToDusClient
#from todus3.main import save_config
#from todus3.main import register
from pathlib import Path
from typing import List

client = ToDusClient()
max_retry = 3
phone_number ="5358096948"


password = "LC0Nw3NlZUEQfvR4E9h99VMX_kWGt2UiUIuLMd4Rryi1ODOfqfYxv4N5RzpiD0hihP4uDP8JtcNUvrrk3FY6Gy5dHrbgLw=="
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2Mjc0OTAxNzYsInVzZXJuYW1lIjoiNTM1ODA5Njk0OCIsInZlcnNpb24iOiIyMTgyMCJ9.7rvoeGF7XDZdONOSfNTNJM3TKYtr2P7CufwNNNp2b_w"

def write_txt(filename: str, urls: List[str], parts: List[str]) -> str:
    txt = "\n".join(f"{down_url}\t{name}" for down_url, name in zip(urls, parts))
    path = Path(f"{filename}.txt").resolve()
    with open(path, "w", encoding="utf-8") as f:
        f.write(txt)
    return str(path)          

print("diga el nombre del archivo a descargar")
name = input()
path = "./"+name
filename = Path(path).name
filename_path = Path(path)
file_uri = client.upload_file(token, filename_path)
txt = write_txt(filename, urls =[file_uri],parts = [filename])
#print(file_uri,"	{filename}")
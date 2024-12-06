def main():
    returned_file = get_input()
    print(get_file(returned_file))


def get_input():
    file = input("File Name: ")
    return file

def get_file(file):
     if ".png" in file:
         return "image/png"
     elif ".pdf" in file:
         return "application/pdf"
     elif ".gif" in file:
         return "image/gif"
     elif ".jpg" in file:
         return "image/jpeg"
     elif ".jpeg" in file:
         return "image/jpeg"
     elif ".zip" in file:
         return "document/zip"
     elif ".txt" in file:
         return "document/txt"
     else:
         return "nonapplication/octet-stream "
    

main()
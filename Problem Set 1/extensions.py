def main():
    extension(input("File name: ").strip().lower())
def extension(ans):
    if ans.endswith(".jpg") or ans.endswith(".jpeg"):
            print("image/jpeg")
    elif ans.endswith(".png"):
          print("image/png")
    elif ans.endswith(".gif"):
          print("image/gif")
    elif ans.endswith(".pdf"):
          print("application/pdf")
    elif ans.endswith(".txt"):
          print("text/plain")
    elif ans.endswith(".zip"):
          print("application/zip")
    else:
          print("application/octet-stream")
main()

ex = input("File name: ").strip().lower()
#pro
if ex.endswith("gif"):
    print("image/gif")

elif ex.endswith("jpg") or ex.endswith("jpeg"):
    print("image/jpeg")

elif ex.endswith("png"):
    print("image/png")

elif ex.endswith("pdf"):
    print("application/pdf")

elif ex.endswith("txt"):
    print("text/plain")

elif ex.endswith("zip"):
    print("application/zip")

else:
    print("application/octet-stream")


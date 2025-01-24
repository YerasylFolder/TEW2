for i in range(2, 26):
    with open(f"student{i}.html", "w") as file:
        file.write(f"<html>\n<head>\n<title>Student {i}</title>\n</head>\n<body>\n<h1>Student {i}</h1>\n</body>\n</html>")

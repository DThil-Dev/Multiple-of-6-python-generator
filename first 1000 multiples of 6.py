# Replace 'Dinod' with your Windows username if it's different
# Also, make sure to have a file named 'multiples_of_6.txt' on your desktop before running this code
path = r"C:\Users\Name\Desktop\multiples_of_6.txt"

with open(path, "w") as f:
    f.write(", ".join(str(i * 6) for i in range(1, 1001)))

print(f"Done! Check your desktop for the file.")
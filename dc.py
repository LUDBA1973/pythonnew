dataset = [
    {"Name": "Alice", "Age": 21, "Email": "alice@example.com"},
    {"Name": "", "Age": 30, "Email": "bob@example.com"}, 
    {"Name": "Charlie", "Age": -5, "Email": "charlie@example.com"},  
    {"Name": "David", "Age": 40, "Email": "davidexample.com"},  
    {"Name": "Eve", "Age": 22, "Email": "eve@example.com"}
]

cleaned_data = []
for entry in dataset:
    name = entry["Name"].strip()
    age = entry["Age"]
    email = entry["Email"]
    
    print(name)
    if name and isinstance(age,int)  and age > 0 and "@" in email:
        # cleaned_data.append(entry)
        cleaned_data.append(f"name:{name}")

for data in cleaned_data:
        print(data)  
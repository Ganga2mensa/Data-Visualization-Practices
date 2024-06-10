Cyber_security_company = {
    "INSA":{
        "Cyber Warfare wing":{
            "Cyber_Defense_Directorate":{
                "Cyber Defense Technology Division":{
                    "Solomon":{"Role": "Division Head", "Salary": 20000}
                }

            }
        }
    }
}

company = {
    "Engineering": {
        "Software": {
            "Alice": {"role": "Engineer", "salary": 70000},
            "Bob": {"role": "Engineer", "salary": 75000}
        },
        "Hardware": {
            "Charlie": {"role": "Technician", "salary": 60000}
        }
    },
    "HR": {
        "Recruitment": {
            "David": {"role": "Recruiter", "salary": 50000}
        }
    }
}

# Accessing specific details
alice_salary = company["Engineering"]["Software"]["Alice"]["salary"]
print("Alice's salary:", alice_salary)  # Output: Alice's salary: 70000

solomon_salary = Cyber_security_company["INSA"]["Cyber Warfare wing"]["Cyber_Defense_Directorate"]
print(f"Solomon's salary is {solomon_salary}")

# Iterating over the organizational structure
for dept, teams in company.items():
    for team, employees in teams.items():
        for employee, details in employees.items():
            print(f"{dept} -> {team} -> {employee}: {details}")

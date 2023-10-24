from models3 import User3, Address3, session

# Create users
user1 = User3(name="John Doe", age=52)
user2 = User3(name="Jane Smith", age=34)

# Create address
address1 = Address3(city="Ha Noi", state="HN", zip_code="10001")
address2 = Address3(city="Da Nang", state="DN", zip_code="10002")
address3 = Address3(city="Ho Chi Minh", state="HC", zip_code="10003")

# Asociating addresses with users
user1.addresses3.extend([address1, address2])
user2.addresses3.append(address3)

# Adding useres and addresses to the session and commiting changes to the database
session.add(user1)
session.add(user2)
session.commit()

print(f"{user1.addresses3 =}")
print(f"{user2.addresses3 =}")

print(f"{address1.user =}")



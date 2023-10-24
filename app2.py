from models2 import User2, Address2, session

# Create users
user1 = User2(name="John Doe", age=52)
user2 = User2(name="Jane Smith", age=34)

# Create address
address1 = Address2(city="Ha Noi", state="HN", zip_code="10001")
address2 = Address2(city="Da Nang", state="DN", zip_code="10002")
address3 = Address2(city="Ho Chi Minh", state="HC", zip_code="10003")

# Asociating addresses with users
user1.addresses2.extend([address1, address2])
user2.addresses2.append(address3)

# Adding useres and addresses to the session and commiting changes to the database
session.add(user1)
session.add(user2)
session.commit()

print(f"{user1.addresses2 =}")
print(f"{user2.addresses2 =}")

print(f"{address1.user =}")



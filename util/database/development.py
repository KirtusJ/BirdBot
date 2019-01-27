import json

with open("util/database/database.json", "r") as db:
	data = json.load(db)
	development = data['development']

development = {
	"username" : development["username"],
	"password" : development["password"],
	"host" : development["host"],
	"name" : development["name"],
	"link" : "mysql://{username}:{password}@{host}/{name}?charset=utf8mb4".format(
				username=development["username"], password=development["password"],
				host=development["host"], name=development["name"]
			)
}

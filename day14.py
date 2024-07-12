import random
data = [
	{
		'name': 'Instagram',
		'follower_count': 346,
		'description': 'Social media platform',
		'country': 'United States'
	},
	{
		'name': 'Cristiano Ronaldo',
		'follower_count': 215,
		'description': 'Footballer',
		'country': 'Portugal'
	},
	{
		'name': 'Ariana Grande',
		'follower_count': 183,
		'description': 'Musician and actress',
		'country': 'United States'
	},

	{
		'name': 'Cristiano Ronaldo',
		'follower_count': 215,
		'description': 'Footballer',
		'country': 'india'
	},
	{
		'name': ' Ronaldo',
		'follower_count': 15,
		'description': 'Footballer',
		'country': 'brazil'
	},
	{
		'name': 'Cris',
		'follower_count': 21,
		'description': 'actor',
		'country': 'nagaland'
	},
	{
		'name': 'neymar',
		'follower_count': 190,
		'description': 'Footballer',
		'country': 'brazil'
	},
]

	# account_name =account_a ["name"]
	# account_desc =account_a["description"]
	# account_country =account_a["country"]
	# print(f" {account_name} ,a { account_desc} ,from {account_country}")
	#
	# account_name =account_b ["name"]
	# account_desc =account_b["description"]
	# account_country =account_b["country"]
	# print(f" {account_name} ,a { account_desc} ,from {account_country}")

# 52 se leake 61 tak hum log function create kar sakte hai
def account_format(account):

	account_name =account["name"]
	account_desc =account["description"]
	account_country =account["country"]
	print(f" {account_name} ,a { account_desc} ,from {account_country}")

def check_answer(guess,account_a,account_b):
	if account_a > account_b:
		return  guess == "a"
	else:
		return guess == "b"

	account_a = random.choice(data)
	account_b = random.choice(data)
			if account_a == account_b:
			account_b = random.choice(data)

	print(f" compare a  : {account_format(account_a)}")
	print(f" compare b  : {account_format(account_b)}")

guess = input(" who has more followers A OR B : ")

a_follower_count = account_a["folloers_count"]
b_follower_count = account_b["folloers_count"]

correct = check_answer(guess,a_follower_count,b_follower_count)
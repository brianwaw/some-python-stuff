users = {
'aeinstein': {
'first': 'albert','last': 'einstein',
'location': 'princeton',
},
'mcurie': {
'first': 'marie',
'last': 'curie',
'location': 'paris',
},
}

for username, user_info in users.items():
    print(f"\nusername: {username}")
    full_name=f"{user_info['first']} {user_info['last']}"
    location=user_info['location']

    print(f"\tfullname: {full_name.title()}")
    print(f"\tlocation: {location.title()}")
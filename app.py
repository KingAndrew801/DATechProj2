
def clean_data(data):
    squeaky = []
    for player in data.copy():
        player['guardians'] = player['guardians'].split(" and ")


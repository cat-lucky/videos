import json

def jsonUpdate(FILE_PATH):
    try:
        with open(FILE_PATH, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("JSON file not found.")
        return
    except json.JSONDecodeError:
        print("Error decoding JSON.")
        return

    json_data = []
    for i in range(len(data)):
        dic = {
            "ID": data[i]["ID"],
            "category": data[i]["category"],
            "name": data[i]["name"],
            "timeStamp": data[i]["timeStamp"],
            "boyName": data[i]['boyName'],
            "girlName": data[i]['girlName'],
            "tags": data[i]['tags'],
            "imageURL": data[i]["imageURL"],
            "iFrameURL": data[i]["iFrameURL"],
            "videoURL": data[i]["videoURL"],
            "downloadURL": data[i]['downloadURL'],
            "websiteURL": data[i]["websiteURL"],
        }
        json_data.append(dic)

    print(json_data[0])

    # with open(FILE_PATH, 'w') as f:
    #     json.dump(json_data, f, indent=2)

if __name__ == '__main__':
    FILE_PATH_1 = 'acg.json'
    FILE_PATH_2 = 'lam.json'

    print(f'1: {FILE_PATH_1}')
    print(f'2: {FILE_PATH_2}')

    choose = int(input(f'\nWhich file you want to update? (1 or 2): '))

    if choose == 1:
        jsonUpdate(FILE_PATH_1)
    else:
        jsonUpdate(FILE_PATH_2)

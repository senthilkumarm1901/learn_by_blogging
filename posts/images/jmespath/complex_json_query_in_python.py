import json
instances_dict = json.load(open('official_example_for_nested.json', 'r'))

for element in instances_dict["reservations"]:
    for instance in element["instances"]:
        for tag in instance["tags"]:
            for value in tag["Values"]:
                if value == "DB":
                    print(f'Instance Type: {instance["type"]}')
                    print(f'Instance State: {instance["state"]}')
                    print(f'Instance Tags: {instance["tags"]}')
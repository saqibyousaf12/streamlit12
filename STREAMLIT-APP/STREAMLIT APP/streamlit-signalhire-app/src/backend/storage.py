def save_data(data: dict):
    with open('data_storage.json', 'a') as f:
        json.dump(data, f)
        f.write('\n')

def retrieve_data(request_id: str):
    results = []
    with open('data_storage.json', 'r') as f:
        for line in f:
            entry = json.loads(line)
            if entry.get('request_id') == request_id:
                results.append(entry)
    return results
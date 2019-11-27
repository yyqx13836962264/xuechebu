import yaml


def build_login_data():
    with open('./data/login_data.yaml', encoding='utf-8') as f:
        data = yaml.safe_load(f)
        data_list = list()  # 声明空列表
        for i in data.values():
            data_list.append((i.get('name'),
                              i.get('pwd')))
        print(data_list)
        return data_list

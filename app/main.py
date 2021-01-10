import yaml
import wget


with open('../datasheet.yml') as file:
    
    data = yaml.load(file, Loader=yaml.FullLoader)
    print(data['vault'])
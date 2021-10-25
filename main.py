import yaml
import scraper

with open("config.yaml") as f:
    config = yaml.safe_load(f)
    username = config['mcgill_user']
    password = config['mcgill_pass']

print(scraper.fetchCurrentTotal(username, password))
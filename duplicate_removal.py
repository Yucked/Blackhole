with open('pihole.txt') as file:
    domains = file.readlines()

dom_len = len(domains)
print(f'Current domains: {dom_len}')
domains = list(dict.fromkeys(domains))
print(f'Removed domains: {dom_len - len(domains)}')

with open('pihole.txt', 'w') as file:
    for domain in domains:
        file.write(domain)

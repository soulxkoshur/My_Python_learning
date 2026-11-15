import re


emails = '''bluefalcon42@example.com

sarah.jenkins88@example.org

techguru2024@example.net

moonlit_raven@example.com

d.martinez.office@example.org

pixel_pioneer@example.net

coffeeaddict99@example.com

j_walker_design@example.org

midnightcoder@example.net

happy_traveler_01@example.com'''


pattern = re.compile(r"[a-zA-Z0-9._-]+?@[a-z]+?\.(com|net|org)")

matches = pattern.finditer(emails)
x = 1
for match in matches:
    print(f"{x}. ", match)
    x += 1

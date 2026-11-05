
SHOWS = [
    "Avatar: The last airbender",
    "Ben 10",
    "Arthur",
    "Spongebob Squarepants",
    "Phineas and ferb",
    "Kim possible",
    "Jimmy Neutron",
    "the Proud family "
]


def main():
    cleaned = []
    for show in SHOWS:
        cleaned.append(show.strip().title())
    print(',\n'.join(cleaned))

main()

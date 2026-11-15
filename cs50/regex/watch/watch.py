
import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = r'<iframe src="(?P<first>https?://)(www\.)?(?P<sec>youtu)(?P<third>be)\.com/embed/(?P<fourth>[a-zA-Z0-9]+)">'
    if match := re.search(pattern, s):
        first = match.group('first')
        sec= match.group('sec')
        third=match.group('third')
        fourth=match.group('fourth')

        return f"https://{sec}.{third}/{fourth}"
    else:
        return None
def process(url):
    ...

if __name__ == "__main__":
    main()

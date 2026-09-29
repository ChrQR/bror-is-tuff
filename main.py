from search import search
from argparse import ArgumentParser

def main():
    parser = ArgumentParser(
        prog="BrorIsTuff",
        description="searches for relevant reddit posts",
        epilog="gng its so easy😭😭😭 just type uv run main.py and type what you want to type"
    )

    parser.add_argument('query', help="query to search for")

    args = parser.parse_args()

    result = search(args.query)

    print_result(result)

def print_result(result):
    for res in result:
        title = res.get("title", "No Title")
        body = res.get("body", "")
        url = res.get("href", "labubu lafufu")
        print(f"- {title} | {body[:25]}... | {url}")

if __name__ == "__main__":
    main()

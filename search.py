from ddgs import DDGS


def search(q: str):
    results  = DDGS().text(f"{q} reddit")
    filtered_results = []
    for res in results:
        if "reddit" in res.get("href", ""):
            filtered_results.append(res)

    return filtered_results

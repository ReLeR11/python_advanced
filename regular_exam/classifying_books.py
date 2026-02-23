def classify_books(*args, **kwargs):
    title_to_isbn = {title: isbn for isbn, title in kwargs.items()}
    fiction = {}
    non_fiction = {}

    for genre, title in args:
        isbn = title_to_isbn.get(title)

        if isbn is None:
            continue

        if genre == "fiction":
            fiction[isbn] = title
        else:
            non_fiction[isbn] = title

    lines = []

    if fiction:
        lines.append("Fiction Books:")

        for isbn in sorted(fiction.keys()):
            lines.append(f"~~~{isbn}#{fiction[isbn]}")

    if non_fiction:
        lines.append("Non-Fiction Books:")
        for isbn in sorted(non_fiction.keys(), reverse=True):
            lines.append(f"***{isbn}#{non_fiction[isbn]}")

    return "\n".join(lines)


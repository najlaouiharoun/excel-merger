
def save(filepath, content):
    content.to_csv(filepath, index=False)
    return 
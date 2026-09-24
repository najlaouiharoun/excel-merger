from charset_normalizer import from_path

def detect_encoding(file_path):
    best = from_path(file_path).best()
    return str(best.encoding) if best else None
def _round_if_num(v):
    try:
        return round(float(v), 2)
    except (ValueError, TypeError):
        return v


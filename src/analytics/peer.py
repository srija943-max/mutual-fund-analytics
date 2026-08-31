def compute_peer_percentiles(df, metric_col, inverse=False):
    ranks = df[metric_col].rank(pct=True, ascending=not inverse)
    return (ranks * 100).round(2)

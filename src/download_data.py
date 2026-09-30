import yfinance as yf
from pathlib import Path

TICKER = "QQQ"
YEARS = 15
OUT_FILE = Path("data/QQQ_daily.csv")


def download(ticker: str = TICKER, years: int = YEARS):
    df = yf.download(
        ticker,
        period=f"{years}y",
        interval="1d",
        auto_adjust=True,
        progress=False,
    )
    df.columns = df.columns.get_level_values(0)
    return df


if __name__ == "__main__":
    data = download()
    OUT_FILE.parent.mkdir(exist_ok=True)
    data.to_csv(OUT_FILE)
    print(data.tail())
    print(f"{len(data)} files guardades a {OUT_FILE}")
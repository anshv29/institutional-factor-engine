import pandas as pd
import yfinance as yf
from sqlalchemy import text
from database import get_engine
import time

def get_sp500_tickers():
    tickers = [
        'AAPL', 'MSFT', 'AMZN', 'NVDA', 'GOOGL', 'META', 'TSLA', 'BRK-B', 'JPM', 'LLY',
        'V', 'UNH', 'AVGO', 'XOM', 'MA', 'JNJ', 'PG', 'HD', 'COST', 'MRK',
        'ABBV', 'CVX', 'CRM', 'BAC', 'AMD', 'WMT', 'KO', 'PEP', 'NFLX', 'TMO',
        'ACN', 'MCD', 'CSCO', 'ABT', 'LIN', 'DHR', 'TXN', 'ADBE', 'WFC', 'PM',
        'CAT', 'GE', 'MS', 'INTU', 'DIS', 'AXP', 'NEE', 'IBM', 'QCOM', 'RTX',
        'GS', 'SPGI', 'HON', 'AMGN', 'LOW', 'UPS', 'ELV', 'ISRG', 'SYK', 'BKNG',
        'PLD', 'T', 'MDLZ', 'ADP', 'VRTX', 'TJX', 'GILD', 'ADI', 'BLK', 'MMC',
        'PGR', 'CB', 'AMAT', 'MU', 'C', 'LRCX', 'ETN', 'SO', 'ZTS', 'SLB',
        'BSX', 'CME', 'REGN', 'BMY', 'NOC', 'WM', 'CI', 'BDX', 'EOG', 'ITW',
        'PNC', 'AON', 'HCA', 'USB', 'FCX', 'APH', 'MCO', 'TGT', 'EMR', 'DE',
        'MPC', 'PSA', 'VLO', 'CL', 'NSC', 'FDX', 'KMB', 'AIG', 'SHW', 'MCK',
        'MMM', 'ECL', 'GD', 'KLAC', 'EW', 'SNPS', 'CDNS', 'OXY', 'ORLY', 'MSI',
        'NEM', 'F', 'GM', 'AZO', 'ROP', 'TFC', 'HUM', 'AFL', 'PAYX', 'MCHP',
        'PSX', 'COF', 'FTNT', 'CARR', 'NXPI', 'WELL', 'TDG', 'FAST', 'ROST', 'CCI',
        'A', 'O', 'EXC', 'SPG', 'KR', 'IDXX', 'MNST', 'CTAS', 'MET', 'IQV',
        'TEL', 'D', 'CTVA', 'GWW', 'PCAR', 'HSY', 'DOW', 'PPG', 'AME', 'ODFL',
        'VRSK', 'BIIB', 'XEL', 'DLR', 'DVN', 'OTIS', 'ACGL', 'URI', 'GEHC', 'HES',
        'GLW', 'CPRT', 'MTD', 'PRU', 'YUM', 'CTSH', 'WAB', 'SBAC', 'DLTR', 'DD',
        'BK', 'CDW', 'HPQ', 'WTW', 'IFF', 'FANG', 'ROK', 'GIS', 'PH', 'ALL',
        'KEYS', 'STZ', 'TROW', 'WEC', 'ANSS', 'LHX', 'AJG', 'PWR', 'FITB', 'EBAY',
        'DG', 'CHD', 'RMD', 'VLTO', 'CBRE', 'BR', 'ETR', 'SW', 'TTWO', 'WBD',
        'HAL', 'HPE', 'AVB', 'MTB', 'EQR', 'RF', 'ES', 'PPL', 'LEN', 'NUE',
        'ZBRA', 'TSN', 'APTV', 'VICI', 'ON', 'BALL', 'WAT', 'FIS', 'CAH', 'FTV',
        'POOL', 'LYB', 'CFG', 'IP', 'TER', 'HUBB', 'OMC', 'STE', 'EXPD', 'MOH',
        'CINF', 'AMCR', 'NTAP', 'HOLX', 'TYL', 'WY', 'ULTA', 'BAX', 'J', 'SWKS',
        'DTE', 'CE', 'AKAM', 'SYF', 'CMS', 'WDC', 'COO', 'CHRW', 'JBHT', 'TECH',
        'MKC', 'PEAK', 'AES', 'PFG', 'INCY', 'EPAM', 'NDSN', 'CPT', 'UDR', 'EVRG',
        'NI', 'FMC', 'L', 'LNC', 'IVZ', 'AIZ', 'HII', 'BIO', 'HSIC', 'REG',
        'NWSA', 'BWA', 'TAP', 'PNW', 'DVA', 'MOS', 'HRL', 'WYNN', 'LKQ', 'AAL',
        'UAL', 'DAL', 'LUV', 'CCL', 'RCL', 'NCLH', 'MGM', 'CZR', 'MAR', 'HLT',
        'SPY', 'QQQ', 'IWM', 'GLD', 'SLV', 'TLT', 'HYG', 'LQD', 'VNQ', 'XLE',
        'XLF', 'XLK', 'XLV', 'XLI', 'XLP', 'XLU', 'XLB', 'XLRE', 'XLC', 'XLY',
        'ADSK', 'PAYC', 'HBAN', 'KEY', 'ALLY', 'SNA', 'WHR', 'LEA', 'NRG', 'APA',
        'MRO', 'COP', 'PXD', 'CTRA', 'PR', 'SM', 'MTDR', 'CHRD', 'PDCE', 'AR',
        'EQT', 'RRC', 'CNX', 'NOV', 'BKR', 'FTI', 'TDW', 'XPRO', 'LBRT', 'PUMP',
        'ACLS', 'AEIS', 'AEVA', 'AGCO', 'AIT', 'ALB', 'ALGN', 'ALLE', 'ALSN', 'AMG',
        'AMTM', 'AMWD', 'AN', 'ANET', 'ANF', 'AOS', 'APD', 'ARE', 'ATO', 'ATVI',
        'AWK', 'AWR', 'AXS', 'AYI', 'AZZ', 'BBY', 'BC', 'BEN', 'BF-B', 'BG',
        'BKI', 'BMRN', 'BOH', 'BR', 'BRO', 'BSIG', 'BXP', 'CABO', 'CCI', 'CCMP',
        'CDK', 'CDAY', 'CFR', 'CHE', 'CHKP', 'CHTR', 'CMA', 'CMI', 'CNP', 'CNS',
        'COHR', 'COLB', 'COR', 'CUBE', 'CW', 'DAR', 'DAN', 'DCI', 'DECK', 'DGX',
        'DKS', 'DKNG', 'DLTR', 'DOV', 'DPZ', 'DRI', 'DT', 'DTM', 'DXC', 'EFX',
        'EG', 'EIX', 'EL', 'EME', 'ENPH', 'ENS', 'EPC', 'ESAB', 'ESNT', 'ESGR',
        'EXR', 'FBIN', 'FBMS', 'FFIV', 'FHN', 'FICO', 'FLO', 'FLR', 'FNF', 'FNV',
        'FR', 'FROG', 'FRT', 'GBCI', 'GFF', 'GFI', 'GNTX', 'GPK', 'GPN', 'GTLS',
        'HAS', 'HBI', 'HIG', 'HIW', 'HLI', 'HMST', 'HNI', 'HPE', 'HRB', 'HRI',
        'HST', 'HTH', 'HWM', 'IAC', 'ICE', 'IDCC', 'IEX', 'IIVI', 'INF', 'INGR',
        'IPG', 'IPGP', 'IRM', 'ITCI', 'ITT', 'JACK', 'JEF', 'JKHY', 'JLL', 'JW-A',
        'KIM', 'KMI', 'KNX', 'KNTK', 'KRC', 'LII', 'LIVN', 'LMT', 'LOPE', 'LPX',
        'LSI', 'LSTR', 'LW', 'LXP', 'LYV', 'MAA', 'MAN', 'MANH', 'MATX', 'MCD',
        'MKSI', 'MLM', 'MMSI', 'MNR', 'MODG', 'MPWR', 'MRC', 'MRNA', 'MSA', 'MSCI',
        'MSM', 'MTN', 'MTZ', 'NDAQ', 'NFG', 'NNN', 'NRZ', 'NTRS', 'NVR', 'NWL',
        'OGE', 'OGS', 'OHI', 'OKE', 'OLN', 'OLLI', 'ORI', 'OSK', 'OVV', 'PAG',
        'PB', 'PCVX', 'PDCO', 'PEN', 'PEG', 'PENN', 'PII', 'PKG', 'PLNT', 'PNFP',
        'PNM', 'POST', 'PPC', 'PRGO', 'PRG', 'PSB', 'PSTG', 'PTCT', 'PVH', 'R',
        'RGA', 'RGP', 'RHI', 'RL', 'RNG', 'RPM', 'RRX', 'RS', 'REXR', 'RGLD',
        'SAM', 'SANM', 'SBCF', 'SBNY', 'SBOW', 'SBUX', 'SFBS', 'SFM', 'SIGI', 'SJM',
        'SKX', 'SLG', 'SNV', 'SON', 'SRPT', 'SSB', 'SUI', 'SWK', 'SWN', 'SXT',
        'TFX', 'THC', 'THO', 'TKR', 'TOL', 'TPH', 'TPR', 'TRMB', 'TRN', 'TRV',
        'TSCO', 'TTC', 'TXRH', 'TXT', 'UGI', 'UMBF', 'UNM', 'UNP', 'VFC', 'VNOM',
        'VNT', 'VTR', 'VVV', 'VZ', 'WAL', 'WBA', 'WCC', 'WEX', 'WH', 'WLK',
        'WMS', 'WOR', 'WPC', 'WRB', 'WRK', 'WSM', 'WSO', 'WTS', 'WWD', 'XYL'
    ]
    print(f"Loaded {len(tickers)} tickers")
    return tickers

def create_price_table():
    engine = get_engine()
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS stock_prices (
        date DATE NOT NULL,
        ticker VARCHAR(10) NOT NULL,
        open FLOAT,
        high FLOAT,
        low FLOAT,
        close FLOAT,
        volume BIGINT,
        PRIMARY KEY (date, ticker)
    );
    """
    with engine.connect() as conn:
        conn.execute(text(create_table_sql))
        conn.commit()
    print("Price table created!")

def pull_and_store_data(tickers, start="2014-01-01", end="2024-12-31"):
    engine = get_engine()
    
    failed  = []
    success = 0
    
    for i, ticker in enumerate(tickers):
        try:
            print(f"[{i+1}/{len(tickers)}] Pulling {ticker}...")
            
            df = yf.download(ticker, start=start, end=end,
                           auto_adjust=True, progress=False)
            
            if df.empty:
                print(f"  No data for {ticker} — skipping")
                failed.append(ticker)
                continue
            
            df = df.reset_index()
            df.columns = df.columns.get_level_values(0)
            df.columns = [c.lower() for c in df.columns]
            df['ticker'] = ticker
            df = df[['date', 'ticker', 'open', 'high', 'low', 'close', 'volume']]
            df['date'] = pd.to_datetime(df['date']).dt.date
            df = df.dropna()
            
            df.to_sql('stock_prices', engine,
                     if_exists='append', index=False, method='multi')
            
            success += 1
            time.sleep(0.3)
            
        except Exception as e:
            print(f"  Failed {ticker}: {e}")
            failed.append(ticker)
            continue
    
    print(f"\nDone! {success} stocks loaded successfully.")
    print(f"Failed: {len(failed)} stocks — {failed[:10]}")

if __name__ == "__main__":
    tickers = get_sp500_tickers()
    create_price_table()
    pull_and_store_data(tickers)
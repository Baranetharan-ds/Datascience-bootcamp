import pandas as pd
import urllib.request

# Download the automobile dataset
url = "https://raw.githubusercontent.com/nunnarilabs/ml/master/automobileEDA.csv"
output_file = "automobileEDA.csv"

try:
    # Method 1: Using pandas read_csv with to_csv
    df = pd.read_csv(url)
    df.to_csv(output_file, index=False)
    print(f"✓ Successfully downloaded and saved {output_file}")
    print(f"  Shape: {df.shape}")
    print(f"  Columns: {list(df.columns)}")
except Exception as e:
    print(f"✗ Error downloading file: {e}")
    
    # Method 2: Fallback using urllib
    try:
        urllib.request.urlretrieve(url, output_file)
        print(f"✓ Successfully downloaded {output_file} using urllib")
    except Exception as e2:
        print(f"✗ Fallback method also failed: {e2}")

import time
from datetime import datetime
INTERVAL = 10 # 実行間隔を秒単位で設定 (例: 1秒, 5秒, 10秒など)
while True:
    start_time = datetime.now()
    print(f"処理実行: {start_time.strftime('%H:%M:%S.%f')}")
    time.sleep(max(0, INTERVAL - (time.time() % INTERVAL)))
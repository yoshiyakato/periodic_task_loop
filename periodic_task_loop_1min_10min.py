import time
from datetime import datetime

BASE_INTERVAL  = 10      # ループ刻み（秒）──「壁時計」に合わせるためだけに使う
INTERVAL_60    = 60      # 60秒タスク
INTERVAL_600   = 600     # 600秒タスク

epoch0 = time.time()
last_blk_60  = int(epoch0 // INTERVAL_60)     # ❶ 直近の 60秒ブロック
last_blk_600 = int(epoch0 // INTERVAL_600)    # ❷ 直近の 600秒ブロック

print(f"ループ開始: {datetime.now()}  (基準={BASE_INTERVAL}s)")

while True:                                     # ❸
    now_epoch = time.time()
    now = datetime.fromtimestamp(now_epoch)
    print(f"@ {now:%H:%M:%S.%f}")

    # --- 60秒ごとの処理 ------------------------------------------
    blk_60 = int(now_epoch // INTERVAL_60)      # ❹
    if blk_60 > last_blk_60:                    # ❺ ブロック更新なら実行
        print(f"Running 60s task  @ {now:%H:%M:%S.%f}")
        last_blk_60 = blk_60                    # ❻

    # --- 600秒（10分）ごとの処理 --------------------------------
    blk_600 = int(now_epoch // INTERVAL_600)    # ❼
    if blk_600 > last_blk_600:                  # ❽
        print(f"Running 600s task @ {now:%H:%M:%S.%f}")
        last_blk_600 = blk_600                  # ❾

    # --- 次の 10秒境界まで待機 -----------------------------------
    time.sleep(max(0, BASE_INTERVAL - (time.time() % BASE_INTERVAL)))  # ❿

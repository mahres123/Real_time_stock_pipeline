import pandas as pd
import json

columns = [
    "timestamp", "instrument_token", "last_price", "volume", "sell_quantity", "last_quantity", "change", "average_price",
    "open", "high", "low", "close",
    "depth_buy_price_0", "depth_buy_orders_0", "depth_buy_quantity_0",
    "depth_sell_price_0", "depth_sell_orders_0", "depth_sell_quantity_0",
    "depth_buy_price_1", "depth_buy_orders_1", "depth_buy_quantity_1",
    "depth_sell_price_1", "depth_sell_orders_1", "depth_sell_quantity_1",
    "depth_buy_price_2", "depth_buy_orders_2", "depth_buy_quantity_2",
    "depth_sell_price_2", "depth_sell_orders_2", "depth_sell_quantity_2",
    "depth_buy_price_3", "depth_buy_orders_3", "depth_buy_quantity_3",
    "depth_sell_price_3", "depth_sell_orders_3", "depth_sell_quantity_3",
    "depth_buy_price_4", "depth_buy_orders_4", "depth_buy_quantity_4",
    "depth_sell_price_4", "depth_sell_orders_4", "depth_sell_quantity_4"
]

# ✅ CHANGER LE SEP EN VIRGULE !
df = pd.read_csv("log_inf.csv", sep=",", names=columns, skiprows=1)

json_data = []

for index, row in df.iterrows():
    if index >= 100:
        break

    tick = {
        "timestamp": row["timestamp"],
        "instrument_token": row["instrument_token"],
        "last_price": row["last_price"],
        "volume": row["volume"],
        "sell_quantity": row["sell_quantity"],
        "last_quantity": row["last_quantity"],
        "change": row["change"],
        "average_price": row["average_price"],
        "open": row["open"],
        "high": row["high"],
        "low": row["low"],
        "close": row["close"],
        "depth": {
            "buy": [],
            "sell": []
        }
    }

    for i in range(5):
        tick["depth"]["buy"].append({
            "price": row[f"depth_buy_price_{i}"],
            "orders": row[f"depth_buy_orders_{i}"],
            "quantity": row[f"depth_buy_quantity_{i}"]
        })
        tick["depth"]["sell"].append({
            "price": row[f"depth_sell_price_{i}"],
            "orders": row[f"depth_sell_orders_{i}"],
            "quantity": row[f"depth_sell_quantity_{i}"]
        })

    json_data.append(tick)

with open("stock_data_sample.json", "w") as f:
    json.dump(json_data, f, indent=2)

print("✅ JSON échantillon généré correctement 🎉")
# flake8: noqa
import vnpy_crypto,time
vnpy_crypto.init()

import pdb
import psycopg2
from typing import Dict, List, Any
from vnpy.event import EventEngine
from vnpy.trader.engine import MainEngine
#from vnpy.trader.setting import SETTING_FILENAME, SETTINGS
from vnpy.trader.utility import TRADER_DIR, TEMP_DIR, load_json



from vnpy_pgsqlsnapshot import PgsqlSnapshotEngine
from vnpy_ib import IbGateway
from vnpy_ftx import FtxGateway
from vnpy_deribit import DeribitGateway
from vnpy_binance import (
    BinanceSpotGateway,
    BinanceUsdtGateway,
    BinanceInverseGateway
)

  
def main():
    """"""
    event_engine = EventEngine()
    main_engine = MainEngine(event_engine)
    gateway_tbl: Dict[ str, BaseGateway] = {"IBSnap":IbGateway, 
                                            "FTX":FtxGateway, 
                                            "Deribit":DeribitGateway,
                                            "Binance_usdt": BinanceUsdtGateway }
    #pdb.set_trace()
    for gateway_name in gateway_tbl:
        print(f"adding gateway {gateway_name}")
        main_engine.add_gateway(gateway_tbl[gateway_name],gateway_name)

    for gateway_name in main_engine.get_all_gateway_names():
        setting_json = f"{TEMP_DIR}/connect_{gateway_name.lower()}.json"
        setting = load_json(setting_json)
        print(f"loading {setting_json}")
        main_engine.connect(setting,gateway_name)
        time.sleep(2)

    snap = main_engine.add_engine(PgsqlSnapshotEngine)

    while True:
        snap.save_account_data(main_engine.get_all_accounts())
        snap.save_position_data(main_engine.get_all_positions())
        time.sleep(2)
        
if __name__ == "__main__":
    main()

#!/usr/bin/env python
# flake8: noqa
import vnpy_crypto,time
vnpy_crypto.init()


from vnpy.event import EventEngine

from vnpy.trader.engine import MainEngine
from vnpy.trader.utility import TRADER_DIR,TEMP_DIR,load_json
from vnpy.trader.ui import MainWindow, create_qapp
import pdb

# from vnpy_ctp import CtpGateway
# from vnpy_ctptest import CtptestGateway
# from vnpy_mini import MiniGateway
# from vnpy_femas import FemasGateway
# from vnpy_sopt import SoptGateway
# from vnpy_sec import SecGateway
# from vnpy_uft import UftGateway
# from vnpy_esunny import EsunnyGateway
# from vnpy_xtp import XtpGateway
# from vnpy_tora import ToraStockGateway
# from vnpy_tora import ToraOptionGateway
# from vnpy_comstar import ComstarGateway
# from vnpy_ib import IbGateway
# from vnpy_tap import TapGateway
# from vnpy_da import DaGateway
# from vnpy_rohon import RohonGateway
# from vnpy_tts import TtsGateway
# from vnpy_ost import OstGateway
# from vnpy_hft import GtjaGateway
from vnpy_pgsqlsnapshot import PgsqlSnapshotEngine

from vnpy_algotrading import AlgoTradingApp
from vnpy_datarecorder import DataRecorderApp
from vnpy_riskmanager import RiskManagerApp
from vnpy_portfoliomanager import PortfolioManagerApp
from vnpy_paperaccount import PaperAccountApp
from vnpy_spreadtrading import SpreadTradingApp


#from vnpy_scripttrader import ScriptTraderApp
#from vnpy_ctastrategy import CtaStrategyApp
#from vnpy_ctabacktester import CtaBacktesterApp
#from vnpy_optionmaster import OptionMasterApp
#from vnpy_portfoliostrategy import PortfolioStrategyApp
#from vnpy_scripttrader import ScriptTraderApp
#from vnpy_chartwizard import ChartWizardApp
#from vnpy_rpcservice import RpcServiceApp
#from vnpy_excelrtd import ExcelRtdApp
#from vnpy_datamanager import DataManagerApp
#from vnpy_webtrader import WebTraderApp

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
    qapp = create_qapp()

    event_engine = EventEngine()

    main_engine = MainEngine(event_engine)



    gateway_tbl: Dict[ str, BaseGateway ] = {"IB":IbGateway, 
                                             "FTX":FtxGateway, 
                                             "Deribit":DeribitGateway,
                                             "Binance_usdt": BinanceUsdtGateway }
    #pdb.set_trace()
    for gateway_name in gateway_tbl:
        print(f"adding gateway {gateway_name}")
        main_engine.add_gateway(gateway_tbl[gateway_name],gateway_name)

    main_engine.add_app(AlgoTradingApp)
    main_engine.add_app(SpreadTradingApp)
    main_engine.add_app(DataRecorderApp)
    main_engine.add_app(PortfolioManagerApp)
    #main_engine.add_app(PaperAccountApp)
    main_engine.add_app(RiskManagerApp)

    main_engine.add_engine(PgsqlSnapshotEngine)

    main_window = MainWindow(main_engine, event_engine)
    main_window.showMaximized()


    for gateway_name in main_engine.get_all_gateway_names():
        setting_json = f"{TEMP_DIR}/connect_{gateway_name.lower()}.json"
        setting = load_json(setting_json)
        print(f"loading {setting_json}")
        main_engine.connect(setting,gateway_name)
        time.sleep(2)
        
        
    # main_engine.add_gateway(CtpGateway)
    # main_engine.add_gateway(CtptestGateway)
    # main_engine.add_gateway(MiniGateway)
    # main_engine.add_gateway(FemasGateway)
    # main_engine.add_gateway(SoptGateway)
    # main_engine.add_gateway(SecGateway)    
    # main_engine.add_gateway(UftGateway)
    # main_engine.add_gateway(EsunnyGateway)
    # main_engine.add_gateway(XtpGateway)
    # main_engine.add_gateway(ToraStockGateway)
    # main_engine.add_gateway(ToraOptionGateway)
    # main_engine.add_gateway(OesGateway)
    # main_engine.add_gateway(ComstarGateway)
    # main_engine.add_gateway(TapGateway)
    # main_engine.add_gateway(DaGateway)
    # main_engine.add_gateway(RohonGateway)
    # main_engine.add_gateway(TtsGateway)
    # main_engine.add_gateway(OstGateway)
    # main_engine.add_gateway(NhFuturesGateway)
    # main_engine.add_gateway(NhStockGateway)

    #main_engine.add_app(CtaStrategyApp)
    #main_engine.add_app(CtaBacktesterApp)
    #main_engine.add_app(OptionMasterApp)
    #main_engine.add_app(PortfolioStrategyApp)
    #main_engine.add_app(ScriptTraderApp)
    #main_engine.add_app(ChartWizardApp)
    #main_engine.add_app(RpcServiceApp)
    #main_engine.add_app(ExcelRtdApp)
    #main_engine.add_app(DataManagerApp)
    #main_engine.add_app(WebTraderApp)
    

    qapp.exec()

if __name__ == "__main__":
    main()

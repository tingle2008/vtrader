#!/usr/bin/env python
import time
import vnpy_crypto
vnpy_crypto.init()


from vnpy.event import EventEngine
from vnpy.trader.engine import MainEngine
from vnpy.trader.setting import SETTING_FILENAME, SETTINGS
from vnpy.trader.ui import MainWindow, create_qapp
from IPython import embed

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

from vnpy_algotrading import AlgoTradingApp

#from vnpy_scripttrader import ScriptTraderApp
#from vnpy_ctastrategy import CtaStrategyApp
#from vnpy_ctabacktester import CtaBacktesterApp
#from vnpy_spreadtrading import SpreadTradingApp
#from vnpy_optionmaster import OptionMasterApp
#from vnpy_portfoliostrategy import PortfolioStrategyApp
#from vnpy_scripttrader import ScriptTraderApp
#from vnpy_chartwizard import ChartWizardApp
#from vnpy_rpcservice import RpcServiceApp
#from vnpy_excelrtd import ExcelRtdApp
#from vnpy_datamanager import DataManagerApp
#from vnpy_datarecorder import DataRecorderApp
#from vnpy_riskmanager import RiskManagerApp
#from vnpy_webtrader import WebTraderApp
from vnpy_portfoliomanager import PortfolioManagerApp
from vnpy_paperaccount import PaperAccountApp


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
    deribit_setting: Dict[str, Any] = {
        "key": "3Vd7PU1y",
        "secret": "hVbykJ8JcyWtt-x6s17OU_hynylG4FdJX-gpTIqN7TM",
        "代理地址": "",
        "代理端口": "",
        "服务器": "REAL"
    }

    ibapi_setting: Dict[str, Any] = {
        "TWS地址": "192.168.1.79",
        "TWS端口": 7496,
        "客户号": 1,
        "交易账户": "U8937395"
    }

    ftx_setting: Dict[str, Any] = {
        "key": "YYf7SjHT0GEBcrgXe5C6UaAgk5Tzx2wrgdiQeFrA",
        "secret": "8mddFgelrpTFcdkJy3rZSYG1ThWViPx5dohZiQui",
        "代理地址": "",
        "代理端口": 0,
    }
    
    binance_setting: Dict[str, Any] = {
    "key": "JdkALn8upltv3bmszoYGik9WxpsJGN3i00G52xRM7a9nu8PjoVsaGhkZ9w092kc8",
    "secret": "ceN93thB5I4KQk5pjLlwRP2AHpGUugBRjecJNSyVyI1n3bVCkG8WVlkPmVTGznrs",
    "服务器": "REAL",
    "代理地址": "",
    "代理端口": 0,
    }
    #settings: dict = copy(SETTINGS)
    #settings.update(load_json(SETTING_FILENAME))

    event_engine = EventEngine()

    main_engine = MainEngine(event_engine)

    main_engine.add_gateway(IbGateway,"IB")
    main_engine.add_gateway(FtxGateway,"FTX")
    main_engine.add_gateway(DeribitGateway,"Deribit")
    main_engine.add_gateway(BinanceUsdtGateway,"BinanceU")

    main_engine.connect(ibapi_setting,"IB")
    main_engine.connect(deribit_setting,"Deribit")
    main_engine.connect(ftx_setting,"FTX")
    main_engine.connect(binance_setting,"BinanceU")
    main_engine.add_app(PortfolioManagerApp)
    main_engine.add_app(AlgoTradingApp)
    embed()

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

    #main_engine.add_app(PaperAccountApp)
    #main_engine.add_app(CtaStrategyApp)
    #main_engine.add_app(CtaBacktesterApp)
    #main_engine.add_app(SpreadTradingApp)
    #main_engine.add_app(OptionMasterApp)
    #main_engine.add_app(PortfolioStrategyApp)
    #main_engine.add_app(ScriptTraderApp)
    #main_engine.add_app(ChartWizardApp)
    #main_engine.add_app(RpcServiceApp)
    #main_engine.add_app(ExcelRtdApp)
    #main_engine.add_app(DataManagerApp)
    #main_engine.add_app(DataRecorderApp)
    #main_engine.add_app(RiskManagerApp)
    #main_engine.add_app(WebTraderApp)

#    while True:
#        time.sleep(10)
#        print(main_engine.get_all_trades())

#        for acc in main_engine.get_all_accounts():
#            print(acc)
#
#        for pos in main_engine.get_all_positions():
#            print(pos)



if __name__ == "__main__":
    main()

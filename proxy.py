##
#
#   Based on: https://github.com/MlgmXyysd/ MITM proxy script
#   Original fiddler script: https://github.lunatic.moe/fiddlerscript
#   MITM proxy: https://snapshots.mitmproxy.org/9.0.1/mitmproxy-9.0.1-windows-x64-installer.exe
#
#   Environment requirement:
#     - mitmdump from mitmproxy
#
#   @original author: MlgmXyysd
#   @version: custom for andigena
#
##

from mitmproxy import http
from proxy_config import USE_SSL_GATE, USE_SSL_DISPATCH, DISPATCH_HOST, DISPATCH_PORT, GATE_HOST, GATE_PORT, GATE_DOMAINS, DISPATCH_DOMAINS

class Andigena_Proxy:
    def request(self, flow: http.HTTPFlow) -> None:
        if flow.request.host in DISPATCH_DOMAINS:
            if USE_SSL_DISPATCH:
                flow.request.scheme = "https"
            else:
                flow.request.scheme = "http"
            flow.request.host = DISPATCH_HOST
            flow.request.port = DISPATCH_PORT
            
        if flow.request.host in GATE_DOMAINS:
            if USE_SSL_GATE:
                flow.request.scheme = "https"
            else:
                flow.request.scheme = "http"
            flow.request.host = GATE_HOST
            flow.request.port = GATE_PORT

addons = [Andigena_Proxy()]

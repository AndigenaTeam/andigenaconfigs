import os

USE_SSL_GATE = False
USE_SSL_DISPATCH = False

GATE_HOST = "127.0.0.1"
GATE_PORT = 669

DISPATCH_HOST = "127.0.0.1"
DISPATCH_PORT = 663

# ===================================================================
#                            DOMAINS
# ===================================================================

GATE_DOMAINS = [
    "user.mihoyo.com",
    "account.mihoyo.com",
    "account.hoyoverse.com",
    "webstatic.mihoyo.com",
    "webstatic-test.mihoyo.com",
    "webstatic-sea.mihoyo.com",
    "webstatic-sea.hoyoverse.com",
    "sdk-os-static.mihoyo.com",
    "sdk-os-static.hoyoverse.com",
    "sdk-static.mihoyo.com",
    "sandbox-sdk.mihoyo.com",
    "hk4e-api-os-static.mihoyo.com",
    "hk4e-sdk.mihoyo.com",
    "hk4e-sdk-os.mihoyo.com",
    "hk4e-sdk-os.hoyoverse.com",
    "hk4e-sdk-os-static.hoyoverse.com",
    "hk4e-sdk-os-s.hoyoverse.com",
    "hk4e-sdk-s.mihoyo.com",
    "gameapi-account.mihoyo.com",
    "api-account-os.hoyoverse.com",
    "webapi-os.account.hoyoverse.com"
    ]
    
DISPATCH_DOMAINS = [
    "ns10dispatch.yuanshen.com"
    "dispatchosglobal.yuanshen.com",
    "dispatchosglobal.yuanshen.com",
    "osusadispatch.yuanshen.com",
    "oseurodispatch.yuanshen.com",
    "osasiadispatch.yuanshen.com",
    "dispatchcntest.yuanshen.com",
    "cnbeta01dispatch.yuanshen.com",
    "dispatchcnglobal.yuanshen.com",
    "cnbeta02dispatch.yuanshen.com",
    "devlog-upload.mihoyo.com",
    "log-upload.mihoyo.com",
    "log-upload-os.mihoyo.com",
    "log-upload-os.hoyoverse.com",
    "ys-log-upload.mihoyo.com",
    "uspider.yuanshen.com",
    "overseauspider.yuanshen.com",
    "api-beta-sdk.mihoyo.com",
    "api-beta-sdk-os.mihoyo.com",
    "minor-api.mihoyo.com",
    "minor-api-os.hoyoverse.com",
    "public-data-api.mihoyo.com",
    "sg-public-data-api.hoyoverse.com",
    "abtest-api-data-sg.hoyoverse.com",
    "api-os-takumi.mihoyo.com"
    ]

if os.getenv('MITM_USE_SSL_GATE') != None:
    USE_SSL_GATE = bool(os.getenv('MITM_USE_SSL_GATE'))
    
if os.getenv('MITM_USE_SSL_DISPATCH') != None:
    USE_SSL_DISPATCH = bool(os.getenv('MITM_USE_SSL_DISPATCH'))
    
if os.getenv('MITM_GATE_HOST') != None:
    GATE_HOST = os.getenv('MITM_GATE_HOST')
    
if os.getenv('MITM_GATE_PORT') != None:
    REMOTE_PORT = int(os.getenv('MITM_GATE_PORT'))

if os.getenv('MITM_DISPATCH_HOST') != None:
    DISPATCH_HOST = os.getenv('MITM_DISPATCH_HOST')
    
if os.getenv('MITM_DISPATCH_PORT') != None:
    DISPATCH_PORT = int(os.getenv('MITM_DISPATCH_PORT'))

print('-----------------------')
print('GateServer SSL: ' + str(USE_SSL_GATE))
print('Dispatch SSL: ' + str(USE_SSL_DISPATCH))
print('-----------------------')
print('GateServer host: ' + GATE_HOST)
print('GateServer port: ' + str(GATE_PORT))
print('-----------------------')
print('Dispatch host: ' + DISPATCH_HOST)
print('Dispatch port: ' + str(DISPATCH_PORT))
print('-----------------------')

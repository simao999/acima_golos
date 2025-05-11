import time
import requests
from telegram import Bot
from apscheduler.schedulers.blocking import BlockingScheduler

BOT_TOKEN = "7359570901:AAHV2m-0w21RDHy15VQU8C7CmtwWLoHC_Q4"
CHAT_ID = "1487784686"

bot = Bot(token=BOT_TOKEN)

def get_live_games():
    # Simulação (vamos integrar dados reais mais tarde)
    return [{
        'league': 'La Liga',
        'home': 'Real Madrid',
        'away': 'Barcelona',
        'minute': 72,
        'score': '1-1',
        'xg': 3.5,
        'shots': 19,
        'dangerous_attacks': 45,
        'pressure': 'Alta',
        'goal_probability': 82,
        'suggested_market': 'Over 2.5'
    }]

def format_message(game):
    return (
        f"⚽ Jogo: {game['home']} vs {game['away']}\n"
        f"⏱ {game['minute']}' | Resultado: {game['score']}\n"
        f"xG Total: {game['xg']} | Remates: {game['shots']}\n"
        f"Ataques perigosos: {game['dangerous_attacks']} | Pressão: {game['pressure']}\n\n"
        f"Probabilidade de mais 1 golo: {game['goal_probability']}%\n"
        f"SINAL: Entrada em {game['suggested_market']} recomendada\n"
        f"Liga: {game['league']}"
    )

def send_signals():
    games = get_live_games()
    for game in games:
        if game['goal_probability'] >= 70:
            message = format_message(game)
            bot.send_message(chat_id=CHAT_ID, text=message)

scheduler = BlockingScheduler()
scheduler.add_job(send_signals, 'interval', minutes=5)
scheduler.start()

import os
from telegram import Bot
import asyncio

bot = Bot("7359570901:AAHV2m-0w21RDHy15VQU8C7CmtwWLoHC_Q4")

async def main():
    await bot.send_message(chat_id="1487784686", text="Bot está online!")

# Para evitar erro de "port scan", vamos forçar a escuta de uma porta fictícia
if __name__ == "__main__":
    import socket
    from threading import Thread

    def keep_alive():
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('0.0.0.0', 5000))  # Porta fictícia
        server_socket.listen(1)
        server_socket.accept()

    # Inicia a "escuta" em segundo plano para evitar erro de porta
    Thread(target=keep_alive).start()

    # Função principal do bot
    asyncio.run(main())


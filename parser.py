# -*- coding: utf-8 -*-
"""Modules for parsing"""
import json
import requests
import config


def create_message(nickname: str, stats: dict) -> str:
    message = f"{nickname}\n&#9889;LVL - {stats['skill_level']} &#9889;" \
                        f"\n&#128142;ELO - {stats['faceit_elo']} &#128142;" \
                        f"\n&#128299;K/D - {stats['Average K/D Ratio']} &#128299;" \
                        f"\n&#128128;Headshots - {stats['Average Headshots %']} % &#128128;" \
                        f"\n&#128302;Winrate - {stats['Win Rate %']} % &#128302;"
    return message


def get_data(nickname: str) -> str:
    """
    :param nickname: A string representing of nickname
    :param faceit_token: A string representing of your faceit token
    """
    headers = {"accept": "application/json", "Authorization": f"Bearer {config.FACEIT_TOKEN}"}
    player_request = requests.get(f"https://open.faceit.com/data/v4/players?nickname={nickname}", headers=headers)
    if player_request.status_code == 200:
        player = json.loads(player_request.content)
        player_data = player["games"]["csgo"]
        stats_request = requests.get(f"https://open.faceit.com/data/v4/players/{player['player_id']}/stats/csgo", headers=headers)
        stats = json.loads(stats_request.content)["lifetime"]
        message = create_message(nickname, {**player_data, **stats})
    elif player_request.status_code == 404:
        message = 'Игрок не найден'
    else:
        message = 'Произошла ошибка'
    return message

import config
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
from parser import get_data

def main() -> None:
    vk_session = vk_api.VkApi(token=config.VK_TOKEN)
    longpoll = VkBotLongPoll(vk_session, config.VK_GROUP_ID)
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            peer_id = event.object.message['peer_id']
            nickname = event.object.message['text']
            stats_message = get_data(nickname)
            vk_session.method("messages.send", {"peer_id": peer_id,
                                                "random_id": get_random_id(),
                                                "message": stats_message})

if __name__ == "__main__":
    main()

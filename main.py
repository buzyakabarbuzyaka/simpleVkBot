from vault import KeyHolder
import random
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

token, group_id = KeyHolder.giveGroupKeys('./vault')

vk_session = vk_api.VkApi(token=token)
longpoll = VkBotLongPoll(vk_session, group_id=group_id)
vk = vk_session.get_api()

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        vk.messages.send(peer_id=event.object.peer_id, message="Ди на хуй)", random_id=random.randint(0, 10000))

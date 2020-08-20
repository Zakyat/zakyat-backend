import vk_api
import os

app_id = os.getenv('VK_APP_ID')
client_secret = os.getenv('VK_CLIENT_SECRET')
website_url = os.getenv('WEBSITE_URL_NEWS_PAGE')


def create_vk_post(title, link):
    vk_sess = vk_api.VkApi(app_id=app_id, client_secret=client_secret, scope='wall')
    vk_sess.auth()
    vk = vk_sess.get_api()
    vk.wall.post(message=title, attachments=f'{website_url}/{link}')
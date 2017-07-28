

# WALL STEALER - скрипт для полного копирования поста, в случае каких-либо ошибок с вашим головным мозгом (не лечит рак, опухоли и др.)



# access token - ключ доступа к странице/группе, куда вы хотите внести пост, без него скрипт работать не будет.
access_token = 'Ваш Токен'

















































# Важная часть работы скрипта - его код. Если у вас есть какие-то болезни головного мозга (галлюны, фобии, рак и т.д.), убедительная просьба, ничего тут не трогать
# Если вы всё же решили что-то изменить, то прошу не репортить проект только из-за ваших кривых рук.

import vk
import requests


session = vk.Session()
api = vk.API(session, access_token=access_token, v='5.67', lang='ru')

checkTokenLink = requests.get("https://api.vk.com/method/status.get?access_token="+str(access_token))
checkTokenResponse = checkTokenLink.text
checkTokenResponse = eval(checkTokenResponse)
if checkTokenResponse.get("error"):
	checkTokenError = checkTokenResponse["error"]["error_code"]
	if checkTokenError == 5:
		print("#################################################")
		print(" ")
		print(" У вас нет ACCESS-TOKEN'а или он недействителен")
		print(" Вы можете получить его, перейдя по ссылке: https://vk.cc/6VP0Qh")
		print(" ")
		exit()

postId = input(" Введите ID поста (вид: (-)<owner_id>_<post_id>) >> ")
posted = api.wall.getById(posts=postId)
postText = posted[0]["text"]
i = 0
attachments = {}
for i in posted[0]["attachments"]:
	aType = i["type"]
	aOwnerId = i[aType]["owner_id"]
	aId = i[aType]["id"]
	if not attachments.get("attachments"):
		attachments["attachments"] = aType+str(aOwnerId)+"_"+str(aId)+", "
	else:
		attachments["attachments"] = attachments["attachments"]+aType+str(aOwnerId)+"_"+str(aId)+", "
api.wall.post(message=postText, attachments=attachments["attachments"])
print("Готово!")
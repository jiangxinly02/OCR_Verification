from aip import AipOcr

APP_ID = '10438914'
API_KEY = 'EatKqd8723kel1xiflajM1Gmu'
SECRET_KEY = 'IlLnOaOcxyRaVPuaAm3W1arwRotlPKDO3'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

# Read Image
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# Call usual ocr interface
result = client.basicGeneral(get_file_content('test4.jpg'))
print(result)
# Call usual ocr interace2
#result2 = client.basicGeneral("http://wwww.xxxx.com/test.jpg")


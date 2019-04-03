from bs4 import BeautifulSoup


URL = 'https://direct.yandex.ru/registered/main.pl?cmd=showCompetitors&nocid=40953348&id=16253609667'
# AUTH_URL = 'https://passport.yandex.ru/auth'
AUTH_URL = 'https://passport.yandex.ru/auth?retpath=https%3A%2F%2Fdirect.yandex.ru%2Fregistered%2Fmain.pl%3Fauthredirlevel%3D1554220969.0%26cmd%3DshowCompetitors%26nocid%3D40953348%26id%3D16253609667'
AUTH_START_URL = 'https://passport.yandex.ru/registration-validations/auth/multi_step/start'
AUTH_COMMIT_URL = 'https://passport.yandex.ru/registration-validations/auth/multi_step/commit_password'
CODE = 'example'
EMAIL = ''
PASSWORD = ""
HEADERS = {
        'Host': 'passport.yandex.ru',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0',
    }


def get_process_uuid(html):
    soup = BeautifulSoup(html, 'lxml')

    passport = soup.find('div', class_='passp-auth-header')
    url = passport.find("a").get("href")
    url = str(url)
    uuid_name = 'process_uuid'
    uuid_pos = url.find(uuid_name)

    return url[uuid_pos + len(uuid_name) + 1:]


def get_csrf_token(html):
    soup = BeautifulSoup(html, 'lxml')
    form = soup.find('form', method='post')
    hidden_input = form.findAll('input')
    res = [_input.get('value') for _input in hidden_input if _input.get('name') == 'csrf_token']

    return res[0] if res else None


def main():
    pass
    # url = AUTH_URL
    # s = requests.Session()
    # s.headers = HEADERS
    # requests.utils.add_dict_to_cookiejar(s.cookies, {'yandexuid': '654789651254663245'})
    # r = s.get(url, timeout=5)
    # if r.ok:
    #     print(f'URL: {url}, response: OK')
    #     html = r.text
    #
    # print(r.status_code)
    #
    # process_uuid = get_process_uuid(html)
    # csrf = get_csrf_token(html)
    # payload = {
    #     'csrf_token': csrf,
    #     'login': EMAIL,
    #     'process_uuid': process_uuid,
    # }
    # print(payload)
    #
    # r = s.post(AUTH_START_URL, data=payload)
    # print(r.ok, r, r.json())
    #
    # if r.ok:
    #     print(f'URL: {AUTH_START_URL}, response: OK')
    #     payload = {
    #         'csrf_token': csrf,
    #         'track_id': r.json()['track_id'],
    #         'password': PASSWORD,
    #     }
    #
    #     print(f'payload = {payload}')
    #
    #     r = s.post(AUTH_COMMIT_URL, data=payload, timeout=10)
    #     print(r.ok, r, r.json())
    #     if r.ok:
    #         print(f'URL: {AUTH_COMMIT_URL}, response: OK')
    #         r = s.get('test1.html', timeout=5)
    #         print(r.ok, r, r.text)
    #         if r.ok:
    #             print(f'URL: {URL}, response: OK')
    #             html = r.text
    #             get_html_data(html)
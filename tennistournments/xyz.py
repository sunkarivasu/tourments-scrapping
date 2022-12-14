import requests

cookies = {
    '_ga': 'GA1.3.1859280322.1670843425',
    '_gid': 'GA1.3.202017164.1670843425',
    '_hjSessionUser_906305': 'eyJpZCI6IjQ0NDQ2MzYzLTdhZTMtNWI5ZS04OWE5LTAwNjkxZWFjODFmZSIsImNyZWF0ZWQiOjE2NzA4NDM0MjQ4OTgsImV4aXN0aW5nIjp0cnVlfQ==',
    '.ASPX_TOURNAMENT_WEBSITE': 'E4D634BF4A1F4278A96447DDF6A3566AA07CB832FD6924991743DDCA24F0A2160A09EB2E150EC5CB7371BA36FF37A1DFAE5F0F10A89D9468433C49EE7CE8EF6FC1FEB3FD4F7960E9434D7D302781B981A507641DC8CB868317027E6EE090BF5998389F3E',
    'st': 'l=3081&exp=45273.7522219329&s=0',
    '_hjSession_906305': 'eyJpZCI6ImYyMTMzNzIxLTUyN2YtNDMyMC05ZGU4LWQzNGZhNzNiY2E1NCIsImNyZWF0ZWQiOjE2NzA5OTM5MzY5MTUsImluU2FtcGxlIjpmYWxzZX0=',
    '_hjAbsoluteSessionInProgress': '0',
    'ASP.NET_SessionId': 'glabfblqc3gg04u5o1bliewj',
    '_hjIncludedInSessionSample': '0',
    '_gat': '1',
}

headers = {
    'authority': 'tournaments.tennis.com.au',
    'accept': '*/*',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,te;q=0.6',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '_ga=GA1.3.1859280322.1670843425; _gid=GA1.3.202017164.1670843425; _hjSessionUser_906305=eyJpZCI6IjQ0NDQ2MzYzLTdhZTMtNWI5ZS04OWE5LTAwNjkxZWFjODFmZSIsImNyZWF0ZWQiOjE2NzA4NDM0MjQ4OTgsImV4aXN0aW5nIjp0cnVlfQ==; .ASPX_TOURNAMENT_WEBSITE=E4D634BF4A1F4278A96447DDF6A3566AA07CB832FD6924991743DDCA24F0A2160A09EB2E150EC5CB7371BA36FF37A1DFAE5F0F10A89D9468433C49EE7CE8EF6FC1FEB3FD4F7960E9434D7D302781B981A507641DC8CB868317027E6EE090BF5998389F3E; st=l=3081&exp=45273.7522219329&s=0; _hjSession_906305=eyJpZCI6ImYyMTMzNzIxLTUyN2YtNDMyMC05ZGU4LWQzNGZhNzNiY2E1NCIsImNyZWF0ZWQiOjE2NzA5OTM5MzY5MTUsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; ASP.NET_SessionId=glabfblqc3gg04u5o1bliewj; _hjIncludedInSessionSample=0; _gat=1',
    'origin': 'https://tournaments.tennis.com.au',
    'referer': 'https://tournaments.tennis.com.au/tournament/C0B0B33B-2910-46C0-9503-1C74A6CB761F/players',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

data = {
    'X-Requested-With': 'XMLHttpRequest',
}

response = requests.post(
    'https://tournaments.tennis.com.au/tournament/c0b0b33b-2910-46c0-9503-1c74a6cb761f/Players/GetPlayersContent',
    cookies=cookies,
    headers=headers,
    data=data,
)

print(response.text)
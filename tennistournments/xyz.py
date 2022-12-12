import requests

cookies = {
    'st': 'l=3081&exp=45269.7684725231',
    '_ga': 'GA1.3.1505240466.1670606802',
    '_gid': 'GA1.3.1901282358.1670606802',
    '_hjSessionUser_906305': 'eyJpZCI6IjU1ZjkwMjJlLTY4OWMtNWRmOS1hMmRjLTA5ZWExZTFkNzExZSIsImNyZWF0ZWQiOjE2NzA2MDY4MDUzNzEsImV4aXN0aW5nIjp0cnVlfQ==',
    'ASP.NET_SessionId': 'vhkrsb1en1yzidfpsnqwqcsg',
    '_hjSession_906305': 'eyJpZCI6ImZmODZjYzZhLTM1N2EtNGVhNC1hYWI3LTE4YzNiZjNmMjlhZCIsImNyZWF0ZWQiOjE2NzA2Nzk1OTE5NzksImluU2FtcGxlIjpmYWxzZX0=',
    '_hjAbsoluteSessionInProgress': '0',
    '_hjIncludedInSessionSample': '0',
    '_gat': '1',
}

headers = {
    'authority': 'tournaments.tennis.com.au',
    'accept': '*/*',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,te;q=0.6',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'st=l=3081&exp=45269.7684725231; _ga=GA1.3.1505240466.1670606802; _gid=GA1.3.1901282358.1670606802; _hjSessionUser_906305=eyJpZCI6IjU1ZjkwMjJlLTY4OWMtNWRmOS1hMmRjLTA5ZWExZTFkNzExZSIsImNyZWF0ZWQiOjE2NzA2MDY4MDUzNzEsImV4aXN0aW5nIjp0cnVlfQ==; ASP.NET_SessionId=vhkrsb1en1yzidfpsnqwqcsg; _hjSession_906305=eyJpZCI6ImZmODZjYzZhLTM1N2EtNGVhNC1hYWI3LTE4YzNiZjNmMjlhZCIsImNyZWF0ZWQiOjE2NzA2Nzk1OTE5NzksImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _hjIncludedInSessionSample=0; _gat=1',
    'origin': 'https://tournaments.tennis.com.au',
    'referer': 'https://tournaments.tennis.com.au/find?DateFilterType=0&StartDate=2022-12-05&EndDate=2023-03-09&Distance=15&page=1',
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
    'Page': '1',
    'TournamentExtendedFilter.SportID': '0',
    'TournamentFilter.Q': '',
    'TournamentFilter.DateFilterType': '0',
    'TournamentFilter.StartDate': '2022-12-05',
    'TournamentFilter.EndDate': '2023-03-09',
    'TournamentFilter.PostalCode': '',
    'TournamentFilter.Distance': '15',
    'TournamentExtendedFilter.OrganizationStateList[0]': 'false',
    'TournamentExtendedFilter.OrganizationStateList[1]': 'false',
    'TournamentExtendedFilter.OrganizationStateList[2]': 'false',
    'TournamentExtendedFilter.OrganizationStateList[3]': 'false',
    'TournamentExtendedFilter.OrganizationStateList[4]': 'false',
    'TournamentExtendedFilter.OrganizationStateList[5]': 'false',
    'TournamentExtendedFilter.OrganizationStateList[6]': 'false',
    'TournamentExtendedFilter.OrganizationStateList[7]': 'false',
    'TournamentExtendedFilter.TournamentCategoryIDList[0]': 'false',
    'TournamentExtendedFilter.TournamentCategoryIDList[1]': 'false',
    'TournamentExtendedFilter.TournamentCategoryIDList[2]': 'false',
    'TournamentExtendedFilter.TournamentCategoryIDList[3]': 'false',
    'TournamentExtendedFilter.TournamentCategoryIDList[4]': 'false',
    'TournamentExtendedFilter.TournamentCategoryIDList[5]': 'false',
    'TournamentExtendedFilter.TournamentCategoryIDList[6]': 'false',
    'TournamentExtendedFilter.TournamentCategoryIDList[7]': 'false',
    'TournamentExtendedFilter.TournamentCategoryIDList[8]': 'false',
    'TournamentExtendedFilter.TournamentCategoryIDList[9]': 'false',
    'TournamentExtendedFilter.TournamentCategoryIDList[10]': 'false',
    'TournamentExtendedFilter.TournamentCategoryIDList[11]': 'false',
    'TournamentExtendedFilter.TournamentCategoryIDList[12]': 'false',
    'TournamentExtendedFilter.OrganizationCourtSurfaceTypeList[0]': 'false',
    'TournamentExtendedFilter.OrganizationCourtSurfaceTypeList[1]': 'false',
    'TournamentExtendedFilter.OrganizationCourtSurfaceTypeList[2]': 'false',
    'TournamentExtendedFilter.OrganizationCourtSurfaceTypeList[3]': 'false',
    'TournamentExtendedFilter.OrganizationCourtSurfaceTypeList[4]': 'false',
    'TournamentExtendedFilter.EventGameTypeIDList[0]': 'false',
    'TournamentExtendedFilter.EventGameTypeIDList[1]': 'false',
    'TournamentExtendedFilter.EventGameTypeIDList[2]': 'false',
    'TournamentExtendedFilter.EventGameTypeIDList[3]': 'false',
    'TournamentExtendedFilter.EventGameTypeIDList[4]': 'false',
    'X-Requested-With': 'XMLHttpRequest',
}

response = requests.post('https://tournaments.tennis.com.au/find/tournament/DoSearch', cookies=cookies, headers=headers, data=data)
# print(response.text)

string = "\r\n                    -17\r\n                  "
print(string.rstrip().strip()+"1")

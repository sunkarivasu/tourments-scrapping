import scrapy
from ..items import TennistournmentsItem

class TennisTournments_spider(scrapy.Spider):

    name = "tennistournments"
    start_urls = ["https://tournaments.tennis.com.au/find?DateFilterType=0&StartDate=2022-12-05&EndDate=2023-03-09&Distance=15&page=1"]
    startDate = ""
    endDate = ""
    pageNo = 1

    url = "https://tournaments.tennis.com.au/find/tournament/DoSearch"
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

    body = "Page=" + str(pageNo) + "&TournamentExtendedFilter.SportID=0&TournamentFilter.Q=&TournamentFilter.DateFilterType=0&TournamentFilter.StartDate=2022-12-05&TournamentFilter.EndDate=2023-03-09&TournamentFilter.PostalCode=&TournamentFilter.Distance=15&TournamentExtendedFilter.OrganizationStateList%5B0%5D=false&TournamentExtendedFilter.OrganizationStateList%5B1%5D=false&TournamentExtendedFilter.OrganizationStateList%5B2%5D=false&TournamentExtendedFilter.OrganizationStateList%5B3%5D=false&TournamentExtendedFilter.OrganizationStateList%5B4%5D=false&TournamentExtendedFilter.OrganizationStateList%5B5%5D=false&TournamentExtendedFilter.OrganizationStateList%5B6%5D=false&TournamentExtendedFilter.OrganizationStateList%5B7%5D=false&TournamentExtendedFilter.TournamentCategoryIDList%5B0%5D=false&TournamentExtendedFilter.TournamentCategoryIDList%5B1%5D=false&TournamentExtendedFilter.TournamentCategoryIDList%5B2%5D=false&TournamentExtendedFilter.TournamentCategoryIDList%5B3%5D=false&TournamentExtendedFilter.TournamentCategoryIDList%5B4%5D=false&TournamentExtendedFilter.TournamentCategoryIDList%5B5%5D=false&TournamentExtendedFilter.TournamentCategoryIDList%5B6%5D=false&TournamentExtendedFilter.TournamentCategoryIDList%5B7%5D=false&TournamentExtendedFilter.TournamentCategoryIDList%5B8%5D=false&TournamentExtendedFilter.TournamentCategoryIDList%5B9%5D=false&TournamentExtendedFilter.TournamentCategoryIDList%5B10%5D=false&TournamentExtendedFilter.TournamentCategoryIDList%5B11%5D=false&TournamentExtendedFilter.TournamentCategoryIDList%5B12%5D=false&TournamentExtendedFilter.OrganizationCourtSurfaceTypeList%5B0%5D=false&TournamentExtendedFilter.OrganizationCourtSurfaceTypeList%5B1%5D=false&TournamentExtendedFilter.OrganizationCourtSurfaceTypeList%5B2%5D=false&TournamentExtendedFilter.OrganizationCourtSurfaceTypeList%5B3%5D=false&TournamentExtendedFilter.OrganizationCourtSurfaceTypeList%5B4%5D=false&TournamentExtendedFilter.EventGameTypeIDList%5B0%5D=false&TournamentExtendedFilter.EventGameTypeIDList%5B1%5D=false&TournamentExtendedFilter.EventGameTypeIDList%5B2%5D=false&TournamentExtendedFilter.EventGameTypeIDList%5B3%5D=false&TournamentExtendedFilter.EventGameTypeIDList%5B4%5D=false&X-Requested-With=XMLHttpRequest"

    def __init__(self):
        print("please enter start date in (YYYY-MM-DD) format:")
        self.startDate = input()
        print("please enter end date in (YYYY-MM-DD) format:")
        self.endDate = input()

        # self.startDate = "2022-12-05"
        # self.endDate = "2023-03-09"
        # self.start_urls[0] = "https://tournaments.tennis.com.au/find?DateFilterType=0&StartDate="+self.startDate+"&EndDate="+self.endDate+"&Distance=15&page=1"

    def changeBodyBasedOnPageNo(self):
        self.body = "Page=" + str(self.pageNo) + "&TournamentExtendedFilter.SportID=0&TournamentFilter.Q=&TournamentFilter.DateFilterType=0&TournamentFilter.StartDate=2022-12-05&TournamentFilter.EndDate=2023-03-09&TournamentFilter.PostalCode=&TournamentFilter.Distance=15&TournamentExtendedFilter.OrganizationStateList%5B0%5D=false&TournamentExtendedFilter.OrganizationStateList%5B1%5D=false&TournamentExtendedFilter.OrganizationStateList%5B2%5D=false&TournamentExtendedFilter.OrganizationStateList%5B3%5D=false&TournamentExtendedFilter.OrganizationStateList%5B4%5D=false&TournamentExtendedFilter.OrganizationStateList%5B5%5D=false&TournamentExtendedFilter.OrganizationStateList%5B6%5D=false&TournamentExtendedFilter.OrganizationStateList%5B7%5D=false&TournamentExtendedFilter.TournamentCategoryIDList%5B0%5D=false&TournamentExtendedFilter.TournamentCategoryIDList%5B1%5D=false&TournamentExtendedFilter.TournamentCategoryIDList%5B2%5D=false&TournamentExtendedFilter.TournamentCategoryIDList%5B3%5D=false&TournamentExtendedFilter.TournamentCategoryIDList%5B4%5D=false&TournamentExtendedFilter.TournamentCategoryIDList%5B5%5D=false&TournamentExtendedFilter.TournamentCategoryIDList%5B6%5D=false&TournamentExtendedFilter.TournamentCategoryIDList%5B7%5D=false&TournamentExtendedFilter.TournamentCategoryIDList%5B8%5D=false&TournamentExtendedFilter.TournamentCategoryIDList%5B9%5D=false&TournamentExtendedFilter.TournamentCategoryIDList%5B10%5D=false&TournamentExtendedFilter.TournamentCategoryIDList%5B11%5D=false&TournamentExtendedFilter.TournamentCategoryIDList%5B12%5D=false&TournamentExtendedFilter.OrganizationCourtSurfaceTypeList%5B0%5D=false&TournamentExtendedFilter.OrganizationCourtSurfaceTypeList%5B1%5D=false&TournamentExtendedFilter.OrganizationCourtSurfaceTypeList%5B2%5D=false&TournamentExtendedFilter.OrganizationCourtSurfaceTypeList%5B3%5D=false&TournamentExtendedFilter.OrganizationCourtSurfaceTypeList%5B4%5D=false&TournamentExtendedFilter.EventGameTypeIDList%5B0%5D=false&TournamentExtendedFilter.EventGameTypeIDList%5B1%5D=false&TournamentExtendedFilter.EventGameTypeIDList%5B2%5D=false&TournamentExtendedFilter.EventGameTypeIDList%5B3%5D=false&TournamentExtendedFilter.EventGameTypeIDList%5B4%5D=false&X-Requested-With=XMLHttpRequest"

    def parse(self,response):
        yield scrapy.Request(self.url,method="POST",body=self.body,headers=self.headers,callback = self.checkForMoreResults,cookies=self.cookies)

    def checkForMoreResults(self,response):
        print("checking for more results ...")
        print("Found more results:"+("True" if response.headers["Hasmoreresults"]==b'true' else "Fasle"))

        if(response.headers["Hasmoreresults"]==b'true'):
            self.pageNo += 1
            self.changeBodyBasedOnPageNo()
            yield scrapy.Request(self.url, method="POST", body=self.body, headers=self.headers,
                                 callback=self.checkForMoreResults, cookies=self.cookies)
        else:
            yield scrapy.Request(self.url, method="POST", body=self.body, callback=self.start_parsing, headers=self.headers,
                                 cookies=self.cookies,dont_filter=True)

    def start_parsing(self,response):

        all_lis = response.xpath(".//div[@class='media']")

        tournament = TennistournmentsItem()

        for li in all_lis:
            title = li.xpath(".//h4[@class='media__title']/a/span/text()").extract_first()
            dates = li.xpath(".//small[@class='media__subheading media__subheading--muted']/span/span/time/text()").extract()
            location = li.xpath(".//small[@class='media__subheading']/span/span/text()").extract_first()
            tournament["title"] = title
            tournament["startDate"] = dates[0]
            tournament["endDate"] = dates[1] if len(dates)>1 else dates[0]
            tournament["location"] = location.replace("\r\n        ","")[2::]

            category_items = li.xpath(".//div/div/ul")

            categories = []
            category = {}
            for category_item in category_items:
                if category_item.css("span.tag--soft::text").extract_first():
                    print("found")
                    if "name" not in category and "ages" not in category:
                        pass
                    else:
                        if "name" not in category:
                            category["name"] = None
                        if "ages" not in category:
                            category["ages"] = []
                        categories.append(category)
                        category ={}
                    category["name"] = category_item.css("span.tag.tag--soft::text").extract_first()
                    category["ages"] = list(map(lambda x: x.rstrip().strip(),category_item.css("span.tag::text").extract()[1::] if len(category_item.css("span.tag::text").extract())>0 else []))
                else:
                    category["ages"] = list(map(lambda x: x.rstrip().strip(),category_item.xpath(".//li/span[@class='tag']/text()").extract()))
            if "name" not in category:
                category["name"] = None
            if "ages" not in category:
                category["ages"] = []
            categories.append(category)

            tournament["categories"] = categories

            yield tournament














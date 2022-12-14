import scrapy
from ..items import Player

class Players_spider(scrapy.Spider):
    name = "players_spider"
    start_urls = ["https://tournaments.tennis.com.au/find?DateFilterType=0&StartDate=2022-12-05&EndDate=2023-03-09&Distance=15&page=1"]
    startDate = ""
    endDate = ""
    playerNo = 1
    pageNo = 1
    checkList = [x for x in range(1,191)]
    totalPlayersCount = 0
    tournmentsCount = 0
    allPlayerLinks = []

    url = "https://tournaments.tennis.com.au/find/tournament/DoSearch"
    headers = {
        'authority': 'tournaments.tennis.com.au',
        'accept': '*/*',
        'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,te;q=0.6',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
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
    cookies = {}

    body = "Page=" + str(pageNo) + "&TournamentExtendedFilter.SportID=0&TournamentFilter.Q=&TournamentFilter.DateFilterType=0&TournamentFilter.StartDate=2022-12-05&TournamentFilter.EndDate=2023-03-09&TournamentFilter.PostalCode=&TournamentFilter.Distance=15&TournamentExtendedFilter.OrganizationStateList%5B0%5D=false&TournamentExtendedFilter.OrganizationStateList%5B1%5D=false&TournamentExtendedFilter.OrganizationStateList%5B2%5D=false&TournamentExtendedFilter.OrganizationStateList%5B3%5D=false&TournamentExtendedFilter.OrganizationStateList%5B4%5D=false&TournamentExtendedFilter.OrganizationStateList%5B5%5D=false&TournamentExtendedFilter.OrganizationStateList%5B6%5D=false&TournamentExtendedFilter.OrganizationStateList%5B7%5D=false&TournamentExtendedFilter.TournamentCategoryIDList%5B0%5D=false&TournamentExtendedFilter.TournamentCategoryIDList%5B1%5D=false&TournamentExtendedFilter.TournamentCategoryIDList%5B2%5D=false&TournamentExtendedFilter.TournamentCategoryIDList%5B3%5D=false&TournamentExtendedFilter.TournamentCategoryIDList%5B4%5D=false&TournamentExtendedFilter.TournamentCategoryIDList%5B5%5D=false&TournamentExtendedFilter.TournamentCategoryIDList%5B6%5D=false&TournamentExtendedFilter.TournamentCategoryIDList%5B7%5D=false&TournamentExtendedFilter.TournamentCategoryIDList%5B8%5D=false&TournamentExtendedFilter.TournamentCategoryIDList%5B9%5D=false&TournamentExtendedFilter.TournamentCategoryIDList%5B10%5D=false&TournamentExtendedFilter.TournamentCategoryIDList%5B11%5D=false&TournamentExtendedFilter.TournamentCategoryIDList%5B12%5D=false&TournamentExtendedFilter.OrganizationCourtSurfaceTypeList%5B0%5D=false&TournamentExtendedFilter.OrganizationCourtSurfaceTypeList%5B1%5D=false&TournamentExtendedFilter.OrganizationCourtSurfaceTypeList%5B2%5D=false&TournamentExtendedFilter.OrganizationCourtSurfaceTypeList%5B3%5D=false&TournamentExtendedFilter.OrganizationCourtSurfaceTypeList%5B4%5D=false&TournamentExtendedFilter.EventGameTypeIDList%5B0%5D=false&TournamentExtendedFilter.EventGameTypeIDList%5B1%5D=false&TournamentExtendedFilter.EventGameTypeIDList%5B2%5D=false&TournamentExtendedFilter.EventGameTypeIDList%5B3%5D=false&TournamentExtendedFilter.EventGameTypeIDList%5B4%5D=false&X-Requested-With=XMLHttpRequest"

    def __init__(self):
        # print("please enter start date in (YYYY-MM-DD) format:")
        # self.startDate = input()
        # print("please enter end date in (YYYY-MM-DD) format:")
        # self.endDate = input()

        self.startDate = "2022-12-05"
        self.endDate = "2023-03-09"
        # self.start_urls[0] = "https://tournaments.tennis.com.au/find?DateFilterType=0&StartDate="+self.startDate+"&EndDate="+self.endDate+"&Distance=15&page=1"

    def changeBodyBasedOnPageNo(self):
        self.body = "Page=" + str(self.pageNo) + "&TournamentExtendedFilter.SportID=0&TournamentFilter.Q=&TournamentFilter.DateFilterType=0&TournamentFilter.StartDate=2022-12-05&TournamentFilter.EndDate=2023-03-09&TournamentFilter.PostalCode=&TournamentFilter.Distance=15&TournamentExtendedFilter.OrganizationStateList%5B0%5D=false&TournamentExtendedFilter.OrganizationStateList%5B1%5D=false&TournamentExtendedFilter.OrganizationStateList%5B2%5D=false&TournamentExtendedFilter.OrganizationStateList%5B3%5D=false&TournamentExtendedFilter.OrganizationStateList%5B4%5D=false&TournamentExtendedFilter.OrganizationStateList%5B5%5D=false&TournamentExtendedFilter.OrganizationStateList%5B6%5D=false&TournamentExtendedFilter.OrganizationStateList%5B7%5D=false&TournamentExtendedFilter.TournamentCategoryIDList%5B0%5D=false&TournamentExtendedFilter.TournamentCategoryIDList%5B1%5D=false&TournamentExtendedFilter.TournamentCategoryIDList%5B2%5D=false&TournamentExtendedFilter.TournamentCategoryIDList%5B3%5D=false&TournamentExtendedFilter.TournamentCategoryIDList%5B4%5D=false&TournamentExtendedFilter.TournamentCategoryIDList%5B5%5D=false&TournamentExtendedFilter.TournamentCategoryIDList%5B6%5D=false&TournamentExtendedFilter.TournamentCategoryIDList%5B7%5D=false&TournamentExtendedFilter.TournamentCategoryIDList%5B8%5D=false&TournamentExtendedFilter.TournamentCategoryIDList%5B9%5D=false&TournamentExtendedFilter.TournamentCategoryIDList%5B10%5D=false&TournamentExtendedFilter.TournamentCategoryIDList%5B11%5D=false&TournamentExtendedFilter.TournamentCategoryIDList%5B12%5D=false&TournamentExtendedFilter.OrganizationCourtSurfaceTypeList%5B0%5D=false&TournamentExtendedFilter.OrganizationCourtSurfaceTypeList%5B1%5D=false&TournamentExtendedFilter.OrganizationCourtSurfaceTypeList%5B2%5D=false&TournamentExtendedFilter.OrganizationCourtSurfaceTypeList%5B3%5D=false&TournamentExtendedFilter.OrganizationCourtSurfaceTypeList%5B4%5D=false&TournamentExtendedFilter.EventGameTypeIDList%5B0%5D=false&TournamentExtendedFilter.EventGameTypeIDList%5B1%5D=false&TournamentExtendedFilter.EventGameTypeIDList%5B2%5D=false&TournamentExtendedFilter.EventGameTypeIDList%5B3%5D=false&TournamentExtendedFilter.EventGameTypeIDList%5B4%5D=false&X-Requested-With=XMLHttpRequest"

    def parse(self,response):

        recievedCookies = response.headers.getlist('Set-Cookie')[0].decode("utf-8").split(";")[0].split("=")
        # print("cookie",recievedCookies)

        for i in range(len(recievedCookies)//2):
            self.cookies[recievedCookies[(2*i)]] = recievedCookies[(2*i)+1]

        # print(self.cookies)
        yield scrapy.Request(self.url,method="POST",body=self.body,headers=self.headers,callback = self.checkForMoreResults,cookies=self.cookies)

    def checkForMoreResults(self,response):
        print("checking for more results ...")
        print("Found more results:"+("True" if response.headers["Hasmoreresults"]==b'true' else "False"))

        if(response.headers["Hasmoreresults"]==b'true'):
            self.pageNo += 1
            self.changeBodyBasedOnPageNo()
            yield scrapy.Request(self.url, method="POST", body=self.body, headers=self.headers,
                                 callback=self.checkForMoreResults,cookies=self.cookies)
        else:
            yield scrapy.Request(self.url, method="POST", body=self.body, callback=self.start_parsing, headers=self.headers,cookies=self.cookies,dont_filter=True)


    def start_parsing(self,response):
        yield scrapy.Request(self.url,method="POST",cookies=self.cookies,body=self.body,callback=self.fetchTournmentsLinks,headers = self.headers,dont_filter=True)

    def fetchTournmentsLinks(self,response):

        tournment_ids = list(map(lambda x : x.split("=")[1],response.xpath(".//a[@class='media__link']/@href").extract()))
        self.tournmentsCount = len(tournment_ids)

        # print("length:",len(tournment_ids))
        i = 1
        for tournment_id in tournment_ids:
            print("fetching tournment links....")
            print("tournment id:",tournment_id)
            self.playerNo = 1
            yield scrapy.Request("https://tournaments.tennis.com.au/tournament/"+tournment_id+"/Players/GetPlayersContent",method="POST",body="X-Requested-With=XMLHttpRequest",callback=self.fetchPlayersDetials,meta={"tournment_id":tournment_id,"tournment_no":i},headers=self.headers,cookies=self.cookies,dont_filter=True)
            i += 1

    def fetchPlayersDetials(self,response):
        self.checkList.remove(response.meta["tournment_no"])
        if(len(self.checkList)==0):
            print("-----------------------------------------------------------------------------------------------------------------------")
            print("completed")
            print("Found "+str(self.totalPlayersCount)+"s from "+str(self.tournmentsCount))
            print("-----------------------------------------------------------------------------------------------------------------------")
            for playerLink in self.allPlayerLinks:
                yield scrapy.Request("https://tournaments.tennis.com.au/" + playerLink,
                                     callback=self.fetchAllPlayersDetails)
            print("Found " + str(self.totalPlayersCount) + "s from " + str(self.tournmentsCount) + " tournments")


        playerLinks = response.xpath(".//h5[@class='media__title']/a/@href").extract()
        self.allPlayerLinks +=playerLinks
        self.totalPlayersCount += len(playerLinks)
        print("Found "+str(len(playerLinks))+" player"+("s" if len(playerLinks)>1 else "")+" in tourment:"+"("+str(response.meta["tournment_no"])+")"+response.meta["tournment_id"])
        # print("player links:",playerLinks)
        # print(response.text)


    def fetchAllPlayersDetails(self,response):
        player = Player()
        playerName = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "text--link", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "nav-link__value", " " ))]/text()').extract_first()
        playerId = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "media__title-aside", " " ))]/text()').extract_first()
        player["name"] = playerName
        player["id"] = playerId
        yield player









        # print("fetching players data...")
        # print(response.meta['tournment_id'])
        #
        # player = Player()
        #
        # playerName = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "text--link", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "nav-link__value", " " ))]/text()').extract_first()
        # if(playerName != None):
        #     playerId = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "media__title-aside", " " ))]/text()').extract_first()
        #     player["name"] = playerName
        #     player["id"] = playerId
        #     print(player)
        #     yield player
        #     self.playerNo += 1
        #     yield scrapy.Request("https://tournaments.tennis.com.au/tournament/"+response.meta["tournment_id"]+"/player/"+str(self.playerNo),callback=self.fetchPlayersDetials,dont_filter=True)
        #
        #









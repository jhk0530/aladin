import os
import requests
from bs4 import BeautifulSoup
from pytz import timezone
from datetime import datetime
from github_utils import get_github_repo, upload_github_issue

if __name__ == "__main__":  
  access_token = os.environ['MY_GITHUB_TOKEN']
  repository_name = "aladin"

  seoul_timezone = timezone('Asia/Seoul')
  today = datetime.now(seoul_timezone)
  today_data = today.strftime("%Y년 %m월 %d일")
  aladin_url = "https://www.aladin.co.kr/usedstore/wbrowse.aspx?offcode=Jamsil&ItemType=0&BrowseTarget=AllView&ViewRowsCount=50&ViewType=Detail&PublishMonth=24&SortOrder=6&page=1&PublishDay=84&CID=351&SearchOption=&CustReviewRankStart=&CustReviewRankEnd=&CustReviewCountStart=&CustReviewCountEnd=&PriceFilterMin=&PriceFilterMax=&IsDirectDelivery=&QualityType=&OrgStockStatus="

  res = requests.get(aladin_url).text
  soup = BeautifulSoup(res, features = 'html.parser')
  titles = soup.find_all("a", {"class":"bo_l"})
  titles2 = [str(i.text.split('<b>')).replace("[","").replace("]","").replace("'","") for i in titles]
  titles2 = '- ' + "\n- ".join(titles2)
  issue_title = f"알라딘 잠실롯데월드타워점 새로 등록된 IT 도서 알림({today_data})"
  repo = get_github_repo(access_token, repository_name)
  upload_github_issue(repo, issue_title, titles2)  

  aladin_url = "https://www.aladin.co.kr/usedstore/wbrowse.aspx?offcode=Sincheon&ItemType=0&BrowseTarget=AllView&ViewRowsCount=50&ViewType=Detail&PublishMonth=24&SortOrder=6&page=1&PublishDay=84&CID=351&SearchOption=&IsDirectDelivery=&QualityType=&OrgStockStatus="
   
  res = requests.get(aladin_url).text
  soup = BeautifulSoup(res, features = 'html.parser')
  titles = soup.find_all("a", {"class":"bo_l"})
  titles2 = [str(i.text.split('<b>')).replace("[","").replace("]","").replace("'","") for i in titles]
  titles2 = '- ' + "\n- ".join(titles2)
  issue_title = f"알라딘 잠실새내역점 새로 등록된 IT 도서 알림({today_data})"
  repo = get_github_repo(access_token, repository_name)
  upload_github_issue(repo, issue_title, titles2)  



import requests
from lxml import etree
# for i in range(1, 30):
#     url = f'https://www.leleketang.com/let3/knowledges.php?grade_id={i}'
#     resp = requests.get(url)
#     tree = etree.HTML(resp)
#     nj = tree.xpath('/html/body/div/div/div/div[4]/div[1]/'
#                     'div/div[2]/div/div/div[1]/div[1]/div/a/@date_name')
#     print(nj)

# url = 'http://121.26.242.250:8001/cxxs.asp'
# resp = requests.get(url, headers={"Cookie":
# "sbmb=a; zkbmsbm=+; sbmzk=b; zkbm=cjk%5C2022zk%5Czk; sbmsp=b; zksj=2023zk; g1bd=; ASPSESSIONIDCSCBQDTA=GACDEBNBOOGGNFIOIJHKADOB; mm7=202208; mm16=202208; dlmccc=%B6%C5%C1%A2%C9%FA; srgkcj=; dlmkq12=%B9%AC%D7%D3%BA%CD; mm6=; mm18=bkf202306; dlma5=%B7%EB%D3%F1%BD%F0; dlmqj=0314; dlmkq43=%B7%EB%D3%F1%BD%F0; dlmkq31=%B6%C5%C1%A2%C9%FA; dlmjf22=%CD%F5%D3%C0%C8%AA; lzkf=200; wzkf=200; mm3=202208; dlmzzx1=%D5%B2%B4%AB%B2%C6; jftj4=%B7%EB%D3%F1%BD%F0; mm1=202307lk; mm17=2023%2D01%2D29; jsxm2=%D5%C5%D3%C0%C3%F1; sbja=%CA%C2; dlmss2=%D5%C5%D1%DE%BA%EC; dlmzzx2=%CD%F5%BD%A8%BA%EC; dlmjf31=%B6%C5%C1%A2%C9%FA; jftj=%D5%C5%D3%C0%C3%F1; mm5=; mm21=bkf202303; dlmss3=%B9%F9%B6%AB%BB%D4; dlma1=%B9%AC%D7%D3%BA%CD; dlmjy=%CD%F5%D6%D2; jftj1=%D5%C5%D3%C0%C3%F1%CD%F5%D3%A2%BB%AA; mm22=bkf202302; dlmcca=%D5%C5%D3%C0%C3%F1; dlmp=%CB%CE%D5%BC%C3%F7; dlme=%C7%C7%B9%FA%C8%F0; dlmkq41=%C0%EE%BE%B4%B3%AC; dlmzzx3=%C0%EE%D1%F3; dlmjf32=%B9%F9%B6%AB%BB%D4; ltyf=295; wtyf=227; wbkf=443; wzdf=506; lbkf=430; lzdf=487; mm4=; sjb=%C8%AB; dlmf=%D5%C5%D3%C0%C3%F1; dlmcj2=%B4%DE%D1%F4; dlmkq44=%C8%CE%CF%F2%C8%D9; dlmkq32=%B7%BF%D0%CB%C8%D9; dlmjf11=%CD%F5%D3%A2%BB%AA; sksjb=2023%2F6%2F22; dlmss1=%D5%B2%B4%AB%B2%C6; dlmcw=%C1%F5%C3%F7%CF%BC; dlma2=%CD%F5%D3%C0%C8%AA; dlmkq42=%B8%DF%CF%B2%D4%AA; dlmzzx4=%CB%E5%B9%FA%C1%D6; dlmjf21=%C1%F5%D6%BE%C7%BF; jftj2=%CD%F5%D3%C0%C8%AA%C1%F5%D6%BE%C7%BF; mm2=202307lk; dlmkq21=%C1%F5%D6%BE%C7%BF; dlmjf12=%D5%C5%D3%C0%C3%F1; mm19=bkf202305; mm20=bkf202304; dlmdd=%CD%F5%D3%C0%C8%AA; dlmc=%B7%EB%D3%F1%BD%F0; dlma3=%B6%C5%C1%A2%C9%FA; dlmcj1=%B3%C2%C1%BC%D3%F1; dlmkq22=%CD%F5%D3%C0%C8%AA; gksj=2023gk; jftj3=%B7%BF%D0%CB%C8%D9%B9%F9%B6%AB%BB%D4; dlmss4=%CB%E5%B9%FA%C1%D6; dlmkq11=%D5%C5%D3%C0%C3%F1; zcmc=; aspa=cxxsa%2Easp; zcmb=; dlye=cxxsa%2Easp; xxb=111; bja1=1; njx1=1; kxsj=2023%2D08%2D15; sbma=b; zkbmb=cjk%5C2023zk%5Czklq; yzxha=+; ljma=; dlm1=+; kma1=%D3%A2%D3%EF; nja4=+; cjkma=cjk; bgs=%D3%A2%D3%EF; zp1=; nj4=3; kma2=%D3%A2%D3%EF; ldbj=; ldbjb=13731420878; yjxx=%C6%BD%C8%AA%CF%D8%D2%BB%D6%D0; bgl=%B2%A9%D1%C5%C2%A5; xj1=; nja3=+; yh2=13731420878; zbxh1=03; njy1=0; njc1=0; aa1=1; jggz1=; yzxh=+; njaa1=3; ipdz=10%2E40%2E3%2E41; xha1=80329; nja1=3; zha=; yhb1=; nja2=0; kma3=wy; dlxha=0; bjaa1=1314; njd1=0; bzr1=; njb1=0; dlma=19671016; dlm=%B6%C5%BD%A8%C7%EF; sbmyz=a"})
# resp.encoding = 'gbk'
# print(resp.text)
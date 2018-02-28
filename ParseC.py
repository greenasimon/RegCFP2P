from bs4 import BeautifulSoup
import csv
import os
import glob

#Open CSV file and add the headers
# Maintaining orders are manadatory for headers to capture the correct data in csv files
csvheaders = [["FormType", "CIK", "FileNumber", "FilmNumber", "FiledDate", "CompanyName", "IncState", "BisCity", "BisState",
               "BisZip", "filercik", "IssuerName", "OrgStatus", "OrgJurisdiction", "DateInc", "PortalName", "PortalCIK",
               "CompAmount", "FinInterest", "SecurityType", "SecurityNum", "SecPrice", "PriceMethod", "OfferingAmt",
               "OverSub", "OverSubType", "MaxOfferAmt", "Deadline", "Employees", "TotalAssetFY1", "TotalAssetFY2",
               "CashEquiFY1", "CashEquiFY2", "ActReceivedFY1", "ActReceivedFY2", "ShortTermDebtFY1", "ShortTermDebtFY2",
               "LongTermDebtFY1", "LongTermDebtFY2", "RevenueFY1", "RevenueFY2", "CostGoodsSoldFY1", "CostGoodsSoldFY2",
               "TaxPaidFY1", "TaxPaidFY2", "NetIncomeFY1", "NetIncomeFY2", "IssuerSign", "IssuerTitle"]]
outFile = open('formC_2017.csv','w')
inputData = []
SecHeaders = ["CENTRAL INDEX KEY","SEC FILE NUMBER","FILM NUMBER","FILED AS OF DATE","COMPANY CONFORMED NAME",
              "STATE OF INCORPORATION","CITY","STATE","ZIP"]
DocHeaders = ["filercik", "nameofissuer", "legalstatusform", "jurisdictionorganization", "dateincorporation", "companyname",
              "commissioncik", "compensationamount", "financialinterest", "securityofferedtype", "noofsecurityoffered",
              "price", "pricedeterminationmethod", "offeringamount", "oversubscriptionaccepted",
              "oversubscriptionallocationtype", "maximumofferingamount", "deadlinedate", "currentemployees",
              "totalassetmostrecentfiscalyear","totalassetpriorfiscalyear","cashequimostrecentfiscalyear",
              "cashequipriorfiscalyear", "actreceivedmostrecentfiscalyear", "actreceivedpriorfiscalyear",
              "shorttermdebtmostrecentfiscalyear", "shorttermdebtpriorfiscalyear", "longtermdebtmostrecentfiscalyear",
              "longtermdebtpriorfiscalyear", "revenuemostrecentfiscalyear", "revenuepriorfiscalyear",
              "costgoodssoldmostrecentfiscalyear", "costgoodssoldpriorfiscalyear", "taxpaidmostrecentfiscalyear",
              "taxpaidpriorfiscalyear", "netincomemostrecentfiscalyear", "netincomepriorfiscalyear", "personsignature",
              "persontitle"]
#Change directory to the file folder
os.chdir('C:/Users/GreenaSimon/PycharmProjects/IS/')
with outFile:
    writer = csv.writer(outFile)
    writer.writerows(csvheaders)
    for file in glob.glob("*.txt"):
        with open(file)as sample:
            soup = BeautifulSoup(sample, "lxml")

        DescHeader = soup.find("acceptance-datetime").contents[0]
        FormType = 'C'
        Outdata = FormType #Initilizing
        # Extracts Sec Header info begin
        for secHeader in SecHeaders:
            Outdata = Outdata+','+DescHeader.split(secHeader+':')[1].splitlines()[0].strip(' \t')
        # sec header info end
        # Extracting tag details begin

        for docHeader in DocHeaders:
            TagHeader = soup.find(docHeader)
            if (TagHeader==None):
                Outdata = Outdata+','
            else:Outdata = Outdata+','+ TagHeader.contents[0].strip(' \t\r\n')
        #write this row to csv
        inputData.append([Outdata])
    writer.writerows(inputData)
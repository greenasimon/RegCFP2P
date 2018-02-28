from bs4 import BeautifulSoup
import csv
import os, glob

#Open CSV file and add the headers
csvheaders = [["CIK","FileNumber","FilmNumber", "FiledDate", "CompanyName", "IncState", "FormType", "BisCity","BisState", "BisZip", "filercik", "IssuerName", "OrgStatus", "OrgJurisdiction", "DateInc", "PortalName", "PortalCIK", "CompAmount", "FinInterest", "SecurityType", "SecurityNum", "SecPrice", "PriceMethod", "OfferingAmt", "OverSub", "OverSubType", "MaxOfferAmt", "Deadline", "Employees", "TotalAssetFY1", "TotalAssetFY2", "CashEquiFY1", "CashEquiFY2", "ActReceivedFY1", "ActReceivedFY2", "ShortTermDebtFY1", "ShortTermDebtFY2", "LongTermDebtFY1", "LongTermDebtFY2", "RevenueFY1", "RevenueFY2", "CostGoodsSoldFY1", "CostGoodsSoldFY2", "TaxPaidFY1", "TaxPaidFY2", "NetIncomeFY1", "NetIncomeFY2", "IssuerSign", "IssuerTitle"]]
outFile = open('formC_2017.csv','w')
inputData = []
os.chdir('C:/Users/GreenaSimon/PycharmProjects/IS/')
with outFile:
    writer = csv.writer(outFile)
    writer.writerows(csvheaders)
    for file in glob.glob("*.txt"):
        with open(file)as sample:
           soup = BeautifulSoup(sample)
        # Extracts Sec Header info begin
        DescHeader = soup.find("acceptance-datetime").contents[0]
        FiledDate = DescHeader.split("FILED AS OF DATE:")[1].splitlines()[0].strip(' \t')
        CompanyName = DescHeader.split("COMPANY CONFORMED NAME:")[1].splitlines()[0].strip(' \t')
        CIK = DescHeader.split("CENTRAL INDEX KEY:")[1].splitlines()[0].strip(' \t')
        IncState = DescHeader.split("STATE OF INCORPORATION:")[1].splitlines()[0].strip(' \t')
        FormType = 'C'
        FileNumber = DescHeader.split("SEC FILE NUMBER:")[1].splitlines()[0].strip(' \t')
        FilmNumber = DescHeader.split("FILM NUMBER:")[1].splitlines()[0].strip(' \t')
        BisCity = DescHeader.split("CITY:")[1].splitlines()[0].strip(' \t')
        BisState = DescHeader.split("STATE:")[1].splitlines()[0].strip(' \t')
        BisZip = DescHeader.split("ZIP:")[1].splitlines()[0].strip(' \t')
        # sec header info end

        # Extracting tag details begin
        filercik = soup.find("filercik").contents[0].strip(' \t\r\n')
        IssuerName = soup.find("nameofissuer").contents[0].strip(' \t\r\n')
        OrgStatus = soup.find("legalstatusform").contents[0].strip(' \t\r\n')
        OrgJurisdiction = soup.find("jurisdictionorganization").contents[0].strip(' \t\r\n')
        DateInc = soup.find("dateincorporation").contents[0].strip(' \t\r\n')
        PortalName = soup.find("companyname").contents[0].strip(' \t\r\n')
        PortalCIK = soup.find("commissioncik").contents[0].strip(' \t\r\n')
        CompAmount = soup.find("compensationamount").contents[0].strip(' \t\r\n')
        FinInterest = soup.find("financialinterest").contents[0].strip(' \t\r\n')
        SecurityType = soup.find("securityofferedtype").contents[0].strip(' \t\r\n')
        SecurityNum = soup.find("noofsecurityoffered").contents[0].strip(' \t\r\n')
        SecPrice = soup.find("price").contents[0].strip(' \t\r\n')
        PriceMethod = soup.find("pricedeterminationmethod").contents[0].strip(' \t\r\n')
        OfferingAmt = soup.find("offeringamount").contents[0].strip(' \t\r\n')
        OverSub = soup.find("oversubscriptionaccepted").contents[0].strip(' \t\r\n')
        OverSubType = soup.find("oversubscriptionallocationtype").contents[0].strip(' \t\r\n')
        MaxOfferAmt = soup.find("maximumofferingamount").contents[0].strip(' \t\r\n')
        Deadline = soup.find("deadlinedate").contents[0].strip(' \t\r\n')
        Employees = soup.find("currentemployees").contents[0].strip(' \t\r\n')
        TotalAssetFY1 = soup.find("totalassetmostrecentfiscalyear").contents[0].strip(' \t\r\n')
        TotalAssetFY2 = soup.find("totalassetpriorfiscalyear").contents[0].strip(' \t\r\n')
        CashEquiFY1 = soup.find("cashequimostrecentfiscalyear").contents[0].strip(' \t\r\n')
        CashEquiFY2 = soup.find("cashequipriorfiscalyear").contents[0].strip(' \t\r\n')
        ActReceivedFY1 = soup.find("actreceivedmostrecentfiscalyear").contents[0].strip(' \t\r\n')
        ActReceivedFY2 = soup.find("actreceivedpriorfiscalyear").contents[0].strip(' \t\r\n')
        ShortTermDebtFY1 = soup.find("shorttermdebtmostrecentfiscalyear").contents[0].strip(' \t\r\n')
        ShortTermDebtFY2 = soup.find("shorttermdebtpriorfiscalyear").contents[0].strip(' \t\r\n')
        LongTermDebtFY1 = soup.find("longtermdebtmostrecentfiscalyear").contents[0].strip(' \t\r\n')
        LongTermDebtFY2 = soup.find("longtermdebtpriorfiscalyear").contents[0].strip(' \t\r\n')
        RevenueFY1 = soup.find("revenuemostrecentfiscalyear").contents[0].strip(' \t\r\n')
        RevenueFY2 = soup.find("revenuepriorfiscalyear").contents[0].strip(' \t\r\n')
        CostGoodsSoldFY1 = soup.find("costgoodssoldmostrecentfiscalyear").contents[0].strip(' \t\r\n')
        CostGoodsSoldFY2 = soup.find("costgoodssoldpriorfiscalyear").contents[0].strip(' \t\r\n')
        TaxPaidFY1 = soup.find("taxpaidmostrecentfiscalyear").contents[0].strip(' \t\r\n')
        TaxPaidFY2 = soup.find("taxpaidpriorfiscalyear").contents[0].strip(' \t\r\n')
        NetIncomeFY1 = soup.find("netincomemostrecentfiscalyear").contents[0].strip(' \t\r\n')
        NetIncomeFY2 = soup.find("netincomepriorfiscalyear").contents[0].strip(' \t\r\n')
        IssuerSign = soup.find("personsignature").contents[0].strip(' \t\r\n')
        IssuerTitle = soup.find("persontitle").contents[0].strip(' \t\r\n')

        #write this row to csv
        inputData &= [[CIK,FileNumber,FilmNumber, FiledDate, CompanyName, IncState, FormType, BisCity,BisState, BisZip, filercik, IssuerName, OrgStatus, OrgJurisdiction, DateInc, PortalName, PortalCIK, CompAmount, FinInterest, SecurityType, SecurityNum, SecPrice, PriceMethod, OfferingAmt, OverSub, OverSubType, MaxOfferAmt, Deadline, Employees, TotalAssetFY1, TotalAssetFY2, CashEquiFY1, CashEquiFY2, ActReceivedFY1, ActReceivedFY2, ShortTermDebtFY1, ShortTermDebtFY2, LongTermDebtFY1, LongTermDebtFY2, RevenueFY1, RevenueFY2, CostGoodsSoldFY1, CostGoodsSoldFY2, TaxPaidFY1, TaxPaidFY2, NetIncomeFY1, NetIncomeFY2, IssuerSign, IssuerTitle]]
    writer.writerows(inputData)






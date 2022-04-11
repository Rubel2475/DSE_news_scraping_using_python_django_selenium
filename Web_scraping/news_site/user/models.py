from django.db import models

from news.models import Company

# Create your models here.

class userInput(models.Model):
    username = models.CharField(max_length=50, default="NULL User")
    # trading_code = models.CharField(max_length=200)
    
    company_data = Company.objects.all()
    
    select_tradingCode = [
        ("{}".format(c_data.company_trading_code), "{}".format(c_data.company_name)) for c_data in company_data
    ]
        
    trading_code = models.CharField(max_length=200, choices=select_tradingCode, default="None")
    
    def __str__(self):
        return self.trading_code
    
    

class Contact(models.Model):
    full_name=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    message=models.TextField()

    def __str__(self):
        return self.full_name








# INSERT INTO news_company(company_trading_code, company_name, company_info) VALUES
# ("AAMRATECH", "aamra technologies limited", "Nothing added yet"),
# ("ABB1STMF", "AB Bank 1st Mutual fund", "Nothing added yet"),
# ("ABBANK", "AB Bank Limited", "Nothing added yet"),
# ("ACFL", "Aman Cotton Fibrous Limited", "Nothing added yet"),
# ("ACI", "ACI Limited", "Nothing added yet"),
# ("ACIFORMULA", "ACI Formulations Limited", "Nothing added yet"),
# ("ACMELAB", "The ACME Laboratories Limited", "Nothing added yet"),
# ("ACMEPL", "ACME Pesticides Limited", "Nothing added yet"),
# ("ACTIVEFINE", "Active Fine Chemicals Limited", "Nothing added yet"),
# ("ADNTEL", "ADN Telecom Limited", "Nothing added yet"),
# ("ADVENT", "Advent Pharma Limited", "Nothing added yet"),
# ("AFCAGRO", "AFC Agro Biotech Ltd.", "Nothing added yet"),
# ("AFTABAUTO", "Aftab Automobiles Limited", "Nothing added yet"),
# ("AGNISYSL", "Agni Systems Ltd.", "Nothing added yet"),
# ("AGRANINS", "Agrani Insurance Co. Ltd.", "Nothing added yet"),
# ("AIBL1STIMF", "AIBL 1st Islamic Mutual Fund", "Nothing added yet"),
# ("AIBLPBOND", "AIBL Mudaraba Perpetual Bond", "Nothing added yet"),
# ("AIL", "Alif Industries Limited", "Nothing added yet"),
# ("AL-HAJTEX", "Al-Haj Textile Mills Limited", "Nothing added yet"),
# ("ALARABANK", "Al-Arafah Islami Bank Ltd", "Nothing added yet"),
# ("ALIF", "Alif Manufacturing Company Ltd.", "Nothing added yet"),
# ("ALLTEX", "Alltex Industries Ltd.", "Nothing added yet"),
# ("AMANFEED", "Aman Feed Limited", "Nothing added yet"),
# ("AMBEEPHA", "Ambee Pharmaceuticals Ltd.", "Nothing added yet"),
# ("AMC", "PRAN Agricultural Marketing Company Ltd.", "Nothing added yet"),
# ("ANLIMAYARN", "Anlimayarn Dyeing Ltd.", "Nothing added yet"),
# ("ANWARGALV", "Anwar Galvanizing Ltd.", "Nothing added yet"),
# ("AOL", "Associated Oxygen Limited", "Nothing added yet"),
# ("APEXFOODS", "Apex Foods Limited", "Nothing added yet"),
# ("APEXFOOT", "Apex Footwear Limited.", "Nothing added yet"),
# ("APEXSPINN", "Apex Spinning & Knitting Mills Limited", "Nothing added yet"),
# ("APEXTANRY", "Apex Tannery Limited", "Nothing added yet"),
# ("APOLOISPAT", "Appollo Ispat Complex Limited", "Nothing added yet"),
# ("ARAMIT", "Aramit Limited", "Nothing added yet"),
# ("ARAMITCEM", "Aramit Cement Limited", "Nothing added yet"),
# ("ARGONDENIM", "Argon Denims Limited", "Nothing added yet"),
# ("ASIAINS", "Asia Insurance Limited", "Nothing added yet"),
# ("ASIAPACINS", "Asia Pacific General Insurance Co. Ltd.", "Nothing added yet"),
# ("ATCSLGF", "Asian Tiger Sandhani Life Growth Fund", "Nothing added yet"),
# ("BANGAS", "Bangas Ltd.", "Nothing added yet"),
# ("BANKASIA", "Bank Asia Ltd.", "Nothing added yet"),
# ("BARKAPOWER", "Baraka Power Limited", "Nothing added yet"),
# ("BATASHOE", "Bata Shoe Company Bangladesh Limited", "Nothing added yet"),
# ("BATBC", "British American Tobacco bangladesh Company Limited", "Nothing added yet"),
# ("BAYLEASING", "Bay Leasing & Investment Limited", "Nothing added yet"),
# ("BBS", "Bangladesh Building Systems Ltd.", "Nothing added yet"),
# ("BBSCABLES", "BBS Cables Limited", "Nothing added yet"),
# ("BDAUTOCA", "Bangladesh Autocars Ltd.", "Nothing added yet"),
# ("BDCOM", "BDCOM Online Ltd.", "Nothing added yet"),
# ("BDFINANCE", "Bangladesh Finance Limited", "Nothing added yet"),
# ("BDLAMPS", "Bangladesh Lamps Limited", "Nothing added yet"),
# ("BDSERVICE", "Bangladesh Services Ltd.", "Nothing added yet"),
# ("BDTHAI", "Bd.Thai Aluminium Ltd.", "Nothing added yet"),
# ("BDTHAIFOOD", "BD Thai Food & Beverage Limited", "Nothing added yet"),
# ("BDWELDING", "Bangladesh Welding Electrodes Ltd.", "Nothing added yet"),
# ("BEACHHATCH", "Beach Hatchery Ltd.", "Nothing added yet"),
# ("BEACONPHAR", "Beacon Pharmaceuticals Limited", "Nothing added yet"),
# ("BENGALWTL", "Bengal Windsor Thermoplastics Ltd.", "Nothing added yet"),
# ("BERGERPBL", "Berger Paints Bangladesh Ltd.", "Nothing added yet"),
# ("BEXGSUKUK", "Beximco Green Sukuk Al Istisna'a", "Nothing added yet"),
# ("BEXIMCO", "Bangladesh Export Import Company Ltd.", "Nothing added yet"),
# ("BGIC", "Bangladesh General Insurance Company Ltd.", "Nothing added yet"),
# ("BIFC", "Bangladesh Industrial Fin. Co. Ltd.", "Nothing added yet"),
# ("BNICL", "Bangladesh National Insurance Company Limited", "Nothing added yet"),
# ("BPML", "Bashundhara Paper Mills Limited", "Nothing added yet"),
# ("BPPL", "Baraka Patenga Power Limited", "Nothing added yet"),
# ("BRACBANK", "BRAC Bank Ltd.", "Nothing added yet"),
# ("BSC", "Bangladesh Shipping Corporation", "Nothing added yet"),
# ("BSCCL", "Bangladesh Submarine Cable Company Limited", "Nothing added yet"),
# ("BSRMLTD", "Bangladesh Steel Re-Rolling Mills Limited", "Nothing added yet"),
# ("BSRMSTEEL", "BSRM Steels Limited", "Nothing added yet"),
# ("BXPHARMA", "Beximco Pharmaceuticals Ltd.", "Nothing added yet"),
# ("BXSYNTH", "Beximco Synthetics Ltd.", "Nothing added yet"),
# ("CAPMBDBLMF", "CAPM BDBL Mutual Fund 01", "Nothing added yet"),
# ("CAPMIBBLMF", "CAPM IBBL Islamic Mutual Fund", "Nothing added yet"),
# ("CENTRALINS", "Central Insurance Company Ltd.", "Nothing added yet"),
# ("CENTRALPHL", "Central Pharmaceuticals Limited", "Nothing added yet"),
# ("CITYBANK", "The City Bank Ltd.", "Nothing added yet"),
# ("CITYGENINS", "City General Insurance Co. Ltd.", "Nothing added yet"),
# ("CNATEX", "C & A Textiles Limited", "Nothing added yet"),
# ("CONFIDCEM", "Confidence Cement Ltd.", "Nothing added yet"),
# ("CONTININS", "Continental Insurance Ltd.", "Nothing added yet"),
# ("COPPERTECH", "Coppertech Industries Limited", "Nothing added yet"),
# ("CROWNCEMNT", "Crown Cement PLC.", "Nothing added yet"),
# ("CRYSTALINS", "Crystal Insurance Company Limited", "Nothing added yet"),
# ("CVOPRL", "CVO Petrochemical Refinery Limited", "Nothing added yet"),
# ("DACCADYE", "The Dacca Dyeing & Manufacturing Co.Ltd.", "Nothing added yet"),
# ("DAFODILCOM", "Daffodil Computers Ltd.", "Nothing added yet"),
# ("DBH", "Delta Brac Housing Finance Corp. Ltd.", "Nothing added yet"),
# ("DBH1STMF", "DBH First Mutual Fund", "Nothing added yet"),
# ("DEBARACEM", "Aramit Cement Ltd",  "Nothing added yet"),
# ("DEBBDLUGG", "Bangladesh Luggage Ind. Ltd Deb-14%", "Nothing added yet"),
# ("DEBBDWELD", "BD Welding Electrodes Ltd Deb-15%", "Nothing added yet"),
# ("DEBBDZIPP", "Bangladesh Zipper Ind. Ltd Deb-14%", "Nothing added yet"),
# ("DEBBXDENIM", "Beximco Denims Ltd Deb-14%", "Nothing added yet"),
# ("DEBBXFISH", "Beximco Fisheries Ltd Deb-14%", "Nothing added yet"),
# ("DEBBXKNI", "Beximco Knitting Ltd Deb-14%", "Nothing added yet"),
# ("DEBBXTEX", "Beximco Textiles Ltd Deb-14%", "Nothing added yet"),
# ("DELTALIFE", "Delta Life Insurance Company Ltd.", "Nothing added yet"),
# ("DELTASPINN", "Delta Spinners Ltd.", "Nothing added yet"),
# ("DESCO", "Dhaka Electric Supply Company Ltd.", "Nothing added yet"),
# ("DESHBANDHU", "Deshbandhu Polymer Limited", "Nothing added yet"),
# ("DGIC", "Desh General Insurance Company Limited", "Nothing added yet"),
# ("DHAKABANK", "Dhaka Bank Ltd.", "Nothing added yet"),
# ("DHAKAINS", "Dhaka Insurance Limited", "Nothing added yet"),
# ("DOMINAGE", "Dominage Steel Building Systems Limited", "Nothing added yet"),
# ("DOREENPWR", "Doreen Power Generations and Systems Limited", "Nothing added yet"),
# ("DSHGARME", "Desh Garments Ltd.", "Nothing added yet"),
# ("DSSL", "Dragon Sweater and Spinning Limited", "Nothing added yet"),
# ("DULAMIACOT", "Dulamia Cotton Spinning Mills Ltd.", "Nothing added yet"),
# ("DUTCHBANGL", "Dutch-Bangla Bank Ltd.", "Nothing added yet"),
# ("EASTERNINS", "Eastern Insurance Company Ltd.", "Nothing added yet"),
# ("EASTLAND", "Eastland Insurance Company Ltd.", "Nothing added yet"),
# ("EASTRNLUB", "Eastern Lubricants Blenders Limited", "Nothing added yet"),
# ("EBL", "Eastern Bank Ltd.", "Nothing added yet"),
# ("EBL1STMF", "EBL First Mutual Fund", "Nothing added yet"),
# ("EBLNRBMF", "EBL NRB Mutual Fund", "Nothing added yet"),
# ("ECABLES", "Eastern Cables Ltd.", "Nothing added yet"),
# ("EGEN", "eGeneration Limited", "Nothing added yet"),
# ("EHL", "Eastern Housing Limited", "Nothing added yet"),
# ("EIL", "Express Insurance Limited", "Nothing added yet"),
# ("EMERALDOIL", "Emerald Oil Industries Ltd.", "Nothing added yet"),
# ("ENVOYTEX", "Envoy Textiles Limited", "Nothing added yet"),
# ("EPGL", "Energypac Power Generation Limited", "Nothing added yet"),
# ("ESQUIRENIT", "Esquire Knit Composite Limited", "Nothing added yet"),
# ("ETL", "Evince Textiles Limited", "Nothing added yet"),
# ("EXIM1STMF", "EXIM Bank 1st Mutual Fund", "Nothing added yet"),
# ("EXIMBANK", "Export Import Exim Bank of Bangladesh Limited", "Nothing added yet"),
# ("FAMILYTEX", "Familytex BD", "Nothing added yet"),
# ("FARCHEM", "Far Chemical Industries Limited", "Nothing added yet"),
# ("FAREASTFIN", "Fareast Finance & Investment Limited", "Nothing added yet"),
# ("FAREASTLIF", "Fareast Islami Life Insurance Co. Ltd.", "Nothing added yet"),
# ("FASFIN", "FAS Finance & Investment Limited", "Nothing added yet"),
# ("FBFIF", "First Bangladesh Fixed Income Fund", "Nothing added yet"),
# ("FEDERALINS", "Federal Insurance Company Ltd.", "Nothing added yet"),
# ("FEKDIL", "Far East Knitting & Dyeing Industries Limited", "Nothing added yet"),
# ("FINEFOODS", "Fine Foods Limited", "Nothing added yet"),
# ("FIRSTFIN", "First Finance Limited", "Nothing added yet"),
# ("FIRSTSBANK", "First Security Islami Bank Limited", "Nothing added yet"),
# ("FORTUNE", "Fortune Shoes Limited", "Nothing added yet"),
# ("FUWANGCER", "Fu-Wang Ceramic Industries Ltd.", "Nothing added yet"),
# ("FUWANGFOOD", "Fu Wang Food Ltd.", "Nothing added yet"),
# ("GBBPOWER", "GBB Power Ltd.", "Nothing added yet"),
# ("GEMINISEA", "Gemini Sea Food Ltd.", "Nothing added yet"),
# ("GENEXIL", "Genex Infosys Limited", "Nothing added yet"),
# ("GENNEXT", "Generation Next Fashions Limited", "Nothing added yet"),
# ("GHAIL", "Golden Harvest Agro Industries Ltd.", "Nothing added yet"),
# ("GHCL", "Global Heavy Chemicals Limited", "Nothing added yet"),
# ("GLOBALINS", "Global Insurance Company Ltd.", "Nothing added yet"),
# ("GOLDENSON", "Golden Son Ltd.", "Nothing added yet"),
# ("GP", "Grameenphone Ltd.", "Nothing added yet"),
# ("GPHISPAT", "GPH Ispat Ltd.", "Nothing added yet"),
# ("GQBALLPEN", "GQ Ball Pen Industries Ltd.", "Nothing added yet"),
# ("GRAMEENS2", "Grameen One : Scheme Two", "Nothing added yet"),
# ("GREENDELMF", "Green Delta Mutual Fund", "Nothing added yet"),
# ("GREENDELT", "Green Delta Insurance Ltd.", "Nothing added yet"),
# ("GSPFINANCE", "GSP Finance Company Bangladesh", "Nothing added yet"),
# ("HAKKANIPUL", "Hakkani Pulp & Paper Mills Ltd.", "Nothing added yet"),
# ("HEIDELBCEM", "Heidelberg Cement Bangladesh Ltd.", "Nothing added yet"),
# ("HFL", "Hamid Fabrics Limited", "Nothing added yet"),
# ("HRTEX", "H.R.Textile Ltd.", "Nothing added yet"),
# ("HWAWELLTEX", "Hwa Well Textiles BD", "Nothing added yet"),
# ("IBBL2PBOND", "IBBL 2nd Perpetual Mudaraba Bond", "Nothing added yet"),
# ("IBBLPBOND", "IBBL Mudaraba Perpetual Bond", "Nothing added yet"),
# ("IBNSINA", "The IBN SINA Pharmaceutical Industry Ltd.", "Nothing added yet"),
# ("IBP", "Indo-Bangla Pharmaceuticals Limited", "Nothing added yet"),
# ("ICB", "Investment Corporation Of Bangladesh", "Nothing added yet"),
# ("ICB3RDNRB", "ICB AMCL Third NRB Mutual Fund", "Nothing added yet"),
# ("ICBAGRANI1", "ICB AMCL First Agrani Bank Mutual Fund", "Nothing added yet"),
# ("ICBAMCL2ND", "ICB AMCL Second Mutual Fund", "Nothing added yet"),
# ("ICBEPMF1S1", "ICB Employees Provident MF 1: Scheme 1", "Nothing added yet"),
# ("ICBIBANK", "ICB Islamic Bank Limited", "Nothing added yet"),
# ("ICBSONALI1", "ICB AMCL Sonali Bank Limited 1st Mutual Fund", "Nothing added yet"),
# ("IDLC", "IDLC Finance Ltd.", "Nothing added yet"),
# ("IFADAUTOS", "IFAD Autos Limited", "Nothing added yet"),
# ("IFIC", "IFIC Bank Ltd.", "Nothing added yet"),
# ("IFIC1STMF", "IFIC Bank 1st Mutual Fund", "Nothing added yet"),
# ("IFILISLMF1", "IFIL Islamic Mutual Fund-1", "Nothing added yet"),
# ("ILFSL", "International Leasing & Financial Services Ltd.", "Nothing added yet"),
# ("IMAMBUTTON", "Imam Button Industries Ltd.", "Nothing added yet"),
# ("INDEXAGRO", "Index Agro Industries Limited", "Nothing added yet"),
# ("INTECH", "Intech Limited", "Nothing added yet"),
# ("INTRACO", "Intraco Refueling Station Limited", "Nothing added yet"),
# ("IPDC", "IPDC Finance Limited", "Nothing added yet"),
# ("ISLAMIBANK", "Islami Bank Bangladesh Limited", "Nothing added yet"),
# ("ISLAMICFIN", "Islamic Finance & Investment Ltd.", "Nothing added yet"),
# ("ISLAMIINS", "Islami Insurance Bangladesh Limited", "Nothing added yet"),
# ("ISNLTD", "Information Services Network Ltd.", "Nothing added yet"),
# ("ITC", "IT Consultants Limited", "Nothing added yet"),
# ("JAMUNABANK", "Jamuna Bank Ltd.", "Nothing added yet"),
# ("JAMUNAOIL", "Jamuna Oil Company Limited", "Nothing added yet"),
# ("JANATAINS", "Janata Insurance Company Ltd.", "Nothing added yet"),
# ("JHRML", "JMI Hospital Requisite Manufacturing Limited", "Nothing added yet"),
# ("JMISMDL", "JMI Syringes & Medical Devices Ltd.", "Nothing added yet"),
# ("JUTESPINN", "Jute Spinners Ltd.", "Nothing added yet"),
# ("KARNAPHULI", "Karnaphuli Insurance Company Ltd.", "Nothing added yet"),
# ("KAY&QUE", "Kay & Que Bangladesh", "Nothing added yet"),
# ("KBPPWBIL", "Khan Brothers PP Woven Bag Industries Limited", "Nothing added yet"),
# ("KDSALTD", "KDS Accessories Limited", "Nothing added yet"),
# ("KEYACOSMET", "Keya Cosmetics Ltd.", "Nothing added yet"),
# ("KOHINOOR", "Kohinoor Chemicals Company Bangladesh", "Nothing added yet"),
# ("KPCL", "Khulna Power Company Limited", "Nothing added yet"),
# ("KPPL", "Khulna Printing & Packaging Limited", "Nothing added yet"),
# ("KTL", "Kattali Textile Limited", "Nothing added yet"),
# ("LANKABAFIN", "LankaBangla Finance Ltd.", "Nothing added yet"),
# ("LEGACYFOOT", "Legacy Footwear Ltd.", "Nothing added yet"),
# ("LHBL", "LafargeHolcim Bangladesh Limited", "Nothing added yet"),
# ("LIBRAINFU", "Libra Infusions Limited", "Nothing added yet"),
# ("LINDEBD", "Linde Bangladesh Limited", "Nothing added yet"),
# ("LOVELLO", "Taufika Foods and Lovello Ice-cream PLC", "Nothing added yet"),
# ("LRBDL", "Lub-rref Bangladesh", "Nothing added yet"),
# ("LRGLOBMF1", "LR Global Bangladesh Mutual Fund One", "Nothing added yet"),
# ("MAKSONSPIN", "Maksons Spinning Mills Limited", "Nothing added yet"),
# ("MALEKSPIN", "Malek Spinning Mills Ltd.", "Nothing added yet"),
# ("MARICO", "Marico Bangladesh Limited", "Nothing added yet"),
# ("MATINSPINNO", "Matin Spinning Mills Ltd.", "Nothing added yet"),
# ("MBL1STMFO", "MBL 1st Mutual Fund", "Nothing added yet"),
# ("MEGCONMILKO", "Meghna Condensed Milk Industries Ltd.", "Nothing added yet"),
# ("MEGHNACEMO", "Meghna Cement Mills Ltd.", "Nothing added yet"), 
# ("MEGHNALIFEO", "Meghna Life Insurance Co. Ltd.", "Nothing added yet"),
# ("MEGHNAPETO", "Meghna Pet Industries Ltd.", "Nothing added yet"),
# ("MERCANBANKO", "Mercantile Bank Ltd.", "Nothing added yet"),
# ("MERCINSO", "Mercantile Insurance Co. Ltd.", "Nothing added yet"),
# ("METROSPIN", "Metro Spinning Ltd.", "Nothing added yet"),
# ("MHSMLN", "Mozaffar Hossain Spinning Mills Ltd.", "Nothing added yet"),
# ("MIDASFINN", "MIDAS Financing Ltd.", "Nothing added yet"),
# ("MIRACLEINDN", "Miracle Industries Ltd.", "Nothing added yet"),
# ("MIRAKHTERN", "Mir Akhter Hossain Limited", "Nothing added yet"),
# ("MITHUNKNITN", "Mithun Knitting and Dyeing Ltd.", "Nothing added yet"),
# ("MJLBDN", "MJL Bangladesh Limited", "Nothing added yet"),
# ("MLDYEINGN", "M.L. Dyeing Limited", "Nothing added yet"),
# ("MONNOAGMLN", "Monno Agro & General Machinery Limited", "Nothing added yet"),
# ("MONNOCERAN", "Monno Ceramic Industries Ltd.", "Nothing added yet"),
# ("MONNOFABRN", "Monno Fabrics Limited", "Nothing added yet"),
# ("MONOSPOOL", "Bangladesh Monospool Paper Manufacturing Co. Limited", "Nothing added yet"),
# ("MPETROLEUM", "Meghna Petroleum Limited", "Nothing added yet"),
# ("MTBM", "Mutual Trust Bank Ltd.", "Nothing added yet"),
# ("NAHEEACPM", "Nahee Aluminum Composite Panel Ltd.", "Nothing added yet"),
# ("NATLIFEINSM", "National Life Insurance Company Ltd.", "Nothing added yet"),
# ("NAVANACNGM", "Navana CNG Limited", "Nothing added yet"),
# ("NBLM", "National Bank Ltd.", "Nothing added yet"),
# ("NCCBANKM", "National Credit and Commerce Bank Ltd.", "Nothing added yet"),
# ("NCCBLMF1M", "NCCBL Mutual Fund-1", "Nothing added yet"),
# ("NEWLINEM", "New Line Clothings Limited", "Nothing added yet"),
# ("NFMLM", "National Feed Mill Limited", "Nothing added yet"),
# ("NHFILM", "National Housing Fin. and Inv. Ltd.", "Nothing added yet"),
# ("NITOLINSM", "Nitol Insurance Co. Ltd.", "Nothing added yet"),
# ("NLI1STMFM", "NLI First Mutual Fund", "Nothing added yet"),
# ("NORTHERNM", "Northern Jute Manufacturing Co. Ltd.", "Nothing added yet"),
# ("NORTHRNINSM", "Northern Islami Insurance Limited", "Nothing added yet"),
# ("NPOLYMERM", "National Polymer Industries Ltd.", "Nothing added yet"),
# ("NRBCBANKM", "NRB Commercial Bank Limited", "Nothing added yet"),
# ("NTCM", "National Tea Company Ltd.", "Nothing added yet"),
# ("NTLTUBESM", "National Tubes Limited", "Nothing added yet"),
# ("NURANIM", "Nurani Dyeing & Sweater Limited", "Nothing added yet"),
# ("OALM", "Olympic Accessories Limited", "Nothing added yet"),
# ("OIMEXM", "Oimex Electrode Limited", "Nothing added yet"),
# ("OLYMPICM", "Olympic Industries Ltd.", "Nothing added yet"),
# ("ONEBANKLTDM", "One Bank Limited", "Nothing added yet"),
# ("ORIONINFUM", "Orion Infusion Ltd.", "Nothing added yet"),
# ("ORIONPHARMM", "Orion Pharma Ltd.", "Nothing added yet"),
# ("PADMALIFEM", "Padma Islami Life Insurance Limited", "Nothing added yet"),
# ("PADMAOILM", "Padma Oil Co. Ltd.", "Nothing added yet"),
# ("PAPERPROCM", "Paper Processing & Packaging Limite", "Nothing added yet"),
# ("PARAMOUNT", "Paramount Insurance Company Ltd.", "Nothing added yet"),
# ("PBLPBOND", "Pubali Bank Perpetual Bond", "Nothing added yet"),
# ("PDL", "Pacific Denims Limited", "Nothing added yet"),
# ("PENINSULA", "The Peninsula Chittagong Limited", "Nothing added yet"),
# ("PEOPLESINS", "Peoples Insurance Company Ltd.", "Nothing added yet"),
# ("PF1STMF", "Phoenix Finance 1st Mutual Fund", "Nothing added yet"),
# ("PHARMAID", "Pharma Aids", "Nothing added yet"),
# ("PHENIXINS", "Phoenix Insurance Company Ltd.", "Nothing added yet"),
# ("PHOENIXFIN", "Phoenix Finance and Investments Ltd", "Nothing added yet"),
# ("PHPMF1", "PHP First Mutual Fund", "Nothing added yet"),
# ("PIONEERINS", "Pioneer Insurance Company Ltd.", "Nothing added yet"),
# ("PLFSL", "Peoples Leasing and Fin. Services Ltd.", "Nothing added yet"),
# ("POPULAR1MF", "Popular Life First Mutual Fund", "Nothing added yet"),
# ("POPULARLIF", "Popular Life Insurance Co. Ltd.", "Nothing added yet"),
# ("POWERGRID", "Power Grid Company of Bangladesh Ltd", "Nothing added yet"),
# ("PRAGATIINS", "Pragati Insurance Ltd", "Nothing added yet"),
# ("PRAGATILIF", "Pragati Life Insurance Ltd.", "Nothing added yet"),
# ("PREBPBOND", "Premier Bank Perpetual Bond", "Nothing added yet"),
# ("PREMIERBAN", "Premier Bank Ltd.", "Nothing added yet"),
# ("PREMIERCEM", "Premier Cement Mills Limited", "Nothing added yet"),
# ("PREMIERLEA", "Premier Leasing & Finance Limited", "Nothing added yet"),
# ("PRIME1ICBA", "Prime Bank 1st ICB AMCL Mutual Fund", "Nothing added yet"),
# ("PRIMEBANK", "Prime Bank Ltd.", "Nothing added yet"),
# ("PRIMEFIN", "Prime Finance & Investment Ltd.", "Nothing added yet"),
# ("PRIMEINSUR", "Prime Insurance Company Ltd.", "Nothing added yet"),
# ("PRIMELIFE", "Prime Islami Life Insurance Ltd.", "Nothing added yet"),
# ("PRIMETEX", "Prime Textile Spinning Mills Limited", "Nothing added yet"),
# ("PROGRESLIF", "Progressive Life Insurance Co. Ltd.", "Nothing added yet"),
# ("PROVATIINS", "Provati Insurance Company Limited", "Nothing added yet"),
# ("PTL", "Paramount Textile Limited", "Nothing added yet"),
# ("PUBALIBANK", "Pubali Bank Ltd.", "Nothing added yet"),
# ("PURABIGEN", "Purabi Gen. Insurance Company Ltd.", "Nothing added yet"),
# ("QUASEMIND", "Quasem Industries Ltd.", "Nothing added yet"),
# ("QUEENSOUTH", "Queen South Textile Mills Limited", "Nothing added yet"),
# ("RAHIMAFOOD", "Rahima Food Corporation Limited", "Nothing added yet"),
# ("RAHIMTEXT", "Rahim Textile Mills Ltd.", "Nothing added yet"),
# ("RAKCERAMIC", "RAK Ceramics (Bangladesh) Limited", "Nothing added yet"),
# ("RANFOUNDRY", "Rangpur Foundry Ltd.", "Nothing added yet"),
# ("RDFOOD", "Rangpur Dairy & Food Products Ltd.", "Nothing added yet"),
# ("RECKITTBEN", "Reckitt Benckiser(Bd.)Ltd.", "Nothing added yet"),
# ("REGENTTEX", "Regent Textile Mills Limited", "Nothing added yet"),
# ("RELIANCE1", "Reliance One the first scheme of Reliance Insurance Mutual Fund", "Nothing added yet"),
# ("RELIANCINS", "Reliance Insurance Ltd.", "Nothing added yet"),
# ("RENATA", "Renata Ltd.", "Nothing added yet"),
# ("RENWICKJA", "Renwick Jajneswar & Co (Bd) Ltd.", "Nothing added yet"),
# ("REPUBLIC", "Republic Insurance Company Limited", "Nothing added yet"),
# ("RINGSHINE", "Ring Shine Textiles Limited", "Nothing added yet"),
# ("RNSPIN", "R.N. Spinning Mills Limited", "Nothing added yet"),
# ("ROBI", "Robi Axiata Limited", "Nothing added yet"),
# ("RSRMSTEEL", "Ratanpur Steel Re-Rolling Mills Limited", "Nothing added yet"),
# ("RUNNERAUTO", "Runner Automobiles Limited", "Nothing added yet"),
# ("RUPALIBANK", "Rupali Bank Ltd.", "Nothing added yet"),
# ("RUPALIINS", "Rupali Insurance Company Ltd.", "Nothing added yet"),
# ("RUPALILIFE", "Rupali Life Insurance Company Limited", "Nothing added yet"),
# ("SAFKOSPINN", "Safko Spinnings Mills Ltd.", "Nothing added yet"),
# ("SAIFPOWER", "SAIF Powertec Limited", "Nothing added yet"),
# ("SAIHAMCOT", "Saiham Cotton Mills Limited", "Nothing added yet"),
# ("SAIHAMTEX", "Saiham Textile Mills Ltd.", "Nothing added yet"),
# ("SALAMCRST", "S. Alam Cold Rolled Steels Ltd.", "Nothing added yet"),
# ("SALVOCHEM", "Salvo Chemical Industry Limited", "Nothing added yet"),
# ("SAMATALETH ", "Samata Leather Complex Ltd.", "Nothing added yet"),
# ("SAMORITA ", "Samorita Hospital Limited", "Nothing added yet"),
# ("SANDHANINS ", "Sandhani Life Insurance Company Ltd.", "Nothing added yet"),
# ("SAPORTL ", "Summit Alliance Port Limited", "Nothing added yet"),
# ("SAVAREFR ", "Savar Refractories Limited", "Nothing added yet"),
# ("SBACBANK ", "South Bangla Agriculture & Commerce Bank Limited", "Nothing added yet"),
# ("SEAPEARL ", "Sea Pearl Beach Resort & Spa Limited", "Nothing added yet"),
# ("SEMLFBSLGF ", "SEML FBLSL Growth Fund", "Nothing added yet"),
# ("SEMLIBBLSF", "SEML IBBL Shariah Fund", "Nothing added yet"),
# ("SEMLLECMF" , "SEML Lecture Equity Management Fund", "Nothing added yet"),
# ("SHAHJABANK" , "Shahjalal Islami Bank Ltd.", "Nothing added yet"),
# ("SHASHADNIM" , "Shasha Denims Limited", "Nothing added yet"),
# ("SHEPHERD" , "Shepherd Industries Limited", "Nothing added yet"),
# ("SHURWID" , "Shurwid Industries Limited", "Nothing added yet"),
# ("SHYAMPSUG" , "Shyampur Sugar Mills Ltd.", "Nothing added yet"),
# ("SIBL" , "Social Islami Bank Limited", "Nothing added yet"),
# ("SILCOPHL" , "Silco Pharmaceuticals Limited", "Nothing added yet"),
# ("SILVAPHL" , "Silva Pharmaceuticals Limited", "Nothing added yet"),
# ("SIMTEX" , "Simtex Industries Limited", "Nothing added yet"),
# ("SINGERBD" , "Singer Bangladesh Limited", "Nothing added yet"),
# ("SINOBANGLA" , "Sinobangla Industries Ltd.", "Nothing added yet"),
# ("SJIBLPBOND" , "SJIBL Mudaraba Perpetual Bond", "Nothing added yet"),
# ("SKICL" , "Sena Kalyan Insurance Company Limited", "Nothing added yet"),
# ("SKTRIMS" , "SK Trims & Industries Limited", "Nothing added yet"),
# ("SONALIANSH" , "Sonali Aansh Industries Limited", "Nothing added yet"),
# ("SONALILIFE" , "Sonali Life Insurance Company Limited", "Nothing added yet"),
# ("SONALIPAPR" , "Sonali Paper & Board Mills Ltd.", "Nothing added yet"),
# ("SONARBAINS" , "Sonar Bangla Insurance Ltd.", "Nothing added yet"),
# ("SONARGAON" , "Sonargaon Textiles Ltd.", "Nothing added yet"),
# ("SOUTHEASTB" , "Southeast Bank Ltd.", "Nothing added yet"),
# ("SPCERAMICS" , "Shinepukur Ceramics Limited", "Nothing added yet"),
# ("SPCL" , "Shahjibazar Power Co. Ltd.", "Nothing added yet"),
# ("SQUARETEXT" , "Square Textile Ltd.", "Nothing added yet"),
# ("SQURPHARMA" , "Square Pharmaceuticals Ltd.", "Nothing added yet"),
# ("SSSTEEL" , "S. S Steel Limited", "Nothing added yet"),
# ("T05Y0715", " 5 Years BGT Bonds Issued on 21.07.2010", "Nothing added yet"),
# ("T05Y0815", " 5 Years BGT Bonds Issued on 18.08.2010", "Nothing added yet"),
# ("T10Y0117", " 10 Years 8.5% BGT Bond Issued 10.01.2007", "Nothing added yet"),
# ("T10Y0118", " 10 Years BGT Bond Issued 02.01.2008", "Nothing added yet"),
# ("T10Y0119", " 10 Years BGT Bond Issued 07.01.2009", "Nothing added yet"),
# ("T10Y0121", " 10 years BGT Bond Issued 05.01.2011", "Nothing added yet"),
# ("T10Y0214", " 10 Years 8.5% BGT Bond Issued 090204", "Nothing added yet"),
# ("T10Y0126", " 10Y BGTB 20/01/2026", "Nothing added yet"),
# ("T10Y0216", " 10 Years 8.5% BGT Bond Issued 13022006", "Nothing added yet"),
# ("T10Y0215", " 10 Years 8.5% BGT Bond Issued 070205", "Nothing added yet"),
# ("T10Y0218", " 10 Years BGT Bond Issued 06.02.2008", "Nothing added yet"),
# ("T10Y0217", " 10 Years 8.5% BGT Bond Issued 07.02.2007", "Nothing added yet"),
# ("T10Y0220", " 10 years BGT Bond issued on 03.02.2010", "Nothing added yet"),
# ("T10Y0219", " 10 Years BGT Bond Issued 04.02.2009", "Nothing added yet"),
# ("T10Y0317", " 10 Years 8.5% BGT Bond Issued 07.03.2007", "Nothing added yet"),
# ("T10Y0221", " 10 years BGT Bond Issued 02.02.2011", "Nothing added yet"),
# ("T10Y0319", " 10 Years BGT Bond Issued 04.03.2009", "Nothing added yet"),
# ("T10Y0318", " 10 Years BGT Bond Issued 05.03.2008", "Nothing added yet"),
# ("T10Y0321", " 10 years BGT Bond Issued 02.03.2011", "Nothing added yet"),
# ("T10Y0320", " 10 years BGT Bond issued on 03.03.2010", "Nothing added yet"),
# ("T10Y0415", " 10 Years 8.5% BGT Bond Issued 040405", "Nothing added yet"),
# ("T10Y0414", " 10 Years 8.5% BGT Bond Issued 050404", "Nothing added yet"),
# ("T10Y0418", " 10 Years BGT Bond Issued 02.04.2008", "Nothing added yet"),
# ("T10Y0416", " 10 Years 8.5% BGT Bond Issued 10042006", "Nothing added yet"),
# ("T10Y0420", " 10 years BGT Bond Issued on 07.04.2010", "Nothing added yet"),
# ("T10Y0419", " 10 Years BGT Bond Issued 08.04.2009", "Nothing added yet"),
# ("T10Y0517", " 10 Years BGT Bond Issued 09.05.2007", "Nothing added yet"),
# ("T10Y0421", " 10 years BGT Bond Issued 06.04.2011", "Nothing added yet"),
# ("T10Y0519", " 10 Years BGT Bond Issued 06.05.2009", "Nothing added yet"),
# ("T10Y0518", " 10 Years BGT Bond Issued 07.05.2008", "Nothing added yet"),
# ("T10Y0521", " 10 years BGT Bond Issued 04.05.2011", "Nothing added yet"),
# ("T10Y0520", " 10 years BGT Bond Issued 05.05.2010", "Nothing added yet"),
# ("T10Y0615", " 10 Years 8.5% BGT Bond Issued 060605", "Nothing added yet"),
# ("T10Y0614", " 10 Years 8.5% BGT Bond Issued 070604", "Nothing added yet"),
# ("T10Y0617", " 10 Years BGT Bond Issued 06.06.2007", "Nothing added yet"),
# ("T10Y0616", " 10 Years 8.5% BGT Bond Issued 12062006", "Nothing added yet"),
# ("T10Y0619", " 10 Years BGT Bond Issued 03.06.2009", "Nothing added yet"),
# ("T10Y0618", " 10 Years BGT Bond Issued 04.06.2008", "Nothing added yet"),
# ("T10Y0717", " 10 Years BGT Bond Issued 04.07.2007", "Nothing added yet"),
# ("T10Y0620", " 10 Years BGT Bond Issued 02.06.2010", "Nothing added yet"),
# ("UNILEVERCL","Unilever Consumer Care Limited", "Nothing added yet"),
# ("T10Y0621", " 10 years BGT Bond Issued 08.06.2011", "Nothing added yet"),
# ("UNIONCAP", " Union Capital Limited", "Nothing added yet"),
# ("UCB", "United Commercial Bank Ltd.", "Nothing added yet"),
# ("UNIQUEHRL", "Unique Hotel & Resorts Limited", "Nothing added yet"),
# ("UNIONBANK", "Union Bank Limited", "Nothing added yet"),
# ("UNITEDINS", "United Insurance Ltd.", "Nothing added yet"),
# ("UNIONINS", "Union Insurance Company Limited", "Nothing added yet"),
# ("UPGDCL", " United Power Generation & Distribution Company Ltd.", "Nothing added yet"),
# ("UNITEDFIN", "United Finance Limited", "Nothing added yet"),
# ("UTTARABANK", " Uttara Bank Limited", "Nothing added yet"),
# ("USMANIAGL", " Usmania Glass Sheet Factory Limited", "Nothing added yet"),
# ("VAMLBDMF1", " Vanguard AML BD Finance Mutual Fund One", "Nothing added yet"),
# ("UTTARAFIN", " Uttara Finance and Investments Limited", "Nothing added yet"),
# ("WALTONHIL", " Walton Hi-Tech Industries PLC", "Nothing added yet"),
# ("VAMLRBBF", " Vanguard AML Rupali Bank Balanced Fund", "Nothing added yet"),
# ("VFSTDL", " VFS Thread Dyeing Limited", "Nothing added yet"),
# ("WATACHEM", " Wata Chemicals Limited", "Nothing added yet"),
# ("WMSHIPYARD", " Western Marine Shipyard Limited", "Nothing added yet"),
# ("YPL", " Yeakin Polymer Limited", "Nothing added yet"),
# ("ZAHEENSPIN", " Zaheen Spinning Limited", "Nothing added yet"),
# ("ZAHINTEX", " Zahintex Industries Limited", "Nothing added yet"),
# ("ZEALBANGLA", " Zeal Bangla Sugar Mills Ltd.", "Nothing added yet");


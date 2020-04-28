# scrapy-covid-data-scrapper
Code to scrap covid cases count agaist country from "worldometers" and store into mongodb using scrapy-python.

### For Example
```
{
        "_id" : ObjectId("5ea44a12019943ef70e31f93"),
        "country" : [
                "USA"
        ],
        "totalDeaths" : [
                "52,243 "
        ],
        "tests_per_1M_pop" : [
                "15,219"
        ],
        "total_cases_per_1M_pop" : [
                "2,799"
        ],
        "totalTests" : [
                "5,037,473"
        ],
        "deaths_per_1M_pop" : [
                "158"
        ],
        "critical" : [
                "15,097"
        ],
        "newDeaths" : [
                "+50"
        ],
        "newCases" : [
                "+1,298"
        ],
        "totalRecovered" : [
                "110,432"
        ],
        "activeCases" : [
                "763,855"
        ],
        "totalCases" : [
                "926,530"
        ]
}
{
        "_id" : ObjectId("5ea44a12019943ef70e31f94"),
        "country" : [
                "Spain"
        ],
        "totalDeaths" : [
                "22,902 "
        ],
        "tests_per_1M_pop" : [
                "19,896"
        ],
        "total_cases_per_1M_pop" : [
                "4,786"
        ],
        "totalTests" : [
                "930,230"
        ],
        "deaths_per_1M_pop" : [
                "490"
        ],
        "critical" : [
                "7,705"
        ],
        "newDeaths" : [
                "+378"
        ],
        "newCases" : [
                "+3,995"
        ],
        "totalRecovered" : [
                "95,708"
        ],
        "activeCases" : [
                "105,149"
        ],
        "totalCases" : [
                "223,759"
        ]
}
```
### Requirement

- **Python  >= v2.7**
- **Scrapy  >= v1.8.x**
- **mongodb >= v4.x**
- **pymongo : Python mongodb library**

### Mongodb DB Configuration

- Open __settings.py__ file and add your mongodb configuration as below

```
MONGODB_SERVER = "127.0.0.1"
MONGODB_PORT = 27017
MONGODB_DB = "covidstacks"
MONGODB_COLLECTION = "country.stack"
```
### Run and Scrap Data

- Goto __covidstack/__ root directory
```
-rw-rw-r-- 1 ruturaj ruturaj    0 Apr 25 12:03 __init__.py
-rw-rw-r-- 1 ruturaj ruturaj  152 Apr 25 12:40 __init__.pyc
-rw-rw-r-- 1 ruturaj ruturaj 1722 Apr 25 14:31 items.py
-rw-rw-r-- 1 ruturaj ruturaj 1526 Apr 25 14:31 items.pyc
-rw-rw-r-- 1 ruturaj ruturaj 1058 Apr 26 05:57 pipelines.py
-rw-rw-r-- 1 ruturaj ruturaj 1418 Apr 25 14:31 pipelines.pyc
-rw-rw-r-- 1 ruturaj ruturaj 3244 Apr 28 19:40 settings.py
-rw-rw-r-- 1 ruturaj ruturaj  505 Apr 28 20:03 settings.pyc
drwxrwxr-x 2 ruturaj ruturaj 4096 Apr 25 14:32 spiders/
```
- Run below command
```
scrapy crawl covidstack
```

### How to change Scrap URL
- To changes scrap URL, open __spiders/covidstack_spider.py__ and update URL against below variable

```
start_urls = ['https://www.worldometers.info/coronavirus/']
```



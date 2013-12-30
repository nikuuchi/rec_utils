from MySQLUtils import *
from postUtils import *

def check_item(sql, c):
    return sql.select_ping(int(c["itemid"]))

def post_check_result(type, location, data, url):
    params = {"type": type, "location": location, "authid": "auth", "data": data}
    c = createJsonRPC("pushRawData", params)
    postData(c, url)

if __name__ == '__main__':
    config = loadConfig()

    Rec_url = config["rec"]["url"]
    dbName = config["mysql"]["dbName"]
    dbUser = config["mysql"]["user"]
    dbPass = config["mysql"]["pass"]
    sql = SQL(dbName, dbUser, dbPass)

    web_config = config["zabbix"]["web"]
    data = check_item(sql, web_config)
    post_check_result("IsDown", web_config["location"], data, Rec_url)

    db_config = config["zabbix"]["db"]
    data = check_item(sql, db_config)
    post_check_result("IsDown", db_config["location"], data, Rec_url)

    app_configs = config["zabbix"]["app"]
    app_location = app_configs[0]["location"]
    data = 1
    for it in app_configs:
        data = data & check_item(sql, web_config)
    post_check_result("IsDown", app_location, data, Rec_url)

    sql.close()
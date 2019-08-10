"""Test module"""

from rival_regins_wrapper import Client


def main():
    """Main method"""
    user = input("User: ")
    passw = input("Pass: ")
    method = input("Method: ")

    client = Client(method, user, passw, show_window=True)
    print(client.var_c)

    action = input("Action: ")
    action_dict = {
        "market": market,
        "article": article
    }

    if action in action_dict:
        action_dict[action](client)

def market(client):
    """Get all market prices"""
    # print(client.market_info('oil'))
    market_info = client.get_all_market_info()
    for i in market_info:
        print("")
        print(i.upper())
        print("#"*len(i))
        for j in market_info[i]:
            print(j.upper() + ':' + market_info[i][j])

def article(client):
    """Create article"""
    client.create_article("Test", "Whoops")

if __name__ == "__main__":
    main()

from collections import defaultdict

from cashback import cardstatements
#from cashback.creditcards import amex,discover

#rewards = capital_one_quicksilver 
#card = CreditCards.RewardsCard(rewards)
#rate = card.dining_rewards


def sort_statement_transactions(statement_file):
    """
        statement_file is an input file .qfx file only
        output:
            {<category name>: [3,2.5,4,5]}
    """
    transactions = cardstatements._open_qfx_data(statement_file)

    cl = cardstatements.CategoryClassifier()
    history = list()

    d = defaultdict(list)

    for trans in transactions:
        text = trans[0]
        category = cl.category(text)
        if (trans[2] < 0):
            amount = trans[2] * -1
            payment = (category.lower(),amount)
            d[category].append(payment)


    return(history)


def calc_cashback(card,payments):
    """
        params: card object, payments
            payments data structure:
                

        returns:
            { category_name : [list of transaction amounts]}
    """
    cashback = 0
    rate = getattr(card,"dining_cb")

    for k,v in payments.items():
        lookup = "reward_" + category
        if card[lookup]:
            rate = getattr(card,lookup)
            all_cb = [int(x) * rate for x in v]
            cashback += sum(all_cb)
    return(cashback)



def format_categories(sorted_transactions):
    other_report = dict()

    for k,v in sorted_transactions.items():
        other_report[k] = "$ " + str(sum(v))
    return(other_report)
        

def calc_all(categories):
    amex_cb = calc_cashback(amex,categories)
    discover_cb = calc_cashback(discover,categories)
    spending_categories = format_categories(categories)

    report = {"Amex Gold":amex_cb,"Discover It":discover_cb}
    return_ = {"Rewards by card":report,"Spending Categories":spending_categories}
    return(return_)


def run(file_):
    transaction_data = sort_statement_transactions(file_)
    sorted_categories = _formulate_payment_data(transaction_data)

    return(sorted_categories)



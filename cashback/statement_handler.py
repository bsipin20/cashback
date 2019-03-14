from .cashback import creditcards
from .constants.card_db import db_creditcards


def get_statement_transactions(file_):
    """
        this gets a list of transactions from the statement file (stored locally) in .ofx format
    """
    transactions = cardstatements._open_qfx_data(statement_file)

    return(transactions)

def categorize_items(transactions):

    """
        accepts list of transactions (look at ofx package for available methods)
        uses a classifier to categorize transactions into relevant cateogories

        statement_file is an input file .qfx file only

        output:
    """ 
    cl = cardstatements.CategoryClassifier()
    d = defaultdict(list)

    for trans in transactions:
        text = trans[0]
        category = cl.category(text)

        if (trans[2] < 0):
            amount = trans[2] * -1
            payment = (category.lower(),amount)
            d[category].append(payment)

    return(history)

def calculate_rewards(sorted_transactions):
    """
        params
        { dining : [4,5,6,7],
          hotel : [40,40,40],
          grocery: [50,30,50,50,100]
        }
    """
    for card in db_creditcards:


    card = creditcards.RewardsCard(

    for category,transactions in sorted_transactions.items():
    
        

def view_report():
    pass
    




from collections import namedtuple
from cashback.constants import card_db

from .constants.card_db import db_creditcards

categories = ('annual_fee dining_cb grocery_cb')

class CashBackCard(namedtuple('CashBackCard',categories)):
    def __new__(cls,annual_fee,dining_cb=None,grocery_cb=None):
        return(super(CashBackCard,cls).__new__(cls,annual_fee,dining_cb,grocery_cb))

amex = CashBackCard(annual_fee=0,dining_cb=0.05,grocery_cb=0.03)
discover = CashBackCard(annual_fee=0,dining_cb=0.03,grocery_cb=0.05)

def rewards_calculator(card):
    """ calculates all rewards if input is card """
    pass

class RewardsCard(object):
    """
        an interface for handling reward cards data structure
    """


    def __init__(self,rewards):
        self.rewards = rewards

    def name(self):
        return(self.rewards['name'])

    def rewardcard_type(self):
        """ returns if type is cashback rewards or miles """
        pass

    def dining_rewards(self):
        reward_rate = self.rewards.get("reward_dining",0)
        units = self.rewards.get("reward_dining_units",0)
        return(reward_rate,units)

    def hotel_rewards(self):
        reward_rate = self.rewards.get("reward_hotels",0)
        units = self.rewards.get("reward_hotels_units",0)
        return(reward_rate,units)

    def all_rewards(self):
        reward_rate = self.rewards.get("reward_all",0)
        units = self.rewards.get("reward_all_units",0)
        return(reward_rate,units)

    def new_member_rewards(self,spending_rate_required):
        min_days = self.rewards.get("min_days_new_member",0)
        min_spending = self.rewards.get("min_spending_new_member",0)

        qualify = False
        if spending_rate_required > min_spending/min_days:
            qualify = True
        reward = 0
        units = 0
        if qualify == True:
            reward = self.rewards.get("reward_new_member",0)
            units = self.rewards.get("reward_new_member_units",0)

        return(reward,units)
    


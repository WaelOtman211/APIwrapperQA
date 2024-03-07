from infra.api_wrapper import APIWrapper


class DeckEndPoints:

    def __init__(self, api_object):
        self.my_api = api_object

    def new_deck_api(self):
        result = self.my_api.api_get_request('deck/new/')
        return result

    def shuffle_deck_api(self, deck_id):
        result = self.my_api.api_get_request(f'deck/{deck_id}/shuffle/')
        return result



    def draw_cards_api(self, deck_id, count):
        result = self.my_api.api_get_request(f'deck/{deck_id}/draw/?count={count}')
        return result.json()

    def draw_specific_card_api(self, deck_id, card_to_draw):
        result = self.my_api.api_get_request(f'deck/{deck_id}/draw/?cards={card_to_draw}')
        return result

    def partial_deck_api(self,cards):
        result = self.my_api.api_get_request(f'deck/new/shuffle/?cards={cards}')
        return result.json()

    def partial_deck_info_api(self, deck_id):
        result = self.my_api.api_get_request(f'deck/{deck_id}')
        return result.json()

    def add_to_pile_api(self, deck_id, pile_name, cards_to_add):
        endpoint = f"deck/{deck_id}/pile/{pile_name}/add/"
        data = {"cards": cards_to_add}
        result = self.my_api.api_post_request(endpoint, data=data)
        print(result)
        return result.json()
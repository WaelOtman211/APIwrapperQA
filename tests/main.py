import unittest
from infra.api_wrapper import APIWrapper
from logic.deck_endpoints import DeckEndPoints
from infra.config_handler import ConfigHandler

class MainTest(unittest.TestCase):

    def setUp(self):
        self.my_api = APIWrapper()
        self.api_logic = DeckEndPoints(self.my_api)
        self.cards = self.my_api.cards

    def test_new_deck(self):
        result = self.api_logic.new_deck_api()
        self.assertTrue(result.json()['success'])

    def test_shuffle_deck(self):
        deck_id = "new"
        result = self.api_logic.shuffle_deck_api(deck_id)
        self.assertTrue(result.ok)

    def test_draw_cards(self):
        deck_id = "new"
        count = 2
        result = self.api_logic.draw_cards_api(deck_id, count)
        print(result)
        self.assertEqual(len(result['cards']), count)

    def test_draw_multiple_cards(self):
        # Initialize APIWrapper and DeckEndPoints instances

        # Create a new deck
        new_deck_result = self.api_logic.new_deck_api()
        self.assertTrue(new_deck_result.ok)

        # Extract the deck_id from the response
        deck_id = new_deck_result.json()['deck_id']

        # Shuffle the deck
        shuffle_result = self.api_logic.shuffle_deck_api(deck_id)
        self.assertTrue(shuffle_result.ok)

        # Draw multiple cards from the deck
        count = 5
        draw_card_result = self.api_logic.draw_cards_api(deck_id, count)

        # Assert that the draw card request was successful
        self.assertTrue(draw_card_result['success'])

        # Extract the drawn cards from the response
        drawn_cards = draw_card_result['cards']
        print(len(drawn_cards))
        # Assert that the correct number of cards were drawn
        self.assertEqual(len(drawn_cards), count)

    def test_partial_deck_information(self):
        partial_deck_result = self.api_logic.partial_deck_api(self.cards)
        deck_id = partial_deck_result['deck_id']
        partial_deck_info_result = self.api_logic.partial_deck_info_api(deck_id)
        expected_remaining = 12
        self.assertEqual(expected_remaining, partial_deck_info_result['remaining'],"not the same")

    def test_add_to_pile(self):
        deck_id = "new"
        pile_name = "wael_pile"
        cards_to_add = ["AS", "2S", "3S"]
        add_to_pile_result = self.api_logic.add_to_pile_api(deck_id, pile_name, cards_to_add)
        self.assertTrue(add_to_pile_result['success'])


if __name__ == '__main__':
    unittest.main()

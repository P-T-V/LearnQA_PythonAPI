class Test_hw_10:

    def test_check_len_phrase(self):
        phrase = input("Set a phrase less than 15 symbols: ")

        assert len(phrase) < 15, f"Input phrase length >= 15 symbols: {len(phrase)} now"
        print(f"Phrase length: {len(phrase)} symbols")
import unittest
import rsalib


class TestRSA(unittest.TestCase):
    def test_eratostheneen_seula(self):
        primes = rsalib.eratostheneen_seula(12)
        print(primes)
        self.assertEqual(primes, [2, 3, 5, 7, 11])

    def test_miller_rabin(self):
        # https://en.wikipedia.org/wiki/RSA_numbers
        self.assertEqual(rsalib.miller_rabin(
            5846418214406154678836553182979162384198610505601062333, 3), True)
        self.assertEqual(rsalib.miller_rabin(
            5846418214406154678836553182979162384198610505601062330, 3), False)

    def test_all(self):
        input_text = "Hello World abcdef12345!#%&/()="
        bits = 2048

        p = rsalib.get_random_n_bit_prime(bits)
        q = rsalib.get_random_n_bit_prime(bits)
        keypair = rsalib.generate_keypair(p, q)
        N = keypair[0]
        e = keypair[1]
        d = keypair[2]
        encoded_text = rsalib.encode(input_text)
        encrypted_message = rsalib.encrypt(encoded_text, e, N)
        decrypted_message = rsalib.decrypt(encrypted_message, d, N)
        decoded_message = rsalib.decode(decrypted_message)

        self.assertEqual(input_text, decoded_message)


if __name__ == '__main__':
    unittest.main()

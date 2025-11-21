import unittest
import rsalib
import random


class TestRSA(unittest.TestCase):
    def setUp(self) -> None:
        # Estäkseen: ResourceWarning: unclosed file
        primefile = open("test_primes.txt", "r")
        primetext = primefile.read()
        primefile.close()
        
        self.openssl_primes = list(map(lambda x: int(x), filter(
            lambda x: len(x) > 0, primetext.split("\n"))))
        return super().setUp()

    def test_eratostheneen_seula(self):
        primes = rsalib.eratostheneen_seula(12)
        self.assertEqual(primes, [2, 3, 5, 7, 11])

    def test_miller_rabin(self):
        # https://en.wikipedia.org/wiki/RSA_numbers
        self.assertEqual(rsalib.miller_rabin(
            5846418214406154678836553182979162384198610505601062333, 3), True)
        self.assertEqual(rsalib.miller_rabin(
            5846418214406154678836553182979162384198610505601062330, 3), False)

    def test_text_input(self):
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

    def test_large_input(self):
        bits = 2048

        p = rsalib.get_random_n_bit_prime(bits)
        q = rsalib.get_random_n_bit_prime(bits)
        keypair = rsalib.generate_keypair(p, q)
        N = keypair[0]
        e = keypair[1]
        d = keypair[2]

        # Salattavan datan maksimikoko on modulus - 1, yritetään siis salata ja purkaa modulus - 1
        input_large_int = N - 1

        encrypted_message = rsalib.encrypt(input_large_int, e, N)
        decrypted_message = rsalib.decrypt(encrypted_message, d, N)

        self.assertEqual(input_large_int, decrypted_message)

    def test_large_composites(self):
        composites = []
        for i in self.openssl_primes:
            composites.append(i * random.choice(self.openssl_primes))

        for i in composites:
            self.assertEqual(rsalib.try_random_n_bit_prime(0, i), None)


    def test_large_primes(self):
        for i in self.openssl_primes:
            self.assertEqual(rsalib.try_random_n_bit_prime(0, i), i)
        


if __name__ == '__main__':
    unittest.main()

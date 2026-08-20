import asyncio

from asv_runner.benchmarks.mark import skip_benchmark_if
from django import conf
from django.contrib.auth.hashers import acheck_password, make_password

from ...utils import bench_setup

try:
    import argon2
except ImportError:
    argon2 = None

try:
    import bcrypt
except ImportError:
    bcrypt = None

# scrypt requires OpenSSL 1.1+
try:
    import hashlib

    scrypt = hashlib.scrypt
except ImportError:
    scrypt = None


PASSWORDS = [
    "password123",
    "qwerty123",
    "helloworld123",
]


# async func aren't automatically benchmarked.
async def op(encoded_passwords):
    await asyncio.gather(
        *[
            acheck_password(password, encoded)
            for password, encoded in zip(PASSWORDS, encoded_passwords)
        ]
    )


class Hasher:
    params = [
        "PBKDF2PasswordHasher",
        "PBKDF2SHA1PasswordHasher",
    ]
    param_names = ["hasher"]

    def setup(self, hasher):
        bench_setup()
        conf.settings.PASSWORD_HASHERS = [f"django.contrib.auth.hashers.{hasher}"]
        self.encoded_passwords = [make_password(password) for password in PASSWORDS]

    def time_acheck_password(self, _):
        asyncio.run(op(self.encoded_passwords))


class HasherArgon:
    def setup(self):
        bench_setup()
        conf.settings.PASSWORD_HASHERS = [
            "django.contrib.auth.hashers.Argon2PasswordHasher"
        ]
        self.encoded_passwords = [make_password(password) for password in PASSWORDS]

    @skip_benchmark_if(argon2 is None)
    def time_acheck_password(self):
        asyncio.run(op(self.encoded_passwords))


class HasherBcrypt:
    def setup(self):
        bench_setup()
        conf.settings.PASSWORD_HASHERS = [
            "django.contrib.auth.hashers.BCryptSHA256PasswordHasher"
        ]
        self.encoded_passwords = [make_password(password) for password in PASSWORDS]

    @skip_benchmark_if(bcrypt is None)
    def time_acheck_password(self):
        asyncio.run(op(self.encoded_passwords))


class HasherScypt:
    def setup(self):
        bench_setup()
        conf.settings.PASSWORD_HASHERS = [
            "django.contrib.auth.hashers.ScryptPasswordHasher"
        ]
        self.encoded_passwords = [make_password(password) for password in PASSWORDS]

    @skip_benchmark_if(scrypt is None)
    def time_acheck_password(self):
        asyncio.run(op(self.encoded_passwords))

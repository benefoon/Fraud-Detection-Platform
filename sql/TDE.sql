-- PostgreSQL Example
CREATE EXTENSION pgcrypto;
SELECT pgp_sym_encrypt('Sensitive Data', 'your-encryption-key');

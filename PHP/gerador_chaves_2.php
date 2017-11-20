<?php
    # Essa array tem as configurações de qual cifra vai ser usada, nesse caso MD;
    #   tipo da chave privada, nesse caso RSA; e tamanho da chave privada em bits.
    $config = array(
        "digest_alg" => OPENSSL_ALGO_MD5,
        "private_key_bits" => 4096,
        "private_key_type" => OPENSSL_KEYTYPE_RSA,
    );
        
    // Create the private and public key
    $res = openssl_pkey_new($config);

    // Extract the private key from $res to $privKey
    openssl_pkey_export($res, $privKey);

    // Extract the public key from $res to $pubKey
    $pubKey = openssl_pkey_get_details($res);
    $pubKey = $pubKey["key"];

    # Dados encriptados vão aqui
    $data = 'Client';

    // Encrypt the data to $encrypted using the public key
    openssl_public_encrypt($data, $encrypted, $pubKey);

    # Mostra a chave privada na variável $privKey
    echo "\n".$privKey."\n";
    # Mostra a chave pública na variável $pubKey
    echo "\n".$pubKey."\n";

    $encrypted_hex = bin2hex($encrypted);

    echo $encrypted_hex;

    // Decrypt the data using the private key and store the results in $decrypted
    openssl_private_decrypt($encrypted, $decrypted, $privKey);

    // echo $decrypted;
?>

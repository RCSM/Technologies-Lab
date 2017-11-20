<?php
    # link para biblioteca em php de comunicações seguras : https://github.com/phpseclib/phpseclib

    $privateKey = openssl_pkey_new(array('private_key_bits' => 2048));
    $details = openssl_pkey_get_details($privateKey);
    $publicKey = $details['key'];

    echo "\n".$privateKey."\n".$details."\n".$publicKey;
    # link para o método que exporta chave para arquivos : http://php.net/manual/en/function.openssl-pkey-export.php
    # link para página que fala como gerar a chave privada : http://stackoverflow.com/questions/36704417/generate-rsa-private-ssh-key-in-php
?>
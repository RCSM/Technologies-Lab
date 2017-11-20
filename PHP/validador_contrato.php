<?php

	$dados_formando = json_decode(file_get_contents("dados_formando.json"), true);		# Testar

	foreach ($dados_formando as $key => $value) {		# Testar
		if ($key == "email")
			$email = $value;
		if ($key == "pk")
			$pk = $value;
	}

  	$headers  = 'MIME-Version: 1.0' . "\r\n";
    $headers .= 'Content-type: text/html; charset=iso-8859-1' . "\r\n";

	$enviar_email = mail($email, "Verificação de finalização de contrato", $pk, $headers);
	if ($enviar_email)
		$URL = "https://www.google.com.br/";
	else
		echo "FAILED TO SEND MAIL";

?>
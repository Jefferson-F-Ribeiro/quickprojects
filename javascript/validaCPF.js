function validarCPF(cpf) {
    // Remove caracteres não numéricos
    cpf = cpf.replace(/[^\d]/g, '');
  
    // Verifica se o CPF tem 11 dígitos
    if (cpf.length !== 11) {
      return false;
    }
  
    // Verifica se todos os dígitos são iguais, o que é inválido
    if (/^(\d)\1{10}$/.test(cpf)) {
      return false;
    }
  
    // Calcula o primeiro dígito verificador
    let soma = 0;
    for (let i = 0; i < 9; i++) {
      soma += parseInt(cpf.charAt(i)) * (10 - i);
    }
    let resto = soma % 11;
    let digito1 = resto < 2 ? 0 : 11 - resto;
  
    // Verifica o primeiro dígito verificador
    if (digito1 !== parseInt(cpf.charAt(9))) {
      return false;
    }
  
    // Calcula o segundo dígito verificador
    soma = 0;
    for (let i = 0; i < 10; i++) {
      soma += parseInt(cpf.charAt(i)) * (11 - i);
    }
    resto = soma % 11;
    let digito2 = resto < 2 ? 0 : 11 - resto;
  
    // Verifica o segundo dígito verificador
    if (digito2 !== parseInt(cpf.charAt(10))) {
      return false;
    }
  
    return true;
  }
  
  // Exemplo de uso
  const cpf = "123.456.789-09";
  if (validarCPF(cpf)) {
    console.log(`${cpf} é um CPF válido.`);
  } else {
    console.log(`${cpf} não é um CPF válido.`);
  }
  
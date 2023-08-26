import java.util.Scanner;

public class passwordGenerator {

	public static void main(String[] args){
		Scanner scanner = new Scanner(System.in);

		System.out.println("####################################################");
		System.out.println("########## Bem vind@ ao gerador de senhas! #########");
		System.out.println("####################################################\n");

		System.out.println("Escolha uma das opções abaixo: \n");

		System.out.println("0 - Somente letras maiúsculas.");
		System.out.println("1 - Somente letras minúsculas.");
		System.out.println("2 - Somente números.");
		System.out.println("3 - Somente símbolos.");
		System.out.println("4 - Escolha customizada.");
		System.out.println("Qualquer outro número - Sair.\n");
		
		int c = scanner.nextInt();
		int l = 6;
		int option = 7;

		switch(c){			
			case 0:
				System.out.println("Quantos caracteres deve ter sua senha? ");
				l = scanner.nextInt();
				option = 0;
				break;
			case 1:
				System.out.println("Quantos caracteres deve ter sua senha? ");
				l = scanner.nextInt();
				option = 1;
				break;
			case 2:
				System.out.println("Quantos caracteres deve ter sua senha? ");
				l = scanner.nextInt();
				option = 2;
				break;
			case 3:
				System.out.println("Quantos caracteres deve ter sua senha? ");		
				l = scanner.nextInt();
				option = 3;	
				break;
			case 4:
				System.out.println("Quantos caracteres deve ter sua senha? ");
				l = scanner.nextInt();
				option = 4;
				break;
			default:
				break;			
		}

		generator g = new generator(l,option);

		System.out.println("\nA sua nova senha é: " + g.generatePassword());
	}

}
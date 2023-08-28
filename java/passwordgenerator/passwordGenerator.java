import java.util.Scanner;

public class passwordGenerator {

	public static void main(String[] args){
		Scanner scanner = new Scanner(System.in);

		System.out.println("####################################################");
		System.out.println("########## Bem vind@ ao gerador de senhas! #########");
		System.out.println("####################################################\n");

		int option = 7;
		boolean test = true;

		while(test){
		System.out.println("Escolha uma das opções abaixo: \n");

		System.out.println("0 - Somente letras maiúsculas.");
		System.out.println("1 - Somente letras minúsculas.");
		System.out.println("2 - Somente números.");
		System.out.println("3 - Somente símbolos.");
		System.out.println("4 - Escolha customizada.");
		System.out.println("5 - Sair.\n");	

		int c = scanner.nextInt();

		if(c == 5){
			test = false;
			System.out.println("\nEncerrando...");
		}

		else{

		System.out.println("Quantos caracteres deve ter sua senha? ");

		int l = scanner.nextInt();
				
		switch(c){			
			case 0:
				option = 0;
				break;
			case 1:
				option = 1;
				break;
			case 2:
				option = 2;
				break;
			case 3:
				option = 3;	
				break;
			case 4:
				option = 4;
				break;
			case 5:
				System.out.println("Você deseja que sua senha possa conter letras maiúsculas? ");
            	String r1 = scanner.next();
            	System.out.println("Você deseja que sua senha possa conter letras minúsculas? ");
            	String r2 = scanner.next();
            	System.out.println("Você deseja que sua senha possa conter números? ");
            	String r3 = scanner.next();
            	System.out.println("Você deseja que sua senha possa conter símbolos? ");
            	String r4 = scanner.next();
				generator g1 = new generator(l,r1,r2,r3,r4);
				System.out.println("\nA sua nova senha é: " + g1.generatePassword() + "\n");
				break;			
		}

		if(option == 0 || option == 1 || option == 2 || option == 3 || option == 4 ){
			generator g = new generator(l,option,scanner);
			System.out.println("\nA sua nova senha é: " + g.generatePassword() + "\n");
		}
		}
		}
	}
}
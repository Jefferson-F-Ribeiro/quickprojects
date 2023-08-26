import java.util.Random;
import java.util.Scanner;

public class generator {

        private passwordCharacters charactersLowerCase = new passwordCharacters("abcdefghijklmnopqrstuvwxyz");
        private passwordCharacters charactersUpperCase = new passwordCharacters("ABCDEFGHIJKLMNOPQRSTUVWXYZ");
        private passwordCharacters charactersNumbers = new passwordCharacters("0123456789");
        private passwordCharacters charactersSymbols = new passwordCharacters("!@#$%^&*");
        private passwordCharacters customSelection;

        private int length;
        private String password;
        
        public generator(){
            this.customSelection = new passwordCharacters();
            this.length = 6;
            customGenerator();
        }

        public generator(int length, int option){

            this.length = length;
            
            switch(option){
                case 0:
                    this.customSelection = this.charactersUpperCase;
                    break;
                case 1:
                    this.customSelection = this.charactersLowerCase;
                    break;
                case 2:
                    this.customSelection = this.charactersNumbers;
                    break;
                case 3:
                    this.customSelection = this.charactersNumbers;
                    break;
                case 4:
                    this.customSelection = new passwordCharacters(customGenerator());
                    break;
            }
        }

        public String generatePassword(){
            StringBuilder p = new StringBuilder();
            Random r = new Random();

            for(int i=0; i<this.length; i++){
                int index = r.nextInt(this.customSelection.getCharacters().length());
                p.append(this.customSelection.getCharacters().charAt(index));
            }

            return p.toString();
        }

        public String customGenerator(){
            Scanner scanner = new Scanner(System.in);
            String s = new String();
            
            System.out.println("Você deseja que sua senha possa conter letras maiúsculas? ");
            String r1 = scanner.nextLine();
            System.out.println("Você deseja que sua senha possa conter letras minúsculas? ");
            String r2 = scanner.nextLine();
            System.out.println("Você deseja que sua senha possa conter números? ");
            String r3 = scanner.nextLine();
            System.out.println("Você deseja que sua senha possa conter símbolos? ");
            String r4 = scanner.nextLine();

            scanner.close();

            if(r1.equals("S") || r1.equals("s")){
                s = s + this.charactersUpperCase.getCharacters();
            }

            if(r2.equals("S") || r2.equals("s")){
                s = s + this.charactersLowerCase.getCharacters();
            }

            if(r3.equals("S") || r3.equals("s")){
                s = s + this.charactersNumbers.getCharacters();
            }

            if(r4.equals("S") || r4.equals("s")){
                s = s + this.charactersSymbols.getCharacters();
            }

            return s;
        }

}
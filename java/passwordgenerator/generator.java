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

        public generator(int length, int option, Scanner scanner){

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
                default:
                    break;
            }
        }

        public generator(int length, String a, String b, String c, String d){

            this.length = length;
            this.customSelection = new passwordCharacters(customGenerator(a, b, c, d));
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

        public String customGenerator(String a, String b, String c, String d){
            String s = new String();
            

            if(a.equals("S") || a.equals("s")){
                s = s + this.charactersUpperCase.getCharacters();
            }

            if(b.equals("S") || b.equals("s")){
                s = s + this.charactersLowerCase.getCharacters();
            }

            if(c.equals("S") || c.equals("s")){
                s = s + this.charactersNumbers.getCharacters();
            }

            if(d.equals("S") || d.equals("s")){
                s = s + this.charactersSymbols.getCharacters();
            }
            return s;
        }

}
import java.util.Random;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;
import java.util.Collections;

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

        public generator(int length){
            this.length = length;
            this.customSelection = new passwordCharacters(customGenerator("s","s","s","s"));
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

        public String exclusiveGeneratePassword(){
            Random r = new Random();
        
            List<Character> upperCaseChars = new ArrayList<>();
            List<Character> symbolChars = new ArrayList<>();
            List<Character> lowerCaseChars = new ArrayList<>();
            List<Character> numberChars = new ArrayList<>();
        
            for (char c : this.charactersUpperCase.getCharacters().toCharArray()) {
                upperCaseChars.add(c);
            }
            for (char c : this.charactersSymbols.getCharacters().toCharArray()) {
                symbolChars.add(c);
            }
            for (char c : this.charactersLowerCase.getCharacters().toCharArray()) {
                lowerCaseChars.add(c);
            }
            for (char c : this.charactersNumbers.getCharacters().toCharArray()) {
                numberChars.add(c);
            }
        
            Collections.shuffle(upperCaseChars);
            Collections.shuffle(symbolChars);
            Collections.shuffle(lowerCaseChars);
            Collections.shuffle(numberChars);
        
            List<Character> masterList = new ArrayList<>();
            masterList.addAll(upperCaseChars);
            masterList.addAll(symbolChars);
            masterList.addAll(lowerCaseChars);
            masterList.addAll(numberChars);
        
            Collections.shuffle(masterList);
        
            StringBuilder password = new StringBuilder();
        
            password.append(upperCaseChars.get(0));
            password.append(symbolChars.get(0));
            password.append(lowerCaseChars.get(0));
            password.append(numberChars.get(0));
        
            for (int i = 4; i < this.length; i++) {
                int index = r.nextInt(this.customSelection.getCharacters().length());
                password.append(this.customSelection.getCharacters().charAt(index));
            }
        
            List<Character> passwordList = new ArrayList<>();
            for (char c : password.toString().toCharArray()) {
                passwordList.add(c);
            }
            Collections.shuffle(passwordList);
            
            StringBuilder randomizedPassword = new StringBuilder();
            for (char c : passwordList) {
                randomizedPassword.append(c);
            }
        
            return randomizedPassword.toString();
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
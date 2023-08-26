import java.util.Random;

public class generator {

        private String charactersLowerCase = "abcdefghijklmnopqrstuvwxyz";
        private String charactersUpperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        private String charactersNumbers = "0123456789";
        private String charactersSymbols = "!@#$%^&*";
        private String customSelection;
        private int length;
        private String password;
        
        public generator(){
            this.customSelection = this.charactersLowerCase + this.charactersUpperCase + this.charactersNumbers + this.charactersSymbols;
            this.length = 6;
        }

        public String generatePassword(){
            StringBuilder p = new StringBuilder();
            Random r = new Random();

            for(int i=0; i<this.length; i++){
                int index = r.nextInt(this.customSelection.length());
                p.append(this.customSelection.charAt(index));
            }

            return p.toString();
        }

}
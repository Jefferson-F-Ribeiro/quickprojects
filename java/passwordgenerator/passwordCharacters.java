public class passwordCharacters{

    private String characters;
    private boolean active;

    public passwordCharacters(){
        this.active = false;
        this.characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*";
    }

    public passwordCharacters(String s){
        this.active = false;
        this.characters = s;
    }

    public String getCharacters(){
        return this.characters;
    }

    public void setCharacters(String s){
        this.characters = s;
    }

    public boolean isActive(){
        return this.active;
    }

    public void setActive(boolean b){
        this.active = b;
    }

}
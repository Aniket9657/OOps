class Static1{
    public void  sound()
    {
        System.out.println("Sound");
    } 
    
}
class S extends Static1{
    public void sound()
    {
        System.out.println("Sound of Dog");
    }

}



public class Staticx{
    public static void main(String[] args) {
        Static1 s1=new Static1();
        s1.sound();
        Static1 s2=new S();
        s2.sound();
    }
}
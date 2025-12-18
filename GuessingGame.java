import java.util.Scanner;
public class GuessingGame 
{
    static Scanner sc = new Scanner(System.in);
    static boolean keepPlaying = true;
    public static void main(String[] args) 
    {
        System.out.println("Let's play a guessing game\n");
        while(keepPlaying)
        {
            playAround();
        }
        System.out.println("\nThank you for playing");
    }
    public static void playAround()
    {
        boolean validInput;
        int number, guess;
        String answer;
        number = (int)(Math.random()*10)+1;
        System.out.println("I am thinking of a number between 1 and 10");
        System.out.println("What do you think it is?");
        do
        {
            guess = sc.nextInt();
            validInput = true;
            if(guess<1||guess>10)
            {
                System.out.println("I said between 1 and 10");
                validInput = false;
            }
        }while(!validInput);
        if(guess==number)
        {
            System.out.println("You are right");
        }
        else
            System.out.println("You are wrong\nThe number was "+number);
        
        do
        {
            System.out.println("Play again?(Y or N)");
            answer = sc.next();
            validInput = true;
            if(answer.equalsIgnoreCase("Y"));
            else if(answer.equalsIgnoreCase("N"))
            {
                keepPlaying = false;
            }
            else 
                validInput = false;
        }while(!validInput);
    }
}

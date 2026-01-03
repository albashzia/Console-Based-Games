import java.util.Scanner;
public class GuessingGame 
{
    static Scanner sc = new Scanner(System.in);
    static boolean keepPlaying = true;
    // main entry point
    public static void main(String[] args) 
    {
        System.out.println("Let's play a guessing game\n");
        while(keepPlaying)
        {
            playAround(); // call to function
        }
        System.out.println("\nThank you for playing");
    }

    //  method for processing the game
    public static void playAround()
    {
        boolean validInput;
        int number, guess;
        String answer;
        number = (int)(Math.random()*10)+1; // generating a random number between 1 and 10
        System.out.println("I am thinking of a number between 1 and 10");
        System.out.println("What do you think it is?");
        do
        {
            guess = sc.nextInt(); // taking a guess from user
            validInput = true;
            if(guess<1||guess>10)
            {
                System.out.println("I said between 1 and 10"); // handling if the number entered by user is outside from specified input limit
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
            System.out.println("Play again?(Y or N)");  // asking if a user wants to continue playing
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

public class JavaQuizGame {
    public static void main(String[] args) {

        int points = 0;
        Scanner input = new Scanner(System.in);
        String questions[] = {
            "Which keyword is used to define a class in Java?",
            "What is the file extension of a Java source file?",
            "Which method is the entry point of a Java program?",
            "Which data type is used to store whole numbers in Java?",
            "Which keyword is used to create an object in Java?",
            "What does System.out.println() do?",
            "Which symbol is used to end a statement in Java?",
            "Which of the following is NOT a Java primitive data type?",
            "What is the default value of an int variable in Java (instance variable)?",
            "Which keyword is used to inherit a class in Java?"
        };


        String options[] = {
            "a) class b) struct c) define d) object",
            "a) .java b) .jav c) .class d) .js",
            "a) start() b) main() c) run() d) init()",
            "a) float b) double c) int d) char",
            "a) make b) create c) new d) object",
            "a) Takes input b) Prints output with new line c) Prints without new line d) Stops program",
            "a) : b) . c) ; d) ,",
            "a) int b) boolean c) String d) char",
            "a) 1 b) 0 c) null d) garbage",
            "a) this b) super c) implements d) extends"
        };


        char answers[] = {
            'a',
            'a',
            'b',
            'c',
            'c',
            'b',
            'c',
            'c',
            'b',
            'd'
        };
    }
}

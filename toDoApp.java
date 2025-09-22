// ToDoApp.java
import java.util.*;

public class toDoApp {
    static ArrayList<String> tasks = new ArrayList<String>();

    public static void addtask(String t) {
        tasks.add(t);
        System.out.println("Task Added!!");
    }

    public static void showTasks() {
        if (tasks.isEmpty()) {
            System.out.println("No tasks yet");
        } else {
            for (int i = 0; i < tasks.size(); i++) {
                System.out.println((i + 1) + ". " + tasks.get(i));
            }
        }
    }

    public static void removeTask(int n) {
        if (n > 0 && n <= tasks.size()) {
            tasks.remove(n - 1); 
            System.out.println("Task removed!");
        } else {
            System.out.println("Invalid task number!");
        }
    }

    public static void main(String args[]) {
        Scanner s = new Scanner(System.in);
        while (true) {
            System.out.println("--------------------------"); // para malupit ung format man
            System.out.println("1 Add Task"); 
            System.out.println("2.Show Tasks");
            System.out.println("3.Remove Task");
            System.out.println("4 Exit");
            System.out.println("--------------------------");
            System.out.print("Enter Choice: ");

            int choice = s.nextInt(); 

            switch (choice) {
                case 1:
                    System.out.print("Enter Task: ");
                    s.nextLine();
                    String t = s.nextLine();
                    addtask(t);
                    break;
                case 2:
                    showTasks();
                    break;
                case 3:
                    System.out.print("Enter task no to remove: ");
                    int n = s.nextInt();
                    removeTask(n); 
                    break;
                case 4:
                    s.close();
                    break;
                default:
                    System.out.print("Wrong Choice!!");
                    break;
            }
            if (choice == 4) {
                break;
            }
        }
    }
}

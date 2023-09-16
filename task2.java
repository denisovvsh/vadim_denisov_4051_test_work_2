package test_work_2;

import java.io.FileWriter;
import java.io.IOException;
import java.util.PriorityQueue;

public class task2 {
    public static void main(String[] args) {
        PriorityQueue<Toy> toyQueue = new PriorityQueue<>((t1, t2) -> Integer.compare(t2.getFrequency(), t1.getFrequency()));

        // Пример входных данных
        String[] toyData = {
            "1,Кукла,5",
            "2,Машинка,3",
            "3,Мяч,7"
        };

        // Заполняем очередь
        for (String data : toyData) {
            String[] parts = data.split(",");
            if (parts.length == 3) {
                int id = Integer.parseInt(parts[0]);
                String name = parts[1];
                int frequency = Integer.parseInt(parts[2]);
                Toy toy = new Toy(id, name, frequency);
                toyQueue.add(toy);
            }
        }

        try {
            FileWriter fileWriter = new FileWriter("toy_queue.txt");
            for (int i = 0; i < 10; i++) {
                Toy toy = toyQueue.poll();
                if (toy != null) {
                    fileWriter.write("ID: " + toy.getId() + ", Name: " + toy.getName() + ", Frequency: " + toy.getFrequency() + "\n");
                }
            }
            fileWriter.close();
            System.out.println("Результат записан в файл 'toy_queue.txt'.");
        } catch (IOException e) {
            System.err.println("Ошибка при записи в файл: " + e.getMessage());
        }
    }
}

class Toy {
    private int id;
    private String name;
    private int frequency;

    public Toy(int id, String name, int frequency) {
        this.id = id;
        this.name = name;
        this.frequency = frequency;
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public int getFrequency() {
        return frequency;
    }
}
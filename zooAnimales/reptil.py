// Paquete zooAnimales
package zooAnimales;

import gestion.Zona;

import java.util.ArrayList;

public class Reptil extends Animal {
    private static int iguanas;
    private static int serpientes;
    private static ArrayList<Reptil> reptiles = new ArrayList<>();

    private String colorEscamas;
    private int largoCola;

    public Reptil(String nombre, int edad, String habitat, String genero, String colorEscamas, int largoCola) {
        super(nombre, edad, habitat, genero);
        this.colorEscamas = colorEscamas;
        this.largoCola = largoCola;
        reptiles.add(this);
    }

    public static Reptil crearIguana(String nombre, int edad, String genero) {
        Reptil iguana = new Reptil(nombre, edad, "bosques", genero, "verde", 3);
        iguanas++;
        return iguana;
    }

    public static Reptil crearSerpiente(String nombre, int edad, String genero) {
        Reptil serpiente = new Reptil(nombre, edad, "selva", genero, "marrón", 5);
        serpientes++;
        return serpiente;
    }

    public static int cantidadReptiles() {
        return reptiles.size();
    }

    public static int getIguanas() {
        return iguanas;
    }

    public static int getSerpientes() {
        return serpientes;
    }

    public String getColorEscamas() {
        return colorEscamas;
    }

    public int getLargoCola() {
        return largoCola;
    }
}


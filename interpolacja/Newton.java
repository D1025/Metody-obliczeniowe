package interpolacja;
class Newton {
    double[] x;
    double[] y;
    double[][] array;

    Newton(double[] x, double[] y)
    {
        this.x = x;
        this.y = y;
        array = new double[x.length][x.length];
        for (int i = 0; i < array.length; i++) {
            for (int j = 0; j < array.length; j++) {
                array[i][j] = 0;
            }
        }
        for (int i = 0; i < y.length; i++) {
            array[0][i]=y[i];
        }
    }


    void interpoluj()
    {

        for (int i = 1; i < array.length; i++) {
            for (int j = 0; j < y.length-i; j++) {
                array[i][j] = (array[i-1][j+1]-array[i-1][j])/(x[j+i]-x[j]);
                //System.out.printf("(%f-%f)/(%f-%f)\n", array[i-1][j+1], array[i-1][j], x[j+i], x[j]);
            }
        }
    }
    void printarray()
    {
        for (int i = 0; i < array.length; i++) {
            for (int j = 0; j < array.length; j++) {
                System.out.print(array[i][j]);
                System.out.print(" ");
            }
            System.out.println();
        }
    }

    double W(double przewidywana)
    {
        interpoluj();
        double W = 0;
        for (int i = 0; i < array.length; i++) {
            double zxka =1;
            for (int j = 1; j <= i; j++) {
                zxka *= (przewidywana-x[j-1]);
            }
            W+=array[i][0]*zxka;
        }
        return W;
    }
    public static void main(String[] args) {

        double[] x1 = {-4, -2, 0, 2, 4};
        double[] y1 = {118, -14, -2, 10, 262};

        Newton n1 = new Newton(x1, y1);

        // n.interpoluj();
        // n.printarray();
        System.out.println(n1.W(3));


    }
}
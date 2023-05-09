package interpolacja;
public class Main {
    public static void main(String[] args) {
        double[][] wartosci = new double[7][7];
        double[] wyniki = new double[7];

        double[] dane_x = new double[5];
        double[] dane_y = new double[5];

        // double[] przechowywane_wyniki = new double[5];

        dane_x[0] = -4; // dane xi
        dane_x[1] = -2;
        dane_x[2] = 0;
        dane_x[3] = 2;
        dane_x[4] = 4;

        dane_y[0] = 118; // dane f(xi)
        dane_y[1] = -14;
        dane_y[2] = -2;
        dane_y[3] = 10;
        dane_y[4] = 262;

        double[] pochodna_x = new double[2];
        double[] pochodna_y = new double[2];

        pochodna_x[0]=-4;
        pochodna_x[1]=4;

        pochodna_y[0]=-174;
        pochodna_y[1]=274;




        double X = 1;

        int LENGTH = dane_x.length;
        for (int i = 0; i < LENGTH + 2; i++) {
            for (int j = 0; j < LENGTH + 2; j++) {
                wartosci[i][j] = 0.0;
            }
        }

        for (int i = 0; i < LENGTH; i++) {
            wartosci[i][0] = 1.0;
            wartosci[i][1] = dane_x[i];
            wartosci[i][2] = Math.pow(dane_x[i], 2);
            wartosci[i][3] = Math.pow(dane_x[i], 3);

            for (int j = 1; j < i; j++) {
                wartosci[i][3 + j] = Math.pow(dane_x[i] - dane_x[j], 3);
            }
            wyniki[i] = dane_y[i];
        }

        for (int i = LENGTH; i < LENGTH + 2; i++) {
            wartosci[i][0] = 0.0;
            wartosci[i][1] = 1.0;
            wartosci[i][2] = 2 * pochodna_x[i - LENGTH];
            wartosci[i][3] = 3 * Math.pow(pochodna_x[i - LENGTH], 2);

            for (int j = 0; j < 3; j++) {
                wartosci[i][4 + j] = 3 * Math.pow(pochodna_x[i - LENGTH] - dane_x[j], 3);
            }
            wyniki[i] = dane_y[i - LENGTH];
        }

        double[] rozwiazanie = gaussElimination(wartosci, wyniki);
        double w = 0;
        w += rozwiazanie[0] + rozwiazanie[1] * X + rozwiazanie[2] * Math.pow(X, 2) + rozwiazanie[3] * Math.pow(X, 3);
        for (int i = 1; i < LENGTH - 1; i++) {
            if (X > dane_x[i]) {
                w += rozwiazanie[i + 3] * Math.pow(X - wartosci[i + 3][0], 3);
            }
        }
        System.out.println(w);
    }

    public static double[] gaussElimination(double[][] A, double[] b) {
        int n = A.length;
        for (int i = 0; i < n; i++) {
            // znajdź wiersz z maksymalną wartością w kolumnie i
            int maxRow = i;
            for (int j = i + 1; j < n; j++) {
                if (Math.abs(A[j][i]) > Math.abs(A[maxRow][i])) {
                    maxRow = j;
                }
            }
            
            // zamień wiersze i i maxRow
            double[] temp = A[i];
            A[i] = A[maxRow];
            A[maxRow] = temp;
            double t = b[i];
            b[i] = b[maxRow];
            b[maxRow] = t;
            
            // wyeliminuj zmienne w kolumnie i
            for (int j = i + 1; j < n; j++) {
                double factor = A[j][i] / A[i][i];
                b[j] -= factor * b[i];
                for (int k = i; k < n; k++) {
                    A[j][k] -= factor * A[i][k];
                }
            }
        }
        
        // wyznacz rozwiązanie
        double[] x = new double[n];
        for (int i = n - 1; i >= 0; i--) {
            double sum = 0.0;
            for (int j = i + 1; j < n; j++) {
                sum += A[i][j] * x[j];
            }
            x[i] = (b[i] - sum) / A[i][i];
        }
        
        return x;
    }    
}
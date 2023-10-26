public class Main {
    public static void main(String[] args) {

        TCar[] cars = new TCar[3];

		cars[0] = new TCar("아반떼 AD", "현대", 2015, 10000000);
        cars[1] = new TCar("C-Class", "Mercedes-Benz", 2022, 55000);
        cars[2] = new TCar("911", "Porsche", 2020, 100000);
		
        for(int i = 0; i < cars.length; i++){
            String result = cars[i].carList();
            String charsToRemove = "{}";
            for (char c : charsToRemove.toCharArray()) {
                result = result.replace(String.valueOf(c), "");
            }
		    System.out.println(result);
        }	
	}
}
